from tictactoe import X, O, initial_state, player, actions, result, winner

board = initial_state()

board = result(board, (0, 0))
board = result(board, (1, 1))
board = result(board, (1, 0))
board = result(board, (1, 2))
board = result(board, (2, 1))
print(board)
print(winner(board))
