from tkinter import*
from tkinter import messagebox
root = Tk()
root.title("Virus")
root.geometry("300x200")

def msg():
    messagebox.showwarning("Alert"," You have been hacked! Virus found")

btn = Button(root, text = "Click me", fg = "Blue", command = msg)
btn.place(x = 80, y = 100)
root.mainloop()