![TicTacToe](https://raw.githubusercontent.com/filipljung/TicTacToe/main/Pictures/Screenshot%202023-06-26%20185623.png)

## Live: https://tictactoe123.herokuapp.com
# Tic Tac Toe Game
This is a simple command-line Tic Tac Toe game implemented in Python. It allows two players to take turns marking spaces in a 3x3 grid. The first player uses the symbol "X" and the second player uses the symbol "O". The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. If all the spaces on the board are filled and no player has won, the game ends in a tie.

## Getting Started
To play the game, follow these steps:

1. Make sure you have Python installed on your system. You can download it from the official Python website: Python Downloads

2. Clone this repository or download the code files.

3. Open a command prompt or terminal and navigate to the directory where the code files are located.

3. Run the following command to start the game:
```python run.py```

5. Follow the on-screen instructions to play the game.

## How to Play
1. The game starts with an introduction and the rules of the game are displayed.

2. Player 1 is asked to choose between "X" and "O". Player 2 is assigned the remaining symbol.

3. The game board is displayed, and players take turns entering their moves.

4. Each player is prompted to enter the row and column numbers of the cell they want to mark. The numbers should be between 0 and 2.

5. If a player selects an already occupied cell or an invalid cell, they will be prompted to choose again.

6. The game continues until one player wins or the board is full.

7. After the game ends, a summary is displayed, indicating the winner or a tie.

## Code Structure
The code is structured into several functions:

`intro()`: Displays the game introduction and rules.

`create_grid()`: Initializes the game board.

`sym()`: Asks the players to choose their symbols.

`play_game(board, symbol_1, symbol_2)`: Manages the game flow and turn-based gameplay.

`start_gaming(board, symbol_1, symbol_2, count)`: Handles each player's turn and updates the game board.

`get_valid_input(message)`: Helper function to validate user input for row and column selection.

`is_winner(board, symbol_1, symbol_2)`: Checks if a player has won the game.

`printPretty(board)`: Prints the game board in a formatted way.

`report(count, winner, symbol_1, symbol_2)`: Displays the game summary.

## Contributing
Contributions to this project are welcome! If you have any suggestions or improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
