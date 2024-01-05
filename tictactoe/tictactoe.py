"""
Tic Tac Toe Player
"""

import math
import copy

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
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                empty_count += 1

    # even # of EMPTY's denotes player O has just moved
    if empty_count % 2 == 1: return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for r in range(3): # rows
        for c in range(3): # colomns
            if board[r][c] == EMPTY:
                # add (r, c) as a tuple
                possible_actions.add((r, c))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # check for valid aciton
    if action not in actions(board):
        raise NameError("Invalid action")

    # get current player
    curr_player = player(board)
    # create deep copy
    new_board = copy.deepcopy(board)
    # set new action with current player
    new_board[action[0]][action[1]] = curr_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check row wins
    for r in range(3):
        if (board[r][0] == board[r][1] == board[r][2] == X): return X
        if (board[r][0] == board[r][1] == board[r][2] == O): return O
    # check column wins
    for c in range(3):
        if (board[0][c] == board[1][c] == board[2][c] == X): return X
        if (board[0][c] == board[1][c] == board[2][c] == O): return O
    # check diagonal wins
    if (board[0][0] == board[1][1] == board[2][2] == X): return X
    if (board[0][0] == board[1][1] == board[2][2] == O): return O
    if (board[0][2] == board[1][1] == board[2][0] == X): return X
    if (board[0][2] == board[1][1] == board[2][0] == O): return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O: return True
    elif actions(board): return False
    else: return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    our_winner = winner(board)
    if our_winner == X: return 1
    if our_winner == O: return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None

    best_move = None
    if player(board) == X:
        move_utility = -math.inf
        for action in actions(board):
            # if the next moves minimum utility is greater than the last, then the
            # next move is better
            min_val = min_value(result(board, action))
            if min_val > move_utility:
                best_move = action
                move_utility = min_val
    else: # O player
        move_utility = math.inf
        for action in actions(board):
            # if the next moves maximum utility is less than the last, then the
            # next move is better
            max_val = max_value(result(board, action))
            if max_val < move_utility:
                best_move = action
                move_utility = max_val

    return best_move


def max_value(board):
    """
    Returns the maximum utility from min_value(result(board, action))
    """
    if terminal(board): return utility(board)

    max_val = -math.inf
    for action in actions(board):
        max_val = max(max_val, min_value(result(board, action)))

    return max_val


def min_value(board):
    """
    Returns the minimum utility from max_value(result(board, action))
    """
    if terminal(board): return utility(board)

    min_val = math.inf
    for action in actions(board):
        min_val = min(min_val, max_value(result(board, action)))

    return min_val
