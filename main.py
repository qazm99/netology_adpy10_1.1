from datetime import date
from application.salary import calculate_salary
from application.db.people import get_employees
if __name__ == '__main__':
    print(f'Добрый день, сегодня {date.today().day}.{date.today().month}.{date.today().year}')
    for employe in get_employees():
        calculate_salary(employe)


