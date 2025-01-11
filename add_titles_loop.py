# Ввод запрашиваемых данных
username = input("Введите имя пользователя: ")
#title = input("Введите заголовок заметки: ")
titles = [] # Создаем пустой список заголовков
active = True # Создаем цикл для ввода заголовков
while active:
    title = input(f"Введите заголовок заметки : ")
    titles.append(title)
    if title == "": #Проверяем на ввод пустого поля
        titles.pop()
        print("Ввод пустого поля не допустим.")
    questing = 'Создать еще одну заметку? Если  не создавать введите "нет": '
    quest = input(questing)
    if quest == 'нет':
        active = False
print('Заголовки заметки:') #Создаем цикл для вывод введенных заголовков в список
for titles1 in titles:
    print("-" + titles1)

