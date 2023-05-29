promt_prefix = "[TIC TAC TOE] "

def ai_move():
    global board

    for Y in range(0,4):
        row = board[Y]
        xcount = row.count("x")
        ocount = row.count("y")
        if ocount == 4 and xcount == 0:
            board[Y] = ["x" if item == " " else item for item in board[Y]]
            return

    for X in range(0,4):
        col = board[:,X]
        xcount = col.count("x")
        ocount = col.count("y")
        if ocount == 4 and xcount == 0:
            board[Y] = ["x" if item == " " else item for item in board[Y]]
            return

    for D in range(0,4):
        xcount = 0
        ocount = 0

        if board[D][D] == "x":
            xcount = xcount + 1
        elif board[D][D] == "o":
            ocount = ocount + 1

        if ocount == 4 and xcount == 0:
            board[Y] = ["x" if item == " " else item for item in board[Y]]
            return
    
    for D in range(0,4):
        xcount = 0
        ocount = 0

        if board[D][4 - D] == "x":
            xcount = xcount + 1
        elif board[D][4 - D] == "o":
            ocount = ocount + 1

        if ocount == 4 and xcount == 0:
            board[Y] = ["x" if item == " " else item for item in board[Y]]
            return

    


def get_user_move(X, Y):
    global board
    board[X][Y] = "o"


def is_player_starting():
    
    player_input = None
    decission = None
    
    while decission == None:
        my_print("Would you like to go first? (Y/n)")
        player_input = input()
        if player_input.lower() == "y":
            decission = True
        elif player_input.lower() == "n":
            decission = False
        else:
            decission = None
    

def my_print(message):
    print(promt_prefix + message, end="")

def my_println(message):
    print(promt_prefix + message)
