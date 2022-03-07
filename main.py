import random
import pyperclip

length_password = int(input("Введите длину пароля: "))

password = ""

for i in range(length_password):
    random_liter = random.randint(33, 127)
    password += chr(random_liter)

print(f"Ваш пароль равен: {password}")

copied_password = input("Введите \"y\" для копирования пароля или любую другую клавишу для выхода: ")
if copied_password == "y" or "Y":
    pyperclip.copy(password)
