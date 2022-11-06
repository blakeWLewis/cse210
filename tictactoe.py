# Blake Lewis Tic-Tac-Toe Assignment
from itertools import groupby


def initialize_board(board_dim):
    board = [[0 for x in range(board_dim)] for y in range(board_dim)]
    counter = 0
    for y in range(board_dim):
        for x in range(board_dim):
            counter = counter + 1
            board[y][x] = f"{counter}"
    return board


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def print_board(board):
    print("\n")
    for y in range(len(board)):
        for x in range(len(board[y])):
            print(board[y][x], end=" ")
            if x < (len(board) - 1):
                print("|", end=" ")
        if y < (len(board) - 1):
            print("\n- + - + -\n")
    print("\n")


def print_prompt(turn):
    return int(input(f"\n{'o' if turn == 0 else 'x'}'s turn to choose a square (1-9): "))


def location_is_available(location, board):
    x, y = get_x_y(location, board)
    value = board[y][x]
    return value.isdigit()


def get_x_y(location, board):
    y = int((location - 1) / len(board))
    x = (location - 1) % len(board)
    return x, y


def update_board(location, board, turn):
    x, y = get_x_y(location, board)
    board[y][x] = 'o' if turn == 0 else 'x'


def is_game_won(board):
    # check rows
    for y in range(len(board)):
        if all_equal(board[y]):
            player = board[y][0]
            return True, player
    # Check Columns
    board_t = list(zip(*board))
    for y in range(len(board)):
        if all_equal(board_t[y]):
            player = board[y][0]
            return True, player

    if (board[0][0] == board[1][1] and board[0][0] == board[2][2]) \
            or (board[0][2] == board[1][1] and board[0][2] == board[2][0]):
        player = board[1][1]
        return True, player

    return False, None



def main():
    board_dim = 3
    turn = 0
    game_continues = True

    board = initialize_board(board_dim)
    print_board(board)

    while game_continues:
        location = print_prompt(turn)

        if location_is_available(location, board):
            update_board(location, board, turn)
            turn = 1 if turn == 0 else 0
            game_won = is_game_won(board)
            if game_won[0]:
                print(f"Congrats {game_won[1]} you won the game! ")
                game_continues = False
            else:
                print_board(board)
        else:
            print("\n***********************\n* That location is not available\n***********************\n")
            print_board(board)


if __name__ == "__main__":
    main()

