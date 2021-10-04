def notation_function(number, notation_system):
    result = ''
    while number > 0:
        result += str(number % notation_system)
        number //= notation_system
    return result[::-1]


number = int(input('Введите число: '))
notation_system = int(input('Введите целевую систему счисления: '))
notation_list = [2, 8]
if notation_system in notation_list:
    if number >= 0:
        print(str(number) + ' -> ' + str(notation_function(number, notation_system)))
    elif number == 0:
        print('0 -> 0')
else:
    print('Данная система счисления не поддерживается.')