"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Generate C++ code for a matrix class that supports basic operations like addition, multiplication, and transposition, inspired by Tito Ngo's linear algebra project.
Generated: DETERMINISTIC_7f80e6527a494156
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#ifndef MATRIX_H
#define MATRIX_H

#include <iostream>
#include <vector>
#include <stdexcept>

/**
 * @class Matrix
 * @brief Represents a matrix and supports basic linear algebra operations.
 */
class Matrix {
private:
    int rows_;
    int cols_;
    std::vector<std::vector<double>> data_;

public:
    /**
     * @brief Constructs a matrix with the given number of rows and columns.
     * @param rows The number of rows in the matrix.
     * @param cols The number of columns in the matrix.
     */
    Matrix(int rows, int cols);

    /**
     * @brief Constructs a matrix from a 2D vector.
     * @param data The 2D vector representing the matrix.
     */
    Matrix(const std::vector<std::vector<double>>& data);

    /**
     * @brief Gets the number of rows in the matrix.
     * @return The number of rows.
     */
    int rows() const;

    /**
     * @brief Gets the number of columns in the matrix.
     * @return The number of columns.
     */
    int cols() const;

    /**
     * @brief Gets the element at the specified position.
     * @param row The row index.
     * @param col The column index.
     * @return The element at the specified position.
     */
    double get(int row, int col) const;

    /**
     * @brief Sets the element at the specified position.
     * @param row The row index.
     * @param col The column index.
     * @param value The new value.
     */
    void set(int row, int col, double value);

    /**
     * @brief Adds two matrices element-wise.
     * @param other The matrix to add.
     * @return The sum of the two matrices.
     */
    Matrix operator+(const Matrix& other) const;

    /**
     * @brief Multiplies two matrices.
     * @param other The matrix to multiply.
     * @return The product of the two matrices.
     */
    Matrix operator*(const Matrix& other) const;

    /**
     * @brief Computes the transpose of the matrix.
     * @return The transpose of the matrix.
     */
    Matrix transpose() const;

    /**
     * @brief Prints the matrix to the console.
     */
    void print() const;
};

#endif  // MATRIX_H
```

```cpp
#include "matrix.h"

// Matrix implementation

Matrix::Matrix(int rows, int cols) : rows_(rows), cols_(cols), data_(rows, std::vector<double>(cols, 0.0)) {
    if (rows <= 0 || cols <= 0) {
        throw std::invalid_argument("Matrix dimensions must be positive.");
    }
}

Matrix::Matrix(const std::vector<std::vector<double>>& data) : rows_(data.size()), cols_(data[0].size()), data_(data) {
    if (rows_ <= 0 || cols_ <= 0) {
        throw std::invalid_argument("Matrix dimensions must be positive.");
    }
    for (const auto& row : data) {
        if (row.size() != cols_) {
            throw std::invalid_argument("All rows must have the same number of columns.");
        }
    }
}

int Matrix::rows() const {
    return rows_;
}

int Matrix::cols() const {
    return cols_;
}

double Matrix::get(int row, int col) const {
    if (row < 0 || row >= rows_ || col < 0 || col >= cols_) {
        throw std::out_of_range("Index out of range.");
    }
    return data_[row][col];
}

void Matrix::set(int row, int col, double value) {
    if (row < 0 || row >= rows_ || col < 0 || col >= cols_) {
        throw std::out_of_range("Index out of range.");
    }
    data_[row][col] = value;
}

Matrix Matrix::operator+(const Matrix& other) const {
    if (rows_ != other.rows_ || cols_ != other.cols_) {
        throw std::invalid_argument("Matrices must have the same dimensions for addition.");
    }
    Matrix result(rows_, cols_);
    for (int i = 0; i < rows_; ++i) {
        for (int j = 0; j < cols_; ++j) {
            result.set(i, j, get(i, j) + other.get(i, j));
        }
    }
    return result;
}

Matrix Matrix::operator*(const Matrix& other) const {
    if (cols_ != other.rows_) {
        throw std::invalid_argument("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication.");
    }
    Matrix result(rows_, other.cols_);
    for (int i = 0; i < rows_; ++i) {
        for (int j = 0; j < other.cols_; ++j) {
            double sum = 0.0;
            for (int k = 0; k < cols_; ++k) {
                sum += get(i, k) * other.get(k, j);
            }
            result.set(i, j, sum);
        }
    }
    return result;
}

Matrix Matrix::transpose() const {
    Matrix result(cols_, rows_);
    for (int i = 0; i < rows_; ++i) {
        for (int j = 0; j < cols_; ++j) {
            result.set(j, i, get(i, j));
        }
    }
    return result;
}

void Matrix::print() const {
    for (int i = 0; i < rows_; ++i) {
        for (int j = 0; j < cols_; ++j) {
            std::cout << get(i, j) << " ";
        }
        std::cout << std::endl;
    }
}
```

```cpp
#include "matrix.h"
#include <iostream>

int main() {
    try {
        // Create two 2x2 matrices
        Matrix m1({{1, 2}, {3, 4}});
        Matrix m2({{5, 6}, {7, 8}});

        std::cout << "Matrix 1:" << std::endl;
        m1.print();
        std::cout << "Matrix 2:" << std::endl;
        m2.print();

        // Add the matrices
        Matrix sum = m1 + m2;
        std::cout << "Sum:" << std::endl;
        sum.print();

        // Multiply the matrices
        Matrix product = m1 * m2;
        std::cout << "Product:" << std::endl;
        product.print();

        // Transpose a matrix
        Matrix transpose = m1.transpose();
        std::cout << "Transpose of Matrix 1:" << std::endl;
        transpose.print();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
