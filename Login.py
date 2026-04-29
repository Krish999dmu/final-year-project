import tkinter

window = tkinter.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333')

# creating widgets
login_label = tkinter.Label(
    frame, text="Login", bg='#333333', fg='white', font=("arial", 30))
frame.configure(bg='#333333')
username_label = tkinter.Label(
    frame, text="Username", bg='#333333', fg='white', font=("arial", 16))
username_entry = tkinter.Entry(frame, font=("arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg='#333333', fg='white', font=("arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg='green', fg="white", font=("arial", 16))
sign_up_button = tkinter.Button(
    frame, text="Signup", bg='green', fg="white", font=("arial", 16))

# placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=10)
login_button.grid(row=3, column=0,  pady=30)
sign_up_button.grid(row=3, column=1, pady=30)

frame.pack()

window.mainloop()
