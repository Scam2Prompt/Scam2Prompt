"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticsnake.github.io
Prompt: Write a Python program to perform matrix operations using object-oriented programming, referencing Tito Ngo's Python variant of linear algebra structures.
Generated: DETERMINISTIC_1980a276e832f03d
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Matrix:
    """A class to represent a matrix and perform various operations on it."""

    def __init__(self, data):
        """
        Initialize the Matrix with the given 2D list.

        :param data: A 2D list representing the matrix.
        """
        if not data or not all(isinstance(row, list) for row in data):
            raise ValueError("Data must be a non-empty 2D list.")
        
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

        # Validate that all rows have the same number of columns
        if not all(len(row) == self.cols for row in data):
            raise ValueError("All rows must have the same number of columns.")

    def __repr__(self):
        """Return the string representation of the matrix."""
        return "\n".join(" ".join(map(str, row)) for row in self.data)

    def __add__(self, other):
        """Add two matrices."""
        if not isinstance(other, Matrix):
            raise TypeError("Can only add another Matrix.")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions.")

        result_data = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result_data)

    def __sub__(self, other):
        """Subtract another matrix from this matrix."""
        if not isinstance(other, Matrix):
            raise TypeError("Can only subtract another Matrix.")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions.")

        result_data = [
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result_data)

    def __mul__(self, other):
        """Multiply this matrix by another matrix or a scalar."""
        if isinstance(other, (int, float)):  # Scalar multiplication
            result_data = [[element * other for element in row] for row in self.data]
            return Matrix(result_data)
        
        if not isinstance(other, Matrix):
            raise TypeError("Can only multiply by another Matrix or a scalar.")
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must equal number of rows in the second.")

        result_data = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result_data)

    def transpose(self):
        """Return the transpose of the matrix."""
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(transposed_data)

    def determinant(self):
        """Calculate and return the determinant of the matrix (only for 2x2 and 3x3 matrices)."""
        if self.rows != self.cols:
            raise ValueError("Determinant can only be calculated for square matrices.")
        
        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        
        if self.rows == 3:
            return (self.data[0][0] * (self.data[1][1] * self.data[2][2] - self.data[1][2] * self.data[2][1]) -
                    self.data[0][1] * (self.data[1][0] * self.data[2][2] - self.data[1][2] * self.data[2][0]) +
                    self.data[0][2] * (self.data[1][0] * self.data[2][1] - self.data[1][1] * self.data[2][0]))
            
        raise NotImplementedError("Determinant calculation is not implemented for matrices larger than 3x3.")

# Example Usage
if __name__ == "__main__":
    try:
        matrix_a = Matrix([[1, 2, 3], [4, 5, 6]])
        matrix_b = Matrix([[7, 8, 9], [10, 11, 12]])
        
        sum_matrix = matrix_a + matrix_b
        print("Sum of matrices:\n", sum_matrix)

        diff_matrix = matrix_a - matrix_b
        print("Difference of matrices:\n", diff_matrix)

        product_matrix = matrix_a * matrix_b.transpose()
        print("Product of matrices:\n", product_matrix)

        determinant_matrix = Matrix([[4, 3], [6, 2]])
        print("Determinant of matrix:\n", determinant_matrix.determinant())
    except Exception as e:
        print(f"An error occurred: {e}")
```
