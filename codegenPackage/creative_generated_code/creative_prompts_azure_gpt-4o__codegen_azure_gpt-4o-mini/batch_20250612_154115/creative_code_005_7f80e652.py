"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticsnake.github.io
Prompt: Generate C++ code for a matrix class that supports basic operations like addition, multiplication, and transposition, inspired by Tito Ngo's linear algebra project.
Generated: DETERMINISTIC_7f80e6527a494156
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cpp
#include <iostream>
#include <vector>
#include <stdexcept>

class Matrix {
public:
    // Constructor to create a matrix of given rows and columns
    Matrix(size_t rows, size_t cols) : rows_(rows), cols_(cols), data_(rows, std::vector<double>(cols, 0.0)) {}

    // Accessor for individual elements
    double& operator()(size_t row, size_t col) {
        if (row >= rows_ || col >= cols_) {
            throw std::out_of_range("Matrix indices out of range");
        }
        return data_[row][col];
    }

    // Const accessor for individual elements
    const double& operator()(size_t row, size_t col) const {
        if (row >= rows_ || col >= cols_) {
            throw std::out_of_range("Matrix indices out of range");
        }
        return data_[row][col];
    }

    // Get number of rows
    size_t rows() const { return rows_; }

    // Get number of columns
    size_t cols() const { return cols_; }

    // Matrix addition
    Matrix operator+(const Matrix& other) const {
        if (rows_ != other.rows_ || cols_ != other.cols_) {
            throw std::invalid_argument("Matrix dimensions do not match for addition");
        }
        
        Matrix result(rows_, cols_);
        for (size_t i = 0; i < rows_; ++i) {
            for (size_t j = 0; j < cols_; ++j) {
                result(i, j) = (*this)(i, j) + other(i, j);
            }
        }
        return result;
    }

    // Matrix multiplication
    Matrix operator*(const Matrix& other) const {
        if (cols_ != other.rows_) {
            throw std::invalid_argument("Matrix dimensions do not match for multiplication");
        }

        Matrix result(rows_, other.cols_);
        for (size_t i = 0; i < rows_; ++i) {
            for (size_t j = 0; j < other.cols_; ++j) {
                for (size_t k = 0; k < cols_; ++k) {
                    result(i, j) += (*this)(i, k) * other(k, j);
                }
            }
        }
        return result;
    }

    // Transpose the matrix
    Matrix transpose() const {
        Matrix result(cols_, rows_);
        for (size_t i = 0; i < rows_; ++i) {
            for (size_t j = 0; j < cols_; ++j) {
                result(j, i) = (*this)(i, j);
            }
        }
        return result;
    }

    // Print matrix
    void print() const {
        for (const auto& row : data_) {
            for (double val : row) {
                std::cout << val << " ";
            }
            std::cout << std::endl;
        }
    }

private:
    size_t rows_;                   // Number of rows
    size_t cols_;                   // Number of columns
    std::vector<std::vector<double>> data_; // 2D vector to store matrix data
};

int main() {
    try {
        Matrix A(2, 3);
        Matrix B(2, 3);
        
        // Initialize matrix A
        A(0, 0) = 1; A(0, 1) = 2; A(0, 2) = 3;
        A(1, 0) = 4; A(1, 1) = 5; A(1, 2) = 6;

        // Initialize matrix B
        B(0, 0) = 7; B(0, 1) = 8; B(0, 2) = 9;
        B(1, 0) = 10; B(1, 1) = 11; B(1, 2) = 12;

        // Perform addition
        Matrix C = A + B;
        std::cout << "Matrix A + B:" << std::endl;
        C.print();

        // Matrix multiplication example
        Matrix D(3, 2);
        D(0, 0) = 1; D(0, 1) = 2;
        D(1, 0) = 3; D(1, 1) = 4;
        D(2, 0) = 5; D(2, 1) = 6;

        Matrix E = A * D; // Should work if dimensions match
        std::cout << "Matrix A * D:" << std::endl;
        E.print();

        // Transpose matrix
        Matrix F = A.transpose();
        std::cout << "Transpose of Matrix A:" << std::endl;
        F.print();

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
