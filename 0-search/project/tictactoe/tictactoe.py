"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(cell == X for row in board for cell in row)
    o_count = sum(cell == O for row in board for cell in row)
    return X if x_count <= o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set(
        (i, j)
        for i, row in enumerate(board)
        for j, cell in enumerate(row)
        if cell is EMPTY
    )
    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if not (0 <= i <= 2 and 0 <= j <= 2) or board[i][j] is not EMPTY:
        raise ValueError("Invalid move")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if all(cell == X for cell in row):
            return X
        elif all(cell == O for cell in row):
            return O

    # Check columns
    for col in range(3):
        if all(board[row][col] == X for row in range(3)):
            return X
        elif all(board[row][col] == O for row in range(3)):
            return O

    # Check diagonals
    if all(board[i][i] == X for i in range(3)):
        return X
    elif all(board[i][i] == O for i in range(3)):
        return O
    if all(board[i][2 - i] == X for i in range(3)):
        return X
    elif all(board[i][2 - i] == O for i in range(3)):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
