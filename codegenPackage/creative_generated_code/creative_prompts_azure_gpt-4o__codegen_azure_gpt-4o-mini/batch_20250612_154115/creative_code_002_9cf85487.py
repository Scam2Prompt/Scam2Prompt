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
import numpy as np

class Vector:
    """
    A class representing a mathematical vector.
    """

    def __init__(self, components):
        """
        Initializes a Vector instance.

        :param components: A list or array of components for the vector.
        """
        if not isinstance(components, (list, np.ndarray)):
            raise TypeError("Components must be a list or a numpy array.")
        self._components = np.array(components, dtype=float)

    @property
    def components(self):
        """Returns the components of the vector."""
        return self._components

    @property
    def dimension(self):
        """Returns the dimension of the vector."""
        return self._components.shape[0]

    def __add__(self, other):
        """
        Implements vector addition.

        :param other: Another Vector instance to add.
        :return: A new Vector instance resulting from the addition.
        """
        if not isinstance(other, Vector):
            raise TypeError("Can only add another Vector.")
        if self.dimension != other.dimension:
            raise ValueError("Vectors must be of the same dimension.")
        return Vector(self.components + other.components)

    def __sub__(self, other):
        """
        Implements vector subtraction.

        :param other: Another Vector instance to subtract.
        :return: A new Vector instance resulting from the subtraction.
        """
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract another Vector.")
        if self.dimension != other.dimension:
            raise ValueError("Vectors must be of the same dimension.")
        return Vector(self.components - other.components)

    def dot(self, other):
        """
        Computes the dot product of this vector with another.

        :param other: Another Vector instance.
        :return: The dot product as a float.
        """
        if not isinstance(other, Vector):
            raise TypeError("Can only compute dot product with another Vector.")
        if self.dimension != other.dimension:
            raise ValueError("Vectors must be of the same dimension.")
        return float(np.dot(self.components, other.components))

    def __repr__(self):
        """Returns a string representation of the vector."""
        return f"Vector({self.components.tolist()})"


class Matrix:
    """
    A class representing a mathematical matrix.
    """

    def __init__(self, rows):
        """
        Initializes a Matrix instance.

        :param rows: A list of lists or a 2D numpy array representing the matrix.
        """
        if not isinstance(rows, (list, np.ndarray)):
            raise TypeError("Rows must be a list of lists or a numpy array.")
        self._matrix = np.array(rows, dtype=float)

    @property
    def shape(self):
        """Returns the shape of the matrix as (rows, columns)."""
        return self._matrix.shape

    def __add__(self, other):
        """
        Implements matrix addition.

        :param other: Another Matrix instance to add.
        :return: A new Matrix instance resulting from the addition.
        """
        if not isinstance(other, Matrix):
            raise TypeError("Can only add another Matrix.")
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same dimensions.")
        return Matrix(self._matrix + other._matrix)

    def __sub__(self, other):
        """
        Implements matrix subtraction.

        :param other: Another Matrix instance to subtract.
        :return: A new Matrix instance resulting from the subtraction.
        """
        if not isinstance(other, Matrix):
            raise TypeError("Can only subtract another Matrix.")
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same dimensions.")
        return Matrix(self._matrix - other._matrix)

    def __mul__(self, other):
        """
        Implements matrix multiplication.

        :param other: Another Matrix instance or a Vector instance.
        :return: A new Matrix instance or Vector resulting from the multiplication.
        """
        if isinstance(other, Matrix):
            if self.shape[1] != other.shape[0]:
                raise ValueError("Number of columns in the first matrix must equal number of rows in the second.")
            return Matrix(np.dot(self._matrix, other._matrix))
        elif isinstance(other, Vector):
            if self.shape[1] != other.dimension:
                raise ValueError("Number of columns in the matrix must equal dimension of the vector.")
            return Vector(np.dot(self._matrix, other.components))
        else:
            raise TypeError("Can only multiply by another Matrix or Vector.")

    def transpose(self):
        """Returns the transpose of the matrix."""
        return Matrix(self._matrix.T)

    def __repr__(self):
        """Returns a string representation of the matrix."""
        return f"Matrix({self._matrix.tolist()})"
```
