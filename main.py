from tkinter import *
from tkinter.ttk import *
from time import stfrtime

root = Tk()
root.title("Clock")

def time():
  string = strftime('%H:%M:%S %p')
  label.config(text=string)
  label.after(1000, time)
  
label = Label(font = ("ds-digital", 80), background = "black", foreground = "red")
label.pack(anchor = 'center')

time()

mainloop()
