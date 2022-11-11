from random import randint, choice

first_names = ("Ван", "Тан", "Брысь", "Дыг", "Дрын")
last_name = ("Зловонный", "Дикий", "Яросный", "Ужасный")


def create_hero(
        name=None,
        money=None,
        xp=None,
        hp=None,
        mp=None,
        damage=None,
        potions=None
        ) -> tuple:
    if not name:
        name = f"({choice(first_names)}, {choice(last_name)})"
    if not money:
        money = randint(0, 500)
    if not xp:
        xp = randint(0, 100)
    if not hp:
        hp=20
    if not mp:
        mp=randint(10, 20)
    if not damage:
        damage=randint(1, 5)
    if not potions:
        potions = randint(0, 2)


    return (name, hp, xp, damage, money, potions)



player = create_hero(name="Искатель", hp=20, xp=0, damage=5, money=50, potions=5)
enemy_0 = create_hero()
enemy_1 = create_hero()
enemy_2 = create_hero()
print(player)
print(enemy_0)
print(enemy_1)
print(enemy_2)