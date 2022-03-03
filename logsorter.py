import os, pyfiglet
from colorama import Fore, init, Back, Style
banner = pyfiglet.figlet_format("LogTools")
print(banner)

try:
	if not os.path.isdir("logs"):
		os.mkdir("logs")
		print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создана папка logs")
	else:
		print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Папка logs уже существует")
except:
	print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось содать папку logs")



try:
	if not os.path.isdir("output"):
		os.mkdir("output")
		print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создана папка output")
	else:
		print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Папка output уже существует")
except:
	print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось содать папку output")




print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Поместите в папку logs ваши логи (папками)")

hueta = input("[SYSTEM] Нажмите Enter для продолжения")

zapros = input("[SYSTEM] Введите необходимый запрос >> ")

try:
	text_file = open(f"output/{zapros}.txt", "w")
except:
	print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Файл чекера создан ({zapros})")

print("Чек начат")
paths = []
try:
	os.chdir("logs")
except:
	pass

for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        # print("Файл:", os.path.join(dirpath, filename))
        if "Passwords.txt" == filename:
        	paths.append(os.path.join(dirpath, filename))


print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Найдено {len(paths)} файлов с паролями")

def is_part_in_list(str_, words):
    for word in words:
        if word.lower() in str_.lower():
            return True
    return False

all_check = []

for filee in paths:
	pupa = open(filee, "r")
	stings = pupa.readlines()
	counter = 0
	check_vhods_result = 0
	mails = ["@gmail.ru", "@mail.ru", "@gmail.com", "@hotmail.com", "@yandex.ru"]
	for check_vhod in stings:
		check_vhod.count(zapros)
		check_vhods_result+=1
	while counter < check_vhods_result:
		if zapros in stings[counter] and not is_part_in_list(stings[counter], mails):
			print(stings[counter])
			log = stings[counter+1].split(': ')[1].replace('\n', '')
			pas = stings[counter+2].split(': ')[1].replace('\n', '')
			print(f"{Fore.RED}[{Fore.WHITE}PARSER{Fore.RED}] {log}:{pas}")

			print("\n\n")
			text_file.write(f"{log}:{pas}")
			text_file.write("\n")
			counter += 3

			all_check.append(f"{log}:{pas}")

		else:
			counter+=1

	pupa.close()

print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Найдено {len(all_check)} строк с паролями")

try:
	os.chdir("..")
except:
	pass

text_file.close()
os.rename(f"output/{zapros}.txt", f"output/[{len(all_check)}] {zapros}.txt")
input("[SYSTEM] Нажмите ENTER чтобы выйти в меню")
os.system("clear")
os.system("python main.py")
