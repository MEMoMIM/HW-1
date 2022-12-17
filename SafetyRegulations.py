import random


def safety_regulations():
    print("закройте двери и окна")
    sf = random.randint(0, 100)
    if sf > 90:
        print("У вас не закрыта какая-то дверь проверьте ещё раз")
