import finv
import random
import sys
from enemies import get_enemy, get_player

story = """
███████ ████████  ██████  ██████  ██    ██ 
██         ██    ██    ██ ██   ██  ██  ██  
███████    ██    ██    ██ ██████    ████   
     ██    ██    ██    ██ ██   ██    ██    
███████    ██     ██████  ██   ██    ██    
                                           
                                           
"""

def try_run(player):
    attempt = random.randint(1, 2)
    if attempt == 1:
        print("Вы смогли сбежать!", end='')
        input()
        print('Настолько удачно, что вы убежали за пространство и время, которое нас окружает. Тут темно и тихо. Ау, есть тут кто?', end='')
        input()
        print('\nМы, в 9ПР-1.23, хоти поблагодарить тебя за игру в TES6. Это было незабываемое приключение, в будущеем, мы наклипаем ещё такого кала в терминале, не теряйтесь!')
        input()
        exit()
        sys.exit(1)
    else:
        player["health"] -= 1
        print("Попытка не удалась! Вам нанесли урон", end='')
        input()

def attack(player, enemy):
    options = [1, 2, 3]
    botint = random.choice(options)
    print(f"\nЗдоровье: {player['health']}")
    print(f"Выбор врага: {botint}")
    print(f"Здоровье врага: {enemy['health']}")
    
    try:
        playerint = int(input("""\nВведите вариант атаки:
        1. Камень
        2. Ножницы
        3. Бумага
        """))
    except ValueError:
        print("Некорректный ввод!")
        return

    if botint == playerint:
        print("Ничья!")
    elif (botint == 1 and playerint == 2) or (botint == 2 and playerint == 3) or (botint == 3 and playerint == 1):
        player["health"] -= enemy["damage"]
        print(f"Ваше здоровье понижено на {enemy['damage']}", end='')
        input()
    else:
        enemy["health"] -= player["damage"]
        print(f"Здоровье врага понижено на {player['damage']}", end='')
        input()

def fight(enemy_type):
    player = get_player()
    enemy = get_enemy(enemy_type)
    
    while player["health"] > 0 and enemy["health"] > 0:
        choice = input("""\nВыберите действие:
        1. Атака
        2. Бежать
        3. Инвентарь               
        """).strip()
        
        if choice == "1":
            attack(player, enemy)
        elif choice == "2":
            try_run(player)
        elif choice == "3":
            buff = finv.inenit()
            player[buff['stat']] += buff['buff']
        else:
            print("Некорректный ввод!")
        
    if enemy["health"] <= 0:
        global result
        result = 'win'
        global choice_final
        try: choice_final = int(input("""Ты победил! Каков итог?
        1. Добить
        2. Пощадить
        """))
        except ValueError:
            print("Некорректный ввод!")
            print('Из-за того, что игрок не читал нормально диалоги, а бесконечно нажимал на Enter, у Сырбыча произошёл сердечный приступ', end='')
            input()
            print('Он упал на спину и долго, мучительно долго, захлёбывался своей слюной', end='')
            input()
            print('\nМы, в 9ПР-1.23, хоти поблагодарить тебя за игру в TES6. Это было незабываемое приключение, в будущеем, мы наклипаем ещё такого кала в терминале, не теряйтесь!')
            input()
            exit()
            sys.exit(1)
        print(story)

    elif player["health"] <= 0:
        result = 'lose'
        print("Ты проиграл!", end='')
        input()

