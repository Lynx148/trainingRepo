import chess
import numpy as np
np.set_printoptions(suppress=True)
import moves
from game import Game, GameState
import itertools
from chess import Board

a = GameState(Board('rb2kB2/pb1pn2p/np3p2/1Qp5/1P1Pp3/N7/P1P1PPPP/RQ2KBNR w - - 4 16'),0)
# print(a.board)
# b = list(a.board.legal_moves)
#
# indexes = [(np.where(moves.movelist == str(action))[0]) for action in b]
# chain = list(itertools.chain.from_iterable(indexes))
#
# for move in chain:
#     print(move)
#
# print(len(chain))
print(moves.movelist[4031])
print(moves.movelist[4094])


# do sprawdzenia
# 2021-10-03 00:00:52,126 INFO rnb1kbnB/p2ppp1p/1pp5/6q1/1P6/8/P1PPPPPP/RN1QKBNR b - - 0 5
# 2021-10-03 00:00:54,317 INFO action: g5a5
# 2021-10-03 00:00:54,317 INFO MCTS perceived value for BLACK: 0.020000
# 2021-10-03 00:00:54,317 INFO NN perceived value for BLACK: -0.020000
# 2021-10-03 00:00:54,318 INFO ====================
# 2021-10-03 00:00:54,322 INFO rnb1kbnB/p2ppp1p/1pp5/q7/1P6/8/P1PPPPPP/RN1QKBNR w - - 1 6
# 2021-10-03 00:00:56,262 INFO action: a5a4
# 2021-10-03 00:00:56,262 INFO MCTS perceived value for WHITE: -0.140000
# 2021-10-03 00:00:56,262 INFO NN perceived value for WHITE: -0.150000
# 2021-10-03 00:00:56,262 INFO ====================
# 2021-10-03 00:00:56,266 INFO rnb1kbnB/p2ppp1p/1pp5/8/QP6/8/P1PPPPPP/RN1QKBNR b - - 0 6
#
