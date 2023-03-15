# Sudoku Solver API
Brandon Hager
`bmh2127@gmail.com`  
This API provides a simple interface to solve Sudoku puzzles. The API accepts a 9x9 Sudoku puzzle as input and returns a solved puzzle in the form of a JSON array and a visual representation in JPEG format.

## Getting Started
These instructions will help you set up and run the Sudoku Solver API on your local machine.

Prerequisites
Python 3.8 or higher
Flask
NumPy
Matplotlib
Installing

## Clone the repository to your local machine:
<pre>
```bash
git clone https://github.com/yourusername/sudoku_solver_api.git
```
</pre>
Change to the project directory:
<pre>
```bash
cd sudoku_solver_api
```
</pre>
Install the required packages:
<pre>
```bash
pip install -r requirements.txt
```
</pre>

## Running the API

To run the API locally, execute the following command:
<pre>
```bash
flask run
```
</pre>
The API will be accessible at http://127.0.0.1:5000/.
## API Usage
## POST /solve
Solve a Sudoku puzzle.

## Input
JSON payload with a puzzle field containing a 9x9 Sudoku puzzle as a list of lists.
Example:

<pre>
```bash
{
  "puzzle": [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
  ]
}
```
</pre>

## Output
Solved puzzle as a JSON array and a visual representation in JPEG format.


