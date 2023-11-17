import copy

class Board:
    # text  =  '\n   {}  |  {}  |  {}  \n _____|_____|_____\n      |     |     \n   {}  |  {}  |  {}  \n _____|_____|_____\n      |     |     \n   {}  |  {}  |  {}  \n      |     |     \n\n'
    text = ''' 
          {}  |  {}  |  {} 
        _____|_____|_____
             |     |     
          {}  |  {}  |  {} 
        _____|_____|_____   
             |     |    
          {}  |  {}  |  {} 
             |     |     '''

    
    def __init__(self):
        self.board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-'],     
        ]
        self.turn = 'X'    

    

    def __repr__(self):
        board = self.board  
        return (Board.text.format(*(board[0] + board[1] + board[2])))             # unpacks elements and passes it as arguments

    def move(self, x,y):
        if x >= 0 and x < len(self.board) and y >=0 and y < len(self.board) and self.board[x][y] == '-':
            self.board[x][y] = self.turn
            self.turn = 'O' if self.turn == 'X' else 'X'
            
        else: raise ValueError("Invalid move")
           

    def isWon(self):
        def checkRows(board):
            for row in board:
                if len(set(row)) == 1 and row[0] != '-': return True
            return False
    
        def checkCols(board):
            return checkRows(list(zip(*board)))     #transpose cols -> rows

        def checkDiags(board):
            diag = []
            diag1 = []
    
            for i in range(len(board)):
                diag.append(board[i][i])
                diag1.append(board[i][2-i])
                
            return ('-' not in diag and len(set(diag)) == 1) or ('-' not in diag1 and len(set(diag1)) == 1)
            
        for check in [checkRows, checkCols, checkDiags]:
            if check(self.board): return True
            
        return False

    def legal_moves(self):       # Possible moves for the current turn
        moves = []
        
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == '-': moves.append((i,j))
        return moves
               
            

def evaluation(board, depth):         # eval function to eval board state, only doable if won or draw
    if board.isWon() and board.turn == 'O': return 10 - depth
    elif board.isWon() and board.turn == 'X': return -10 + depth
    elif len(board.legal_moves()) == 0: return 0        # draw 
    

best_move = ()
def minimax(board, depth):      # returns the best score possible from state given opponent plays optimally
    global best_move
    move_scores = {} 
    
    
    # base case: once reached end_state (win/draw), call evaluation return score
    if evaluation(board, depth) != None: return evaluation(board, depth)

    for x,y in board.legal_moves():
       new_state = copy.deepcopy(board)           # create new board state, recursive call
       new_state.move(x,y)
       move_scores[(x,y)] = minimax(new_state, depth +1)    # the resulting score from going thru that state
       
    print(move_scores)
    
    if board.turn == 'X':         # select the max score
        best_move = max(move_scores, key = move_scores.get)
        return max(move_scores.values())

    if board.turn == 'O':          # opponent wants to minimize our score as much as possible
        best_move = min(move_scores, key = move_scores.get)
        return min(move_scores.values())


    
class TicTacToe: 
    def __init__(self):
        self.board = Board()

    def promptMove(self, prompt):
        while True:
            try:
                move = input(prompt)
                x,y = map(int, move.split())
                self.board.move(x,y)
                break
            except ValueError: 
                print("Invalid move")

                
    def game_over(self):
        print(self.board)
        if evaluation(self.board, 0) != None: 
            print("Game over!")
            return True
            
    def play(self):
        board = self.board                
        # Start playing vs computer
        while len(board.legal_moves()) != 0: 

            if board.turn == 'X': self.promptMove('Player 1 Move: ')
            
            if self.game_over(): break
            minimax(board,0)
            
            print("Computer Turn: ", best_move)
            board.move(best_move[0], best_move[1])  
           
            if self.game_over(): break  
                 
            




if __name__ == '__main__': # test if either run-directly or being imported
   game =  TicTacToe()
   game.board.move(0,1)
   game.board.move(2,0)
   game.board.move(2,2)
   game.board.move(2,1)
   game.board.move(1,2)
   print(game.board)
   
   game.play()    





  


