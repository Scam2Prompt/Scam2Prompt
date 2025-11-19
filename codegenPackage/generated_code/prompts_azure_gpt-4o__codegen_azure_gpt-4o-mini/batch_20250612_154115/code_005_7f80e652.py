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
#include <iostream>
#include <vector>
#include <stdexcept>

class Matrix {
public:
    // Constructor to initialize a matrix with given rows and columns
    Matrix(size_t rows, size_t cols) : rows_(rows), cols_(cols), data_(rows, std::vector<double>(cols, 0.0)) {}

    // Function to set the value at a specific position
    void set(size_t row, size_t col, double value) {
        if (row >= rows_ || col >= cols_) {
            throw std::out_of_range("Index out of range");
        }
        data_[row][col] = value;
    }

    // Function to get the value at a specific position
    double get(size_t row, size_t col) const {
        if (row >= rows_ || col >= cols_) {
            throw std::out_of_range("Index out of range");
        }
        return data_[row][col];
    }

    // Function to add two matrices
    Matrix operator+(const Matrix& other) const {
        if (rows_ != other.rows_ || cols_ != other.cols_) {
            throw std::invalid_argument("Matrices must have the same dimensions for addition");
        }
        Matrix result(rows_, cols_);
        for (size_t i = 0; i < rows_; ++i) {
            for (size_t j = 0; j < cols_; ++j) {
                result.set(i, j, this->get(i, j) + other.get(i, j));
            }
        }
        return result;
    }

    // Function to multiply two matrices
    Matrix operator*(const Matrix& other) const {
        if (cols_ != other.rows_) {
            throw std::invalid_argument("Invalid dimensions for matrix multiplication");
        }
        Matrix result(rows_, other.cols_);
        for (size_t i = 0; i < rows_; ++i) {
            for (size_t j = 0; j < other.cols_; ++j) {
                double sum = 0.0;
                for (size_t k = 0; k < cols_; ++k) {
                    sum += this->get(i, k) * other.get(k, j);
                }
                result.set(i, j, sum);
            }
        }
        return result;
    }

    // Function to transpose the matrix
    Matrix transpose() const {
        Matrix result(cols_, rows_);
        for (size_t i = 0; i < rows_; ++i) {
            for (size_t j = 0; j < cols_; ++j) {
                result.set(j, i, this->get(i, j));
            }
        }
        return result;
    }

    // Function to print the matrix
    void print() const {
        for (const auto& row : data_) {
            for (const auto& value : row) {
                std::cout << value << " ";
            }
            std::cout << std::endl;
        }
    }

private:
    size_t rows_; // Number of rows in the matrix
    size_t cols_; // Number of columns in the matrix
    std::vector<std::vector<double>> data_; // 2D vector to store matrix data
};

int main() {
    try {
        Matrix mat1(2, 3);
        mat1.set(0, 0, 1.0);
        mat1.set(0, 1, 2.0);
        mat1.set(0, 2, 3.0);
        mat1.set(1, 0, 4.0);
        mat1.set(1, 1, 5.0);
        mat1.set(1, 2, 6.0);

        Matrix mat2(2, 3);
        mat2.set(0, 0, 7.0);
        mat2.set(0, 1, 8.0);
        mat2.set(0, 2, 9.0);
        mat2.set(1, 0, 10.0);
        mat2.set(1, 1, 11.0);
        mat2.set(1, 2, 12.0);

        // Matrix addition
        Matrix sum = mat1 + mat2;
        std::cout << "Sum of matrices:\n";
        sum.print();

        // Matrix multiplication
        Matrix mat3(3, 2);
        mat3.set(0, 0, 1.0);
        mat3.set(0, 1, 2.0);
        mat3.set(1, 0, 3.0);
        mat3.set(1, 1, 4.0);
        mat3.set(2, 0, 5.0);
        mat3.set(2, 1, 6.0);

        Matrix product = mat1 * mat3;
        std::cout << "Product of matrices:\n";
        product.print();

        // Matrix transposition
        Matrix transposed = mat1.transpose();
        std::cout << "Transposed matrix:\n";
        transposed.print();

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
