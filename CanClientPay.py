import random

import SafetyRegulations


def can_client_pay():
    client_money = random.randint(0, 10000)
    cost = 1200
    remains = client_money - cost
    a = cost - client_money
    print(f"Цена помывки 1200 руб.")
    print(f"На вашем счету есть", client_money, "руб.")
    if client_money >= 1200:
        SafetyRegulations.safety_regulations()
        print("..Процедура начинается..")
        print("..Машина с удовольствием моется..")
        print("Машина помылась.")
        print(f"Благодарим вас за пользавание нашей автомойкой. ")
        print(f"На вашем счете осталось", remains, "руб")
    else:
        print(f"Извините, вам не хватает", a, "руб.")
