import random
import os


def random_list(a):
    for num in range(3):
        a.append(list())
        for num_sec in range(3):
            a[num].append(0)
    a[random.randint(0, 2)][random.randint(0, 2)] = 1
def prnt():
    print('[', cars[0], ']', '[', cars[1], ']', '[', cars[2], ']', '    [', cars_bot[0], ']', '[', cars_bot[1], ']', '[', cars_bot[2], ']')
    print('[', cars[3], ']', '[', cars[4], ']', '[', cars[5], ']', '    [', cars_bot[3], ']', '[', cars_bot[4], ']', '[', cars_bot[5], ']')
    print('[', cars[6], ']', '[', cars[7], ']', '[', cars[8], ']',  '    [', cars_bot[6], ']', '[', cars_bot[7], ']', '[', cars_bot[8], ']')






cars = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cars_bot = [1, 2, 3, 4, 5, 6, 7, 8, 9]
prnt()
player = 0
res = []
res_bot = []
count = 0
random_list(res)
random_list(res_bot)
lst = {
    1: res[0][0],
    2: res[0][1],
    3: res[0][2],
    4: res[1][0],
    5: res[1][1],
    6: res[1][2],
    7: res[2][0],
    8: res[2][1],
    9: res[2][2]}
lst_bot = {
    1: res_bot[0][0],
    2: res_bot[0][1],
    3: res_bot[0][2],
    4: res_bot[1][0],
    5: res_bot[1][1],
    6: res_bot[1][2],
    7: res_bot[2][0],
    8: res_bot[2][1],
    9: res_bot[2][2]}
while True:
    if player == 0:
        finish = int(input('Введите координату удара (от 1-9): '))
        if lst[finish] == 1:
            print('Победил пользователь')
            print(f'{count} попыток использовано')
            quit()
        else:
            cars[finish - 1] = 'X'
            os.system('CLS')
            prnt()
            print('Вы промахнулись, попробуйте еще раз')
            count += 1
            player = 1

    else:
        print('Ходит бот')
        finish_bot = random.randint(1, 9)
        if lst_bot[finish_bot] == 1:
            print('БОТ ПОБЕДИЛ')
            quit()
        else:
            cars_bot[finish_bot - 1] = 'X'
            os.system('CLS')
            prnt()
            print('Бот промахнулся')
            player = 0



