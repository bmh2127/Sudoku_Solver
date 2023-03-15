import numpy as np

# Define a function to solve the Sudoku puzzle
def solve_sudoku(puzzle):
    """
    Given a 9x9 Sudoku puzzle as a 2D numpy array, returns the solved puzzle.
    If no solution is possible, returns None.
    """
    # Define a function to check if a solution is valid
    def is_valid_solution(solution):
        # Check rows
        if any(np.unique(row).size != 9 for row in solution):
            return False
        # Check columns
        if any(np.unique(solution[:,col]).size != 9 for col in range(9)):
            return False
        # Check 3x3 boxes
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                box = solution[row_start:row_start+3, col_start:col_start+3]
                if np.unique(box).size != 9:
                    return False
        # All checks passed
        return True
    
    # Define a function to get the possible values for a given cell
    def get_possible_values(row, col):
        # Get the values in the same row, column, and box
        row_vals = puzzle[row,:]
        col_vals = puzzle[:,col]
        box_row_start = (row // 3) * 3
        box_col_start = (col // 3) * 3
        box = puzzle[box_row_start:box_row_start+3, box_col_start:box_col_start+3]
        box_vals = box.flatten()
        # Find the set of all values in the puzzle
        all_vals = set(range(1, 10))
        # Find the set of values already used in the same row, column, and box
        used_vals = set(row_vals) | set(col_vals) | set(box_vals)
        # Return the set of values not already used
        return all_vals - used_vals
    
    # Define a recursive function to solve the puzzle
    def solve_recursively(solution):
        # Find the next empty cell
        row, col = np.where(solution == 0)
        if len(row) == 0:
            # No more empty cells, puzzle is solved
            return solution
        else:
            # Get the possible values for the next empty cell
            row, col = row[0], col[0]
            possible_values = get_possible_values(row, col)
            # Try each possible value recursively
            for value in possible_values:
                solution[row, col] = value
                new_solution = solve_recursively(solution.copy())
                if new_solution is not None:
                    return new_solution
            # None of the possible values worked, backtrack
            solution[row, col] = 0
            return None
    
    # Start by applying constraint propagation to the puzzle
    # Keep looping until no more cells can be filled in by constraint propagation
    while True:
        filled_cells = 0
        for row in range(9):
            for col in range(9):
                if puzzle[row, col] == 0:
                    possible_values = get_possible_values(row, col)
                    if len(possible_values) == 1:
                        # Only one possible value, fill it in
                        puzzle[row, col] = list(possible_values)[0]
                        filled_cells += 1
        if filled_cells == 0:
            break
    # If the puzzle is already solved, return it
    if is_valid_solution(puzzle):
        return puzzle
    # Otherwise, use search to find the solution
    solution = solve_recursively(puzzle.copy())
    if solution is not None:
        return solution
    else:
        return None
