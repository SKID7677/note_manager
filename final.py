
#Создаем словарь для хранения информации о заметке
note = []

# Ввод запрашиваемых данных
username = input("Введите имя пользователя: ")
note.append(username)

#Создание списков заголовков
title = []
for i in range(3):
    titles = input(f"Введите заголовок заметки {i + 1}: ")
    title.append(titles)
note.append(title)
content = input("Введите описание заметки: ")
note.append(content)
status = input("Введите статус заметки (например: 'Активна', 'Выполнена'): ")
note.append(status)
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
note.append(created_date)
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
note.append(issue_date)

#Вывод на экран введенных данных
print(note)
print("\nВы ввели следующие данные:")
print("\nИмя пользователя:", note[0])
for i in title:
    print("Заголовок заметки:", i)
print("Описание заметки:", note[2])
print("Статус заметки:", note[3])
print("Дата создания заметки:", note[4])
print("Дата истечения заметки:", note[5])
