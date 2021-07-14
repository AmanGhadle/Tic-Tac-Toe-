#tic toe game is basically a 3x3 right and wrong game
#create a board of initially 9 blank spaces

board=["  " for i in range(9)]

# define a fucktion to print the board in a matrix form

def print_board():
     row1="| {} | {} | {} |".format(board[0], board[1], board[2])
     row2="| {} | {} | {} |".format(board[3], board[4], board[5])
     row3="| {} | {} | {} |".format(board[6], board[7], board[8])

     print()                       #these print functions are just to print blank lines,nothing else
     print(row1)
     print(row2)
     print(row3)
     print()

#create a function for both players

def player_move(icon):
     if icon=="X":
          number=1
     if icon=="O":
          number=2
     print("Your turn player{}".format(number))
     print_board() 
     choice=int(input("Enter your move (1-9): ").strip())
     if board[choice-1] == "  ":
          board[choice-1]=icon
     else:
          print()
          print("That grid is occupied")

#define a function to check if any player has won or not

def has_won(icon):
     if (board[0]==icon and board[1]==icon and board[2]==icon) or \
        (board[3]==icon and board[4]==icon and board[5]==icon) or \
        (board[6]==icon and board[7]==icon and board[8]==icon) or \
        (board[0]==icon and board[3]==icon and board[6]==icon) or \
        (board[1]==icon and board[4]==icon and board[7]==icon) or \
        (board[2]==icon and board[5]==icon and board[8]==icon) or \
        (board[0]==icon and board[4]==icon and board[8]==icon) or \
        (board[2]==icon and board[4]==icon and board[6]==icon) :
          return True
     else:
          return False
#define a function to check if its a draw
def draw():
     if "  " not in board:
          return True
     else:
          return False
     


#create a loop for moves i=of both the players
while True:
     print_board()
     player_move("X")
     print_board()
     if has_won("X"):
          print("Player1 wins")
          break
     elif draw():
          print("The game is draw")
          break
     
  
     player_move("O")
     print_board()
     if has_won("O"):
          print("Player2 wins")
          break
     elif draw():
          print("The game is draw")
          break
     
     
     
          
  
