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
