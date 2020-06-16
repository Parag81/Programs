
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

game_continue = True
player = "X"
winner = None


def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])
    
def play_game():
    global winner
    
    display_board()
    while game_continue: 

        handle_player(player)
        result()
        flip_player()
    
    if winner == "X" or winner == "O":
        print("Congrats "+ winner + " won.")
    elif winner == None:
        print("Its a Tie.")
    
def handle_player(player):
    print(player + " turn.")
    
    position = input("Enter a position from 1 to 9=")
    
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Enter a position from 1 to 9=")
    
        position = int(position)-1
    
        if board[position] == "-":
            valid = True 
        else:
            print("You can't go there. Try again")
          
    
    board[position] = player
    display_board()
            
def result():
    check_the_winner()
    check_if_tie()
    
def check_the_winner():
    global winner
    
    #rows
    row_winner = check_rows()
    #columns
    column_winner = check_columns()
    #diagonals
    diagonal_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    return 

def check_rows():
    global game_continue
    
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_continue = False
        
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return 

def check_columns():
    global game_continue
    
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_continue = False
        
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return 

def check_diagonals():
    global game_continue
    
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    if diagonal_1 or diagonal_2:
        game_continue = False
        
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return 

def check_if_tie():
    global game_continue
    
    #Checking for tie
    if "-" not in board:
        game_continue = False
    return 
    
def flip_player():
    global player
    
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    
play_game()

