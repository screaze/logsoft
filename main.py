import os, pyfiglet
banner = pyfiglet.figlet_format("LogTools")
print(banner)
print("[SYSTEM] LogTools V2 By Screaze")
menugraph = """
[1] Прочекать логи на сиды и приватные ключи Google Keep.
[2] Прочекать логи на дискорд токены.
[3] Прочекать логи на куки.
[4] Просмотреть запросы в логах.
"""
print(menugraph)
menuinput = input("[SYSTEM] Введите пункт меню > ")

if menuinput == "1":
  os.system("clear")
  os.system("python seedchecker.py")
 
if menuinput == "2":
  os.system("clear")
  os.system("python discordtoken.py")

if menuinput == "3":
  os.system("clear")
  os.system("python cookiechecker.py")
 
if menuinput == "4":
  os.system("clear")
  os.system("python logsorter.py")
