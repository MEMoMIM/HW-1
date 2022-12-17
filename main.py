import CarParameters
import ClientsGrade

print("Добро пожвловать на автомойку")
print("Желаете ли вы воспользоваться нашей автомойкой?")
print("1-да,2-нет")
answer = int(input())
if answer == 1:
    CarParameters.car_parameters()
else:
    print("Удачи на дорогах")
ClientsGrade.clients_grade()
