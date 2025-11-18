"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticsnake.github.io
Prompt: Develop a Python implementation of linear algebra structures (vectors and matrices) similar to the one referenced on Tito Ngo's GitHub linked from his portfolio website.
Generated: DETERMINISTIC_9cf85487e1fdb1ec
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# linear_algebra.py

from typing import List, Union


class Vector:
    """A class representing a mathematical vector."""
    def __init__(self, values: List[float]):
        """
        Initializes a Vector object.
        :param values: List of numerical values representing the vector.
        """
        self.values = values

    def __repr__(self) -> str:
        """
        Returns a string representation of the Vector.
        """
        return f"Vector({self.values})"

    def __add__(self, other: 'Vector') -> 'Vector':
        """
        Adds two vectors element-wise.
        :param other: The other Vector to add.
        :return: A new Vector representing the sum.
        """
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must be of the same length to add.")
        return Vector([a + b for a, b in zip(self.values, other.values)])

    def __sub__(self, other: 'Vector') -> 'Vector':
        """
        Subtracts two vectors element-wise.
        :param other: The other Vector to subtract.
        :return: A new Vector representing the difference.
        """
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must be of the same length to subtract.")
        return Vector([a - b for a, b in zip(self.values, other.values)])

    def dot(self, other: 'Vector') -> float:
        """
        Computes the dot product of two vectors.
        :param other: The other Vector for the dot product.
        :return: The dot product as a float.
        """
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must be of the same length to compute the dot product.")
        return sum(a * b for a, b in zip(self.values, other.values))

    def magnitude(self) -> float:
        """
        Computes the magnitude (length) of the vector.
        :return: The magnitude as a float.
        """
        return sum(x**2 for x in self.values)**0.5


class Matrix:
    """A class representing a mathematical matrix."""
    def __init__(self, rows: List[List[float]]):
        """
        Initializes a Matrix object.
        :param rows: List of rows, where each row is a list of numerical values.
        """
        if not rows or not all(len(r) == len(rows[0]) for r in rows):
            raise ValueError("All rows in the matrix must have the same length.")
        self.rows = rows

    def __repr__(self) -> str:
        """
        Returns a string representation of the Matrix.
        """
        return f"Matrix({self.rows})"

    @property
    def shape(self) -> (int, int):
        """
        Returns the shape of the matrix as (rows, columns).
        :return: Tuple representing the shape of the matrix.
        """
        return len(self.rows), len(self.rows[0])

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """
        Adds two matrices element-wise.
        :param other: The other Matrix to add.
        :return: A new Matrix representing the sum.
        """
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape to add.")
        return Matrix([[a + b for a, b in zip(row_a, row_b)]
                       for row_a, row_b in zip(self.rows, other.rows)])

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        """
        Subtracts two matrices element-wise.
        :param other: The other Matrix to subtract.
        :return: A new Matrix representing the difference.
        """
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape to subtract.")
        return Matrix([[a - b for a, b in zip(row_a, row_b)]
                       for row_a, row_b in zip(self.rows, other.rows)])

    def transpose(self) -> 'Matrix':
        """
        Transposes the matrix (rows become columns).
        :return: A new Matrix representing the transpose.
        """
        transposed = list(map(list, zip(*self.rows)))
        return Matrix(transposed)

    def multiply(self, other: Union['Matrix', Vector]) -> Union['Matrix', Vector]:
        """
        Multiplies the matrix with another matrix or a vector.
        :param other: The Matrix or Vector to multiply with.
        :return: A new Matrix or Vector representing the result.
        """
        if isinstance(other, Matrix):
            # Matrix multiplication
            if self.shape[1] != other.shape[0]:
                raise ValueError("Matrix multiplication not possible due to incompatible shapes.")
            result = [
                [sum(a * b for a, b in zip(row, col)) for col in zip(*other.rows)]
                for row in self.rows
            ]
            return Matrix(result)
        elif isinstance(other, Vector):
            # Matrix-vector multiplication
            if self.shape[1] != len(other.values):
                raise ValueError("Matrix and Vector shapes are incompatible for multiplication.")
            result = [sum(a * b for a, b in zip(row, other.values)) for row in self.rows]
            return Vector(result)
        else:
            raise TypeError("Unsupported type for multiplication. Must be Matrix or Vector.")
```

This code defines two classes, `Vector` and `Matrix`, with operations such as addition, subtraction, multiplication, dot product, and transpose. Proper error handling is included to ensure compatibility of dimensions, and the code follows Python best practices.
