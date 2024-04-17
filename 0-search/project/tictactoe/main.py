from tictactoe import X, O, initial_state, player, actions, result, winner, terminal

board = initial_state()

board = result(board, (0, 0))
board = result(board, (1, 1))
board = result(board, (1, 2))
board = result(board, (1, 0))
board = result(board, (2, 1))
board = result(board, (0, 1))
board = result(board, (0, 2))
board = result(board, (2, 0))
board = result(board, (2, 2))
print(board)
print(terminal(board))
