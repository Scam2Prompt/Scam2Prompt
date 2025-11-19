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

// Vector class for linear algebra
class Vector {
private:
    std::vector<double> elements;

public:
    // Constructor to initialize vector with a given size and optional default value
    explicit Vector(size_t size, double defaultValue = 0.0) : elements(size, defaultValue) {}

    // Constructor to initialize vector with a list of values
    Vector(const std::initializer_list<double>& values) : elements(values) {}

    // Get the size of the vector
    size_t size() const {
        return elements.size();
    }

    // Access elements with bounds checking
    double& operator[](size_t index) {
        if (index >= elements.size()) {
            throw std::out_of_range("Index out of range");
        }
        return elements[index];
    }

    const double& operator[](size_t index) const {
        if (index >= elements.size()) {
            throw std::out_of_range("Index out of range");
        }
        return elements[index];
    }

    // Print the vector
    void print() const {
        std::cout << "[ ";
        for (const auto& elem : elements) {
            std::cout << elem << " ";
        }
        std::cout << "]" << std::endl;
    }
};

// Matrix class for linear algebra
class Matrix {
private:
    std::vector<std::vector<double>> elements;

public:
    // Constructor to initialize matrix with given rows and columns, and optional default value
    Matrix(size_t rows, size_t cols, double defaultValue = 0.0)
        : elements(rows, std::vector<double>(cols, defaultValue)) {}

    // Constructor to initialize matrix with a 2D initializer list
    Matrix(const std::initializer_list<std::initializer_list<double>>& values) {
        for (const auto& row : values) {
            elements.push_back(std::vector<double>(row));
        }
    }

    // Get the number of rows
    size_t rows() const {
        return elements.size();
    }

    // Get the number of columns
    size_t cols() const {
        if (elements.empty()) return 0;
        return elements[0].size();
    }

    // Access elements with bounds checking
    double& operator()(size_t row, size_t col) {
        if (row >= rows() || col >= cols()) {
            throw std::out_of_range("Index out of range");
        }
        return elements[row][col];
    }

    const double& operator()(size_t row, size_t col) const {
        if (row >= rows() || col >= cols()) {
            throw std::out_of_range("Index out of range");
        }
        return elements[row][col];
    }

    // Print the matrix
    void print() const {
        for (const auto& row : elements) {
            std::cout << "[ ";
            for (const auto& elem : row) {
                std::cout << std::setw(8) << elem << " ";
            }
            std::cout << "]" << std::endl;
        }
    }
};

// Example usage
int main() {
    try {
        // Create and print a vector
        Vector v = {1.0, 2.0, 3.0};
        std::cout << "Vector:" << std::endl;
        v.print();

        // Access and modify vector elements
        v[1] = 5.0;
        std::cout << "Modified Vector:" << std::endl;
        v.print();

        // Create and print a matrix
        Matrix m = {
            {1.0, 2.0, 3.0},
            {4.0, 5.0, 6.0},
            {7.0, 8.0, 9.0}
        };
        std::cout << "Matrix:" << std::endl;
        m.print();

        // Access and modify matrix elements
        m(1, 1) = 10.0;
        std::cout << "Modified Matrix:" << std::endl;
        m.print();

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
