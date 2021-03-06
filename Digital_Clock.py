# Clock project 1

# Import Tkinter package.
from tkinter import *
from tkinter.ttk import *

# Get time or Import time.
from time import strftime

# Making UI for our Clock.
root = Tk()
root.title("Digital Clock")  # Title for the window.


# Defining our function time
# and making the format as Hour:Minutes:seconds: am/pm, The day and Date.
def time():
    str = strftime(" %I:%M:%S:%p \n %a,%d/%m/%y")
    label.config(text=str)
    label.after(1000, time)


# Creating label giving our window background color, font size, style and font color.
label = Label(root, font=("ds-digital", 130), background="black", foreground='Green')
label.pack(anchor='center')

# Calling our function time.
time()

# Tkinter event loop to keep the time updated.
mainloop()
