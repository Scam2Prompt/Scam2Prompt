"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Create C++ classes for linear algebra data structures, such as vectors and matrices, based on the project showcased on Tito Ngo's website.
Generated: DETERMINISTIC_27d22d901c7c0471
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
#include <iomanip>
#include <cmath>

class Vector {
public:
    // Constructor to initialize a vector of given size
    Vector(size_t size) : data(size) {
        if (size == 0) {
            throw std::invalid_argument("Vector size must be greater than zero.");
        }
    }

    // Accessor for vector elements
    double& operator[](size_t index) {
        if (index >= data.size()) {
            throw std::out_of_range("Index out of range.");
        }
        return data[index];
    }

    // Const accessor for vector elements
    const double& operator[](size_t index) const {
        if (index >= data.size()) {
            throw std::out_of_range("Index out of range.");
        }
        return data[index];
    }

    // Get the size of the vector
    size_t size() const {
        return data.size();
    }

    // Method to compute the dot product with another vector
    double dot(const Vector& other) const {
        if (data.size() != other.size()) {
            throw std::invalid_argument("Vectors must be of the same size for dot product.");
        }
        double result = 0.0;
        for (size_t i = 0; i < data.size(); ++i) {
            result += data[i] * other[i];
        }
        return result;
    }

    // Method to print the vector
    void print() const {
        std::cout << "[ ";
        for (const auto& value : data) {
            std::cout << std::fixed << std::setprecision(2) << value << " ";
        }
        std::cout << "]" << std::endl;
    }

private:
    std::vector<double> data; // Internal storage for vector elements
};

class Matrix {
public:
    // Constructor to initialize a matrix with given rows and columns
    Matrix(size_t rows, size_t cols) : data(rows, Vector(cols)) {
        if (rows == 0 || cols == 0) {
            throw std::invalid_argument("Matrix dimensions must be greater than zero.");
        }
    }

    // Accessor for matrix elements
    Vector& operator[](size_t index) {
        if (index >= data.size()) {
            throw std::out_of_range("Row index out of range.");
        }
        return data[index];
    }

    // Const accessor for matrix elements
    const Vector& operator[](size_t index) const {
        if (index >= data.size()) {
            throw std::out_of_range("Row index out of range.");
        }
        return data[index];
    }

    // Get the number of rows in the matrix
    size_t rows() const {
        return data.size();
    }

    // Get the number of columns in the matrix
    size_t cols() const {
        return data.empty() ? 0 : data[0].size();
    }

    // Method to multiply the matrix by a vector
    Vector multiply(const Vector& vec) const {
        if (cols() != vec.size()) {
            throw std::invalid_argument("Matrix columns must match vector size for multiplication.");
        }
        Vector result(rows());
        for (size_t i = 0; i < rows(); ++i) {
            result[i] = data[i].dot(vec);
        }
        return result;
    }

    // Method to print the matrix
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
        // Example usage of Vector
        Vector v(3);
        v[0] = 1.0;
        v[1] = 2.0;
        v[2] = 3.0;
        v.print();

        // Example usage of Matrix
        Matrix m(2, 3);
        m[0][0] = 1.0; m[0][1] = 2.0; m[0][2] = 3.0;
        m[1][0] = 4.0; m[1][1] = 5.0; m[1][2] = 6.0;
        m.print();

        // Multiply matrix by vector
        Vector result = m.multiply(v);
        result.print();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
