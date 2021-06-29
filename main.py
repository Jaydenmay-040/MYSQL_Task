from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.geometry("600x400")
window.resizable(False, False)
window.title("Login Page")
window.config(bg="black")

# Label and Entries
username_label = Label(window, text='Please enter username', bg='black', fg='white')
username_label.place(x=90, y=20)
username_entry = Entry(window)
username_entry.place(x=270, y=20)
password_label = Label(window, text='Please enter password', bg='black', fg='white')
password_label.place(x=90, y=70)
password_entry = Entry(window, show='*')
password_entry.place(x=270, y=70)


def login():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Hospital', auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    xy = mycursor.execute('Select * from Login')
    for i in mycursor:
        print(i)


def register():
    user = username_entry.get()
    password = password_entry.get()
    if username_entry == "" or password_entry == "":
        messagebox.showerror(message="Please ensure that username and password are filled in:(")
    elif user.isdigit():
        messagebox.showerror(message="Name does not contain letters:(")
    else:
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='Hospital', auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()

        sql = "INSERT INTO Login  VALUES (%s, %s)"
        val = (username_entry.get(), password_entry.get())
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        mycursor.execute('Select * from Login')
        messagebox.showinfo(message="New user and password added")

        # Adding text to file
        with open("Login.txt", "a+") as f:
            f.write('Name: ' + username_entry.get() + '\n')
            f.write('Surname: ' + password_entry.get() + '\n')

# Buttons
btn = Button(window, text="Login", width=10, command=login)
btn.place(x=200, y=200)
btn2 = Button(window, text="Register", width=10, command=register)
btn2.place(x=350, y=200)
clrbtn = Button(window, text="Clear", width=10, command=login)
clrbtn.place(x=100, y=350)
exit_button = Button(window, text="Exit", width=10, command=exit)
exit_button.place(x=500, y=350)

window.mainloop()