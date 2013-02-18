#Функция создания таблицы
def tabl ():
    file = open(file_name + '.txt')
    # Вывод заголовка таблицы на экран
    print ("+{0:^20}+{0:^20}+{0:^20}+".format('-'*20))
    print ("|{0:^20}|{1:^20}|{2:^20}|".format('Число', 'Квадрат','Куб'))
    print ("+{0:^20}+{0:^20}+{0:^20}+".format('-'*20))
    # Обработка исходных данных и формирование таблицы
    for line in file:
        line = line.rstrip('\n')
        try:
            line = float(line)
        except ValueError:
            #print ('|{0:<62}|'.format (line + ' не является числом'))
            #print ("+{0:^20}+{0:^20}+{0:^20}+".format('-'*20))
            continue
        print ("|{0:>20.3f}|{1:>20.3f}|{2:>20.3f}|".format(line, line**2, line**3))
        print ("+{0:^20}+{0:^20}+{0:^20}+".format('-'*20))
#Функция считывания слов из файла, их сортировки по второму символу и записи отсортированного списка в файл.
def sortTabl():
    file = open(file_name + '.txt')
    lst = []
    for line in file:
        line = line.rstrip('\n')
        try:
            line = float(line)
        except ValueError:
            line = str(line)
            lst.append(line)   
    lst.sort(key=lambda x: x[1:])
    f = open(r"file.txt", "w")
    f.writelines(str(lst))
    f.close
    print('Файл записан успешно')
while True:
    file_name = input ('Введите имя файла: ')
    #Открытие файла с данными
    try:
        file = open(file_name + '.txt')
    # Если имя файла введено неправильно, то программа выведет следующее сообщение
    except:
        print ('Неправильно введено имя файла. Ввести ещё раз?')
        ok = input ()
        if ok not in ('y', 'ye', 'yes'):
            print ('Bye-bye!')
            start = False
            break
    else:
        start = True
        break
while start:
    menuk = input("выход - 0, таблица квадратов и кубов - 1, сортировка слов по второму символу - 2: ")
    menu = int (menuk)
    if menu == 1:
        tabl()
    elif menu == 0:
        print ('Good bye')
        break
    elif menu == 2:
        sortTabl()
    else:
        print ('Нужно ввести 0 или 1 или 2')
