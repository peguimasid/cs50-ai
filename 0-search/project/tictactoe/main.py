from tictactoe import X, O, initial_state, player, actions, result, winner

board = initial_state()

board = result(board, (0, 0))
board = result(board, (1, 1))
board = result(board, (2, 2))
print(board)
