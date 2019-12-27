'''
Tic Tac Toe Game
This is a tic tac toe game for 2 players using 3 x 3 board.
Each player can mark any position in the board that is not yet occupied alternately
with the goal to create three consecutive mark either horizontal, vertical, or diagonal.
At the start of the game, the first player to play will be assigned randomly

'''

import random

def ask_player1_symbol():
    '''
    this function request player 1 to choose the symbol of either 'X' or 'O'
    based on his choice, player 2 symbol will be the other symbol.
    '''
    while True:
        p1_symbol = input("Player 1, please choose your symbol 'X' or 'O': ")
        if p1_symbol not in ['X', 'O']:
            print("Your input is invalid, please try again.")
            continue
        else:
            print("Player 1 symbol is ", p1_symbol)
            if p1_symbol == 'X':
                print("Player 2 symbol is O")
                return p1_symbol, 'O'
            else:
                print("Player 2 symbol is X")
                return p1_symbol, 'X'

def choose_first_player():
    '''
    This function choose who will be the first player to move first
    '''
    r= random.randrange(1,2)
    if r ==1:
        return "Player 1"
    else:
        return "Player 2"

def print_board(board):
    '''
    This is the function to print the board
    '''
    print('\n-------------')
    for i in range(0,3):
        for j in range(0,3):
            print('| '+ board[i*3+j+1], end=' ')
        print('|')
    print('-------------\n')

def check_win(board, symbol):
    '''
    function to check whether the symbol has won
    '''
    if (board[1] == symbol and board[2]== symbol and board[3]==symbol) or \
        (board[4] == symbol and board[5]== symbol and board[6]==symbol) or \
            (board[7] == symbol and board[8]== symbol and board[9]==symbol) or \
                (board[1] == symbol and board[4]== symbol and board[7]==symbol) or \
                    (board[2] == symbol and board[5]== symbol and board[8]==symbol) or \
                        (board[3] == symbol and board[6]== symbol and board[9]==symbol) or \
                            (board[1] == symbol and board[5]== symbol and board[9]==symbol) or \
                                (board[7] == symbol and board[5]== symbol and board[3]==symbol):
                                return True
    else:
        return False

def check_board_full(board):
    '''
    function to check whether the board is full
    '''
    if ' ' not in board:
        return True
    else:
        return False

def ask_player_position(board, symbol):
    '''
    function to ask which position player choose, and assign the symbol
    '''
    while True:
        try:
            p = int(input("Please enter the position (1-9) you want to mark with "+ symbol +": " ))
        except ValueError:
            print("The value entered is not number, please enter number between 1-9. ")
            continue
        else:
            if p<1 or p>9:
                print("The value can only be between 1-9")
                continue
            elif board[p]!=" ":
                print("The position you entered is already marked, please choose other position")
                continue
            else:
                board[p]= symbol
                break



print("-----------------------------")
print(" Welcome to Tic Tac Toe Game ")
print("-----------------------------")

play = True
while play:
    # Initialize the board
    board = ['#'] + [' ']*9

    # ask player 1 for symbol he wants to use
    p1_symbol, p2_symbol = ask_player1_symbol()

    players =[' ']*2
    players_symbols =[' ']*2

    # randomly choose which player to move first
    players[0] = choose_first_player()

    if players[0] =="Player 1":
        players_symbols[0] = p1_symbol
        players_symbols[1] = p2_symbol
        players[1] = "Player 2"
    else:
        players_symbols[0] = p2_symbol
        players_symbols[1] = p1_symbol
        players[1] = "Player 1"

    game_on = True
    while game_on:
        for i in range(0,2):
            print("\n"+players[i]+" this is your turn")
            ask_player_position(board, players_symbols[i])
            print_board(board)
            if check_win(board, players_symbols[i]):
                print(players[i]+ ", you WIN!")
                game_on = False
                break
            if check_board_full(board):
                print("The board is FULL, it's a DRAW")
                game_on=False
                break
    
    play_input = input("Do you want to play again? Please enter 'y' if you want to play again: ")
    if play_input !='y':
        play = False
    