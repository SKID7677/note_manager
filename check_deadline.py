import datetime #импортрируем библиотеку дататайм
from datetime import date

current_date = datetime.date.today() #Создаем и выводим переменную с текущей датой
print(f"Текущая дата:  {current_date.strftime('%d-%m-%Y')}")
#print(type(current_date))

issue_date = input('Введите дату дедлайна в формате дата-месяц-год:')
date_obj = datetime.datetime.strptime(issue_date, '%d-%m-%Y').date()
#print(date_obj)
#print(type(date_obj))

difference_date = date_obj - current_date
#print(difference_date.days)
difference_date1 = int(difference_date.days)


while True:
    if difference_date1 == 0:
        print("Дата дедлайна сегодня.")
        break
    elif difference_date1 == 1:
        print("До дедлайна остался 1 день.")
        break
    elif difference_date1 >= 2 and difference_date1 <= 4:
        print(f"До дедлайна осталось {difference_date.days} дня.")
        break
    elif difference_date1 >= 5:
        print(f"До дедлайна осталось {difference_date.days} дней.")
        break
    elif difference_date1 == -1:
        print("Дедлайн закончился 1 день назад.")
        break
    elif difference_date1 >= -4 and difference_date1 <= -2:
        ddd = difference_date1 - difference_date1 - difference_date1
        print(f"Дедлайн закончился {ddd} дня назад.")
        break
    elif difference_date1 <= 5:
        ddd = difference_date1 - difference_date1 - difference_date1
        print(f"Дедлайн закончился {ddd} дней назад.")
        break






