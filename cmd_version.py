import random
import pyperclip

def pass_func(length_password):
    exit_value = True

    while exit_value:
        if length_password >= 10000000:
            print("Пароль слишком большой")
            length_password = int(input("Введите длину пароля: "))
        elif length_password <= 10000000:
            password = ""
            for i in range(length_password):
                random_liter = random.randint(33, 127)
                password += chr(random_liter)
            copied_password = input("Введите \"y\" для копирования пароля или любую другую клавишу для выхода: ")
            if copied_password == "y" or "Y":
                pyperclip.copy(password)
                exit_value = False


length_password = int(input("Введите длину пароля: "))
pass_func(length_password)