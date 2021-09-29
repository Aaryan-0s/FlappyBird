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
label_2 = Label(root, text="Welcome", font='Ubuntu', fg='blue')
label_2.place(x=150, y=10)

# creating database
con = sqlite3.connect('Login and Registration.db')

cur = con.cursor()


# Fuction to get into game
def logdata():
    con = sqlite3.connect("Login and Registration.db")
    cur = con.cursor()

    lnam = Username_entry.get()
    lpass = Password_entry.get()

    cur.execute("SELECT * FROM addressA")
    record = cur.fetchall()
    print(record)
    user = []
    passw = []

    for records in record:
        user += [records[1]]
        passw += [records[2]]
    print(user)
    print(passw)

    if lnam in user and lpass in passw:
        if user.index(lnam) == passw.index(lpass):
            print("sucess")
            import main


        else:
            messagebox.showinfo("FAILED", "Invalid Username or Password")

    else:
        messagebox.showinfo("FAILED", "Invalid Username or Password")

    Username_entry.delete(0, END)
    Password_entry.delete(0, END)

    con.commit()
    con.close()
# making labels, entries and buttons
UsernameLabel = Label(root, text="Username", font='Helvetica', bg="red").place(x=50, y=100)
Username_entry = Entry(root, font='Cambria 15 italic', bd=3, relief=SUNKEN)
Username_entry.place(x=150, y=100)
PasswordLabel = Label(root, text="Password", font='Helvetica', bg="red").place(x=50, y=200)
Password_entry = Entry(root, font='Cambria 15 italic', bd=3, relief=SUNKEN)
Password_entry.place(x=150, y=200)
'''
NewPlayer = Label(root, text="SIGNUP IF YOURE A NEW PLAYER", font='Helvetica', fg='blue', bg="#C4CFD8", width=70)
NewPlayer.place(x=5, y=270)
'''
login_button = Button(root, text="Login", font='Helvetica', bg="red",command=logdata).place(x=180, y=400)


con.commit()

con.close()

mainloop()