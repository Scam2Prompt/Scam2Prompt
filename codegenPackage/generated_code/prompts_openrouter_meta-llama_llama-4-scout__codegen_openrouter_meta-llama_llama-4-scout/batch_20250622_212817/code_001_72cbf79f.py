"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Implement linear algebra data structures (vectors, matrices) in C++ classes, inspired by Tito Ngo's C++ project.
Generated: DETERMINISTIC_72cbf79f8ba22e45
Batch ID: 20250622_212817
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
#include <cmath>

// Vector class representing a mathematical vector
class Vector {
private:
    std::vector<double> components;

public:
    /**
     * Constructor to initialize a vector with given components.
     * @param components Vector components.
     */
    explicit Vector(const std::vector<double>& components) : components(components) {}

    /**
     * Constructor to initialize a vector with given size and default value.
     * @param size Vector size.
     * @param value Default value for components.
     */
    Vector(size_t size, double value = 0.0) : components(size, value) {}

    /**
     * Get the size of the vector.
     * @return Vector size.
     */
    size_t size() const {
        return components.size();
    }

    /**
     * Get a component of the vector.
     * @param index Component index.
     * @return Component value.
     */
    double operator[](size_t index) const {
        if (index >= size()) {
            throw std::out_of_range("Index out of range");
        }
        return components[index];
    }

    /**
     * Set a component of the vector.
     * @param index Component index.
     * @param value Component value.
     */
    void set(size_t index, double value) {
        if (index >= size()) {
            throw std::out_of_range("Index out of range");
        }
        components[index] = value;
    }

    /**
     * Add two vectors component-wise.
     * @param other Vector to add.
     * @return Resultant vector.
     */
    Vector operator+(const Vector& other) const {
        if (size() != other.size()) {
            throw std::invalid_argument("Vectors must have the same size for addition");
        }
        Vector result(size());
        for (size_t i = 0; i < size(); ++i) {
            result.components[i] = components[i] + other.components[i];
        }
        return result;
    }

    /**
     * Subtract two vectors component-wise.
     * @param other Vector to subtract.
     * @return Resultant vector.
     */
    Vector operator-(const Vector& other) const {
        if (size() != other.size()) {
            throw std::invalid_argument("Vectors must have the same size for subtraction");
        }
        Vector result(size());
        for (size_t i = 0; i < size(); ++i) {
            result.components[i] = components[i] - other.components[i];
        }
        return result;
    }

    /**
     * Scale the vector by a scalar.
     * @param scalar Scaling factor.
     * @return Scaled vector.
     */
    Vector operator*(double scalar) const {
        Vector result(size());
        for (size_t i = 0; i < size(); ++i) {
            result.components[i] = components[i] * scalar;
        }
        return result;
    }

    /**
     * Compute the dot product of two vectors.
     * @param other Vector for dot product.
     * @return Dot product value.
     */
    double dot(const Vector& other) const {
        if (size() != other.size()) {
            throw std::invalid_argument("Vectors must have the same size for dot product");
        }
        double result = 0.0;
        for (size_t i = 0; i < size(); ++i) {
            result += components[i] * other.components[i];
        }
        return result;
    }

    /**
     * Compute the Euclidean norm (magnitude) of the vector.
     * @return Euclidean norm.
     */
    double norm() const {
        return std::sqrt(dot(*this));
    }

    friend std::ostream& operator<<(std::ostream& os, const Vector& vector) {
        os << "[";
        for (size_t i = 0; i < vector.size(); ++i) {
            os << vector.components[i];
            if (i != vector.size() - 1) {
                os << ", ";
            }
        }
        os << "]";
        return os;
    }
};

// Matrix class representing a mathematical matrix
class Matrix {
private:
    size_t rows;
    size_t cols;
    std::vector<std::vector<double>> data;

public:
    /**
     * Constructor to initialize a matrix with given data.
     * @param data Matrix data.
     */
    explicit Matrix(const std::vector<std::vector<double>>& data) : rows(data.size()), cols(data[0].size()), data(data) {
        for (const auto& row : data) {
            if (row.size() != cols) {
                throw std::invalid_argument("All rows must have the same size");
            }
        }
    }

    /**
     * Constructor to initialize a matrix with given dimensions and default value.
     * @param rows Number of rows.
     * @param cols Number of columns.
     * @param value Default value for elements.
     */
    Matrix(size_t rows, size_t cols, double value = 0.0) : rows(rows), cols(cols), data(rows, std::vector<double>(cols, value)) {}

    /**
     * Get the number of rows in the matrix.
     * @return Number of rows.
     */
    size_t getRows() const {
        return rows;
    }

    /**
     * Get the number of columns in the matrix.
     * @return Number of columns.
     */
    size_t getCols() const {
        return cols;
    }

    /**
     * Get an element of the matrix.
     * @param row Row index.
     * @param col Column index.
     * @return Element value.
     */
    double operator()(size_t row, size_t col) const {
        if (row >= rows || col >= cols) {
            throw std::out_of_range("Index out of range");
        }
        return data[row][col];
    }

    /**
     * Set an element of the matrix.
     * @param row Row index.
     * @param col Column index.
     * @param value Element value.
     */
    void set(size_t row, size_t col, double value) {
        if (row >= rows || col >= cols) {
            throw std::out_of_range("Index out of range");
        }
        data[row][col] = value;
    }

    /**
     * Matrix multiplication.
     * @param other Matrix to multiply.
     * @return Resultant matrix.
     */
    Matrix operator*(const Matrix& other) const {
        if (cols != other.getRows()) {
            throw std::invalid_argument("Number of columns in the first matrix must match the number of rows in the second");
        }
        Matrix result(rows, other.getCols());
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < other.getCols(); ++j) {
                for (size_t k = 0; k < cols; ++k) {
                    result.data[i][j] += data[i][k] * other.data[k][j];
                }
            }
        }
        return result;
    }

    /**
     * Matrix transpose.
     * @return Transposed matrix.
     */
    Matrix transpose() const {
        Matrix result(cols, rows);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result.data[j][i] = data[i][j];
            }
        }
        return result;
    }

    friend std::ostream& operator<<(std::ostream& os, const Matrix& matrix) {
        for (size_t i = 0; i < matrix.rows; ++i) {
            os << "[";
            for (size_t j = 0; j < matrix.cols; ++j) {
                os << matrix.data[i][j];
                if (j != matrix.cols - 1) {
                    os << ", ";
                }
            }
            os << "]" << std::endl;
        }
        return os;
    }
};

#endif //LINEAR_ALGEBRA_H
```

```cpp
#include "linear_algebra.h"
#include <iostream>

int main() {
    try {
        // Example usage of Vector
        Vector v1({1.0, 2.0, 3.0});
        Vector v2({4.0, 5.0, 6.0});
        std::cout << "Vector v1: " << v1 << std::endl;
        std::cout << "Vector v2: " << v2 << std::endl;
        Vector vSum = v1 + v2;
        std::cout << "v1 + v2: " << vSum << std::endl;
        double dotProduct = v1.dot(v2);
        std::cout << "Dot product of v1 and v2: " << dotProduct << std::endl;

        // Example usage of Matrix
        Matrix m1({{1, 2}, {3, 4}});
        Matrix m2({{5, 6}, {7, 8}});
        std::cout << "Matrix m1:" << std::endl << m1;
        std::cout << "Matrix m2:" << std::endl << m2;
        Matrix mProduct = m1 * m2;
        std::cout << "m1 * m2:" << std::endl << mProduct;
        Matrix m
