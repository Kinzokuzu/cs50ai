"""
Tic Tac Toe Player
"""

import math
import re

# possible moves
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # count all instances of EMPTY
    empty_count = 0
    for row in board:
        for col in row:
            if col == "EMPTY":
                empty_count += 1

    # even # of EMPTY's denotes player 'O' has just moved
    if empty_count % 2: return 'X'
    return 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for r in range(len(board)): # rows
        for c in range(len(board[r])): # colomns
            if board[r][c] == "EMPTY":
                possible_actions.add(board[r][c])

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # check for valid aciton
    if board[action[0]][action[1]] != "EMPTY":
        raise NameError("Invalid action")

    # get current player
    curr_player = player(board)
    # create deep copy
    new_board = board.deepcopy()
    # set new action with current player
    new_board[action[0]][action[1]] = curr_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check row wins
    for r in range(3):
        if 'X' in (board[r][0], board[r][1], board[r][2]): return 'X'
        if 'O' in (board[r][0], board[r][1], board[r][2]): return 'O'
    # check for column wins
    for c in range(3):
        if 'X' in (board[0][c], board[1][c], board[2][c]): return 'X'
        if 'O' in (board[0][c], board[1][c], board[2][c]): return 'O'
    # check for diagnal wins
    if 'X' in (board[0][0], board[1][1], board[2][2]): return 'X'
    if 'O' in (board[0][0], board[1][1], board[2][2]): return 'O'
    if 'X' in (board[0][2], board[1][1]. board[2][0]): return 'X'
    if 'O' in (board[0][2], board[1][1]. board[2][0]): return 'O'

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board): return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    our_winner = winner(board)
    if our_winner == 'X': return -1
    if our_winner == 'O': return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
