from PIL import Image, ImageDraw, ImageFont,ImageTk
import random
import os
import datetime
import qrcode
import glob
from tkinter import *
import tkinter as tk
from tkinter.simpledialog import askstring
import PIL. Image
from tkinter import messagebox as mb


# To create a Window
top=Tk()
top.geometry("700x700")
top.title("Id Card Generator")

# To Get Logo Onto a Tkinter Window
img = PIL.Image.open("Id.png")
img = ImageTk.PhotoImage(img)
panel = Label(top, image=img)
panel.image = img
panel.pack(side = TOP)

# To get Date and Time
d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y \t %I:%M:%S %p")


# For Labelling
ourMessage ='Please Provide the Data in Capital Letters and make sure you enter the data properly'
messageVar = Message(top, text = ourMessage) 
messageVar.config(bg='lightgreen')
messageVar.pack()
clg_name = Label(top, text = "College Name").place(x = 30,y = 80)
idno = Label(top, text = "Id No").place(x = 30, y = 110)
name = Label(top, text = "Name").place(x = 30,y = 140)
gender = Label(top, text = "Gender").place(x = 30,y = 170)
age = Label(top, text = "Age").place(x = 30,y = 200)
dob = Label(top, text = "DOB").place(x = 30,y = 230)
blood_group = Label(top, text = "Blood Group").place(x = 30,y = 260)
mob_num = Label(top, text = "Mobile Number").place(x = 30,y = 290)
city = Label(top, text = "City").place(x = 30,y = 320)
#To Get Entered Text in a Entry Widget
str1=tk.StringVar()
str2=tk.StringVar()
str3=tk.StringVar()
str4=tk.StringVar()
str5=tk.StringVar()
str6=tk.StringVar()
str7=tk.StringVar()
str8=tk.StringVar()
str9=tk.StringVar()

#For Entry Widget
e1=  Entry(top,textvariable=str1).place(x = 120, y = 80)
e2 = Entry(top,textvariable=str2).place(x = 120, y = 110)
e3 = Entry(top,textvariable=str3).place(x = 120, y = 140)
e4 = Entry(top,textvariable=str4).place(x = 120, y = 170)
e5 = Entry(top,textvariable=str5).place(x = 120, y = 200)
e6 = Entry(top,textvariable=str6).place(x = 120, y = 230)
e7 = Entry(top,textvariable=str7).place(x = 120, y = 260)
e8 = Entry(top,textvariable=str8).place(x = 120, y = 290)
e9 = Entry(top,textvariable=str9).place(x = 120, y = 320)



def submit():
    image = PIL.Image.new('RGB', (1100,1000), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=45)
    #Clg_Name
    (x, y) = (50, 50)
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=40)
    draw.text((x, y),str1.get(), fill=color, font=font)
    #Idno
    (x, y) = (600, 150)
    message = str('ID '+str(str2.get()))
    color = 'rgb(0, 0, 0)' # black color
    font = ImageFont.truetype('arial.ttf', size=40)
    draw.text((x, y), message, fill=color, font=font)
    #Name
    (x, y) = (50, 250)
    color = 'rgb(0, 0, 0)' # black color
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), str3.get(), fill=color, font=font)
    #Gender
    (x, y) = (50, 350)
    color = 'rgb(0, 0, 0)' # black color 
    draw.text((x, y),str4.get(), fill=color, font=font)
    #Age
    (x, y) = (250, 350)
    color = 'rgb(0, 0, 0)' # black color
    draw.text((x, y), str5.get(), fill=color, font=font)
    #DOB
    (x, y) = (50, 450)
    draw.text((x, y),  str6.get(), fill=color, font=font)
    #Blood  Group
    (x, y) = (50, 550)
    color = 'rgb(255, 0, 0)' # black color 
    draw.text((x, y),  str7.get(), fill=color, font=font)
    #Mobile Number
    (x, y) = (50, 650)
    color = 'rgb(0, 0, 0)' # black color
    draw.text((x, y),  str8.get(), fill=color, font=font)
    #Address
    (x, y) = (50, 750)
    color = 'rgb(0, 0, 0)' # black color 
    draw.text((x, y),  str9.get(), fill=color, font=font)
    #Date and Time
    (x, y) = (600,800)
    font = ImageFont.truetype('arial.ttf', size=20)
    color = 'rgb(0, 0, 0)' # black color 
    draw.text((x, y),reg_format_date  , fill=color, font=font)
    
    # save the edited image
    image.save(str(str3.get())+'.png')
    img = qrcode.make(str(str1.get())+"\n"+str(str2.get())+"\n"+str(str3.get()))   # this info. is added in QR code, also add other things
    img.save(str(str2.get())+'.bmp')
    til = PIL.Image.open(str3.get()+'.png')
    im = PIL.Image.open(str(str2.get())+'.bmp') #25x25
    im1 = PIL.Image.open("logo.png")#25x25
    til.paste(im1,(640,250))
    til.paste(im,(600,350))
    til.save(str3.get()+'.png')
    mylist=[f for f in glob.glob("*.bmp")]
    os.remove(mylist[0])
    mb.showinfo("Id Card Generator","Your ID card  has been Generated as : ** "+str3.get()+'.png **')
    str1.set("")
    str2.set("")
    str3.set("")
    str4.set("")
    str5.set("")
    str6.set("")
    str7.set("")
    str8.set("")
    str9.set("")
    

def reset():
    str1.set("")
    str2.set("")
    str3.set("")
    str4.set("")
    str5.set("")
    str6.set("")
    str7.set("")
    str8.set("")
    str9.set("")
b1 = tk.Button(top,text = "Submit",state=ACTIVE,command = submit,activeforeground = "red",activebackground = "pink").place(x=80,y=350)
b2 = tk.Button(top,text = "Reset",state=ACTIVE,command = reset,activeforeground = "red",activebackground = "pink").place(x=160,y=350)
top.mainloop()
    
    
