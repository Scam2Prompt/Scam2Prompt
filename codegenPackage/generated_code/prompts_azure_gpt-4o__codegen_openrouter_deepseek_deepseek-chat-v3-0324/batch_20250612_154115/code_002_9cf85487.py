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
from typing import List, Union, Optional, overload

class Vector:
    """
    A mathematical vector with basic linear algebra operations.
    """
    
    def __init__(self, components: List[float]):
        """
        Initialize a vector with given components.
        
        Args:
            components: List of float values representing vector components
        """
        if not components:
            raise ValueError("Vector must have at least one component")
        self.components = components.copy()
    
    def __str__(self) -> str:
        """String representation of the vector."""
        return f"Vector({self.components})"
    
    def __repr__(self) -> str:
        """Official string representation of the vector."""
        return self.__str__()
    
    def __len__(self) -> int:
        """Return the dimension of the vector."""
        return len(self.components)
    
    def __getitem__(self, index: int) -> float:
        """Get component at given index."""
        return self.components[index]
    
    def __setitem__(self, index: int, value: float):
        """Set component at given index."""
        self.components[index] = value
    
    def __eq__(self, other: object) -> bool:
        """Check if two vectors are equal."""
        if not isinstance(other, Vector):
            return False
        return self.components == other.components
    
    def __add__(self, other: 'Vector') -> 'Vector':
        """Add two vectors of same dimension."""
        if len(self) != len(other):
            raise ValueError("Vectors must be of same dimension for addition")
        return Vector([a + b for a, b in zip(self.components, other.components)])
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        """Subtract two vectors of same dimension."""
        if len(self) != len(other):
            raise ValueError("Vectors must be of same dimension for subtraction")
        return Vector([a - b for a, b in zip(self.components, other.components)])
    
    def __mul__(self, scalar: float) -> 'Vector':
        """Multiply vector by scalar."""
        return Vector([a * scalar for a in self.components])
    
    def __rmul__(self, scalar: float) -> 'Vector':
        """Multiply scalar by vector (commutative)."""
        return self.__mul__(scalar)
    
    def dot(self, other: 'Vector') -> float:
        """Compute dot product with another vector."""
        if len(self) != len(other):
            raise ValueError("Vectors must be of same dimension for dot product")
        return sum(a * b for a, b in zip(self.components, other.components))
    
    def magnitude(self) -> float:
        """Compute the magnitude (length) of the vector."""
        return math.sqrt(sum(a**2 for a in self.components))
    
    def normalize(self) -> 'Vector':
        """Return a unit vector in the same direction."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return self * (1.0 / mag)
    
    def cross(self, other: 'Vector') -> 'Vector':
        """Compute cross product (only for 3D vectors)."""
        if len(self) != 3 or len(other) != 3:
            raise ValueError("Cross product only defined for 3D vectors")
        a, b, c = self.components
        d, e, f = other.components
        return Vector([
            b * f - c * e,
            c * d - a * f,
            a * e - b * d
        ])

class Matrix:
    """
    A mathematical matrix with basic linear algebra operations.
    """
    
    def __init__(self, rows: List[List[float]]):
        """
        Initialize a matrix with given rows.
        
        Args:
            rows: List of lists representing matrix rows
        """
        if not rows:
            raise ValueError("Matrix must have at least one row")
        row_len = len(rows[0])
        if row_len == 0:
            raise ValueError("Matrix rows must have at least one element")
        for row in rows:
            if len(row) != row_len:
                raise ValueError("All matrix rows must have same length")
        self.rows = [row.copy() for row in rows]
    
    def __str__(self) -> str:
        """String representation of the matrix."""
        return f"Matrix({self.rows})"
    
    def __repr__(self) -> str:
        """Official string representation of the matrix."""
        return self.__str__()
    
    def __eq__(self, other: object) -> bool:
        """Check if two matrices are equal."""
        if not isinstance(other, Matrix):
            return False
        return self.rows == other.rows
    
    def num_rows(self) -> int:
        """Return number of rows in the matrix."""
        return len(self.rows)
    
    def num_cols(self) -> int:
        """Return number of columns in the matrix."""
        return len(self.rows[0]) if self.rows else 0
    
    def __getitem__(self, index: tuple[int, int]) -> float:
        """Get element at given (row, col) index."""
        row, col = index
        return self.rows[row][col]
    
    def __setitem__(self, index: tuple[int, int], value: float):
        """Set element at given (row, col) index."""
        row, col = index
        self.rows[row][col] = value
    
    def __add__(self, other: 'Matrix') -> 'Matrix':
        """Add two matrices of same dimensions."""
        if self.num_rows() != other.num_rows() or self.num_cols() != other.num_cols():
            raise ValueError("Matrices must be of same dimensions for addition")
        return Matrix([
            [a + b for a, b in zip(row_a, row_b)]
            for row_a, row_b in zip(self.rows, other.rows)
        ])
    
    def __sub__(self, other: 'Matrix') -> 'Matrix':
        """Subtract two matrices of same dimensions."""
        if self.num_rows() != other.num_rows() or self.num_cols() != other.num_cols():
            raise ValueError("Matrices must be of same dimensions for subtraction")
        return Matrix([
            [a - b for a, b in zip(row_a, row_b)]
            for row_a, row_b in zip(self.rows, other.rows)
        ])
    
    def __mul__(self, other: Union['Matrix', float]) -> Union['Matrix', 'Vector']:
        """
        Multiply matrix by another matrix, vector, or scalar.
        
        Args:
            other: Matrix, Vector, or scalar to multiply by
            
        Returns:
            Result of multiplication
        """
        if isinstance(other, (int, float)):
            return self._scalar_multiply(other)
        elif isinstance(other, Vector):
            return self._vector_multiply(other)
        elif isinstance(other, Matrix):
            return self._matrix_multiply(other)
        else:
            raise TypeError(f"Cannot multiply Matrix by {type(other)}")
    
    def __rmul__(self, scalar: float) -> 'Matrix':
        """Multiply scalar by matrix (commutative)."""
        return self._scalar_multiply(scalar)
    
    def _scalar_multiply(self, scalar: float) -> 'Matrix':
        """Multiply matrix by scalar."""
        return Matrix([
            [a * scalar for a in row]
            for row in self.rows
        ])
    
    def _vector_multiply(self, vector: Vector) -> Vector:
        """Multiply matrix by vector."""
        if self.num_cols() != len(vector):
            raise ValueError("Matrix columns must match vector dimension for multiplication")
        return Vector([
            sum(a * b for a, b in zip(row, vector.components))
            for row in self.rows
        ])
    
    def _matrix_multiply(self, other: 'Matrix') -> 'Matrix':
        """Multiply matrix by another matrix."""
        if self.num_cols() != other.num_rows():
            raise ValueError("Number of columns in first matrix must match number of rows in second matrix")
        
        result = []
        for i in range(self.num_rows()):
            row = []
            for j in range(other.num_cols()):
                element = sum(self[i, k] * other[k, j] for k in range(self.num_cols()))
                row.append(element)
            result.append(row)
        return Matrix(result)
    
    def transpose(self) -> 'Matrix':
        """Return the transpose of the matrix."""
        return Matrix([
            [self.rows[j][i] for j in range(self.num_rows())]
            for i in range(self.num_cols())
        ])
    
    def determinant(self) -> float:
        """Compute the determinant of the matrix (only for square matrices)."""
        if self.num_rows() != self.num_cols():
            raise ValueError("Determinant only defined for square matrices")
        
        n = self.num_rows()
        if n == 1:
            return self[0, 0]
        elif n == 2:
            return self[0, 0] * self[1, 1] - self[0, 1] * self[1, 0
