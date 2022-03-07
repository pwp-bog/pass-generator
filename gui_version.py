from tkinter import *
from tkinter import messagebox
import pyperclip
import random

def inp_inf():
    len_pass = InputInformation.get()
    password = ""
    for i in range(int(len_pass)):
        random_liter = random.randint(33, 127)
        password += chr(random_liter)
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
    btn = Button(text="Сгенерировать пароль", command=inp_inf)
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

InputInformation = Entry(gui)
InputInformation.place(x = 255, y = 100, height=30,width=200)
InputInformation.focus()

main_text()
input_text()
inp_btn()

gui.mainloop()
