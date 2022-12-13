# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота



from random import *
import os

text = ('Добро пожаловать на игру!!!\n'
        'Правила иргы:\n'
        'На столе лежит 2021 конфета, вы берете их поочереди,\n'
        'ВНИМАНИЕ!!!, за один раз можно взять не больше 28 конфет.\n'
        'Выигрывает тот, кто последним ходом заберет все конфеты.\n')
print(text)


def player_vs_player():
    candies_total = 2021
    max_take = 28
    count = 0
    player_1 = input('\nВедите имя Игрока 1: ')
    player_2 = input('\nВедите имя Игрока 2: ')

    print('\nСначала жеребьёвка.\n')

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f'{lucky} ты ходишь первым !')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\n {lucky} = '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nВнимательнее!!! Можно взять только {max_take} конфет {lucky}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна столе еще {candies_total}')
            count = 1
        else:
            print('Конфеты кончились!!!')

        if count == 1:
            step = int(input(f'\n {loser} '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nВнимательнее!!! Можно взять только {max_take} конфет {loser}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна столе еще {candies_total}')
            count = 0
        else:
            print('Конфеты кончились!!!')

    if count == 1:
        print(f'{loser} ПОБЕДИЛ')
    if count == 0:
        print(f'{lucky} ПОБЕДИЛ')


player_vs_player()


def player_vs_bot():
    candies_total = 2021
    max_take = 28
    player_1 = input('\nВведите имя: ')
    player_2 = 'Компьютер'
    players = [player_1, player_2]
    print('\nСначала жеребьёвка.\n')

    lucky = randint(-1, 0)

    print(f'{players[lucky+1]} ты ходишь первым !')

    while candies_total > 0:
        lucky += 1

        if players[lucky % 2] == 'Компьютер':
            print(
                f'\nХодит {players[lucky%2]} \nНа столе {candies_total}.: ')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total//28
                step = candies_total - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take - 1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1, 28)
            print(step)
        else:
            step = int(
                input(f'\nХодит  {players[lucky%2]} \nНа столе {candies_total} :  '))
            while step > max_take or step > candies_total:
                step = int(input(
                    f'\nВнимательнее!!! Можно взять только {max_take} конфет, попробуй еще раз: '))
        candies_total = candies_total - step

    print(f'На столе осталось {candies_total} \nПобедил {players[lucky%2]}')


player_vs_bot()