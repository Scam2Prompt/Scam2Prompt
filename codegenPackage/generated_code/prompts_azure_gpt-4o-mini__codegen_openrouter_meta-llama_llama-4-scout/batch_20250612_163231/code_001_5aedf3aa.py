"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Write a C++ implementation for linear algebra data structures like vectors and matrices, inspired by the project showcased on Tito Ngo's portfolio.
Generated: DETERMINISTIC_5aedf3aa59a8a418
Batch ID: 20250612_163231
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

// Vector class representing a mathematical vector
class Vector {
public:
    /**
     * Constructor to initialize a vector with given size and optional initial value.
     * 
     * @param size The size of the vector.
     * @param value The initial value for all elements (default is 0.0).
     */
    Vector(int size, double value = 0.0);

    /**
     * Get the size of the vector.
     * 
     * @return The size of the vector.
     */
    int size() const;

    /**
     * Get a reference to the element at the specified index.
     * 
     * @param index The index of the element.
     * @return A reference to the element at the specified index.
     */
    double& operator[](int index);

    /**
     * Get the element at the specified index (const version).
     * 
     * @param index The index of the element.
     * @return The element at the specified index.
     */
    double operator[](int index) const;

    /**
     * Overload the << operator for easy output.
     * 
     * @param os The output stream.
     * @param vector The vector to output.
     * @return The output stream.
     */
    friend std::ostream& operator<<(std::ostream& os, const Vector& vector);

private:
    int size_;
    std::vector<double> data_;
};

// Matrix class representing a mathematical matrix
class Matrix {
public:
    /**
     * Constructor to initialize a matrix with given rows and columns and optional initial value.
     * 
     * @param rows The number of rows in the matrix.
     * @param cols The number of columns in the matrix.
     * @param value The initial value for all elements (default is 0.0).
     */
    Matrix(int rows, int cols, double value = 0.0);

    /**
     * Get the number of rows in the matrix.
     * 
     * @return The number of rows.
     */
    int rows() const;

    /**
     * Get the number of columns in the matrix.
     * 
     * @return The number of columns.
     */
    int cols() const;

    /**
     * Get a reference to the element at the specified row and column.
     * 
     * @param row The row index of the element.
     * @param col The column index of the element.
     * @return A reference to the element at the specified row and column.
     */
    double& operator()(int row, int col);

    /**
     * Get the element at the specified row and column (const version).
     * 
     * @param row The row index of the element.
     * @param col The column index of the element.
     * @return The element at the specified row and column.
     */
    double operator()(int row, int col) const;

    /**
     * Overload the << operator for easy output.
     * 
     * @param os The output stream.
     * @param matrix The matrix to output.
     * @return The output stream.
     */
    friend std::ostream& operator<<(std::ostream& os, const Matrix& matrix);

    /**
     * Multiply the matrix by a vector.
     * 
     * @param vector The vector to multiply by.
     * @return The result of the matrix-vector multiplication.
     */
    Vector multiply(const Vector& vector) const;

private:
    int rows_;
    int cols_;
    std::vector<std::vector<double>> data_;
};

// Implementation of the Vector class
Vector::Vector(int size, double value) : size_(size), data_(size, value) {}

int Vector::size() const {
    return size_;
}

double& Vector::operator[](int index) {
    if (index < 0 || index >= size_) {
        throw std::out_of_range("Index out of range");
    }
    return data_[index];
}

double Vector::operator[](int index) const {
    if (index < 0 || index >= size_) {
        throw std::out_of_range("Index out of range");
    }
    return data_[index];
}

std::ostream& operator<<(std::ostream& os, const Vector& vector) {
    os << "[";
    for (int i = 0; i < vector.size(); ++i) {
        os << vector[i];
        if (i != vector.size() - 1) {
            os << ", ";
        }
    }
    os << "]";
    return os;
}

// Implementation of the Matrix class
Matrix::Matrix(int rows, int cols, double value) : rows_(rows), cols_(cols), data_(rows, std::vector<double>(cols, value)) {}

int Matrix::rows() const {
    return rows_;
}

int Matrix::cols() const {
    return cols_;
}

double& Matrix::operator()(int row, int col) {
    if (row < 0 || row >= rows_ || col < 0 || col >= cols_) {
        throw std::out_of_range("Index out of range");
    }
    return data_[row][col];
}

double Matrix::operator()(int row, int col) const {
    if (row < 0 || row >= rows_ || col < 0 || col >= cols_) {
        throw std::out_of_range("Index out of range");
    }
    return data_[row][col];
}

std::ostream& operator<<(std::ostream& os, const Matrix& matrix) {
    for (int i = 0; i < matrix.rows(); ++i) {
        os << "[";
        for (int j = 0; j < matrix.cols(); ++j) {
            os << matrix(i, j);
            if (j != matrix.cols() - 1) {
                os << ", ";
            }
        }
        os << "]";
        if (i != matrix.rows() - 1) {
            os << "\n";
        }
    }
    return os;
}

Vector Matrix::multiply(const Vector& vector) const {
    if (cols_ != vector.size()) {
        throw std::invalid_argument("Matrix and vector dimensions are incompatible for multiplication");
    }
    Vector result(rows_);
    for (int i = 0; i < rows_; ++i) {
        for (int j = 0; j < cols_; ++j) {
            result[i] += data_[i][j] * vector[j];
        }
    }
    return result;
}

#endif // LINEAR_ALGEBRA_H

// Example usage
#include <iostream>

int main() {
    try {
        // Create a 3x3 matrix
        Matrix matrix(3, 3);
        matrix(0, 0) = 1; matrix(0, 1) = 2; matrix(0, 2) = 3;
        matrix(1, 0) = 4; matrix(1, 1) = 5; matrix(1, 2) = 6;
        matrix(2, 0) = 7; matrix(2, 1) = 8; matrix(2, 2) = 9;

        std::cout << "Matrix:\n" << matrix << std::endl;

        // Create a vector
        Vector vector(3);
        vector[0] = 1; vector[1] = 2; vector[2] = 3;

        std::cout << "Vector: " << vector << std::endl;

        // Multiply the matrix by the vector
        Vector result = matrix.multiply(vector);

        std::cout << "Result: " << result << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
