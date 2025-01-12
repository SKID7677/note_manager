status = {1:'Выполнено', 2: 'В процессе',3: 'Отложено',4: 'Добавить новый статус' }
mes1 = 'Выберите новый статус для заметки или добавьте свой: '
mes2 = 'Хотите добавить новый статус? 1 - "ДА", 2-"НЕТ": '
print(f"Текущий статус заметки: {status[2]}")
def st_all(): #Создаем функцию для вывода доступных заметок
    print(mes1)
    n = 1
    for stat1 in status.values():
        print(f"{str(n)} - {stat1}")
        n = n + 1
st_all() #вызываем функцию вывода доступных заметок
def slovar_list(): # Считает колличество пар значений в словаре
    len(status)
    sst = len(status)
o_status = True
while o_status: #Запускает цикл по выбору статуса заметки
    mes3 = "Введите номер статуса:"
    status_inputs = input(mes3)
    stat_inp2 = str(status_inputs)
    status_vvod = True
    while status_vvod:  # Запускает цикл по проверке введенных данных
        try:
            len(status)
            sst = int(len(status))
            if int(status_inputs) >= 1 and int(status_inputs) <= sst and int(status_inputs) != 4: #Проверка на введение активных заметок
                stat_inp = int(status_inputs)
                print(f"Статус заметки обновлен на: {status[stat_inp]} ")
                status_vvod = False
                o_status = False
                break
            elif int(status_inputs) == 4: # Проверка на введение  статуса 4
                len(status)
                sst = len(status)
                status_news = True
                while status_news: # Запуск цикла для добавления нового статуса и проверка вводимых данных
                    new_stat = input(mes2)
                    new_stat1 = int(new_stat)
                    if new_stat1 == 1:
                        sst1 = sst + 1
                        new_stat_new = input("Введите название нового статуса: ")
                        status[sst1] = new_stat_new
                        print("Статус добавлен.")
                        status_news = False
                        st_all()
                        break
                    elif new_stat1 == 2:
                        print("Добавление нового статуса отменено.")
                        status_news = False
                        status_vvod = True
                        st_all()
                        #break
                    elif new_stat1 != 1 and new_stat1 != 2:
                        print("Неверный ввод.Повторите.")
                        status_news = True
                    elif new_stat1 == "":
                        print("Неверный ввод.Повторите.")
                        status_news = True
                    else:
                        print("Повторите ввод:")
                        #status_news = False
                        status_vvod = True
                status_news = False
                o_status = True
            elif stat_inp2 == "":
                print("Неверный ввод.Повторите.")
                status_vvod = True
            else:
                status_vvod = True
                print("Неверный ввод")
        except ValueError:
            print("Неверный ввод")
        break
print(status) # Ввывод словаря (не обязательно)

















