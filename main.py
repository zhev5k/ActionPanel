import time
import sys
import os
from rich import print

def typewriter(mes1):
	for char in mes1:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.02)

mes1 = ''' ______   _ _______     _____  _   _ _____ _____
|__  / | | | ____\ \   / / _ \| \ | | ____|__  /
  / /| |_| |  _|  \ \ / / | | |  \| |  _|   / /
 / /_|  _  | |___  \ V /| |_| | |\  | |___ / /_
/____|_| |_|_____|  \_/  \___/|_| \_|_____/____|
'''
os.system('cls')
typewriter(mes1)
time.sleep(3)
os.system('cls')

name = input("Введите ваше имя: ")
name2 = input("Ваше имя обидчика: ")

os.system('cls')

def mainmenu():
	print('''
[1] Ударить
[2] Обосрали
[3] Убили
[4] Выебать
[5] Унизить
[6] Обоссать
[7] Обкончать
[8] Сватнуть''')

mainmenu()

choice = input("Выбери действие: ")
if not choice.isdigit():
	print("Ты аутист? Число выбери")
	exit(0)
choice = int(choice)



if choice == 1:
	print(name, "ударил", name2)
	time.sleep(5)
	os.system('cls')
	mainmenu()
	choice = input("Выбери действие: ")
	if not choice.isdigit():
		print("Ты аутист? Число выбери")
		exit(0)
	choice = int(choice)


if choice == 2:
	print(name, "обосрал", name2)
	time.sleep(5)
	os.system('cls')
	mainmenu()
	choice = input("Выбери действие: ")
	if not choice.isdigit():
		print("Ты аутист? Число выбери")
		exit(0)
	choice = int(choice)

if choice == 3:
	print(name, "убил", name2)
	time.sleep(5)
	os.system('cls')
	mainmenu()
	choice = input("Выбери действие: ")
	if not choice.isdigit():
		print("Ты аутист? Число выбери")
		exit(0)
	choice = int(choice)

if choice == 4:
	print(name, "выебал", name2)
	time.sleep(5)
	os.system('cls')
	mainmenu()
	choice = input("Выбери действие: ")
	if not choice.isdigit():
		print("Ты аутист? Число выбери")
		exit(0)
	choice = int(choice)

if choice == 5:
	print(name, "унизил", name2)
	time.sleep(5)
	os.system('cls')
	mainmenu()
	choice = input("Выбери действие: ")
	if not choice.isdigit():
		print("Ты аутист? Число выбери")
		exit(0)
	choice = int(choice)

if choice == 6:
	print(name, "обоссал", name2)
	time.sleep(5)
	os.system('cls')
	mainmenu()
	choice = input("Выбери действие: ")
	if not choice.isdigit():
		print("Ты аутист? Число выбери")
		exit(0)
	choice = int(choice)

if choice == 7:
	print(name, "обкончал", name2)
	time.sleep(5)
	os.system('cls')
	mainmenu()
	choice = input("Выбери действие: ")
	if not choice.isdigit():
		print("Ты аутист? Число выбери")
		exit(0)
	choice = int(choice)

if choice == 8:
	print(name, "сватнул", name2)
	time.sleep(5)
	os.system('cls')
	mainmenu()
	choice = input("Выбери действие: ")
	if not choice.isdigit():
		print("Ты аутист? Число выбери")
		exit(0)
	choice = int(choice)
