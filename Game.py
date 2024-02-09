
import random
board = ["b", "b", "b", "b", "b", "b", "b", "b", "b"]

#This represents a blank game board with 9 spots to play.
# "b" in a spot means that that spot on the board is

def check_victory(x):  # This function can check if a chosen player has won or not.
    # Each of these if statements represents one of the 8 possible ways to get three in a row
    if board[0] == x and board[1] == x and board[2] == x:
        return True
        # The function returns true if it finds three in a row.  Otherwise it tryurns false.
    elif board[0] == x and board[3] == x and board[6] == x:
        return True
    elif board[0] == x and board[4] == x and board[8] == x:
        return True
    elif board[1] == x and board[4] == x and board[7] == x:
        return True
    elif board[2] == x and board[5] == x and board[8] == x:
        return True
    elif board[2] == x and board[4] == x and board[6] == x:
        return True
    elif board[3] == x and board[4] == x and board[5] == x:
        return True
    elif board[6] == x and board[7] == x and board[8] == x:
        return True
    else:
        return False
def check_draw():  # This function checks if a draw has been reached
    i = 0
    while i <= 8:
        if board[i] == "b":
            return False # If there are any blank spots left on the board it returns false
        i = i + 1
    return True # If the board is full it returns true


def y_plays(): # This function randomly selects the opponent's next move.
    p = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
    while board[p] == "y" or board[p] == "x":
        # If the random number generator would have them play something that has already been played
        p = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        # We have them generate another number, repeating until they find a blank spot.
    board[p] = "y"
    print("Your opponent played in position " + str(p+1))

print("This is a game of Tic-Tac-Toe")
print("The top left position is 1.  The top center is 2 and the top right is 3")
print("The middle left position is 4.  The middle center is 5 and the middle right is 6")
print("The bottom left position is 7.  The bottom center is 8 and the middle right is 9")
print("When prompted, type a capitol letter corresponding to the position where you want to play your move")
print("\n | 1 | 2 | 3 |")
print(" -------------")
print(" | 4 | 5 | 6 |")
print(" -------------")
print(" | 7 | 8 | 9 |")

while check_victory("x") == False and check_victory("y") == False and check_draw() == False:
    # The game continues as long as neither player has won, or a draw hasn't occured
    t=input("Type the number corresponding to your next move: ")
    if t not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or board[int(t)-1] != "b":
        print("That is not a valid move.  Pick a number 1-9 that has not already been played")
        # This will print out an error if the user picks something other than a number between 1 and 9
    else:
        board[int(t)-1] = "x"
        if check_victory("x") == True: # If the user has won, we want out of the game immediately
            print("")
        elif check_draw() == True: # Same goes for a draw
            print("The game is a draw")
        else:
            y_plays() # If the game is not a win for the user or a draw, the loop continues

if check_victory("x") == True: # If the user has won we congratulate
    print("You are victorious")
else: # If the user has lost, or a draw has occurred, we inform them
    print("you are not victorious")
