import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

from tkinter import *

# Set up root to put stuff on
root = Tk()

#TKinter works on widgets
myLabel1 = Label(root,text="Hello World")
myLabel2 = Label(root,text="My Name is Ben")

myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=5) 
# grid is relative. I could make it column 5 for mylabel2, but if there's nothing in columns 1-4, it doesn't matter

# Could also write
'''
myLabel1 = Label(root,text="Hello World").grid(row=0,column=0)
myLabel2 = Label(root,text="My Name is Ben").myLabel2.grid(row=1,column=5) 
# ... but readability 
'''


# myLabel1.pack() # pack is basic method of putting stuff on screenls


root.mainloop()