import cv2 as vehicle


def main(result, ROI,Th,Det_line):
    count = 0
       
    video= vehicle.VideoCapture(result)
    Thr=Th
    subs = vehicle.createBackgroundSubtractorMOG2(history=250, varThreshold=50)  #yesko 
    
    _, frame= video.read()
    try:
        line_x1=int(Det_line[0][0])
        line_y1=int(Det_line[0][1])
        line_x2=int(Det_line[1][0])
        line_y2=int(Det_line[1][1])
    except:
        line_x1=0
        line_y1=int(0.75*frame.shape[0]) 
        line_x2=int(frame.shape[1])
        line_y2=line_y1
        
    try:
        line_m = (line_y2-line_y1)/(line_x2-line_x1)
    except:
        line_m = 0
    
    line_c= int(0.75*frame.shape[0]) 
    
    try:
        line_x_end=int(line_x2)
    except:
        line_x_end = frame.shape[1]
        
    font = vehicle.FONT_HERSHEY_SIMPLEX
    #temp=[1,2,3]
    while (video.isOpened()):
        _, frame= video.read()
        frame = vehicle.GaussianBlur(frame, (15, 15), 0)
        
        mask =  subs.apply(frame)
        (_,cnts,_) = vehicle.findContours(mask.copy(), vehicle.RETR_EXTERNAL, vehicle.CHAIN_APPROX_SIMPLE)  #yesko
        for contour in cnts:
            if vehicle.contourArea(contour) < Thr:        #removes noise/ sadow i.e. select area less than 1000 pixel
                continue
            (x,y,w,h) = vehicle.boundingRect(contour)          #create rectangle box in the frame
            if(not(x>ROI[0][0] and x<ROI[2][0] and y>ROI[0][1] and y<ROI[2][1]) ):
                continue
            vehicle.rectangle(frame,(x,y), (x+w,y+h), (0,255,0),2)
            #temp.append((line_m * x) + line_c -y)
            if(abs((line_m * x) + line_c -y)<5 ):
                count = count + 1
        
        vehicle.line(frame,(line_x1,line_y1),(line_x2,line_y2),(0,255,0),5)
        vehicle.line(frame,(ROI[0][0],ROI[0][1]),(ROI[1][0],ROI[1][1]),(0,255,0),5)
        vehicle.line(frame,(ROI[1][0],ROI[1][1]),(ROI[2][0],ROI[2][1]),(0,255,0),5)
        vehicle.line(frame,(ROI[2][0],ROI[2][1]),(ROI[3][0],ROI[3][1]),(0,255,0),5)
        vehicle.line(frame,(ROI[3][0],ROI[3][1]),(ROI[0][0],ROI[0][1]),(0,255,0),5)
        x=str(count)
        vehicle.putText(frame,x,(0,line_c), font, 4,(255,255,255),2,vehicle.LINE_AA)
        frame = vehicle.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))
        mask = vehicle.resize(mask,(int(mask.shape[1]/2),int(mask.shape[0]/2)))   
        vehicle.imshow('Frame', frame)
        vehicle.imshow('Mask', mask)                # yesko
        
        key = vehicle.waitKey(11)
        if key == 27 :
            break
    
    video.release()
    
    vehicle.destroyAllWindows()
    print(frame.shape)
    print(x)
if (__name__ =="__main__"):
    result='testx.mp4'
    ROI=[[5,5],
       [1275,5],
       [1275,715],
       [5,715]]
    Th=1000
    Det_line=[[0,540],
              [1275,540]]
    main(result, ROI,Th,Det_line)
