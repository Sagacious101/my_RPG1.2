import os



def in_shop(player:tuple) -> tuple:
    #делаем сылки игрока
    name = player[0]
    money = player[1]
    xp = player[2]
    hp = player[3]
    mp = player[4]
    damage = player[5]
    potions = player[6]
    while True:
        os.system("cls")
        #печатаем персонажа
        print("Состояние персонажа:")
        print(f"Имя: {name}")
        print(f"Деньги: {money}")
        print(f"Опыт: {xp}")
        print(f"HP: {hp}")
        print(f"MP: {mp}")
        print(f"АТК: {damage}")
        print(F"Зелья: {potions}\n")

        #печатаем ситуацию
        print(f"{name} приехал в лавку снаряжения\n")

        #печатаем выборы
        print("1 - Купить зелье лечения за 3 монеты")
        print("2 - Выйти из лавки обратно в город\n")

        # проверяем выбор
        answer = input("Введите номер варианта и нажмите ENTER: ")
        if answer == "1":
            if money >= 3:
                money -= 3
                potions += 1

            else:
                print("Недостаточно монет!\n")
                input("Нажмите ENTER чтобы продолжить: ")
        elif answer == "2":
                return (name, money, xp, hp, mp, damage, potions)



