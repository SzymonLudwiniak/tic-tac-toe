import is_game_over from studentA

def announce_outcome(board, players_move):
    
    if players_move and is_game_over(board):
        print("computer won!")
        return

    if not players_move and is_game_over(board):
        print("player won!")
        return
    
    print("draw!!")
    return
    
