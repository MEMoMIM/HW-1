import random
import CanClientPay


def car_parameters():
    width = random.randint(1, 3)
    height = random.randint(1, 3)
    print("Размер вашего автомобиля", width, "метр(а) в ширину и", height, "метр(а) высоту")
    if width < 3 and height < 3:
        CanClientPay.can_client_pay()
    else:
        print(f"Извините, ваш автомобиль не сможет проехать на нашу автомойку")
