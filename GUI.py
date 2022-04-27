
from tkinter import *
from PIL import ImageTk, Image
import os

from Vehicle import main

def calculate():
 main(var, temp)
    

root = Tk()
root.title("Vehicle Counting System")
root.geometry("1000x500+0+0")
path = ''


left = Frame(root, width = 500, height = 500, bd = 1 , relief = "raise")
left.grid(row=0,column=0)
   #label
lbl1=Label (left, text="Region of interest",font=("Arial Bold",10))
lbl1.grid (column=0,row=0)
lbl2=Label (left,text="Threshold Frame",font=("Arial Bold",10))
lbl2.grid (column=0,row=4)
lbl3=Label (left,text="Detection Line",font=("Arial Bold",10))
lbl3.grid (column=0,row=5)   
    #button
button1=Button(left,text="Calculate",command=calculate,bg="yellow",fg="red")
button1.grid(column=1,row=7)
button2=Button(left,text="Exit",command=root.destroy,bg="yellow",fg="red")
button2.grid(column=2,row=7)
    #entry
entry_field1=Entry(left,width=10)
entry_field1.grid(column=1,row=0)
entry_field2=Entry(left,width=10)
entry_field2.grid(column=2,row=0)
entry_field3=Entry(left,width=10)
entry_field3.grid(column=1,row=1)
entry_field4=Entry(left,width=10)
entry_field4.grid(column=2,row=1)
entry_field5=Entry(left,width=10)
entry_field5.grid(column=1,row=2)
entry_field6=Entry(left,width=10)
entry_field6.grid(column=2,row=2)
entry_field7=Entry(left,width=10)
entry_field7.grid(column=1,row=3)
entry_field8=Entry(left,width=10)
entry_field8.grid(column=2,row=3)
entry_field9=Entry(left,width=10)
entry_field9.grid(column=1,row=4)
entry_field10=Entry(left,width=10)
entry_field10.grid(column=1,row=5)
entry_field11=Entry(left,width=10)
entry_field11.grid(column=2,row=5)
entry_field12=Entry(left,width=10)
entry_field12.grid(column=1,row=6)
entry_field13=Entry(left,width=10)
entry_field13.grid(column=2,row=6)

right = Frame(root, width = 500, height = 500, bd = 1 , relief = "raise")
right.grid(row=0,column=1)

img = Image.open("1234.png")
img = ImageTk.PhotoImage(img)
lbl = Label(right, image = img)
lbl.image = img 
lbl.grid(row=0,column=0)
var ='testx.mp4'
temp=123





root.mainloop()
