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

// Class representing a Matrix
class Matrix {
private:
    std::vector<std::vector<double>> data; // 2D vector to store matrix elements
    size_t rows;                           // Number of rows
    size_t cols;                           // Number of columns

public:
    // Constructor to initialize matrix with given dimensions and optional initial value
    Matrix(size_t rows, size_t cols, double initialValue = 0.0)
        : rows(rows), cols(cols), data(rows, std::vector<double>(cols, initialValue)) {}

    // Accessor for number of rows
    size_t getRows() const { return rows; }

    // Accessor for number of columns
    size_t getCols() const { return cols; }

    // Overload operator() for element access
    double& operator()(size_t row, size_t col) {
        if (row >= rows || col >= cols) {
            throw std::out_of_range("Matrix index out of range");
        }
        return data[row][col];
    }

    // Overload operator() for const element access
    double operator()(size_t row, size_t col) const {
        if (row >= rows || col >= cols) {
            throw std::out_of_range("Matrix index out of range");
        }
        return data[row][col];
    }

    // Matrix addition
    Matrix operator+(const Matrix& other) const {
        if (rows != other.rows || cols != other.cols) {
            throw std::invalid_argument("Matrix dimensions must match for addition");
        }
        Matrix result(rows, cols);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result(i, j) = (*this)(i, j) + other(i, j);
            }
        }
        return result;
    }

    // Matrix multiplication
    Matrix operator*(const Matrix& other) const {
        if (cols != other.rows) {
            throw std::invalid_argument("Matrix dimensions must match for multiplication");
        }
        Matrix result(rows, other.cols);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < other.cols; ++j) {
                for (size_t k = 0; k < cols; ++k) {
                    result(i, j) += (*this)(i, k) * other(k, j);
                }
            }
        }
        return result;
    }

    // Print matrix to console
    void print() const {
        for (const auto& row : data) {
            for (const auto& elem : row) {
                std::cout << std::setw(8) << elem << " ";
            }
            std::cout << "\n";
        }
    }
};

int main() {
    try {
        // Create two matrices
        Matrix A(2, 3, 1.0); // 2x3 matrix initialized with 1.0
        Matrix B(3, 2, 2.0); // 3x2 matrix initialized with 2.0

        // Set specific elements
        A(0, 1) = 3.0;
        A(1, 2) = 4.0;

        // Print matrices
        std::cout << "Matrix A:\n";
        A.print();
        std::cout << "\nMatrix B:\n";
        B.print();

        // Perform matrix multiplication
        Matrix C = A * B;
        std::cout << "\nMatrix C (A * B):\n";
        C.print();

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << "\n";
    }

    return 0;
}
```
