import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Images')
# root.iconbitmap('file location .ico')

my_img1 = ImageTk.PhotoImage(Image.open("Images\Kill it with Fire.jpg")) 
my_img2 = ImageTk.PhotoImage(Image.open("Images\Ico (5).jpg")) 
my_img3 = ImageTk.PhotoImage(Image.open("Images\dust.jpg")) 

image_list =[my_img1,my_img2,my_img3]

status = Label(root,text="Image 1 of "+str (len(image_list)),bd=1, relief=SUNKEN, anchor=E)
# bd is border
# relief makes is sunken
# anchor is based on compass system

my_label = Label(image=my_img1)
my_label.grid(row=0,column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    my_label.grid(row=0,column=0, columnspan=3)
    
    button_back = Button(root,text="<<",command=lambda: back(image_number-1))
    button_forward = Button(root,text=">>",command=lambda: forward(image_number+1))
    button_exit = Button(root,text="Exit Program",command=root.quit)
    status = Label(root,text="Image " + str(image_number) + " of "+str (len(image_list)),bd=1, relief=SUNKEN, anchor=E)

    if image_number==3:
        button_forward = Button(root,text=">>",state=DISABLED)

    button_back.grid(row=1,column=0)
    button_exit.grid(row=1,column=1)
    button_forward.grid(row=1,column=2,pady=10)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)


def back(image_number):
    global my_label
    global button_forward
    global button_back
   
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    my_label.grid(row=0,column=0, columnspan=3)
    
    button_back = Button(root,text="<<",command=lambda: back(image_number-1))
    button_forward = Button(root,text=">>",command=lambda: forward(image_number+1))
    button_exit = Button(root,text="Exit Program",command=root.quit)
    status = Label(root,text="Image " + str(image_number) + " of "+str (len(image_list)),bd=1, relief=SUNKEN, anchor=E)

    if image_number==1:
        button_back = Button(root,text="<<",state=DISABLED)

    button_back.grid(row=1,column=0)
    button_exit.grid(row=1,column=1)
    button_forward.grid(row=1,column=2,pady=10)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)



button_back = Button(root,text="<<",command=lambda: back(),state=DISABLED)
button_forward = Button(root,text=">>",command=lambda: forward(2))
button_exit = Button(root,text="Exit Program",command=root.quit)

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)
# Sticky is stretch based on a compass system

root.mainloop()