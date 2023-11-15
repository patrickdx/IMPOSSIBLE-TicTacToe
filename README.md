# unbeatable_tictactoe

Small tic-tac-toe game where winning is impossible! The game will always draw or if you play suboptimally, the computer may win. The computer moves are generated off the basis use of the [Minimax Algorithm](https://en.wikipedia.org/wiki/Minimax). 


### How it works 
Essentially it recursively goes through all the potential moves at the current game state and evaluates them using `minimax()`. Once it knows the end-game outcomes of all potential moves, it picks the most optimal one, (whether that would lead into a guaranteed draw or win, regardless of player O's move)
![](https://images.squarespace-cdn.com/content/v1/5a0c6978bff2001ef7581170/1513544600041-LK94ONS0M8TSFUFCPPNB/full-minimax-move-tree.png?format=1500w)

#### What is minimax? 
"The maximin value is the highest guaranteed value that the player can be sure to get without knowing the actions of the other players", or can think of as the 'best score' you are 100% sure to get, given both players play optimally.

### Interesting facts: 
- The game's fate is decided after the player's first move. After this, the computer has already calculated the series of moves to lead to a draw, even if player 1 plays perfectly.
- If player X were to play `(0,0)`, then: `{(0, 1): 10, (0, 2): 10, (1, 0): 10, (1, 1): 0, (1, 2): 10, (2, 0): 10, (2, 1): 10, (2, 2): 10}`
Computer Turn:  `(1, 1)`
