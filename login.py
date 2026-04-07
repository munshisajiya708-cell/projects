import tkinter as tk
from tkinter import messagebox


def login():
    username=user.get()
    password=pwd.get()
    
    if user.get() =="admin" and pwd.get()=="1234":
        messagebox.showinfo("Login","Login successful")
         
    else:
        messagebox.showerror("Login","Invalid username or password")
        

root=tk.Tk()
root.title("Login")
root.geometry("300x300")

frame=tk.Frame(root)
frame.pack(pady=30)


tk.Label(frame,text="username").grid(row=0,column=0,pady=10)
user=tk.Entry(frame)
user.grid(row=0,column=1)

tk.Label(frame,text="pasword").grid(row=1,column=0)
pwd=tk.Entry(frame)
pwd.grid(row=1,column=1)

tk.Button(frame,text="login",command=login,bg="blue",fg="white",font=("Arial",12)).grid(row=2,column=1,columnspan=2,pady=30)

root.mainloop()