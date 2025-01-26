import datetime

notes = []

def create_note():
    #Создает новую заметку и возвращает ее в виде словаря
    note = {}

    note['username'] = input('Введите Ваше имя: ')

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
    note['titles'] = titles

    note['content'] = input('Введите описание заметки: ')

    status_all = ["Активна", "Выполнено", "Отложено"]
    while True:
        print("Выберите новый статус заметки:")
        for i, status in enumerate(status_all):
            print(f"{i + 1}. {status}")

        selected_select = input("Ваш выбор: ")
        if selected_select.isdigit() and 1 <= int(selected_select) <= len(status_all):
            note['status'] = status_all[int(selected_select) - 1]
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите номер из списка.")

    # Определение текущей даты
    current_date = datetime.date.today()
    todays_date = current_date.strftime("%d-%m-%Y")
    note['created_date'] = todays_date

    while True:
        issue_date = input('Введите дату истечения срока заметки, в формате dd-mm-yyyy: ')
        try:
            datetime.datetime.strptime(issue_date, "%d-%m-%Y")
            note['issue_date'] = issue_date
            break
        except ValueError:
            print('Неверный формат даты (dd-mm-yyyy)')
    return note


while True:
    note = create_note()
    notes.append(note)
    add_more = input("Хотите добавить ещё одну заметку? (да/нет): ").lower()
    if add_more != "да":
        break

print("\nСписок заметок:")
for i, note in enumerate(notes, 1):
    print(f"\n{i}.")
    print(f"  Имя пользователя: {note['username']}")
    print(f"  Заголовки: {', '.join(note['titles'])}")
    print(f"  Описание: {note['content']}")
    print(f"  Статус: {note['status']}")
    print(f"  Дата создания: {note['created_date'][:5]}")
    print(f"  Дедлайн: {note['issue_date'][:5]}")