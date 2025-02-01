board = [ 
    [0, 0, 0, 0, 0, 0, 6, 0, 0],
    [9, 3, 8, 0, 1, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 8, 0, 9],
    [0, 2, 0, 0, 7, 0, 1, 0, 0],
    [7, 0, 1, 4, 9, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 9, 8, 3, 0, 0, 7],
    [0, 0, 0, 0, 0, 7, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 0]
]

def print_board(board):
    for i in range(0, len(board), 3):
        for row in board[i:i+3]:
            print(" ".join(map(str, row[:3])) + " | " + " ".join(map(str, row[3:6])) + " | " + " ".join(map(str, row[6:9])))
        if i < 6:
            print("-" * 21)

def valid_move(board, row, col, num):  
    if num in board[row]:
        return False  
    for r in range(9):
        if board[r][col] == num:
            return False  
    cube_row = (row // 3) * 3
    cube_col = (col // 3) * 3
    for r in range(3):
        for c in range(3):
            if board[cube_row + r][cube_col + c] == num:
                return False
    return True

def empty_cell(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

def solver(board):
    empty = empty_cell(board)
    if not empty:
        return True
    r, c = empty
    for n in range(1,10):
        if valid_move(board, r, c, n):
            board[r][c] = n
            if solver(board):
                return True
            board[r][c] = 0
    return False        

solver(board)

print_board(board)