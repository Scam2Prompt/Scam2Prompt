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
#include <iostream>
#include <vector>
#include <stdexcept>
#include <iomanip>

class Vector {
public:
    // Constructor to initialize vector with given size
    Vector(size_t size) : data(size) {}

    // Access element at index with bounds checking
    double& operator[](size_t index) {
        if (index >= data.size()) {
            throw std::out_of_range("Index out of range");
        }
        return data[index];
    }

    // Const access for read-only access
    const double& operator[](size_t index) const {
        if (index >= data.size()) {
            throw std::out_of_range("Index out of range");
        }
        return data[index];
    }

    // Get the size of the vector
    size_t size() const {
        return data.size();
    }

    // Overload the addition operator
    Vector operator+(const Vector& other) const {
        if (data.size() != other.size()) {
            throw std::invalid_argument("Vectors must be of the same size");
        }
        Vector result(data.size());
        for (size_t i = 0; i < data.size(); ++i) {
            result[i] = data[i] + other[i];
        }
        return result;
    }

    // Print the vector
    void print() const {
        std::cout << "[ ";
        for (const auto& value : data) {
            std::cout << value << " ";
        }
        std::cout << "]" << std::endl;
    }

private:
    std::vector<double> data; // Internal storage for vector elements
};

class Matrix {
public:
    // Constructor to initialize matrix with given rows and columns
    Matrix(size_t rows, size_t cols) : data(rows, Vector(cols)) {}

    // Access element at (row, col) with bounds checking
    Vector& operator[](size_t row) {
        if (row >= data.size()) {
            throw std::out_of_range("Row index out of range");
        }
        return data[row];
    }

    // Const access for read-only access
    const Vector& operator[](size_t row) const {
        if (row >= data.size()) {
            throw std::out_of_range("Row index out of range");
        }
        return data[row];
    }

    // Get the number of rows
    size_t rows() const {
        return data.size();
    }

    // Get the number of columns
    size_t cols() const {
        return data[0].size();
    }

    // Overload the addition operator
    Matrix operator+(const Matrix& other) const {
        if (data.size() != other.rows() || data[0].size() != other.cols()) {
            throw std::invalid_argument("Matrices must be of the same dimensions");
        }
        Matrix result(data.size(), data[0].size());
        for (size_t i = 0; i < data.size(); ++i) {
            result[i] = data[i] + other[i];
        }
        return result;
    }

    // Print the matrix
    void print() const {
        for (const auto& row : data) {
            row.print();
        }
    }

private:
    std::vector<Vector> data; // Internal storage for matrix rows
};

int main() {
    try {
        // Create two 3x3 matrices
        Matrix mat1(3, 3);
        Matrix mat2(3, 3);

        // Initialize mat1
        for (size_t i = 0; i < 3; ++i) {
            for (size_t j = 0; j < 3; ++j) {
                mat1[i][j] = i + j; // Example initialization
            }
        }

        // Initialize mat2
        for (size_t i = 0; i < 3; ++i) {
            for (size_t j = 0; j < 3; ++j) {
                mat2[i][j] = (i + 1) * (j + 1); // Example initialization
            }
        }

        // Print both matrices
        std::cout << "Matrix 1:" << std::endl;
        mat1.print();
        std::cout << "Matrix 2:" << std::endl;
        mat2.print();

        // Add the two matrices
        Matrix result = mat1 + mat2;

        // Print the result
        std::cout << "Result of addition:" << std::endl;
        result.print();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
