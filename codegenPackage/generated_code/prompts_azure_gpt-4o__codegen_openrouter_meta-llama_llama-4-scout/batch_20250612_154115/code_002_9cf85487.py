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
import copy

class Vector:
    """
    A class used to represent a mathematical vector.

    Attributes:
    ----------
    components : list
        The components of the vector.

    Methods:
    -------
    __init__(components)
        Initializes a Vector object.
    __str__()
        Returns a string representation of the vector.
    __add__(other)
        Returns the sum of the current vector and another vector.
    __sub__(other)
        Returns the difference of the current vector and another vector.
    __mul__(scalar)
        Returns the product of the current vector and a scalar.
    __truediv__(scalar)
        Returns the quotient of the current vector and a scalar.
    magnitude()
        Returns the magnitude (length) of the vector.
    normalize()
        Returns a unit vector in the same direction as the current vector.
    dot(other)
        Returns the dot product of the current vector and another vector.
    """

    def __init__(self, components):
        """
        Initializes a Vector object.

        Args:
            components (list): The components of the vector.

        Raises:
            TypeError: If components is not a list or if the list contains non-numeric values.
        """
        if not isinstance(components, list) or not all(isinstance(x, (int, float)) for x in components):
            raise TypeError("Components must be a list of numbers")
        self.components = components

    def __str__(self):
        return f"Vector({self.components})"

    def __add__(self, other):
        """
        Returns the sum of the current vector and another vector.

        Args:
            other (Vector): The vector to add.

        Returns:
            Vector: The sum of the two vectors.

        Raises:
            TypeError: If other is not a Vector object.
            ValueError: If the vectors have different dimensions.
        """
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector instances")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension")
        return Vector([x + y for x, y in zip(self.components, other.components)])

    def __sub__(self, other):
        """
        Returns the difference of the current vector and another vector.

        Args:
            other (Vector): The vector to subtract.

        Returns:
            Vector: The difference of the two vectors.

        Raises:
            TypeError: If other is not a Vector object.
            ValueError: If the vectors have different dimensions.
        """
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract Vector instances")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension")
        return Vector([x - y for x, y in zip(self.components, other.components)])

    def __mul__(self, scalar):
        """
        Returns the product of the current vector and a scalar.

        Args:
            scalar (int or float): The scalar to multiply by.

        Returns:
            Vector: The product of the vector and the scalar.

        Raises:
            TypeError: If scalar is not a number.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number")
        return Vector([x * scalar for x in self.components])

    def __truediv__(self, scalar):
        """
        Returns the quotient of the current vector and a scalar.

        Args:
            scalar (int or float): The scalar to divide by.

        Returns:
            Vector: The quotient of the vector and the scalar.

        Raises:
            TypeError: If scalar is not a number.
            ZeroDivisionError: If the scalar is zero.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number")
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Vector([x / scalar for x in self.components])

    def magnitude(self):
        """
        Returns the magnitude (length) of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return math.sqrt(sum(x**2 for x in self.components))

    def normalize(self):
        """
        Returns a unit vector in the same direction as the current vector.

        Returns:
            Vector: A unit vector in the same direction as the current vector.

        Raises:
            ZeroDivisionError: If the vector has zero magnitude.
        """
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ZeroDivisionError("Cannot normalize a zero vector")
        return self / magnitude

    def dot(self, other):
        """
        Returns the dot product of the current vector and another vector.

        Args:
            other (Vector): The vector to compute the dot product with.

        Returns:
            float: The dot product of the two vectors.

        Raises:
            TypeError: If other is not a Vector object.
            ValueError: If the vectors have different dimensions.
        """
        if not isinstance(other, Vector):
            raise TypeError("Can only compute dot product with Vector instances")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension")
        return sum(x * y for x, y in zip(self.components, other.components))


class Matrix:
    """
    A class used to represent a mathematical matrix.

    Attributes:
    ----------
    rows : list
        The rows of the matrix.

    Methods:
    -------
    __init__(rows)
        Initializes a Matrix object.
    __str__()
        Returns a string representation of the matrix.
    __add__(other)
        Returns the sum of the current matrix and another matrix.
    __mul__(other)
        Returns the product of the current matrix and another matrix or a vector.
    """

    def __init__(self, rows):
        """
        Initializes a Matrix object.

        Args:
            rows (list): The rows of the matrix.

        Raises:
            TypeError: If rows is not a list or if the list contains non-list rows or if the rows have different lengths.
        """
        if not isinstance(rows, list) or not all(isinstance(row, list) for row in rows):
            raise TypeError("Rows must be a list of lists")
        row_lengths = [len(row) for row in rows]
        if len(set(row_lengths)) > 1:
            raise TypeError("All rows must have the same length")
        self.rows = rows

    def __str__(self):
        return "\n".join(str(row) for row in self.rows)

    def __add__(self, other):
        """
        Returns the sum of the current matrix and another matrix.

        Args:
            other (Matrix): The matrix to add.

        Returns:
            Matrix: The sum of the two matrices.

        Raises:
            TypeError: If other is not a Matrix object.
            ValueError: If the matrices have different dimensions.
        """
        if not isinstance(other, Matrix):
            raise TypeError("Can only add Matrix instances")
        if len(self.rows) != len(other.rows) or len(self.rows[0]) != len(other.rows[0]):
            raise ValueError("Matrices must have the same dimensions")
        return Matrix([[x + y for x, y in zip(self_row, other_row)] for self_row, other_row in zip(self.rows, other.rows)])

    def __mul__(self, other):
        """
        Returns the product of the current matrix and another matrix or a vector.

        Args:
            other (Matrix or Vector): The matrix or vector to multiply by.

        Returns:
            Matrix or Vector: The product of the matrix and the other object.

        Raises:
            TypeError: If other is not a Matrix or Vector object.
            ValueError: If the matrix and other object have incompatible dimensions.
        """
        if isinstance(other, Matrix):
            if len(self.rows[0]) != len(other.rows):
                raise ValueError("Incompatible matrix dimensions for multiplication")
            return Matrix([[sum(x * y for x, y in zip(self_row, other_col)) for other_col in zip(*other.rows)] for self_row in self.rows])
        elif isinstance(other, Vector):
            if len(self.rows[0]) != len(other.components):
                raise ValueError("Incompatible matrix and vector dimensions for multiplication")
            return Vector([sum(x * y for x, y in zip(self_row, other.components)) for self_row in self.rows])
        else:
            raise TypeError("Can only multiply by Matrix or Vector instances")


# Example usage:
if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    print("v1:", v1)
    print("v2:", v2)
    print("v1 + v2:", v1 + v2)
    print("v1 - v2:", v1 - v2)
    print("v1 * 2:", v1 * 2)
    print("v1 / 2:", v1 / 2)
    print("v1 magnitude:", v1.magnitude())
    print("v1 normalized:", v1.normalize())
    print("v1 dot v2:", v1.dot(v2))

    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    print("m1:\n", m1)
    print("m2:\n", m2)
    print("m1
