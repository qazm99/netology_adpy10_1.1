from time import sleep
from random import random


def calculate_salary(name_people):
    print(f'Cейчас мы посчитаем зарплату {name_people}')
    sleep(2)
    print(f'Ваша зарплата {name_people}: {random()*100000: 0.0f} рублей')
