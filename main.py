import os
from dotenv import load_dotenv
from tictactoe import Board
from tictactoe.egtb import Generator
import functools
import operator
from tictactoe.egtb import Reader


def check_password():
    load_dotenv()
    my_pass = os.getenv('password')
    user_pass = input('Введите пароль: ')
    if user_pass == my_pass:
        print('Пароль подтвержден')
    else:
        print('Пароль не подтвержден')


check_password()
print()


def tic_tac_game(board_size):
    print('Игра крестики-нолики')
    generate_endgame_db(board_size)
    board = Board((board_size, board_size), board_size)
    step_count = board_size ** 2
    tic_step = True
    i = 0
    res = 0
    while i < step_count:
        print(board)
        fig = 'Крестик' if tic_step else 'Нолик'
        input_step = input(f'Ход {i + 1}. {fig}. Укажите колонку (0 - 2) и ряд (0 - 2) через пробел: ')
        try:
            step = tuple(list(map(int, input_step.split())))
            board.push(step)
        except:
            print('Ход неправильный. Повторите ввод: ')
            continue

        if i >= board_size * 2 - 1:
            reader = Reader((board_size, board_size), board_size, i + 1)
            res = reader.index(board)
            if res > 0:
                print()
                print(board)
                print(f'Выиграл {fig.lower()}!!!')
                break
        tic_step = not tic_step
        i += 1
        print()
    if res == 0:
        print('Ничья!')


def generate_endgame_db(board_size):
    print('Генерация таблицы результатов. Подождите...')
    dimensions = (board_size, board_size)
    total_squares = functools.reduce(operator.mul, dimensions)
    for index in reversed(range(total_squares + 1)):
        Generator(dimensions, board_size, index)


board_size = 3
tic_tac_game(board_size)
