# Sudoku Solver

This is a Sudoku Solver that takes a 9x9 Sudoku puzzle as input and returns the solved puzzle. If no solution is possible, it returns None. This solver uses constraint propagation and backtracking search to efficiently find the solution.

## How It Works

The Sudoku Solver is based on the following steps:

1. **Constraint Propagation**: The algorithm iteratively fills in cells that have only one possible value based on the current state of the puzzle. This step helps reduce the search space for the next step.

2. **Backtracking Search**: If the constraint propagation step does not fully solve the puzzle, the algorithm proceeds to a backtracking search. The search explores the possible values for each unfilled cell by recursively trying each value and checking if the resulting solution is valid.

The solver defines several functions for different purposes:

- `is_valid_solution(solution)`: Checks if the given solution is valid by validating rows, columns, and 3x3 boxes.

- `get_possible_values(row, col)`: Returns the set of possible values for the given cell (row, col) that are not already used in the same row, column, and box.

- `solve_recursively(solution)`: A recursive function that performs the backtracking search, trying each possible value for the empty cells.

The code provided above is an adaptation of the Sudoku solver from the blog post "[Solving Sudoku in Python with Constraint Propagation and Search](https://norvig.com/sudoku.html)" by Peter Norvig. We recommend reading the blog post for a deeper understanding of the concepts and techniques used in this solver.

## Usage

To use the Sudoku Solver, first import the required library:

```python
import numpy as np
```
Then, define your Sudoku puzzle as a 9x9 numpy array, where 0 represents an empty cell. For example:
```python
puzzle = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])
```
Finally, call the `**solve_sudoku(puzzle)**` function to get the solved puzzle:
```python
solved_puzzle = solve_sudoku(puzzle)
print(solved_puzzle)
```
