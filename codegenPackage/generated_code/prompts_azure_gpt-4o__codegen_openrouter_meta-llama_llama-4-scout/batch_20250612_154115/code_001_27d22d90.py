"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Create C++ classes for linear algebra data structures, such as vectors and matrices, based on the project showcased on Tito Ngo's website.
Generated: DETERMINISTIC_27d22d901c7c0471
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#ifndef LINEAR_ALGEBRA_H
#define LINEAR_ALGEBRA_H

#include <iostream>
#include <vector>
#include <stdexcept>
#include <string>
#include <sstream>

/**
 * @class Vector
 * @brief Represents a mathematical vector in n-dimensional space.
 */
class Vector {
private:
    std::vector<double> components;

public:
    /**
     * @brief Constructor to initialize a vector with given components.
     * @param components The components of the vector.
     */
    explicit Vector(const std::vector<double>& components) : components(components) {}

    /**
     * @brief Get the number of dimensions of the vector.
     * @return The number of dimensions.
     */
    size_t dimensions() const {
        return components.size();
    }

    /**
     * @brief Get the component at a specific index.
     * @param index The index of the component.
     * @return The component at the given index.
     * @throws std::out_of_range If the index is out of range.
     */
    double operator[](size_t index) const {
        if (index >= components.size()) {
            throw std::out_of_range("Index out of range");
        }
        return components[index];
    }

    /**
     * @brief Overload + operator for vector addition.
     * @param other The vector to add.
     * @return The sum of the two vectors.
     * @throws std::invalid_argument If the vectors have different dimensions.
     */
    Vector operator+(const Vector& other) const {
        if (dimensions() != other.dimensions()) {
            throw std::invalid_argument("Vectors must have the same dimensions for addition");
        }
        std::vector<double> result(dimensions());
        for (size_t i = 0; i < dimensions(); ++i) {
            result[i] = components[i] + other.components[i];
        }
        return Vector(result);
    }

    /**
     * @brief Overload - operator for vector subtraction.
     * @param other The vector to subtract.
     * @return The difference of the two vectors.
     * @throws std::invalid_argument If the vectors have different dimensions.
     */
    Vector operator-(const Vector& other) const {
        if (dimensions() != other.dimensions()) {
            throw std::invalid_argument("Vectors must have the same dimensions for subtraction");
        }
        std::vector<double> result(dimensions());
        for (size_t i = 0; i < dimensions(); ++i) {
            result[i] = components[i] - other.components[i];
        }
        return Vector(result);
    }

    /**
     * @brief Calculate the dot product of two vectors.
     * @param other The vector for the dot product.
     * @return The dot product of the two vectors.
     * @throws std::invalid_argument If the vectors have different dimensions.
     */
    double dot(const Vector& other) const {
        if (dimensions() != other.dimensions()) {
            throw std::invalid_argument("Vectors must have the same dimensions for dot product");
        }
        double result = 0.0;
        for (size_t i = 0; i < dimensions(); ++i) {
            result += components[i] * other.components[i];
        }
        return result;
    }

    /**
     * @brief Calculate the magnitude (Euclidean norm) of the vector.
     * @return The magnitude of the vector.
     */
    double magnitude() const {
        return std::sqrt(dot(*this));
    }

    /**
     * @brief Overload << operator for easy output.
     * @param os The output stream.
     * @param vector The vector to output.
     * @return The output stream.
     */
    friend std::ostream& operator<<(std::ostream& os, const Vector& vector) {
        os << "(";
        for (size_t i = 0; i < vector.components.size(); ++i) {
            os << vector.components[i];
            if (i != vector.components.size() - 1) {
                os << ", ";
            }
        }
        os << ")";
        return os;
    }
};

/**
 * @class Matrix
 * @brief Represents a mathematical matrix.
 */
class Matrix {
private:
    std::vector<std::vector<double>> data;
    size_t rows;
    size_t cols;

public:
    /**
     * @brief Constructor to initialize a matrix with given data.
     * @param data The 2D vector representing the matrix.
     */
    explicit Matrix(const std::vector<std::vector<double>>& data) : data(data), rows(data.size()), cols(data[0].size()) {
        // Check if all rows have the same number of columns
        for (const auto& row : data) {
            if (row.size() != cols) {
                throw std::invalid_argument("All rows must have the same number of columns");
            }
        }
    }

    /**
     * @brief Get the number of rows in the matrix.
     * @return The number of rows.
     */
    size_t getRows() const {
        return rows;
    }

    /**
     * @brief Get the number of columns in the matrix.
     * @return The number of columns.
     */
    size_t getCols() const {
        return cols;
    }

    /**
     * @brief Get the element at a specific row and column.
     * @param row The row index.
     * @param col The column index.
     * @return The element at the given position.
     * @throws std::out_of_range If the indices are out of range.
     */
    double operator()(size_t row, size_t col) const {
        if (row >= rows || col >= cols) {
            throw std::out_of_range("Indices out of range");
        }
        return data[row][col];
    }

    /**
     * @brief Overload * operator for matrix-vector multiplication.
     * @param vector The vector to multiply.
     * @return The result of the matrix-vector multiplication.
     * @throws std::invalid_argument If the number of columns in the matrix does not match the dimensions of the vector.
     */
    Vector operator*(const Vector& vector) const {
        if (cols != vector.dimensions()) {
            throw std::invalid_argument("Number of columns in matrix must match vector dimensions for multiplication");
        }
        std::vector<double> result(rows, 0.0);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result[i] += data[i][j] * vector[j];
            }
        }
        return Vector(result);
    }

    /**
     * @brief Overload * operator for matrix-matrix multiplication.
     * @param other The matrix to multiply.
     * @return The result of the matrix-matrix multiplication.
     * @throws std::invalid_argument If the number of columns in the first matrix does not match the number of rows in the second matrix.
     */
    Matrix operator*(const Matrix& other) const {
        if (cols != other.getRows()) {
            throw std::invalid_argument("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication");
        }
        std::vector<std::vector<double>> result(rows, std::vector<double>(other.getCols(), 0.0));
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < other.getCols(); ++j) {
                for (size_t k = 0; k < cols; ++k) {
                    result[i][j] += data[i][k] * other(k, j);
                }
            }
        }
        return Matrix(result);
    }

    /**
     * @brief Overload << operator for easy output.
     * @param os The output stream.
     * @param matrix The matrix to output.
     * @return The output stream.
     */
    friend std::ostream& operator<<(std::ostream& os, const Matrix& matrix) {
        for (size_t i = 0; i < matrix.rows; ++i) {
            os << "[";
            for (size_t j = 0; j < matrix.cols; ++j) {
                os << matrix.data[i][j];
                if (j != matrix.cols - 1) {
                    os << ", ";
                }
            }
            os << "]";
            if (i != matrix.rows - 1) {
                os << "\n";
            }
        }
        return os;
    }
};

#endif // LINEAR_ALGEBRA_H
```

```cpp
#include "linear_algebra.h"

int main() {
    try {
        // Example usage of Vector
        Vector v1({1.0, 2.0, 3.0});
        Vector v2({4.0, 5.0, 6.0});
        std::cout << "v1: " << v1 << std::endl;
        std::cout << "v2: " << v2 << std::endl;
        Vector sum = v1 + v2;
        std::cout << "v1 + v2: " << sum << std::endl;
        double dotProduct = v1.dot(v2);
        std::cout << "v1 · v2: " << dotProduct << std::endl;

        // Example usage of Matrix
        Matrix m({{1, 2}, {3, 4}});
        std::cout << "Matrix m:\n" << m << std::endl;
        Vector v({5.0
