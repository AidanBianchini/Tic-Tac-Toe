from typing import List, Tuple
import random
import os

#Constants
HORIZONTAL = 3
VERTICAL   = 3

#Pieces
SPOT_ONE   = 0
SPOT_TWO   = 1
SPOT_THREE = 2
SPOT_FOUR  = 3
SPOT_FIVE  = 4
SPOT_SIX   = 5
SPOT_SEVEN = 6
SPOT_EIGHT = 7
SPOT_NINE  = 8

#Tuples
Game = Tuple[str,str, int, str, List[str]]
PLAYER_ONE = 0
PLAYER_TWO = 1
TURN_COUNT = 2
OPPONENT   = 3
BOARD      = 4

def print_board(moves: List[str]) -> None:
    """ Takes moves the players have done, then prints a tic-tac-toe board
    
    Precondition: The list, named moves has 9 values
    
    >>> print_board (['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'])
    
    a     b     c  
       |     |     
1    x |  x  |  x   
  _____|_____|_____
       |     |     
2    x |  x  |  x   
  _____|_____|_____
       |     |     
3    x |  x  |  x   
       |     |     
       
    >>> print_board (['x', 'x', 'x', 'y', 'y', 'x', 'y', 'y', 'y'])
    a     b     c  
       |     |     
1    x |  x  |  x   
  _____|_____|_____
       |     |     
2    y |  y  |  x   
  _____|_____|_____
       |     |     
3    y |  y  |  y   
       |     |     
    
    >>> print_board ([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    a     b     c  
       |     |     
1      |     |      
  _____|_____|_____
       |     |     
2      |     |      
  _____|_____|_____
       |     |     
3      |     |      
       |     |     
    """
    
    print ("\n      |     |     ")
    print ("   ", moves[SPOT_ONE], "| ", moves[SPOT_TWO], " | ", moves[SPOT_THREE], "  ")
    print (" _____|_____|_____")
    print ("      |     |     ")
    print ("   ", moves[SPOT_FOUR], "| ", moves[SPOT_FIVE], " | ", moves[SPOT_SIX], "  ")
    print (" _____|_____|_____")
    print ("      |     |     ")
    print ("   ", moves[SPOT_SEVEN], "| ", moves[SPOT_EIGHT], " | ", moves[SPOT_NINE], "  ")
    print ("      |     |     \n")
    
def start_game () -> Game:
    """
    Starts the tic tac toe game by letting players choose their pieces and resetting board
    Precondition: user doesn't input a number
    """
    
    moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
    
    player1 = input('Player 1 Enter your piece: ')
    player1 = piece_error_check_recursive(player1, None)
    
    player2 = input('Player 2 Enter your piece: ')
    player2 = piece_error_check_recursive(player2, player1)
    
    Game = (player1, player2, random.randint(0, 1), ' ', moves)
    
    print_board(Game[BOARD])
    
    return Game

def piece_error_check_recursive (piece: str, other: str) -> str:
    """ Error Checks to see if there are issues with the pieces inputted
    
    >>> piece_error_check_recursive ('x', 'x')
    Please enter a piece different than player 1: x
    Please enter a piece different than player 1: xx
    Please enter a piece with a length of 1: o
    'o'
    
    >>> piece_error_check_recursive ('x', 'o')
    'o'
    
    >>> piece_error_check_recursive ('o', 'x')
    'x'
    
    >>> piece_error_check_recursive ('x', 'oo')
    Please enter a piece with a length of 1: o
    'o'
    
    """
    if (len(piece) != 1):
        piece = input('Please enter a piece with a length of 1: ')
        return piece_error_check_recursive(piece, other)        
    
    elif (piece == other):
        piece = input('Please enter a piece different than player 1: ')
        return piece_error_check_recursive(piece, other)
    
    else:
        return piece    
        
    
