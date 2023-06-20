import random


board = [' ' for i in range(9)]     # создаем пустую доску для игры
player1_marker = None   # маркер 1 игрока
player2_marker = None   # маркер 2 игрока
current_player = None   # текущий игрок


def print_board():
    print('_____________')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('_____________')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('_____________')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('_____________')


def choose_mode():
    mode = None
    while mode not in ('1', '2'):
        mode = input('\nВыберете режим игры:\n1) Человек - человек\n2) Человек - компьютер\nВведите номер режима: ')
    return mode


def choose_marker():
    global player1_marker, player2_marker
    while player1_marker not in ('X', 'O'):
        player1_marker = input('Игрок 1, выберете маркер Х или О: ').upper()
        if player1_marker not in ('X', 'O'):
            print('Выберете Х или О (eng)')
        if player1_marker == 'X':
            player2_marker = 'O'
        else:
            player2_marker = 'X'


def first_player():
    global current_player
    if random.randint(0, 1) == 0:
        current_player = 'player_1'
    else:
        current_player = 'player_2'
    print(f'{current_player} ходит первым')


def player_move():
    global current_player, board
    while True:
        move = input(f'{current_player}, введите номер ячейки для хода (1-9): ')
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print('Некорректный ввод. Выберете номер ячейки от 1 до 9')
            continue
        move = int(move) - 1
        if board[move] != ' ':
            print('Эта ячейка уже занята')
        else:
            if current_player == 'player_1':
                board[move] = player1_marker
            else:
                board[move] = player2_marker
            break


# версия с легким ботом (ставит свою метку рандомно)
def computer_move():
    global board
    available_move = [i for i in range(9) if board[i] == ' ']
    move = random.choice(available_move)
    board[move] = player2_marker
    print(f'Компьютер выбрал ячейку {move + 1}.')


def check_win(board, player):
    # Проверяем горизонтальные, вертикальные и диагональные линии
    if(
        (board[0] == board[1] == board[2] == player) or
        (board[3] == board[4] == board[5] == player) or
        (board[6] == board[7] == board[8] == player) or
        (board[0] == board[3] == board[6] == player) or
        (board[1] == board[4] == board[7] == player) or
        (board[2] == board[5] == board[8] == player) or
        (board[0] == board[4] == board[8] == player) or
        (board[2] == board[4] == board[6] == player)
    ):
        return True
    return False


# функция проверки ничьей
def check_tie():
    global board
    if ' ' not in board:
        return True
    return False


# функция смены текущего игрока
def swich_player():
    global current_player
    if current_player == 'player_1':
        current_player = 'player_2'
    else:
        current_player = 'player_1'


def play():
    print('\nДОБРО ПОЖАЛОВАТЬ в игру крестики-нолики!')
    mode = choose_mode()
    choose_marker()
    first_player()
    print_board()
    while True:
        if current_player == 'player_1' or (current_player == 'player_2' and mode == '1'):
            player_move()
        else:
            computer_move()

        print_board()
        
        if check_win(board, player1_marker):
            print('Игрок 1 победил!!!')
            break
        elif check_win(board, player2_marker):
            if mode == '1':
                print('Игрок 2 победил!!!')
            else:
                print('Компьютер победил!!!')
            break
        elif check_tie():
            print('Ничья')
            break
        else:
            swich_player()


play()