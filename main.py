import random


length_password = int(input("Введите длину пароля: "))

password = ""

for i in range(length_password):
    random_liter = random.randint(33, 127)
    password += chr(random_liter)

print(f"Ваш пароль равен: {password}")