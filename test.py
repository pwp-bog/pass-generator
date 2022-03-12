import tkinter as tk
from tkinter import Variable, font
from list import all_symbols_list
import random

OptionList = [
    "Все символы",
    "Цифры",
    "Маленькие буквы",
    "Большие буквы",
    "Символы"
]

app = tk.Tk()

app.geometry('500x500')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack(side="top")


label_test = tk.Label(text="",font=('Helvetica', 12), fg='black')
label_test.pack(side="bottom")


def callback(*args):
    value_group = str(variable.get())
    print(value_group)
    password = ""
    if value_group == "Все символы":
        for i in range(10):
            password += random.choice(all_symbols_list)
        label_test.configure(text=password)
    else:
        label_test.configure(text="Прикол")


variable.trace("w", callback)

app.mainloop()
