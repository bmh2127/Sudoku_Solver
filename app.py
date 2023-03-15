from flask import Flask, request, jsonify, make_response, send_from_directory, render_template, send_file
import numpy as np
from sudoku_solver import solve_sudoku
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return make_response("", 204)

@app.route('/solve', methods=['POST'])
def solve():
    # Extract the Sudoku puzzle from the JSON request body
    puzzle = np.array(request.json['puzzle'])
    # Solve the Sudoku puzzle
    solution = solve_sudoku(puzzle)
    if solution is not None:
        # Create a JPEG image and save it in memory
        img = create_solution_image(solution)
        buf = io.BytesIO()
        img.savefig(buf, format='jpeg')
        buf.seek(0)

        # Serve the JPEG image
        return send_file(buf, mimetype='image/jpeg')
    else:
        return jsonify({"error": "No solution found"}), 400

def create_solution_image(solution):
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.axis('tight')
    
    ax.table(cellText=solution, cellLoc='center', loc='center', edges='closed', colWidths=[0.1] * 9)
    
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

    return fig

if __name__ == '__main__':
    app.run()