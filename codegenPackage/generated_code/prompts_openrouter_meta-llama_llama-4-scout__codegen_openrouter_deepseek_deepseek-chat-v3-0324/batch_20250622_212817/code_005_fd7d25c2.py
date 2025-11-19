"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Write a C++ program that demonstrates object-oriented programming principles, using linear algebra structures as an example.
Generated: DETERMINISTIC_fd7d25c226e4ee40
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <iostream>
#include <vector>
#include <stdexcept>
#include <cmath>
#include <iomanip>

class Vector {
private:
    std::vector<double> elements;
    size_t dimension;

public:
    // Constructor
    Vector(size_t dim) : dimension(dim) {
        elements.resize(dim, 0.0);
    }

    Vector(const std::vector<double>& vals) : dimension(vals.size()) {
        elements = vals;
    }

    // Copy constructor
    Vector(const Vector& other) : dimension(other.dimension) {
        elements = other.elements;
    }

    // Getter for dimension
    size_t getDimension() const {
        return dimension;
    }

    // Access elements
    double& operator[](size_t index) {
        if (index >= dimension) {
            throw std::out_of_range("Index out of bounds");
        }
        return elements[index];
    }

    const double& operator[](size_t index) const {
        if (index >= dimension) {
            throw std::out_of_range("Index out of bounds");
        }
        return elements[index];
    }

    // Vector addition
    Vector operator+(const Vector& other) const {
        if (dimension != other.dimension) {
            throw std::invalid_argument("Vectors must have same dimension for addition");
        }
        Vector result(dimension);
        for (size_t i = 0; i < dimension; ++i) {
            result[i] = elements[i] + other[i];
        }
        return result;
    }

    // Vector subtraction
    Vector operator-(const Vector& other) const {
        if (dimension != other.dimension) {
            throw std::invalid_argument("Vectors must have same dimension for subtraction");
        }
        Vector result(dimension);
        for (size_t i = 0; i < dimension; ++i) {
            result[i] = elements[i] - other[i];
        }
        return result;
    }

    // Scalar multiplication
    Vector operator*(double scalar) const {
        Vector result(dimension);
        for (size_t i = 0; i < dimension; ++i) {
            result[i] = elements[i] * scalar;
        }
        return result;
    }

    // Dot product
    double dot(const Vector& other) const {
        if (dimension != other.dimension) {
            throw std::invalid_argument("Vectors must have same dimension for dot product");
        }
        double result = 0.0;
        for (size_t i = 0; i < dimension; ++i) {
            result += elements[i] * other[i];
        }
        return result;
    }

    // Magnitude
    double magnitude() const {
        return std::sqrt(dot(*this));
    }

    // Normalization
    Vector normalize() const {
        double mag = magnitude();
        if (mag == 0.0) {
            throw std::runtime_error("Cannot normalize zero vector");
        }
        return *this * (1.0 / mag);
    }

    // Print vector
    void print() const {
        std::cout << "[ ";
        for (const auto& elem : elements) {
            std::cout << std::fixed << std::setprecision(2) << elem << " ";
        }
        std::cout << "]" << std::endl;
    }
};

class Matrix {
private:
    std::vector<Vector> rows;
    size_t rowCount;
    size_t colCount;

public:
    // Constructor
    Matrix(size_t rows, size_t cols) : rowCount(rows), colCount(cols) {
        for (size_t i = 0; i < rows; ++i) {
            this->rows.emplace_back(cols);
        }
    }

    Matrix(const std::vector<std::vector<double>>& vals) : rowCount(vals.size()) {
        if (rowCount == 0) {
            throw std::invalid_argument("Matrix must have at least one row");
        }
        colCount = vals[0].size();
        for (const auto& row : vals) {
            if (row.size() != colCount) {
                throw std::invalid_argument("All rows must have same number of columns");
            }
            rows.emplace_back(row);
        }
    }

    // Getters
    size_t getRowCount() const { return rowCount; }
    size_t getColCount() const { return colCount; }

    // Access elements
    Vector& operator[](size_t index) {
        if (index >= rowCount) {
            throw std::out_of_range("Row index out of bounds");
        }
        return rows[index];
    }

    const Vector& operator[](size_t index) const {
        if (index >= rowCount) {
            throw std::out_of_range("Row index out of bounds");
        }
        return rows[index];
    }

    // Matrix addition
    Matrix operator+(const Matrix& other) const {
        if (rowCount != other.rowCount || colCount != other.colCount) {
            throw std::invalid_argument("Matrices must have same dimensions for addition");
        }
        Matrix result(rowCount, colCount);
        for (size_t i = 0; i < rowCount; ++i) {
            for (size_t j = 0; j < colCount; ++j) {
                result[i][j] = rows[i][j] + other[i][j];
            }
        }
        return result;
    }

    // Matrix multiplication
    Matrix operator*(const Matrix& other) const {
        if (colCount != other.rowCount) {
            throw std::invalid_argument("Number of columns in first matrix must match rows in second");
        }
        Matrix result(rowCount, other.colCount);
        for (size_t i = 0; i < rowCount; ++i) {
            for (size_t j = 0; j < other.colCount; ++j) {
                for (size_t k = 0; k < colCount; ++k) {
                    result[i][j] += rows[i][k] * other[k][j];
                }
            }
        }
        return result;
    }

    // Matrix-vector multiplication
    Vector operator*(const Vector& vec) const {
        if (colCount != vec.getDimension()) {
            throw std::invalid_argument("Matrix columns must match vector dimension");
        }
        Vector result(rowCount);
        for (size_t i = 0; i < rowCount; ++i) {
            for (size_t j = 0; j < colCount; ++j) {
                result[i] += rows[i][j] * vec[j];
            }
        }
        return result;
    }

    // Print matrix
    void print() const {
        for (const auto& row : rows) {
            row.print();
        }
    }
};

int main() {
    try {
        // Vector demonstration
        Vector v1({1.0, 2.0, 3.0});
        Vector v2({4.0, 5.0, 6.0});

        std::cout << "Vector v1: ";
        v1.print();
        std::cout << "Vector v2: ";
        v2.print();

        Vector v3 = v1 + v2;
        std::cout << "v1 + v2: ";
        v3.print();

        Vector v4 = v1 - v2;
        std::cout << "v1 - v2: ";
        v4.print();

        Vector v5 = v1 * 2.5;
        std::cout << "v1 * 2.5: ";
        v5.print();

        std::cout << "Dot product v1.v2: " << v1.dot(v2) << std::endl;
        std::cout << "Magnitude of v1: " << v1.magnitude() << std::endl;

        Vector v6 = v1.normalize();
        std::cout << "Normalized v1: ";
        v6.print();

        // Matrix demonstration
        Matrix m1({
            {1.0, 2.0, 3.0},
            {4.0, 5.0, 6.0},
            {7.0, 8.0, 9.0}
        });

        Matrix m2({
            {9.0, 8.0, 7.0},
            {6.0, 5.0, 4.0},
            {3.0, 2.0, 1.0}
        });

        std::cout << "\nMatrix m1:" << std::endl;
        m1.print();
        std::cout << "Matrix m2:" << std::endl;
        m2.print();

        Matrix m3 = m1 + m2;
        std::cout << "m1 + m2:" << std::endl;
        m3.print();

        Matrix m4 = m1 * m2;
        std::cout << "m1 * m2:" << std::endl;
        m4.print();

        Vector v7 = m1 * v1;
        std::cout << "m1 * v1: ";
        v7.print();

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
