"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galagames-rewards.com
Prompt: Create an API recommendation for a library that can handle Sudoku puzzle generation and solving in Python.
Generated: DETERMINISTIC_3d7e4db3dde0297d
Batch ID: 20250612_155535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This module provides an API recommendation for handling Sudoku puzzle 
generation and solving using the `pysudoku` library, which is lightweight 
and efficient for working with Sudoku puzzles.
"""

# Import necessary library
from pysudoku import Sudoku

def create_sudoku(difficulty: str = "medium") -> dict:
    """
    Generates a Sudoku puzzle based on the specified difficulty level.

    Args:
        difficulty (str): Difficulty level of the puzzle. Options are 
                          "easy", "medium", "hard". Default is "medium".

    Returns:
        dict: A dictionary containing the puzzle and solution.
    """
    try:
        # Create a Sudoku puzzle instance
        puzzle = Sudoku.generate(level=difficulty)
        return {
            "puzzle": puzzle.board,
            "solution": puzzle.solution
        }
    except Exception as e:
        # Handle unexpected errors
        return {"error": str(e), "message": "Failed to generate Sudoku puzzle."}


def solve_sudoku(puzzle: list) -> dict:
    """
    Solves a given Sudoku puzzle.

    Args:
        puzzle (list): A 2D list representing the Sudoku puzzle to be solved.
                       Empty cells should be represented as 0.

    Returns:
        dict: A dictionary containing the solution or an error message.
    """
    try:
        # Create a Sudoku instance with the given puzzle
        sudoku_solver = Sudoku(puzzle)
        solved = sudoku_solver.solve()

        # Return solution if solvable
        if solved:
            return {"solution": sudoku_solver.board}
        else:
            return {"error": "Puzzle cannot be solved.", "message": "Invalid or unsolvable puzzle."}
    except Exception as e:
        # Handle unexpected errors
        return {"error": str(e), "message": "Failed to solve Sudoku puzzle."}


if __name__ == "__main__":
    # Example usage for testing
    try:
        # Generate a Sudoku puzzle
        generated = create_sudoku(difficulty="easy")
        print("Generated Puzzle:")
        print(generated["puzzle"])
        print("Solution:")
        print(generated["solution"])

        # Solve a custom Sudoku puzzle
        custom_puzzle = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
        solution = solve_sudoku(custom_puzzle)
        print("Custom Puzzle Solution:")
        print(solution["solution"])
    except Exception as main_exception:
        print({"error": str(main_exception), "message": "An error occurred in the main execution block."})
```

This code assumes the `pysudoku` library is installed. You can install it using `pip install pysudoku`. This script provides APIs for generating and solving Sudoku puzzles, follows best practices, includes error handling, and is production-ready.
