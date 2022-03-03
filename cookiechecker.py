import os
import shutil
import pyfiglet
banner = pyfiglet.figlet_format("LogTools")
print(banner)
print("[SYSTEM] Укажите путь до папки с логами > ")
path = input()
count = 0
main_path = os.path.dirname(os.path.abspath(__file__))
for f in os.listdir(path):
	if os.path.isdir(os.path.join(path, f)):
		count += 1
try:
	os.mkdir("cookies")
except:
	pass
print(f"[LOG] Загружено {count} логов. Нажмите ENTER чтобы продолжить")
input()
print("[LOG] Достаем куки...")
cookie = 0
logs = 0
for f in os.listdir(path):
	if os.path.isdir(os.path.join(path, f)):
		pathcook = path + "/" + f + "/Cookies"
		try:
			for c in os.listdir(pathcook):
				if os.path.isfile(os.path.join(pathcook, c)):
					cookie += 1
					pcook = pathcook + "/" + c
					copyto = main_path + f"/cookies/Cookie {cookie}.txt"
					print(f"Cookie {cookie}")
					shutil.copyfile(pcook, copyto)
			print(f"[LOG] Лог {f} обработан")
			logs += 1
		except:
			print("[LOG] Папка cookies не найдена")

print(f"[LOG] Добавлено {cookie} куков")
print(f"[LOG] {logs} логов обработано")
input("[SYSTEM] Нажмите ENTER чтобы выйти в меню")
os.system("clear")
os.system("python main.py")
