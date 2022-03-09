import random
import pyperclip

symbols_list = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", ":", ";", "<", "=", ">", "?", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
big_letters_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
little_letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
all_symbols_list = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]

length = int(input("Введите длину пароля: "))
type_password = input('''
Если вы хотите что бы ваш пароль состоял только из опеределённых символов:
Введите s - для пароля из символов
Введите n - для пароля из цифр
Введите b - для пароля из больших английских букв
Введите l - для пароля из маленьких английских букв
''')
password = ""

def pass_func(length: int, password: str, type_password: str = "a") -> str :
    if type_password == "s":
        for i in range(length):
            password += random.choice(symbols_list)
    elif type_password == "n":
        for i in range(length):
            password += random.choice(numbers_list)
    elif type_password == "b":
        for i in range(length):
            password += random.choice(big_letters_list)
    elif type_password == "l":
        for i in range(length):
            password += random.choice(little_letters_list)
    else:
        for i in range(length):
            password += random.choice(all_symbols_list)

    copied_password = input("Введите \"y\" для копирования пароля или любую другую клавишу для выхода: ")
    if copied_password == "y" or "Y":
        pyperclip.copy(password)

pass_func(length, password, type_password)