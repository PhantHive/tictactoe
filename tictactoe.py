"""
Tic Tac Toe Player
"""

import math

# As it has been recommended in the course, I have used deepcopy here
from copy import deepcopy

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

    # check if board is full
    if terminal(board):
        return None
    else:

        # check how many X's and O's are on the board
        x_count = 0
        o_count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    x_count += 1
                elif board[i][j] == O:
                    o_count += 1

        # if X's are more than O's, it's O's turn
        if x_count > o_count:
            return O
        else:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # check if board is full
    if terminal(board):
        return None
    else:
        # check for empty spaces
        actions_set = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    actions_set.append((i, j))
        return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # return a new board with the action applied to the current player

    if actions(board) is not None:
        # check if action is valid
        if action not in actions(board):
            # return board
            print("last board:", board)
            print(actions(board))
            print("action:", action)
            raise Exception("Invalid action")

        else:
            # create a new board
            new_board = deepcopy(board)
            # make the move
            new_board[action[0]][action[1]] = player(board)
            return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.

    # 4 win possibilities to check
    # 1. horizontal
    # 2. vertical
    # 3. diagonal
    # 4. anti-diagonal
    """

    for i in range(3):
        # check for horizontal wins
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        # check for vertical wins
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]

    # check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]

    # check for anti-diagonal wins
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    # if no winner, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # check if board is full
    print("board:", board)
    if winner(board):
        return True
    else:
        # check for empty spaces
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
        # tie condition
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # check if X won
    if winner(board) == X:
        return 1
    # check if O won
    elif winner(board) == O:
        return -1

    # if no winner, return 0
    else:
        return 0


# minimax PING PONG
# ==============================
# helper functions for minimax
# ==============================
def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        # undo move
        board[action[0]][action[1]] = EMPTY
    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        # undo move
        board[action[0]][action[1]] = EMPTY
    return v

# ==============================
# MINIMAX
# ==============================
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """


    #
    if terminal(board):
        # return None if board is full
        # As asked in the instructions.
        return None
    else:

        best_action = None
        # check if it's X's turn
        if player(board) == X:
            test_board = deepcopy(board)
            v = -math.inf
            for action in actions(board):
                if min_value(result(test_board, action)) > v:
                    v = min_value(result(test_board, action)) # using helper function
                    best_action = action

            return best_action

        # check if it's O's turn
        if player(board) == O:
            test_board = deepcopy(board)
            v = math.inf
            for action in actions(board):
                if max_value(result(test_board, action)) < v:
                    v = max_value(result(test_board, action)) # using helper function
                    best_action = action

            return best_action




