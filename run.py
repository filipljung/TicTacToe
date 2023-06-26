def main():
    intro()
    board = create_grid()
    symbol_1, symbol_2 = sym()
    play_game(board, symbol_1, symbol_2)


def intro():
    print("Hello! Welcome to Filip's Tic Tac Toe game!\n")
    print("Rules: Player 1 and player 2, represented by X and O, take turns "
          "marking the spaces in a 3x3 grid. The player who succeeds in placing "
          "three of their marks in a horizontal, vertical, or diagonal row wins.\n")
    input("Press enter to continue.\n")


def create_grid():
    print("Here is the playboard: ")
    board = [[" " for _ in range(3)] for _ in range(3)]
    printPretty(board)
    return board


def sym():
    symbol_1 = input("Player 1, do you want to be X or O? ").upper()
    if symbol_1 == "X":
        symbol_2 = "O"
        print("Player 2, you are O.")
    else:
        symbol_2 = "X"
        print("Player 2, you are X.")
    input("Press enter to continue.\n")
    return symbol_1, symbol_2


def play_game(board, symbol_1, symbol_2):
    count = 1
    winner = False

    while count <= 9 and not winner:
        board = start_gaming(board, symbol_1, symbol_2, count)
        printPretty(board)

        if count == 9:
            print("The board is full. Game over.\nThere is a tie.")
            break

        winner = is_winner(board, symbol_1, symbol_2)
        count += 1

    if not winner:
        print("Game over.")

    report(count, winner, symbol_1, symbol_2)


def start_gaming(board, symbol_1, symbol_2, count):
    # Decide the turn
    if count % 2 == 0:
        player = symbol_1
    else:
        player = symbol_2

    print("Player " + player + ", it is your turn.")
    row = get_valid_input("Pick a row [0, 1, 2]: ")
    column = get_valid_input("Pick a column [0, 1, 2]: ")

    while board[row][column] != " ":
        print("The square you picked is already filled. Pick another one.")
        row = get_valid_input("Pick a row [0, 1, 2]: ")
        column = get_valid_input("Pick a column [0, 1, 2]: ")

    board[row][column] = player
    return board


def get_valid_input(message):
    while True:
        try:
            value = int(input(message))
            if value in [0, 1, 2]:
                return value
            print("Invalid input. Please enter a value between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def is_winner(board, symbol_1, symbol_2):
    # Check the rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != " ":
            print("Player " + board[row][0] + ", you won!")
            return True

    # Check the columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            print("Player " + board[0][col] + ", you won!")
            return True

    # Check the diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        print("Player " + board[0][0] + ", you won!")
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        print("Player " + board[0][2] + ", you won!")
        return True

    return False


def printPretty(board):
    print("---+---+---")
    for row in board:
        print(row[0], "|", row[1], "|", row[2])
        print("---+---+---")


def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("Press enter to see the game summary.")
    if winner and count % 2 == 1:
        print("Winner: Player " + symbol_1 + ".")
    elif winner and count % 2 == 0:
        print("Winner: Player " + symbol_2 + ".")
    else:
        print("There is a tie.")


# Call Main
main()
