
from list import all_symbols_list, little_letters_list, numbers_list, symbols_list, big_letters_list
from operator import length_hint
from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import tkinter as tk


def reqr_func():
    len_pass = input_information.get()
    if int(len_pass) >= 100000:
        messagebox.showinfo("pass-gen", "пароль слишком большой")
    else:
        inp_inf(len_pass)


def inp_inf(len_pass):

    if int(len_pass) >= 100000:
        messagebox.showinfo("pass-gen", "пароль слишком большой")

    if value_menu == "Все символы":
        password = ""
        for i in range(int(len_pass)):
            password += random.choice(all_symbols_list)
        pyperclip.copy(password)

    elif value_menu == "Цифры":
        password = ""
        for i in range(int(len_pass)):
            password += random.choice(numbers_list)
        pyperclip.copy(password)

    elif value_menu == "Маленькие буквы":
        password = ""
        for i in range(int(len_pass)):
            password += random.choice(little_letters_list)
        pyperclip.copy(password)

    elif value_menu == "Большие буквы":
        password = ""
        for i in range(int(len_pass)):
            password += random.choice(big_letters_list)
        pyperclip.copy(password)
    elif value_menu == "Символы":
        password = ""
        for i in range(int(len_pass)):
            password += random.choice(symbols_list)
        pyperclip.copy(password)

    messagebox.showinfo("pass-gen", "Пароль скопирован")


def main_text():
    label1 = Label(text="Генератор паролей: ",
                   fg="white",
                   bg="black",
                   font="24")

    label1.pack(side=TOP)


def input_text():
    label1 = Label(text="Введите длину пароля:",
                   fg="white",
                   bg="black",
                   font=24)
    label1.place(x=5, y=100)


def inp_btn():
    btn = Button(text="Сгенерировать пароль", command=reqr_func)
    btn.place(x=600,
              y=115,
              anchor="c",
              height=35,
              width=150,
              bordermode=OUTSIDE)


gui = Tk()
gui.title("pass-gen")
gui.geometry("700x200+600+200")
gui.configure(bg="black")

input_information = Entry(gui)
input_information.place(x=255, y=100, height=30, width=200)
input_information.focus()

main_text()
input_text()
inp_btn()

OptionList = [
    "Все символы",
    "Цифры",
    "Маленькие буквы",
    "Большие буквы",
    "Символы"
]
variable = tk.StringVar(gui)
variable.set(OptionList[0])
opt = tk.OptionMenu(gui, variable, *OptionList)
opt.config(width=20, font=('Helvetica', 12),
           background="black", foreground="white")
opt.place(x=235, y=35)


def callback(*args):
    global value_menu
    value_menu = str(variable.get())


variable.trace("w", callback)
value_menu = str(variable.get())


gui.mainloop()
