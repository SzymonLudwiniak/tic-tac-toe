def print_board(board):
    for y in range(0, 5):
        print('--------------------------')
        print('| ', end="")
        for x in range(0, 5):
            print(board[y][x], ' | ', end="")
        print("")
    print('--------------------------')


def is_game_over(board):
    # first diagonal
    flag = True
    for i in range(0, 5):
        if board[i][i] != board[0][0]:
            flag = False
    if flag and board[0][0] != ' ':
        return True

    # #second diagonal
    flag = True
    for i in range(0, 5):
        if board[i][i] != board[4][0]:
            flag = False
    if flag and board[4][0] != ' ':
        return True
    
    #columns, idk if u can do this in smarter way but at least works
    for x in range(0, 5):
        flag = True
        for y in range(0, 5):
            if board[y][x] != board[0][x]:
                flag = False
        if flag and board[0][x] != ' ':
            return True
    
    for y in range(0, 5):
        flag = True
        for x in range(0, 5):
            if board[y][x] != board[y][0]:
                flag = False
        if flag and board[y][0] != ' ':
            return True

    return False


def new_board():
    return [['o',' ',' ',' ',' '],
            [' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ']]

print(is_game_over(new_board()))