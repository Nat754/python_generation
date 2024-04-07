from random import randint


def is_valid(s, k):
    try:
        num = int(s)
    except ValueError:
        num = 0
    return 0 < num <= k


def game():
    k = 0
    while k == 0:
        print(f'До какого числа мне загадать?)')
        try:
            k = int(input())
        except ValueError:
            print('Это не число больше 0')
    print(f'Хорошо 😜 Я задумала число от 1 до {k} 🙈\nУгадай!')
    number = randint(1, k)
    flag = 1
    step = 0
    while flag == 1:
        num = input()
        step += 1
        if is_valid(num, k):
            if int(num) > number:
                print(f'🔻 Ваше число больше загаданного, попробуйте еще разок')
            elif int(num) < number:
                print(f'🔺️ Ваше число меньше загаданного, попробуйте еще разок')
            else:
                print(f'💃 Вы угадали, поздравляем! 💃\nКоличество попыток: {step}👌')
                flag = 0
        else:
            print(f'❌А может быть все-таки введем целое число от 1 до {k}?❌\nУгадай!')
    print(f'Хотите сыграть еще? (напишите Да)')


print(f'Добро пожаловать в числовую угадайку')
game()
while input().lower() == 'да':
    game()
print(f'Спасибо, что играли в числовую угадайку. Еще увидимся...🤗\n')
