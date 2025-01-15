from data import *
import random
import time


def fight (current_enemy):
    round = random.randint(1, 2)
    enemy = enimes[current_enemy]
    enemy_hp = enimes[current_enemy]["hp"]
    print(f"Противник - {enemy["name"]}: {enemy["script"]}")
    input("Нажмите Enter, чтобы продолжить: ")
    print()

    while player["hp"] > 0 and enemy_hp > 0:
        if round %2 == 1:
            print(f"{player["name"]} атакует {enemy["name"]}")
            crit = random.randint(1, 100)
            if crit < player["luck"]:
                enemy_hp -= player["attack"] * 3
            else:
                enemy_hp -= player["attack"]
            time.sleep(1)
            print(f"{player['name']} - {player['hp']}\n{enemy['name']} - {enemy_hp}")
            print()
            time.sleep(1)
        else:
            print(f"{player["name"]} атакует {enemy["name"]}")
            player["hp"] -= enemy["attack"]
            time.sleep(1)
            print(f"{player['name']} - {player['hp']}\n{enemy['name']} - {enemy_hp}")
            print()
            time.sleep(1)
        round += 1

    if player["hp"] > 0:
        print(f'Противник - {enemy['name']} - {enemy['win']}')
    else:
        print(f'Противник - {enemy['name']} - {enemy['loss']}')
    player["hp"] = 100
    return current_enemy

def training(training_type):
    skip = "2"
    if items["2"]["name"] in player["inventory"]:
        skip = input("Хотите пропустить тренировку? 1 - да, 2 - нет")
    if skip == 2:
        for i in range(0, 101, 20):
            print(f'Тренировка заверена на {i}%')
            time.sleep(1.5)
    if training_type == '1':
        player["attack"] += 2
        print(f'Тренировка окончена! Теперь ваша величина атаки равна {player["attack"]}')
    elif training_type == '2':
        player["armor"] -=0.09
        print(f'Тренировка окончена! Теперь броня поглащает {100 - player["armor"] * 100}% урона')
    print()


def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"]}ед.) равен {player["luck"]}')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')

def display_enemy(current_enemy):
    enemy = enimes[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Веилична атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')


def display_inventory():
    print("У вас есть:")
    for value in player["inventory"]:
        print(value)
    print(f"У вас есть {player["money"]} монет")
    print()
    if "Зелье удачи" in player["inventory"]:
        potion = input("Хотите выпить Зелье удачи? 1 - да, 2 - нет ")
        if potion == 1:
            player["luck"] += 7
            print(f"Готово! Теперь ваш шанс нанести критический урон равен {player['luck']}")
            player['inventory'].remove("Зелье удачи")



def shop():
    print("Добро пожаловать в лавку, что желаете приобрести?")
    print(f"У вас {player['money']} монет")
    for key, value in items.items():
        print(f"{key} - {value['name']}: {value['price']}")

    item = input()
    if item in player["inventory"]:
        print(f"У вас уже есть {items[item]['name']}")
    elif player["money"] >= items[item]["price"]:
        print(f"Поздравляю, вы приобрели {items[item]['name']}")
        player["inventory"].append(items[item]['name'])
        player["money"] -= items[item]["price"]
    else:
        print("Не хватает монет для покупки")
    print()
    print("Буду ждать тебя снова, путник")
    print()


def earn():
    print("Добро пожаловать на завод. У вас есть 67% шанс зароботать 500 монет, 33% потерять 500 монет")
    result = random.randint(0, 100)
    time.sleep(1.5)
    print("Результат...")
    time.sleep(3)
    if result < 67:
        print("Вы получили 500 монет!")
        player['money'] += 500
    else:
        print("Вы потеряли 500 монет!")
        player['money'] -= 500
    print()
    print(f"Осталось {player['money']} монет")
    print()