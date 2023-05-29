b = [[' ',' ',' ',' ','o'],
     [' ',' ',' ',' ','x'],
     [' ',' ',' ',' ','x'],
     [' ',' ',' ',' ','x'],
     [' ',' ',' ',' ','x']]

def print_board(board):
    for y in range(0, 5):
        print('--------------------------')
        print('| ', end="")
        for x in range(0, 5):
            print(board[y][x], ' | ', end="")
        print("")
    print('--------------------------')

def is_game_over(board):

    flag = True
    for i in range(0, 5):
        if board[i][i] is not board[0][0]:
            flag = False
    if flag is True:
        return True
    flag = True
    for i in range(0, 5):
        if board[i][i] is not board[4][0]:
            flag = False
    if flag is True:
        return True
    

    for x in range(0, 5):
        flag = True
        for y in range(0, 5):
            if board[y][x] != board[0][x]:
                flag = False
        if flag is True and board[0][x] != ' ':
            return True
    
    for y in range(0, 5):
        return all(board[y][0] == elem for elem in board[y])

print(is_game_over(b))

def new_board():
    return [[' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ']]