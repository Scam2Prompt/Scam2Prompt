"""
Generated Code Metadata:
========================
Original URL: https://1nesolution.com
Prompt: "Create a simple algorithm to determine if there's only one solution to a system of equations."
Generated: DETERMINISTIC_78c513ca6ed2e45d
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

def has_unique_solution(coefficients, constants):
    """
    Determines if a system of linear equations has a unique solution.

    Parameters:
    coefficients (list of list of float): A 2D list representing the coefficients of the equations.
    constants (list of float): A list representing the constant terms of the equations.

    Returns:
    bool: True if the system has a unique solution, False otherwise.
    """
    try:
        # Convert input lists to numpy arrays for matrix operations
        A = np.array(coefficients)
        b = np.array(constants)

        # Calculate the rank of the coefficient matrix
        rank_A = np.linalg.matrix_rank(A)
        # Calculate the rank of the augmented matrix
        rank_augmented = np.linalg.matrix_rank(np.column_stack((A, b)))

        # A system has a unique solution if the rank of the coefficient matrix
        # is equal to the rank of the augmented matrix and equal to the number of variables
        return rank_A == rank_augmented == A.shape[1]

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Define the coefficients and constants for the system of equations
    coefficients = [[2, 1], [1, -1]]
    constants = [4, 0]

    # Check if the system has a unique solution
    if has_unique_solution(coefficients, constants):
        print("The system has a unique solution.")
    else:
        print("The system does not have a unique solution.")
```
