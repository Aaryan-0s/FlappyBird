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

'''
cur.execute("""CREATE TABLE addressA(
                Name text,
        Username text,
        Password text
)""")
'''
print("Table created successfully")


# creating database for SIGNUP
def Signin():
    def signUp():
        con = sqlite3.connect("Login and Registration.db")
        cur = con.cursor()

        cur.execute("INSERT INTO addressA VALUES(:Name_label, :Username_label, :Password_label)", {
            'Name_label': Name_entry.get(),
            'Username_label': Username_entry.get(),
            'Password_label': Password_entry.get()
                    })

        print(' SUCCESSFUL')
        data = cur.fetchall()
        print(data)

        con.commit()
        con.close()

        Name_entry.delete(0, END)
        Username_entry.delete(0, END)
        Password_entry.delete(0, END)


    signwindow = Toplevel()
    signwindow.geometry('400x700')
    signwindow.resizable(False, False)
    signwindow.title(' SIGNUP TO PLAY')
    signwindow.iconbitmap('icon.png')
    signwindow.configure(bg="Sky Blue")

    Frame1 = Frame(signwindow, bd=10, bg='blue', width=300, relief=RIDGE)
    Frame1.place(x=15, y=100)

    Frame1_label = Label(Frame1, font=('Helvetica', 10, 'bold'), bg='light pink',
                         text='Hurry... SignUp and Enjoy The Game', padx=50)
    Frame1_label.grid()

    Entry_frame_details = Frame(signwindow, bd=10, bg='#D1C3BE', width=380, height=290, padx=250, relief=RIDGE)
    Entry_frame_details.place(x=15, y=200)

    # making labels, entries and buttons for signup
    Name_label = Label(Entry_frame_details, text='Name', font='Helvetica', bg="#D1C3BE").place(x=-240, y=8)

    Name_entry = Entry(Entry_frame_details, font='Cambria 15 italic', bd=3, relief=SUNKEN)
    Name_entry.place(x=-140, y=3)

    Username_label = Label(Entry_frame_details, text="Username", font='Helvetica', bg="#D1C3BE").place(
        x=-240, y=50)

    Username_entry = Entry(Entry_frame_details, font='Cambria 15 italic', bd=3, relief=SUNKEN)
    Username_entry.place(x=-140, y=50)

    Password_label = Label(Entry_frame_details, text="Password", font='Helvetica', bg="#D1C3BE").place(
        x=-240, y=100)

    Password_entry = Entry(Entry_frame_details, font='Cambria 15 italic', bd=3, relief=SUNKEN)
    Password_entry.place(x=-140, y=100)

    #Country_label = Label(Entry_frame_details, text="Country", font='Ubuntu', bg="#D1C3BE").place(x=-220,
                                                                                                  #y=150)

    #Country_entry = Entry(Entry_frame_details, font='Cambria 15 italic', bd=3, relief=SUNKEN)
    #Country_entry.place(x=-130, y=150)

    SubmitButton = Button(Entry_frame_details, text="Submit", font='Helvetica', bg="green", command=signUp).place(
        x=-130,
        y=203)

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
            import main_game


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
signup_button = Button(root, text="Sign Up", font='Helvetica', bg="red", command=Signin).place(x=168, y=500)

con.commit()

con.close()

mainloop()
