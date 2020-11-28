# -*- coding: utf-8 -*-
import math
while True:  
    
    # Создание шахматной доски
    chess = []
    for i in range(8):
        temp = []
        for j in range(8):
            if j % 2 == 0:
                temp.append('###')
            else:
                temp.append('___')
        if i % 2 != 0:
            temp.reverse()
        chess.append(temp)

    print('Внимание! Шахматная доска 8х8 клеток, поэтому координаты позиций фигур должны быть числами от 1 до 8!')
    
    # Ввод координат позиций фигур
    while True:  
        try:
            while True:
                k = int(input('Введите номер вертикали первой позиции (при счете слева направо): '))
                if 1<=k<=8: break
            while True:
                l = int(input('Введите номер горизонтали первой позиции (при счете снизу вверх): '))
                if 1<=l<=8: break
            while True:
                m = int(input('Введите номер вертикали второй позиции (при счете слева направо): '))
                if 1<=m<=8: break
            while True:
                n = int(input('Введите номер горизонтали второй позиции (при счете снизу вверх): '))
                if 1<=n<=8: break
            break
        except ValueError:
            print('Введён неправильный символ!')
    
    # Проверка цвета полей
    if chess[8-l][k-1] == chess[8-n][m-1]: color = True
    else: color = False
    
    if chess[8-l][k-1] == '___': chess[8-l][k-1] = '_1_'
    else: chess[8-l][k-1] = '#1#'
    if chess[8-n][m-1] == '___': chess[8-n][m-1] = '_2_'
    else: chess[8-n][m-1] = '#2#'
    
    # Построение шахматной доски
    print('    ________________________')
    for i in range(8):
        print(8 - i, ' |', end='')
        for row in chess[i]:
            print(row, end='')
        print('|')
    print('     A  B  C  D  E  F  G  H')
    
    # Вывод результата проверки цвета полей
    if color == True: print('\nа) Цвет полей одинаковый')
    else: print('\nа) Цвет полей разный')
    
    # Проверка угрозы ферзя в первом поле второму полю
    if l == n or k == m:
        print('б) Ферзь в поле 1 угрожает полю 2')
        ferz = True
    elif ((k > m and l > n) or (k < m and l < n)) and k - l == m - n:
        print('б) Ферзь в поле 1 угрожает полю 2')
        ferz = True
    elif ((k > m and l < n) or (k < m and l > n)) and k + l == m + n:
        print('б) Ферзь в поле 1 угрожает полю 2')
        ferz = True
    else:
        print('б) Ферзь в поле 1 не угрожает полю 2')
        ferz = False
    
    # Проверка угрозы коня в первом поле второму полю
    if color == True: print('в) Конь в поле 1 не угрожает полю 2')
    else:
        if k+2 == m and l+1 == n or k+2 == m and l-1 == n or k-2 == m and l+1 == n or k-2 == m and l-1 == n or k+1 == m and l+2 == n or k+1 == m and l-2 == n or k-1 == m and l+2 == n or k-1 == m and l-2:
            print('б) Конь в поле 1 угрожает полю 2')
        else: print('в) Конь в поле 1 не угрожает полю 2')
        
    # Проверка возможности хода ладьи из первого поля во второе
    if k==m or l==n:
        print('г) Ладья из поля 1 может попасть за один ход в поле 2')
    else:
        print('г) Ладья из поля 1 может попасть за два хода в поле 2, с промежуточным ходом в поле (', k, ',', n, ') или в поле (', m, ',', l, ')', sep='')
        
    # Проверка возможности хода ферзя из первого поля во второе
    if ferz == True:
        print('д) Ферзь из поля 1 может попасть в поле 2 за один ход')
    else:
        print('д) Ферзь из поля 1 может попасть за два хода в поле 2 (варианты промежуточных ходов: поля', sep='', end='')
        for i in range(8):
            I = 7 - i
            for j in range(8):
                del_k = k-1 - j
                del_l = 8-l - I
                del_m = m-1 - j
                del_n = 8-n - I
                try:
                    angle = round(math.degrees(math.acos((del_k * 1) / ((del_k**2 + del_l**2) ** (0.5)))), 5)
                    angle_1 = round(math.degrees(math.acos((del_k * del_m + del_l * del_n) / (((del_k ** 2 + del_l ** 2) * (del_m ** 2 + del_n ** 2)) ** (0.5)))), 5)
                    if (angle_1 == 90 or angle_1 == 45 or angle_1 == 135) and (angle == 45 or angle == 135 or angle == 0 or angle == 90 or angle == 180):
                        print(' (', j+1, ',', 8-I, ')', sep='', end='')
                        if i !=7: print(',', end='')
                except ZeroDivisionError:
                    pass
                
    # Проверка возможности хода слона из первого поля во второе
    if color == False: print('\ne) Слон с поля 1 не может попасть на поле 2')
    elif ((k > m and l > n) or (k < m and l < n)) and k - l == m - n:
        print('n\e) Слон с поля 1 может попасть в поле 2 за один ход')
    elif ((k > m and l < n) or (k < m and l > n)) and k + l == m + n:
        print('n\e) Слон с поля 1 может попасть в поле 2 за один ход')
    else:
        print('\ne) Слон с поля 1 может попасть за два хода в поле 2 (варианты промежуточных ходов: поля', sep='', end='')
        for i in range(8):
            I = 7 - i
            for j in range(8):
                del_k = k-1 - j
                del_l = 8-l - I
                del_m = m-1 - j
                del_n = 8-n - I
                cos = del_k * del_m + del_l * del_n
                try:
                    angle = round(math.degrees(math.acos(del_k / ((del_k **2 + del_m**2) ** (0.5)))), 5)
                    if cos == 0 and (angle == 45 or angle == 135):
                        if j == m and I == n:
                            pass
                        else:
                            print(' (', j+1, ',', 8-I, ')', sep='', end='')
                            if i !=7: print(',', end='')
                except ZeroDivisionError:
                    pass

    # Возможность выбора: продолжение работы программы либо прекращение её работы
    print('\nХотите задать другие координаты полей? Введите 1, если да, введите 0, чтобы завершить выполнение программы.')
    while True:
        try:
            choise = int(input('> '))
            if choise != 1 and choise != 0:
                print('Вы должны ввести 1 или 0!')
            else: break
        except ValueError:
            print('Введён неправильный символ!')
    if choise == 0: break