def slot_choice () -> int:
    """ Takes the players turns that they want to do
    """
    chosen_number = input ('Please input the slot you want your piece in: ')
    chosen_number = int(chosen_number)-1
    chosen_number = player_turns_recursive(chosen_number)
    
    return chosen_number
    
def player_turns_recursive (number: int) -> int:
    """Checks if the number inputted is valid
    """
    
    if (number >= 0 and number <= 8):
        return number
    
    else:
        number = input('Please enter a valid number between (1-9): ')
        number = int(number)-1
        return player_turns_recursive (number)
    
def easy_ai (Game) -> Game:
    """
    Uses a random number generator to pick a spot on the board
    """
    
    choice = random.randint(0, 8)
    
    if (type(Game[BOARD][choice]) is int):
        Game[BOARD][choice] = Game[PLAYER_TWO]
        Game = tuple(change_turns(Game))
        return Game
    
    else:
        return easy_ai(Game)
    
def place_piece (Game) -> Game:
    """
    Places piece on board
    """
    
    piece = Game[int(Game[TURN_COUNT])]
    
    print ("It is ", piece, "'s turn", sep = '')
    
    if (Game[OPPONENT] == '1' or piece == Game[PLAYER_ONE]):
        choice = slot_choice ()
        
        if (type(Game[BOARD][choice]) is int):
            Game[BOARD][choice] = piece
            Game = tuple(change_turns(Game))
            return Game
        
        else:
            print ("That space is already occupied")
            return place_piece(Game)        
    
    elif (Game[OPPONENT] == '2'):
        choice = easy_ai (Game)
        return choice
    
    elif (Game[OPPONENT] == '3'):
        choice = hard_ai (Game)
        return choice

def dummy_call () -> None:
    moves = ['x', 'x', 3, 4, 5, 6, 7, 8, 9]
    
    player1 = 'x'
    player2 = 'o'
    
    Game = (player1, player2, random.randint(0, 1), ' ', moves)
    
    #print_board(Game[BOARD])
    
    hard_ai(Game)

def hard_ai (Game) -> Game:
    """
    Logic for an impossible ai to function
    """
    #copy = Game[BOARD]
    
    copy_board = tuple(Game[BOARD])
    computer = Game[PLAYER_TWO]
    player   = Game[PLAYER_ONE]
    
    #Check if can win next round
    for i in range(0, 8):
        temporary = list(Game)
        temporary[BOARD] = list(copy_board)
        Game = tuple(temporary)
        
        if (type(Game[BOARD][i]) is int):
            Game[BOARD][i] = computer
            
            if(check_wins(Game, 0) == computer):
                print_board(Game[BOARD])
                return Game
            
            else:
                Game[BOARD][i] = player
                
            
            if(check_wins(Game, 0) == player):
                Game[BOARD][i] = computer
                print_board(Game[BOARD])
                return Game
        
def hard_ai_tester (Game) -> Game:
    """
    Logic for an impossible ai to function
    """
    #copy = Game[BOARD]
    
    copy_board = tuple(Game[BOARD])
    computer = Game[PLAYER_TWO]
    player   = Game[PLAYER_ONE]
    
    #Check if can win next round
    for i in range(0, 8):
        temporary = list(Game)
        temporary[BOARD] = list(copy_board)
        Game = tuple(temporary)
        
        if (type(Game[BOARD][i]) is int):
            Game[BOARD][i] = computer
            
            if(check_wins(Game, 0) == computer):
                print_board(Game[BOARD])
                return Game
            
            else:
                Game[BOARD][i] = player
                
            
            if(check_wins(Game, 0) == player):
                Game[BOARD][i] = computer
                print_board(Game[BOARD])
                return Game
    
