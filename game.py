import os
import shop #импортируем файл shop.py


def create_hero(name="Искатель", money=5, xp=0, hp=20, mp=20, damage=3, potions=3) -> tuple:

    return (name, money, xp, hp, mp, damage, potions)


def start_game():
    """
    Создаёт персонажа:
        player_name - имя игрока
        player_money - деньги игрока
        player_xp - опыт игрока
        player_hp - жизни игрока, >= 0 иначе игра заканчивается
        player_mp - мана персонажа
        player_damage - урон игрока
        player_potions - зелья лечения здоровья
            Doto:
        player_items - вещи игрока
    Запускает игру
    Игра контролируется переменной is_game
    """
    """
    os.system("cls")
    player_money = 5
    player_xp = 0
    player_hp = 20
    player_mp = 20
    player_damage = 3
    player_potions = 3
    player_name = input("Введите имя игрока и нажмите ENTER: ")
    if not player_name: player_name = "Богатырь"
    """

    player = create_hero()
    os.system("cls")

    #главный цикл игры
    is_game = True
    while is_game:
        os.system("cls")
        print("Персонаж: \n")
        print(f"Имя: {player[0]}")
        print(f"Деньги: {player[1]}")
        print(f"Опыт: {player[2]}")
        print(f"HP: {player[3]}")
        print(f"MP: {player[4]}")
        print(f"АТК: {player[5]}")
        print(F"Зелья: {player[6]}\n")
        # показываем вариант
        print(f"{player[0]} приехал в стартовый город.")
        print("0 - Выйти в главное меню")
        print("1 - Поехать в магический лес")
        print("2 - Поехать в таверну(кости)")
        print("3 - поехать в лавку снаряжения\n")
        answer = input("Введите номер ответа и нажмите ENTER: ")

        #проверяем ответ
        if answer == "0":
            break
        elif answer == "1":
            print("Вы прибыли в магический лес")
        elif answer == "2":
            print("Вы приехали в таверну")
        elif answer == "3":
            player = shop.in_shop(player)


if __name__ == "__main__":
    print("Этот модуль запустили не посредственно")
