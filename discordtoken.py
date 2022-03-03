import os, pyfiglet
import asyncio
from os import system

from time import gmtime, strftime
banner = pyfiglet.figlet_format("LogTools")
print(banner)
path = input('[SYSTEM] Введите путь к папке с логами > ')
a = list(filter(os.path.isdir, [f'{path}/' + x for x in os.listdir(path)]))
all_tokens = []
for i in a:
    file = os.listdir(i)
    print(f'Open {i.replace(f"{path}/", "")}')
    if 'Discord' in file:
        filetokens = os.listdir(f'{i}/Discord')
        if 'Tokens.txt' in filetokens:
            with open(f"{i}/Discord/Tokens.txt", 'r', encoding="utf-8") as f:
                gg = [g.replace('\r', '') for g in f.readlines()]
                if len(gg) > 0:
                    print(f'[LOG] Найдено {len(gg)} токенов')
                    all_tokens += gg
                else:
                    print('[LOG] Найдено 0 токенов')
        else:
            continue

    elif 'Other' in file:
        othres = os.listdir(f"{i}/Other")
        if 'Discord Token(s).txt' in othres:
            print(i)
            with open(f"{i}/Other/Discord Token(s).txt", 'r', encoding="utf-8",errors='ignote') as f:
                try:
                    gg = [g.replace('\r', '') for g in f.readlines() if "Discord not installed!" and " " and "?" not in g.replace('\r', '') and len(g.replace('\r', '').replace(',','')) == 60]
                except Exception as e:
                    print(f'[LOG] Ошибка {e}\n{i}')
                else:
                    if len(gg) > 0:
                        print(f'[LOG] Найдено {len(gg)} токенов!')
                        all_tokens += gg
                    else:
                        print('[LOG] Найдено 0 токенов!')

    else:
        print('[LOG] Найдено 0 токенов!')



result = list(set(all_tokens))




if not result:
    print(f'[LOG] Финальный результат: найдено 0 токенов!')
else:
    print(f'[LOG] Дубли: Найдено {len(all_tokens)} токенов!')
    with open(f'Result {strftime("%Y.%m.%d %H-%M-%S", gmtime())}.txt', 'w') as f:
        for i in result:
            f.write(i)
    print(f'[LOG] Финальный результат: найдено {len(result)} токенов!')
    print('[LOG] Найти токены вы можете в папке с софтом.')
    
