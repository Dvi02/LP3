
# Python program to solve N-Queen Problem using Backtracking

N = 4

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


# Check whether a queen can be placed safely
def isSafe(board, row, col):

    # Check the left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left
    for i, j in zip(range(row, N),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col):

    # Base case: All queens are placed
    if col >= N:
        return True

    # Try placing a queen in each row
    for i in range(N):
        if isSafe(board, i, col):

            # Place the queen
            board[i][col] = 1

            # Recur for the next column
            if solveNQUtil(board, col + 1):
                return True

            # Backtrack if no solution is found
            board[i][col] = 0

    return False


def solveNQ():

    # Initialize the chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]

    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False

    print("Solution for", N, "Queens:")
    printSolution(board)
    return True


# Driver code
solveNQ()
