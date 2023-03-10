import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

from tkinter import *

# For Button
def myClick():
    hello = "Hello" + e.get()
    myLabel = Label(root,text=hello)
    myLabel.grid(row=2,column=1)


# Set up root to put stuff on
root = Tk()

# TKinter works on widgets
'''
# Labels
myLabel1 = Label(root,text="Hello World")
myLabel2 = Label(root,text="My Name is Ben")

myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=5) 
# grid is relative. I could make it column 5 for mylabel2, but if there's nothing in columns 1-4, it doesn't matter
# myLabel1.pack() # pack is basic method of putting stuff on screenls
# Cannot mix pack and grid
'''

'''
# Could also write
myLabel1 = Label(root,text="Hello World").grid(row=0,column=0)
myLabel2 = Label(root,text="My Name is Ben").myLabel2.grid(row=1,column=5) 
# ... but readability 
'''

#Buttons
myButton = Button(root,text="Enter Your Name",padx=50,pady=50,command=myClick,fg="blue",bg="red")
# "State" is disabled (cannot be clicked)
# "padx","pady" is length and height; rest of columns/rows adjust. Likely not necessary to resize if using grid properly
# "fg", "bg" for text and box color. Can also use color codes
# ... etc. Check documentation
# Do not use () for the command. If you do, it will treat as a function and count it as already run (i.e. the text already appears without clicking)
# By not using (), it is "attached" to the button per run cycle. Or somethign
# Have to use "command = lambda: fun()"
myButton.grid(row=1,column=1)


# Input boxes
e = Entry(root,width=50,borderwidth=10)
# "fg" and "bg" work the same as for buttons
e.grid(row=0,column=1)
# e.get() # get what was typed in
e.insert(0,"Type your name here") # Default text; does not auto delete when you try to type


# Run
root.mainloop()