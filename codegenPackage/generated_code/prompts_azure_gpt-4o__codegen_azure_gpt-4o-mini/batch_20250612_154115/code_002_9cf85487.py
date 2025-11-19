"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Develop a Python implementation of linear algebra structures (vectors and matrices) similar to the one referenced on Tito Ngo's GitHub linked from his portfolio website.
Generated: DETERMINISTIC_9cf85487e1fdb1ec
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Union

class Vector:
    """A class to represent a mathematical vector."""
    
    def __init__(self, components: List[Union[int, float]]):
        """Initialize the vector with given components."""
        if not components:
            raise ValueError("Vector components cannot be empty.")
        self.components = components

    def __add__(self, other: 'Vector') -> 'Vector':
        """Add two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension to add.")
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other: 'Vector') -> 'Vector':
        """Subtract two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension to subtract.")
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def dot(self, other: 'Vector') -> float:
        """Calculate the dot product of two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self) -> float:
        """Calculate the magnitude (length) of the vector."""
        return math.sqrt(sum(x ** 2 for x in self.components))

    def __repr__(self) -> str:
        """Return a string representation of the vector."""
        return f"Vector({self.components})"


class Matrix:
    """A class to represent a mathematical matrix."""
    
    def __init__(self, rows: List[List[Union[int, float]]]):
        """Initialize the matrix with given rows."""
        if not rows or not all(len(row) == len(rows[0]) for row in rows):
            raise ValueError("Matrix must be non-empty and all rows must have the same length.")
        self.rows = rows

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """Add two matrices."""
        if len(self.rows) != len(other.rows) or len(self.rows[0]) != len(other.rows[0]):
            raise ValueError("Matrices must be of the same dimensions to add.")
        return Matrix([[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self.rows, other.rows)])

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        """Subtract two matrices."""
        if len(self.rows) != len(other.rows) or len(self.rows[0]) != len(other.rows[0]):
            raise ValueError("Matrices must be of the same dimensions to subtract.")
        return Matrix([[a - b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self.rows, other.rows)])

    def transpose(self) -> 'Matrix':
        """Transpose the matrix."""
        return Matrix([[self.rows[j][i] for j in range(len(self.rows))] for i in range(len(self.rows[0]))])

    def __repr__(self) -> str:
        """Return a string representation of the matrix."""
        return f"Matrix({self.rows})"

    def multiply(self, other: 'Matrix') -> 'Matrix':
        """Multiply two matrices."""
        if len(self.rows[0]) != len(other.rows):
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second.")
        result = [[0 for _ in range(len(other.rows[0]))] for _ in range(len(self.rows))]
        for i in range(len(self.rows)):
            for j in range(len(other.rows[0])):
                result[i][j] = sum(self.rows[i][k] * other.rows[k][j] for k in range(len(other.rows)))
        return Matrix(result)

# Example usage:
if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    print("Vector Addition:", v1 + v2)
    print("Dot Product:", v1.dot(v2))
    print("Magnitude of v1:", v1.magnitude())

    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    print("Matrix Addition:", m1 + m2)
    print("Matrix Transpose:", m1.transpose())
    print("Matrix Multiplication:", m1.multiply(m2))
```
