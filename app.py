import time
from tkinter import *
from time import *

def update():
    time_string = strftime("%I, %M, %S, %p")
    time_label.config(text=time_string)

    date_string = strftime("%A")
    date_label.config(text=date_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    window.after(1000, update)

window = Tk()

day_label = Label(window, font=('consolas', 30),fg="green",bg="black")
day_label.pack()

date_label = Label(window, font=('consolas', 30))
date_label.pack()

time_label = Label(window, font=('Ink free', 30))
time_label.pack()

update()

window.mainloop()