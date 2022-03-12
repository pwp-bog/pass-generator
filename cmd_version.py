import random
import pyperclip
from list import little_letters_list, numbers_list, symbols_list, big_letters_list, all_symbols_list

# Получаем размер и проверяем на его пригодность
bool_value = True
while bool_value:
	length = int(input("Введите длину пароля: "))
	if length <= 10000:
		bool_value = False
		print(f"Длина пароля: {length}")
	else:
		print("Пароль слишком большой")

# Получаем информацию о типе пароля
type_password = input('''
Если вы хотите что бы ваш пароль состоял только из опеределённых символов:
Введите s - для пароля из символов
Введите n - для пароля из цифр
Введите b - для пароля из больших английских букв
Введите l - для пароля из маленьких английских букв
''')
password = ""


# Функция для проверки параметров и генерация пароля
def pass_func(length: int, password: str, type_password: str = "a") -> str:
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

	# Копирование пароля в буфер обмена
	copied_password = input(
			"Введите \"y\" для копирования пароля или любую другую клавишу для выхода: ")
	if copied_password == "y" or "Y":
		pyperclip.copy(password)


pass_func(length, password, type_password)
