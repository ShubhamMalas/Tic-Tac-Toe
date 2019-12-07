def Tic_Toc_Board(board):
   print(board[7] ,'|' , board[8] ,'|', board[9])
   print('--|---|--')
   print(board[4] ,'|' , board[5] ,'|', board[6])
   print('--|---|--')
   print(board[1] ,'|' , board[2] ,'|', board[3])
   return board


def user_symbol():
  player = [0]*2
  while True:
      player[0] = str(input("Enter player 1 symbol(x/o)\n"))
      if player[0] not in ('x','o') :
                        continue
      else:
                        if player[0].lower() == 'x':
                           player[1] = 'o'
                        else:
                           player[1] = 'x'
                        break  
  print('Player 1 is using {}'.format(player[0]))  #formating usng .format method
  print(f'Player 2 is using {player[1]}')         # formating usng f method
  return player

def Check_Winner(board):
  if ((board[1] == board[2] == board[3] == 'x') or
      (board[4] == board[5] == board[6] == 'x') or
      (board[7] == board[8] == board[9] == 'x') or
      (board[1] == board[4] == board[7] == 'x') or
      (board[2] == board[5] == board[8] == 'x') or
      (board[3] == board[6] == board[9] == 'x') or
      (board[1] == board[5] == board[9] == 'x') or
      (board[3] == board[5] == board[7] == 'x')):
        return True 
  else:
     if ((board[1] == board[2] == board[3] == 'o') or
         (board[4] == board[5] == board[6] == 'o') or
         (board[7] == board[8] == board[9] == 'o') or
         (board[1] == board[4] == board[7] == 'o') or
         (board[2] == board[5] == board[8] == 'o') or
         (board[3] == board[6] == board[9] == 'o') or
         (board[1] == board[5] == board[9] == 'o') or
         (board[3] == board[5] == board[7] == 'o')): 
          return True
     
                        
def Lets_Play(board,player):
  count = 9
  first ,second =True,True
  while count != 0:
    if first:
      print("player 1 turn")
      position = int(input(f'Enter the position to insert {player[0]}: '))
      if position in board:
        board[position] = player[0]
        Tic_Toc_Board(board)
        if Check_Winner(board):
          print("Player 1 Wins..........")
          break
        count -= 1
        first = False
        second = True
    if second and count > 0:
      print("player 2 turn")
      position = int(input(f'Enter the position to insert {player[1]}: '))
      if position in board:
        board[position] = player[1]
        Tic_Toc_Board(board)
        if Check_Winner(board):
          print("Player 2 Wins..........")
          break
        count -= 1
        first = True
        second = False
  if count == 0:
    print("Game Tied")
                  
board = list(range(0,10))
Tic_Toc_Board(board)
player = user_symbol()
Lets_Play(board,player)
