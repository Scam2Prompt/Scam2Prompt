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
import numpy as np

class Matrix:
    """
    A class to represent a matrix and perform linear algebra operations.
    """

    def __init__(self, data):
        """
        Initialize the Matrix with a 2D list or numpy array.
        :param data: 2D list or numpy array representing the matrix.
        """
        try:
            self.data = np.array(data, dtype=float)
            if self.data.ndim != 2:
                raise ValueError("Matrix data must be a 2D structure.")
        except Exception as e:
            raise ValueError(f"Error initializing matrix: {e}")

    def __repr__(self):
        """
        String representation of the matrix.
        """
        return f"Matrix({self.data})"

    def shape(self):
        """
        Return the shape of the matrix.
        :return: Tuple representing (rows, columns).
        """
        return self.data.shape
    
    def transpose(self):
        """
        Return the transpose of the matrix.
        :return: Matrix instance of the transposed matrix.
        """
        return Matrix(self.data.T)
    
    def add(self, other):
        """
        Add another matrix to this matrix.
        :param other: Matrix instance to add.
        :return: Matrix instance representing the sum.
        """
        if not isinstance(other, Matrix):
            raise TypeError("Operand must be an instance of Matrix.")
        if self.shape() != other.shape():
            raise ValueError("Matrix dimensions must match for addition.")
        return Matrix(self.data + other.data)
    
    def subtract(self, other):
        """
        Subtract another matrix from this matrix.
        :param other: Matrix instance to subtract.
        :return: Matrix instance representing the difference.
        """
        if not isinstance(other, Matrix):
            raise TypeError("Operand must be an instance of Matrix.")
        if self.shape() != other.shape():
            raise ValueError("Matrix dimensions must match for subtraction.")
        return Matrix(self.data - other.data)
    
    def multiply(self, other):
        """
        Perform matrix multiplication with another matrix.
        :param other: Matrix instance to multiply with.
        :return: Matrix instance representing the product.
        """
        if not isinstance(other, Matrix):
            raise TypeError("Operand must be an instance of Matrix.")
        if self.shape()[1] != other.shape()[0]:
            raise ValueError("Invalid dimensions for matrix multiplication.")
        return Matrix(np.dot(self.data, other.data))
    
    def scalar_multiply(self, scalar):
        """
        Multiply the matrix by a scalar.
        :param scalar: A numeric value to multiply with.
        :return: Matrix instance representing the scaled matrix.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a numeric value.")
        return Matrix(self.data * scalar)
    
    def determinant(self):
        """
        Calculate the determinant of the matrix (only for square matrices).
        :return: Determinant value.
        """
        if self.shape()[0] != self.shape()[1]:
            raise ValueError("Determinant can only be calculated for square matrices.")
        return np.linalg.det(self.data)
    
    def inverse(self):
        """
        Calculate the inverse of the matrix (only for square matrices).
        :return: Matrix instance representing the inverse.
        """
        if self.shape()[0] != self.shape()[1]:
            raise ValueError("Inverse can only be calculated for square matrices.")
        if np.linalg.det(self.data) == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        return Matrix(np.linalg.inv(self.data))


# Example usage
if __name__ == "__main__":
    try:
        # Define matrices
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[5, 6], [7, 8]])
        
        # Perform operations
        print("Matrix A:", A)
        print("Matrix B:", B)
        print("A + B:", A.add(B))
        print("A - B:", A.subtract(B))
        print("A * B:", A.multiply(B))
        print("Transpose of A:", A.transpose())
        print("Determinant of A:", A.determinant())
        print("Inverse of A:", A.inverse())
        print("A scaled by 2:", A.scalar_multiply(2))

    except Exception as e:
        print(f"Error: {e}")
```
