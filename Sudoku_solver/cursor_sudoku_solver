def is_valid(grid, row, col, num):
    # Check row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(grid):
    row = col = 0
    empty = False
    
    # Find empty cell
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                row = i
                col = j
                empty = True
                break
        if empty:
            break

    # If no empty cell found, puzzle is solved
    if not empty:
        return True

    # Try digits 1-9
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0

    return False

def print_grid(grid):
    for row in grid:
        print(row)

# Example usage
if __name__ == "__main__":
    # Example puzzle (0 represents empty cells)
    grid = [
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
    
    if solve_sudoku(grid):
        print_grid(grid)
    else:
        print("No solution exists")