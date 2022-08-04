#imports
from tkinter import *
from tkinter.ttk import*
from time import strftime

root = Tk()
root.iconbitmap('clock.ico')
root.title("Reactor Clock")

#main function
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label= Label(root, font=("Reactor7", 50), background="black", foreground="magenta")
label.pack(anchor='center')
time()

mainloop()