#Implementation of Two Player Tic-Tac-tOE GAME IN PYTHON
'''We will make board using dictionary in which keys will bethe location(i.e : top-left, mid-right, etc.) and inititally it's values will be empty space and then after every move we will change the value according to player's choice of move'''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ', 
            '4': ' ' , '8': ' ' , '9': ' ',
            '1': ' ' , '2': ' ' , '3': ' '}

board_keys = []

for hey in theBoard:
    board_keys.append(key)

'''We will have to print the updated board after every move in the game and thus we will make a function in which we'll define the printBoard function so that we cane asily print the board everytime by calling this function.'''

def printBoard(board):
    print(board['7'] +'|' + board['8']+'|' + board['9'])
    print('-+-+-')
    print(board['4'] +'|' + board['5']+'|' + board['6'])
    print('-+-+-')
    print(board['1'] +'|' + board['2']+'|' + board['3'])
    print('-+-+-')

# Now we will write the gameplay function which has all the functionality.
def game():

    turn = 'X'
    count = '0'

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + "Move to which place?")
        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print('That place is already filled. \nMove to which place?')
            continue

         # Now we will check if player X or 0 has won, for every move after 5 moves
        if count >= 5:
           if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': #across the top
              printBoard(theBoard)
              print("\nGame Over.\n")
              print(" **** " + turn + "won.****")
              break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 


# if neither X nor 0 wins and the board is full, we'll decalre the result as 'tie'

if count == 9:
   print("\nGame Over.\n")
   print("It's a tie!!")

# Now we have to change the player after  every move
if turn == 'X':
   turn = 'O'
else:
   turn = 'X'

# Now we will ask if the player wants to restart the game or not
restart = input("Do you want to play again?(y/n)")
if restart == "y" or restart == "Y":
   for key in board_keys:
      theBoard[key] = " "

   game()
if __name__ == "__main__":
   game()