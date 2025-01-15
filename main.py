import random
import time
from helpers import *
from data import *

name = input("Как тебя звать, путник?: ")
player["name"] = name
#карент енеми это противник по списку, например волк-0
current_enemy = 0


while True:
    action = input('''Выбери:
1 - В бой
2 - Тренировка
3 - инфо об игроке 
4 - инфо об противнике 
5 - Инвентарь
6 - Магазин
7 - На завод
''')
    if action == '1':
        current_enemy = fight(current_enemy)
        if current_enemy == 3:
            break
    elif action == '2':
        training_type = input('''
1 - тренировать атаку
2 - тренировать оборону
''')
        training(training_type)
    elif action == '3':
        display_player()
        print()
    elif action == '4':
        display_enemy(current_enemy)
        print()
    elif action == '5':
        display_inventory()
        print()
    elif action == '6':
        shop()
        print()
    elif action == '7':
        earn()
        print()
    print()