import copy
"""
Tic Tac Toe Player
"""

import math

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
    xcount, ocount = 0, 0
    if board == initial_state():
        return X
    else:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == X:
                    xcount = xcount + 1
                elif board[i][j] == O: 
                    ocount = ocount + 1
        if xcount > ocount:
            return O
        else: 
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                action_set.add((i, j))
    return action_set     


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action == EMPTY or 0 > action[0] > 2 or 0 > action[1] > 2:
        raise Exception("Invalid Action")
    else:
        copyboard = copy.deepcopy(board)
        copyboard[action[0]][action[1]] = player(board)
    return copyboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    elif board[2][0] == board[1][1] == board[0][2] and board[2][0] is not EMPTY:
        return board[2][0]

    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
        elif board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is EMPTY:
                return False
            
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) is True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None
    
    turn = player(board)

    if turn == X:
        best_score = -math.inf
        best_move = None
        for move in actions(board):
            score = min_value(result(board, move))
            if score > best_score:
                best_score = score
                best_move = move
        return best_move
    else:
        best_score = math.inf
        best_move = None
        for move in actions(board):
            score = max_value(result(board, move))
            if score < best_score:
                best_score = score
                best_move = move
        return best_move
    
    
def max_value(board):
    if terminal(board): 
        return utility(board)
    v = -math.inf
    for move in actions(board):
        v = max(v, min_value(result(board, move)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for move in actions(board):
        v = min(v, max_value(result(board, move)))
    return v