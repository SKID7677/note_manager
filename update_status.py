#Создаем пустой список заголовков
note = []
#Запрос имени пользователя и добавление в список
username = input('Введите Ваше имя: ')
note.append(username)

titles = set()
#Цикл для ввода и добавления заголовков
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
#Ввод и добавление описания заметок в список
content = input('Введите описание заметки: ')
note.append(content)

status_all = ["Активна", "Выполнено", "Отложено"]

while True:
    print("Выберите новый статус заметки:")
    for i, status in enumerate(status_all):
        print(f"{i + 1}. {status}")

    selected_select = input("Выбран статус: ")

    if selected_select.isdigit() and 1 <= int(selected_select) <= len(status_all):
        status_i = status_all[int(selected_select) - 1]
        note.append(status_i)
        break
    else:
        print("Некорректный ввод. Пожалуйста, введите номер из списка.")
print("\nСтатус заметки успешно обновлен на:", note[3])

created_date = input('Введите дату создания заметки, в формате dd-mm-yyyy: ')
note.append(created_date)

issue_date = input('Введите дату дедлайна заметки, в формате dd-mm-yyyy: ')
note.append(issue_date)

print("-----")

print("\nИмя пользователя:", note[0])
print("Содержание заметки:", note[2])
print("Статус:", note[3])
print("Дата создания заметки:", note [4][:5])
print("Дата дедлайна:", note [5][:5])
print("\nЗаголовки Ваших заметок:")
for title in note[1]:
    print(f"- {title}")