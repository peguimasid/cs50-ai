from tictactoe import X, O, initial_state, player, actions

board = initial_state()

board[1][0] = X
print(board)
print(actions(board))
