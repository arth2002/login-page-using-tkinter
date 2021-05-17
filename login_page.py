import tkinter as tk
from tkinter import Button, Entry, Label, StringVar, Tk, Toplevel
import ast
import tkinter.messagebox as tmsg


def login():
    global login
    global user_name
    global password
    global show_hide_pass_btn

    login = Toplevel(root)
    login.geometry("600x500")
    login.title("Login Page")
    Label(login, text="Login", background="red",
          fg="white", height=3, font="ariel 15").pack(fill="x")
    user_name = StringVar()
    password = StringVar()
    Label(login, text="User Name: ").pack()
    user_name = Entry(login, text="User Name", textvariable=user_name)
    user_name.pack()

    Label(login, text="Password: ").pack()
    password = Entry(login, text="Password", textvariable=password, show="*")
    password.pack()

    show_hide_pass_btn = Button(login, text="Show", width=5,
                                command=toggle_show_hide_passw)
    show_hide_pass_btn.pack()

    Button(login, text="Login", command=verify_user).pack()


def toggle_show_hide_passw():
    global password
    global show_hide_pass_btn
    if password.cget('show') == '':
        password.config(show='*')
        show_hide_pass_btn.config(text='Show')
    else:
        password.config(show='')
        show_hide_pass_btn.config(text='Hide')


def verify_user():
    global user_name
    global password
    getuser = user_name.get()
    getpassw = password.get()
    # with open("all_user_data.txt", "r") as f:
    try:
        myfile = open("all_user_data.txt", "r")
        # while myfile:
        for line in myfile:
            # line = myfile.readline()
            # print(line)
            data_for_login = ast.literal_eval(line)

            data_user_id = data_for_login[0]["user_id"]
            data_passw = data_for_login[0]["passw"]
            if data_user_id == getuser:
                if data_passw == getpassw:
                    # print("OK")
                    tmsg.showinfo("Login", "You successfully Loged in")
                    break
                else:
                    tmsg.showerror(
                        "Error", "username or password didn't match")
                    # print("password not match")
        myfile.close()
    except Exception as e:
        print(e)


def register_page():
    global register_page
    register_page = Toplevel(root)
    register_page.geometry("600x500")
    register_page.title("Register yourself here")

    global user_id
    global userid
    global email
    global passw

    userid = StringVar()
    email = StringVar()
    passw = StringVar()
    Label(register_page, text="Register Here", background="red",
          fg="white", height=3, font="ariel 15").pack(fill="x")

    Label(register_page, text="User Name: ").pack()
    user_id = Entry(register_page, textvariable=userid)
    user_id.pack()

    Label(register_page, text="Email Id:").pack()
    email = Entry(register_page, textvariable=email)
    email.pack()

    Label(register_page, text="Password:").pack()
    passw = Entry(register_page, textvariable=passw)
    passw.pack()

    user_data = {
        "user_id": userid.get(),
        "email": email.get(),
        "passw": passw.get()
    }

    Button(register_page, text="Register",
           command=get_data).pack()


def get_data():
    global userid
    global passw
    global email
    getuser = userid.get()
    getemail = email.get()
    getpassw = passw.get()
    all_user_data = []
    user_data = {
        "user_id": f"{getuser}",
        "email": f"{getemail}",
        "passw": f"{getpassw}"
    }
    all_user_data.append(user_data)
    try:
        with open("all_user_data.txt", "a") as f:
            f.write(str(all_user_data))
            f.write("\n")
    except Exception as e:
        tmsg.showerror("Error", "Error occured")
    finally:
        tmsg.showinfo("Success", "You've successfully Registered")


# ======================================
# programm will start from here..
root = Tk()
root.geometry("500x450")
root.title("Join Us")

header = Label(text="Join Us", background="red",
               fg="white", height=3, font="ariel 15")
header.pack(fill="x")
login_btn = Button(root, text="Login", width=10,
                   height=1, command=login)
login_btn.pack(pady=20)
register_btn = Button(root, text="Register", width=10,
                      height=1, command=register_page)
register_btn.pack()

root.mainloop()
