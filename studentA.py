b = [[' ',' ',' ',' ',' '],
     [' ',' ',' ',' ',' '],
     [' ',' ',' ',' ',' '],
     [' ',' ',' ',' ',' '],
     [' ',' ',' ',' ',' ']]

def print_board(board):
    for y in range(0, 5):
        print('--------------------------')
        print('| ', end="")
        for x in range(0, 5):
            print(board[y][x], ' | ', end="")
        print("")
    print('--------------------------')

def is_game_over(board):
    for y in range(0, 5):
        if all(ele == 'o' for ele in board[y]):
            return 'o'

    flag = True
    for i in range(0, 4):
        if board[i][i] is not board[i+1][i+1]:
            flag = False
    if flag is True:
        return board[2][2]
    flag = True
    for i in range(0, 4):
        if board[4-i][i] is not board[4-i-1][i+1]:
            flag = False
    if flag is True:
        return board[2][2]
    

    for x in range(0, 5):
        flag = True
        for y in range(0, 4):
            if board[y][x] != board[y+1][x]:
                flag = False
        if flag is True and board[x][0] != ' ':
            return board[x][0]

    return ' '

def new_board():
    return [[' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ']]