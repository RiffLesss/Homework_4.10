def change():
    try:
        amount = int(input('Введите сумму '))
    except ValueError:
        print('Ошибка! Изначальная сумма должна быть числом.')
        print('Попробуйте ещё раз.')
        change()
    else:
        if amount > 0:
            count_500 = 0
            count_200 = 0
            count_100 = 0
            count_10 = 0
            count_5 = 0
            count_2 = 0
            count_1 = 0
            while amount >= 500:
                amount -= 500
                count_500 += 1
            while amount >= 200:
                amount -= 200
                count_200 += 1
            while amount >= 100:
                amount -= 100
                count_100 += 1
            while amount >= 10:
                amount -= 10
                count_10 += 1
            while amount >= 5:
                amount -= 5
                count_5 += 1
            while amount >= 2:
                amount -= 2
                count_2 += 1
            while amount >= 1:
                amount -= 1
                count_1 += 1
            if count_500 > 0 or count_200 > 0 or count_100 > 0:
                print('Купюры: ')
                if count_500 > 0:
                    for i in range(count_500):
                        print(500, end=' ')
                if count_200 > 0:
                    for i in range(count_200):
                        print(200, end=' ')
                if count_100 > 0:
                    for i in range(count_100):
                        print(100, end=' ')
                print()
            if count_10 or count_5 or count_2 or count_1:
                print('Монеты: ')
                if count_10 > 0:
                    for i in range(count_10):
                        print(10, end=' ')
                if count_5 > 0:
                    for i in range(count_5):
                        print(5, end=' ')
                if count_2 > 0:
                    for i in range(count_2):
                        print(2, end=' ')
                if count_1 > 0:
                    for i in range(count_1):
                        print(1, end=' ')
        else:
            print('Ошибка! Изначальная сумма должна быть положительной.')
            print('Попробуйте ещё раз.')
            change()


change()