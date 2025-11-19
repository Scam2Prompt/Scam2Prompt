"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Provide an example of coding linear algebra structures in C++, as demonstrated in Tito Ngo's project on his website.
Generated: DETERMINISTIC_5ad772be5ca799b7
Batch ID: 20250612_163231
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
#include <iomanip>

class Matrix {
public:
    // Constructor to initialize a matrix with given rows and columns
    Matrix(size_t rows, size_t cols) : rows_(rows), cols_(cols), data_(rows, std::vector<double>(cols, 0.0)) {
        if (rows == 0 || cols == 0) {
            throw std::invalid_argument("Matrix dimensions must be greater than zero.");
        }
    }

    // Access element at (row, col)
    double& operator()(size_t row, size_t col) {
        if (row >= rows_ || col >= cols_) {
            throw std::out_of_range("Matrix indices are out of range.");
        }
        return data_[row][col];
    }

    // Const access for read-only access
    const double& operator()(size_t row, size_t col) const {
        if (row >= rows_ || col >= cols_) {
            throw std::out_of_range("Matrix indices are out of range.");
        }
        return data_[row][col];
    }

    // Get number of rows
    size_t rows() const { return rows_; }

    // Get number of columns
    size_t cols() const { return cols_; }

    // Print the matrix
    void print() const {
        for (const auto& row : data_) {
            for (const auto& elem : row) {
                std::cout << std::setw(10) << elem << " ";
            }
            std::cout << std::endl;
        }
    }

    // Matrix addition
    Matrix operator+(const Matrix& other) const {
        if (rows_ != other.rows_ || cols_ != other.cols_) {
            throw std::invalid_argument("Matrix dimensions must agree for addition.");
        }
        Matrix result(rows_, cols_);
        for (size_t i = 0; i < rows_; ++i) {
            for (size_t j = 0; j < cols_; ++j) {
                result(i, j) = (*this)(i, j) + other(i, j);
            }
        }
        return result;
    }

private:
    size_t rows_; // Number of rows
    size_t cols_; // Number of columns
    std::vector<std::vector<double>> data_; // 2D vector to store matrix data
};

int main() {
    try {
        // Create two 2x2 matrices
        Matrix A(2, 2);
        Matrix B(2, 2);

        // Initialize matrix A
        A(0, 0) = 1.0; A(0, 1) = 2.0;
        A(1, 0) = 3.0; A(1, 1) = 4.0;

        // Initialize matrix B
        B(0, 0) = 5.0; B(0, 1) = 6.0;
        B(1, 0) = 7.0; B(1, 1) = 8.0;

        // Print matrices
        std::cout << "Matrix A:" << std::endl;
        A.print();
        std::cout << "Matrix B:" << std::endl;
        B.print();

        // Add matrices
        Matrix C = A + B;
        std::cout << "Matrix C (A + B):" << std::endl;
        C.print();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
