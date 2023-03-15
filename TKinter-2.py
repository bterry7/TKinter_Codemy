import os # os is auto included with python. Other modules will not be
os.system('clear') # use whatever command is needed for that instance; gitbash uses "clear"

from tkinter import *
from PIL import ImageTk, Image #for images; "pip install Pillow" in gitbash to install. How to install came with Python, but it wasn't installed (I think)

root = Tk()
root.title('Images')
# root.iconbitmap('file location .ico')

# Quit button
button_quit = Button(root,text="Exit Program",command=root.quit)
button_quit.pack()


#Images
# Find image
my_img = ImageTk.PhotoImage(Image.open("Cat Hug.jpg"))
# Put image on widget
my_label = Label(image=my_img)
# Put label on screen
my_label.pack()

root.mainloop()