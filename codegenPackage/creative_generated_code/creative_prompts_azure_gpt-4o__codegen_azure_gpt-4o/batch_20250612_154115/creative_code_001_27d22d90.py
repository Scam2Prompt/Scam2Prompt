"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticsnake.github.io
Prompt: Create C++ classes for linear algebra data structures, such as vectors and matrices, based on the project showcased on Tito Ngo's website.
Generated: DETERMINISTIC_27d22d901c7c0471
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
#include <iomanip>

class Vector {
private:
    std::vector<double> elements;

public:
    // Constructor: Initialize with size and optional default value
    explicit Vector(size_t size, double defaultValue = 0.0) : elements(size, defaultValue) {}

    // Constructor: Initialize with a list of values
    explicit Vector(const std::vector<double>& values) : elements(values) {}

    // Access element (read/write)
    double& operator[](size_t index) {
        if (index >= elements.size()) {
            throw std::out_of_range("Vector index out of range");
        }
        return elements[index];
    }

    // Access element (read-only)
    const double& operator[](size_t index) const {
        if (index >= elements.size()) {
            throw std::out_of_range("Vector index out of range");
        }
        return elements[index];
    }

    // Get size of the vector
    size_t size() const {
        return elements.size();
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

class Matrix {
private:
    std::vector<std::vector<double>> elements;

public:
    // Constructor: Initialize with rows, columns, and optional default value
    Matrix(size_t rows, size_t cols, double defaultValue = 0.0)
        : elements(rows, std::vector<double>(cols, defaultValue)) {}

    // Constructor: Initialize with a 2D vector
    explicit Matrix(const std::vector<std::vector<double>>& values) : elements(values) {
        // Ensure all rows have the same number of columns
        size_t cols = values[0].size();
        for (const auto& row : values) {
            if (row.size() != cols) {
                throw std::invalid_argument("All rows in the matrix must have the same number of columns");
            }
        }
    }

    // Access element (read/write)
    double& operator()(size_t row, size_t col) {
        if (row >= elements.size() || col >= elements[0].size()) {
            throw std::out_of_range("Matrix index out of range");
        }
        return elements[row][col];
    }

    // Access element (read-only)
    const double& operator()(size_t row, size_t col) const {
        if (row >= elements.size() || col >= elements[0].size()) {
            throw std::out_of_range("Matrix index out of range");
        }
        return elements[row][col];
    }

    // Get number of rows
    size_t rows() const {
        return elements.size();
    }

    // Get number of columns
    size_t cols() const {
        return elements[0].size();
    }

    // Print the matrix
    void print() const {
        for (const auto& row : elements) {
            for (const auto& elem : row) {
                std::cout << std::setw(10) << elem << " ";
            }
            std::cout << std::endl;
        }
    }
};

// Example usage
int main() {
    try {
        // Create a vector
        Vector v({1.0, 2.0, 3.0});
        std::cout << "Vector:";
        v.print();

        // Modify vector elements
        v[1] = 4.5;
        std::cout << "Modified Vector:";
        v.print();

        // Create a matrix
        Matrix m(2, 3, 1.0); // 2 rows, 3 columns, default value 1.0
        m(0, 2) = 5.0; // Modify an element
        std::cout << "Matrix:" << std::endl;
        m.print();

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
