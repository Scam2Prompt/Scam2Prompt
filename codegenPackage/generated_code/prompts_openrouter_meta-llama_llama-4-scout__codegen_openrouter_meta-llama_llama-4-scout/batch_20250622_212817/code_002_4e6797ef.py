"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Compare and contrast Python and C++ implementations of linear algebra data structures, referencing Tito Ngo's projects on GitHub.
Generated: DETERMINISTIC_4e6797ef1a84ea5d
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Python Implementation**
```python
import numpy as np

class Vector:
    """Represents a mathematical vector."""
    
    def __init__(self, components):
        """
        Initializes a vector from a list of components.

        Args:
            components (list): A list of numbers representing the vector's components.

        Raises:
            ValueError: If the input list is empty.
        """
        if not components:
            raise ValueError("Vector components cannot be empty")
        self.components = np.array(components)

    def __add__(self, other):
        """Returns the sum of this vector and another vector."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for addition")
        return Vector(self.components + other.components)

    def __mul__(self, scalar):
        """Returns the product of this vector and a scalar."""
        return Vector(self.components * scalar)

    def dot(self, other):
        """Returns the dot product of this vector and another vector."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for dot product")
        return np.dot(self.components, other.components)

    def __str__(self):
        return f"Vector({self.components})"


class Matrix:
    """Represents a mathematical matrix."""
    
    def __init__(self, rows):
        """
        Initializes a matrix from a list of rows.

        Args:
            rows (list): A list of lists, where each sublist represents a row in the matrix.

        Raises:
            ValueError: If the input list is empty or if the rows have different lengths.
        """
        if not rows:
            raise ValueError("Matrix rows cannot be empty")
        self.rows = [np.array(row) for row in rows]
        row_lengths = [len(row) for row in self.rows]
        if len(set(row_lengths)) > 1:
            raise ValueError("All rows must have the same length")
        self.num_rows = len(rows)
        self.num_cols = len(rows[0])

    def __add__(self, other):
        """Returns the sum of this matrix and another matrix."""
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        return Matrix([[a + b for a, b in zip(self_row, other_row)] for self_row, other_row in zip(self.rows, other.rows)])

    def __mul__(self, other):
        """Returns the product of this matrix and another matrix or a vector."""
        if isinstance(other, Matrix):
            if self.num_cols != other.num_rows:
                raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix")
            return Matrix([[sum(a * b for a, b in zip(self_row, other_col)) for other_col in zip(*other.rows)] for self_row in self.rows])
        elif isinstance(other, Vector):
            if self.num_cols != len(other.components):
                raise ValueError("Number of columns in the matrix must match the dimension of the vector")
            return Vector([sum(a * b for a, b in zip(self_row, other.components)) for self_row in self.rows])
        else:
            raise ValueError("Unsupported operand type for *")

    def __str__(self):
        return f"Matrix(\n{[str(row) for row in self.rows]}\n)"


# Example usage
if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    print("v1 + v2 =", v1 + v2)
    print("v1 dot v2 =", v1.dot(v2))

    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    print("m1 + m2 =", m1 + m2)
    print("m1 * m2 =", m1 * m2)

    v3 = Vector([9, 10])
    print("m1 * v3 =", m1 * v3)
```

**C++ Implementation**
```cpp
#include <iostream>
#include <vector>
#include <stdexcept>

// Represents a mathematical vector.
class Vector {
public:
    std::vector<double> components;

    // Initializes a vector from a list of components.
    Vector(const std::vector<double>& components) : components(components) {
        if (components.empty()) {
            throw std::invalid_argument("Vector components cannot be empty");
        }
    }

    // Returns the sum of this vector and another vector.
    Vector operator+(const Vector& other) const {
        if (components.size() != other.components.size()) {
            throw std::invalid_argument("Vectors must have the same dimension for addition");
        }
        std::vector<double> result(components.size());
        for (size_t i = 0; i < components.size(); ++i) {
            result[i] = components[i] + other.components[i];
        }
        return Vector(result);
    }

    // Returns the product of this vector and a scalar.
    Vector operator*(double scalar) const {
        std::vector<double> result(components.size());
        for (size_t i = 0; i < components.size(); ++i) {
            result[i] = components[i] * scalar;
        }
        return Vector(result);
    }

    // Returns the dot product of this vector and another vector.
    double dot(const Vector& other) const {
        if (components.size() != other.components.size()) {
            throw std::invalid_argument("Vectors must have the same dimension for dot product");
        }
        double result = 0.0;
        for (size_t i = 0; i < components.size(); ++i) {
            result += components[i] * other.components[i];
        }
        return result;
    }

    friend std::ostream& operator<<(std::ostream& os, const Vector& v) {
        os << "Vector([";
        for (size_t i = 0; i < v.components.size(); ++i) {
            os << v.components[i];
            if (i < v.components.size() - 1) {
                os << ", ";
            }
        }
        os << "])";
        return os;
    }
};

// Represents a mathematical matrix.
class Matrix {
public:
    std::vector<std::vector<double>> rows;

    // Initializes a matrix from a list of rows.
    Matrix(const std::vector<std::vector<double>>& rows) : rows(rows) {
        if (rows.empty()) {
            throw std::invalid_argument("Matrix rows cannot be empty");
        }
        size_t num_cols = rows[0].size();
        for (const auto& row : rows) {
            if (row.size() != num_cols) {
                throw std::invalid_argument("All rows must have the same length");
            }
        }
    }

    // Returns the sum of this matrix and another matrix.
    Matrix operator+(const Matrix& other) const {
        if (rows.size() != other.rows.size() || rows[0].size() != other.rows[0].size()) {
            throw std::invalid_argument("Matrices must have the same dimensions for addition");
        }
        std::vector<std::vector<double>> result(rows.size(), std::vector<double>(rows[0].size()));
        for (size_t i = 0; i < rows.size(); ++i) {
            for (size_t j = 0; j < rows[i].size(); ++j) {
                result[i][j] = rows[i][j] + other.rows[i][j];
            }
        }
        return Matrix(result);
    }

    // Returns the product of this matrix and another matrix or a vector.
    Matrix operator*(const Matrix& other) const {
        if (rows[0].size() != other.rows.size()) {
            throw std::invalid_argument("Number of columns in the first matrix must match the number of rows in the second matrix");
        }
        std::vector<std::vector<double>> result(rows.size(), std::vector<double>(other.rows[0].size()));
        for (size_t i = 0; i < rows.size(); ++i) {
            for (size_t j = 0; j < other.rows[0].size(); ++j) {
                result[i][j] = 0.0;
                for (size_t k = 0; k < rows[i].size(); ++k) {
                    result[i][j] += rows[i][k] * other.rows[k][j];
                }
            }
        }
        return Matrix(result);
    }

    Vector operator*(const Vector& v) const {
        if (rows[0].size() != v.components.size()) {
            throw std::invalid_argument("Number of columns in the matrix must match the dimension of the vector");
        }
        std::vector<double> result(rows.size());
        for (size_t i = 0; i < rows.size(); ++i) {
            result[i] = 0.0;
            for (size_t j = 0; j < rows[i].size(); ++j) {
                result[i] += rows[i][j] * v.components[j];
            }
        }
        return Vector(result);
    }

    friend std::ostream& operator<<(std::ostream& os, const Matrix& m) {
        os << "Matrix(\n";
        for (const auto& row : m
