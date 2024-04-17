from tictactoe import initial_state, player, X, O

board = initial_state()

board[1][0] = X
print(board)
print(player(board))
