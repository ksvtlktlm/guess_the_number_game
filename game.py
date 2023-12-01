def continue_game():
    while True:
        print('Игра окончена! Хочешь сыграть еще разок? "д" - да, "н" - нет...')
        ans = input()
        if ans == 'д' or ans == 'l':
            guess_the_number()
        if ans == 'н' or ans == 'y':
            print('Пока-пока!')
            break


def is_valid_borders(border):
    if border.isdigit():
        return True
    else:
        return False


def is_valid(user_number, a, b):
    return user_number.isdigit() and int(user_number) in range(a, b+1)


def guess_the_number():
    import random

    print('Добро пожаловать в числовую угадайку! Попробуй угадать число, которое загадала программа.''\n'
          'У тебя будет 7 попыток.')
    print('Как тебя зовут?')
    name = input()
    print()
    print(f'{name}, введи левую границу диапазона: ')
    a = input()
    flag_bord = is_valid_borders(a)
    while not flag_bord:
        print('Нужно ввести число.')
        a = input()
        flag_bord = is_valid_borders(a)
    if flag_bord:
        a = int(a)
    print('А теперь введи правую: ')
    b = input()
    flag_bord = is_valid_borders(b)
    while not flag_bord:
        print('Нужно ввести число.')
        b = input()
        flag_bord = is_valid_borders(b)
    if flag_bord:
        b = int(b)
    while b < a or a == b:
        print('Правая граница диапазона должна быть больше левой!')
        print('Введи правую границу:')
        b = input()
        flag_bord = is_valid_borders(b)
        while not flag_bord:
            print('Нужно ввести число.')
            b = input()
            flag_bord = is_valid_borders(b)
        if flag_bord:
            b = int(b)
    hidden_number = random.randint(a, b)
    count = 0
    attempt = 7
    print('Какое число загадала программа?')
    user_number = input()
    flag = is_valid(user_number, a, b)
    while not flag:
        print(f'Введи число от {a} до {b}!')
        user_number = input()
        flag = is_valid(user_number, a, b)
    user_number = int(user_number)

    while True:
        if user_number == hidden_number:
            count += 1
            if count >= 5:
                print(f'Верно! Было не просто, но ты угадал(а) за {count} попыток. Молодец, {name}')
                break
            if 2 <= count <= 4:
                print(f'{name}, верно! В шоу "Интуиция" тебе не было бы равных! Ты угадал(а) за {count} попытки.')
                break
            else:
                print(f'Вот это да! Ты угадал(а) всего за {count} попытку. Мое почтение, {name}!')
                break

        if user_number > hidden_number:
            attempt -= 1
            if attempt == 0:
                print(f'В этот раз не повезло! Загаданное число - {hidden_number}.')
                break
            print('Слишком много, попробуй еще раз.')
            user_number = input()
            flag = is_valid(user_number, a, b)
            while not flag:
                print(f'Введи число от {a} до {b}!')
                user_number = input()
                flag = is_valid(user_number, a, b)
            user_number = int(user_number)
            count += 1
        elif user_number < hidden_number:
            attempt -= 1
            if attempt == 0:
                print(f'В этот раз не повезло! Загаданное число - {hidden_number}.')
                break
            print('Слишком мало, попробуй еще раз.')
            user_number = input()
            flag = is_valid(user_number, a, b)
            while not flag:
                print(f'Введи число от {a} до {b}!')
                user_number = input()
                flag = is_valid(user_number, a, b)
            user_number = int(user_number)
            count += 1


guess_the_number()
print()
continue_game()