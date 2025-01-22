import datetime

note = []

username = input('Введите Ваше имя: ')
note.append(username)

titles = set()

while True:
    title = input("Введите заголовок (или оставьте пустым для завершения): ")

    if title:
        if title in titles:
            print("Такой заголовок уже существует. Пожалуйста, введите другой заголовок.")
        else:
            titles.add(title)
    else:
        break
note.append(titles)

content = input('Введите описание заметки: ')
note.append(content)

status_all = ["Активна", "Выполнено", "Отложено"]

while True:
    print("Выберите новый статус заметки:")
    for i, status in enumerate(status_all):
        print(f"{i + 1}. {status}")

    selected_select = input("Ваш выбор: ")

    if selected_select.isdigit() and 1 <= int(selected_select) <= len(status_all):
        selected_status = status_all[int(selected_select) - 1]
        note.append(selected_status)
        break
    else:
        print("Некорректный ввод. Пожалуйста, введите номер из списка.")
print("\nСтатус заметки успешно обновлен на:", note[3])

while True:
    created_date = input('Введите дату создания заметки, в формате dd-mm-yyyy: ')
    try:
      datetime.datetime.strptime(created_date, "%d-%m-%Y")
      break
    except ValueError:
      print('Неверный формат даты (dd-mm-yyyy)')
note.append(created_date)


while True:
    issue_date = input('Введите дату истечения срока заметки, в формате dd-mm-yyyy: ')
    try:
      datetime.datetime.strptime(issue_date, "%d-%m-%Y")
      break
    except ValueError:
      print('Неверный формат даты (dd-mm-yyyy)')
note.append(issue_date)


print("Имя пользователя:", note[0].title())
print("Содержание заметки:", note[2])
print("Статус:", note[3])
print("Дата создания заметки:", note [4][:5])
print("Дата дедлайна:", note [5][:5])
print("\nЗаголовки заметки:")
for title in note[1]:
    print(f"- {title}")

# Функция проверки дедлайна
def check_deadline(issue_date):
    try:
        today = datetime.date.today()
        issue_date_obj = datetime.datetime.strptime(issue_date, "%d-%m-%Y").date()
        days_difference = (issue_date_obj - today).days

        if days_difference <= -5:
            days_diff = days_difference - days_difference - days_difference
            print(f"Внимание! Дедлайн истёк {days_diff} дней назад.")
        elif days_difference >= -4 and days_difference <= -2:
            days_diff = days_difference - days_difference - days_difference
            print(f"Внимание! Дедлайн истёк {days_diff} дня назад.")
        elif days_difference == -1:
            days_diff = days_difference - days_difference - days_difference
            print(f"Внимание! Дедлайн истёк {days_diff} день назад.")
        elif days_difference == 0:
            print("Внимание! Дедлайн сегодня.")
        elif days_difference == 1:
            print(f"Внимание! До дедлайна остался {days_difference} день.")
        elif days_difference >= 2 and days_difference <= 4:
            print(f"Внимание! До дедлайна осталось {days_difference} дня.")
        else:
            print(f"До дедлайна осталось {days_difference} дней.")
    except ValueError:
        print("Неверный формат даты. Пожалуйста, введите дату в формате dd-mm-yyyy.")

# Вызов функции проверки дедлайна
check_deadline(note[5])