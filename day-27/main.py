import os
from tkinter import *


KM = "km to miles"
M = "Miles to km"


def action():
    try:
        value = float(entry.get())
        value = value * 100
        value = int(value)
        value = float(value) / 100
        if checked_state.get() == 1:
            result = value / 1.609
            label3.config(text=str(result))
        else:
            result = value * 1.609
            label3.config(text=str(result))

    except ValueError:
        entry.delete(0, END)
        entry.insert(END, "0")


def checkbutton_used():
    if checked_state.get() == 1:
        label1.config(text="km")
        label4.config(text="miles")
    else:
        label1.config(text="miles")
        label4.config(text="km")

    action()



window = Tk()
window.title(KM)
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)



label0 = Label(text="")
label0.grid(column=0 , row=0)



entry = Entry(width=30)
entry.insert(END, string="0")
entry.grid(column=1, row=0)



label1 = Label(text="miles")
label1.grid(column=2, row=0)



label2 = Label(text="is equal to")
label2.grid(column=0, row=1)



label3 = Label(text="0")
label3.grid(column=1, row=1)



label4 = Label(text="km")
label4.grid(column=2, row=1)



button = Button(text="convert", command=action)
button.grid(column=1, row=2)



checked_state = IntVar()
checkbutton = Checkbutton(text="miles to km", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=1, row=3)



window.mainloop()