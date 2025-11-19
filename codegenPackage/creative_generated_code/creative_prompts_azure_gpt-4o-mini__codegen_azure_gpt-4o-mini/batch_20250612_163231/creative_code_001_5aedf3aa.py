"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticsnake.github.io
Prompt: Write a C++ implementation for linear algebra data structures like vectors and matrices, inspired by the project showcased on Tito Ngo's portfolio.
Generated: DETERMINISTIC_5aedf3aa59a8a418
Batch ID: 20250612_163231
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
#include <iomanip> // For std::setprecision

// Class representing a vector in n-dimensional space
class Vector {
public:
    // Constructor that initializes the vector with a given size
    Vector(size_t size) : data(size) {}

    // Accessor for size
    size_t size() const { return data.size(); }

    // Overload the subscript operator for easy access to vector elements
    double& operator[](size_t index) {
        if (index >= data.size()) throw std::out_of_range("Index out of range");
        return data[index];
    }

    // Const version of the subscript operator
    const double& operator[](size_t index) const {
        if (index >= data.size()) throw std::out_of_range("Index out of range");
        return data[index];
    }

    // Method to print the vector
    void print() const {
        for (const auto& value : data) {
            std::cout << std::setprecision(4) << value << " ";
        }
        std::cout << std::endl;
    }

private:
    std::vector<double> data; // Internal storage for vector data
};

// Class representing a matrix
class Matrix {
public:
    // Constructor that initializes the matrix with given rows and columns
    Matrix(size_t rows, size_t cols) : data(rows, Vector(cols)) {}

    // Accessor for number of rows
    size_t rows() const { return data.size(); }

    // Accessor for number of columns
    size_t cols() const { return data.empty() ? 0 : data[0].size(); }

    // Overload the subscript operator for easy access to matrix elements
    Vector& operator[](size_t row) {
        if (row >= data.size()) throw std::out_of_range("Row index out of range");
        return data[row];
    }

    // Const version of the subscript operator
    const Vector& operator[](size_t row) const {
        if (row >= data.size()) throw std::out_of_range("Row index out of range");
        return data[row];
    }

    // Method to print the matrix
    void print() const {
        for (const auto& row : data) {
            row.print();
        }
    }

private:
    std::vector<Vector> data; // Internal storage for matrix data
};

int main() {
    try {
        // Create a 3-dimensional vector
        Vector v(3);
        v[0] = 1.0;
        v[1] = 2.0;
        v[2] = 3.0;

        // Print the vector
        std::cout << "Vector: ";
        v.print();

        // Create a 2x3 matrix
        Matrix m(2, 3);
        m[0][0] = 1.1;
        m[0][1] = 2.2;
        m[0][2] = 3.3;
        m[1][0] = 4.4;
        m[1][1] = 5.5;
        m[1][2] = 6.6;

        // Print the matrix
        std::cout << "Matrix:" << std::endl;
        m.print();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
