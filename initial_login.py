from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Flappy bird')
root.geometry('400x700')
root.iconbitmap('icon.png')
root.resizable(False, False)


### Using an image as background###
# resize image
bg = Image.open("background-day.png")
resize_bg = bg.resize((400, 700), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resize_bg)
label_1 = Label(root, image=new_pic)
label_1.place(x=-3, y=0)

mainloop()
