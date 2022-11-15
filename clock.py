from tkinter import *
from time import *

# recursive funciton to display time
def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    if(day_string == "Tuesday"):
        time_label.config(fg="pink")

    # delay update for 1000 ms and call update again
    time_label.after(1000,update)

window = Tk()
window.title("Clock")

frame = Frame(window, bg = "black")
frame.pack()

# label to store time in the window
time_label = Label(frame, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(frame, font=("Papyrus", 25), bg="black")
day_label.pack()

date_label = Label(frame, font=("Papyrus", 40), bg="black")
date_label.pack()

update()

window.mainloop()