def check_wins (Game, count: int) -> str:
    """
    Checks if there are any wins
    """
    
    if (Game[BOARD][SPOT_ONE] == Game[BOARD][SPOT_TWO] and  Game[BOARD][SPOT_TWO] == Game[BOARD][SPOT_THREE]):
        Game = change_turns (Game)
        return Game[int(Game[TURN_COUNT])]
    
    elif (Game[BOARD][SPOT_FOUR] == Game[BOARD][SPOT_FIVE] and  Game[BOARD][SPOT_FIVE] == Game[BOARD][SPOT_SIX]):
        Game = change_turns (Game)
        return Game[int(Game[TURN_COUNT])]

    elif (Game[BOARD][SPOT_SEVEN] == Game[BOARD][SPOT_EIGHT] and  Game[BOARD][SPOT_NINE] == Game[BOARD][SPOT_EIGHT]):
        Game = change_turns (Game)
        return Game[int(Game[TURN_COUNT])]
    
    elif (Game[BOARD][SPOT_ONE] == Game[BOARD][SPOT_FOUR] and  Game[BOARD][SPOT_SEVEN] == Game[BOARD][SPOT_FOUR]):
        Game = change_turns (Game)
        return Game[int(Game[TURN_COUNT])]
    
    elif (Game[BOARD][SPOT_TWO] == Game[BOARD][SPOT_FIVE] and  Game[BOARD][SPOT_FIVE] == Game[BOARD][SPOT_EIGHT]):
        Game = change_turns (Game)
        return Game[int(Game[TURN_COUNT])]
    
    elif (Game[BOARD][SPOT_THREE] == Game[BOARD][SPOT_SIX] and  Game[BOARD][SPOT_SIX] == Game[BOARD][SPOT_NINE]):
        Game = change_turns (Game)
        return Game[int(Game[TURN_COUNT])]
    
    elif (Game[BOARD][SPOT_ONE] == Game[BOARD][SPOT_FIVE] and  Game[BOARD][SPOT_FIVE] == Game[BOARD][SPOT_NINE]):
        Game = change_turns (Game)
        return Game[int(Game[TURN_COUNT])]
    
    elif (Game[BOARD][SPOT_SEVEN] == Game[BOARD][SPOT_FIVE] and  Game[BOARD][SPOT_FIVE] == Game[BOARD][SPOT_THREE]):
        Game = change_turns (Game)
        return Game[int(Game[TURN_COUNT])]
    
    elif (count == 9):
        return 'TT'
    
    else:
        return '  '
    
def change_turns (Game) -> Game:
    """
    Changes turns
    """
    temporary = list(Game)
    
    if (Game[TURN_COUNT] == 0):
        temporary[TURN_COUNT] = 1
    
    else:
        temporary[TURN_COUNT] = 0
        
    return temporary
    
def play_again_recursion () -> Game:
    """
    asks if the user wants to play again
    """
    print ("\nEnter 1 to play tic tac toe with a friend")
    print ("Enter 2 to play tic tac toe against an easy ai")
    print ("Enter 3 to play tic tac toe against a hard ai")
    print ("Enter 4 to quit")
    choice = input("Choice: ")
    
    if (choice == '1' or choice == '2' or choice == '3'):
        Game = start_game()
        temporary = list(Game)
        temporary[OPPONENT] = choice
        
        return temporary
    
    elif (choice == '4'):
        Game = (' ', ' ', 2, '4', [' '])
        print ("\nGoodbye")
        
        return Game
    
    else:
        print ("That is not one of the options, choose 1,2, 3 or 4")
        return play_again_recursion() 

def game () -> None:
    """
    plays the game
    """
    Game = tuple(play_again_recursion())
    
    if (Game[OPPONENT] != '4'):
        winner  = '  '
        counter = 0
    
        while (winner != Game[PLAYER_ONE] and winner != Game[PLAYER_TWO] and winner != 'TT'):
            Game = place_piece(Game)
            
            counter += 1
            
            winner = check_wins(Game, counter)
            
            print_board(Game[BOARD])
            
        if (winner != 'TT'):    
            print ("Player", winner, "wins!")
        
        else:
            print ("Its a tie")
    
        game()
        
#game()