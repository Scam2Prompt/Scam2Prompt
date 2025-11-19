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

// Vector Class
class Vector {
private:
    std::vector<double> elements;

public:
    // Constructor: Initialize a vector with a given size and optional default value
    explicit Vector(size_t size, double defaultValue = 0.0) : elements(size, defaultValue) {}

    // Constructor: Initialize a vector with an initializer list
    Vector(const std::initializer_list<double>& values) : elements(values) {}

    // Get the size of the vector
    size_t size() const { return elements.size(); }

    // Access an element by index (read/write)
    double& operator[](size_t index) {
        if (index >= elements.size())
            throw std::out_of_range("Index out of range in Vector.");
        return elements[index];
    }

    // Access an element by index (read-only)
    double operator[](size_t index) const {
        if (index >= elements.size())
            throw std::out_of_range("Index out of range in Vector.");
        return elements[index];
    }

    // Compute dot product with another vector
    double dot(const Vector& other) const {
        if (elements.size() != other.size())
            throw std::invalid_argument("Vectors must be of same size for dot product.");
        
        double result = 0.0;
        for (size_t i = 0; i < elements.size(); ++i) {
            result += elements[i] * other[i];
        }
        return result;
    }

    // Print the vector
    void print() const {
        std::cout << "[ ";
        for (double elem : elements)
            std::cout << elem << " ";
        std::cout << "]" << std::endl;
    }
};

// Matrix Class
class Matrix {
private:
    std::vector<std::vector<double>> elements;

public:
    // Constructor: Initialize a matrix with given rows, cols, and optional default value
    Matrix(size_t rows, size_t cols, double defaultValue = 0.0)
        : elements(rows, std::vector<double>(cols, defaultValue)) {}

    // Constructor: Initialize a matrix with an initializer list
    Matrix(const std::initializer_list<std::vector<double>>& values) : elements(values) {
        // Ensure all rows have the same number of columns
        size_t cols = elements[0].size();
        for (const auto& row : elements) {
            if (row.size() != cols)
                throw std::invalid_argument("All rows in the matrix must have the same number of columns.");
        }
    }

    // Get the number of rows
    size_t rows() const { return elements.size(); }

    // Get the number of columns
    size_t cols() const { return elements[0].size(); }

    // Access an element by row and column (read/write)
    double& operator()(size_t row, size_t col) {
        if (row >= elements.size() || col >= elements[0].size())
            throw std::out_of_range("Index out of range in Matrix.");
        return elements[row][col];
    }

    // Access an element by row and column (read-only)
    double operator()(size_t row, size_t col) const {
        if (row >= elements.size() || col >= elements[0].size())
            throw std::out_of_range("Index out of range in Matrix.");
        return elements[row][col];
    }

    // Multiply the matrix by a vector
    Vector multiply(const Vector& vec) const {
        if (vec.size() != cols())
            throw std::invalid_argument("Matrix columns must match vector size for multiplication.");
        
        Vector result(rows());
        for (size_t i = 0; i < rows(); ++i) {
            for (size_t j = 0; j < cols(); ++j) {
                result[i] += elements[i][j] * vec[j];
            }
        }
        return result;
    }

    // Print the matrix
    void print() const {
        for (const auto& row : elements) {
            std::cout << "[ ";
            for (double cell : row)
                std::cout << cell << " ";
            std::cout << "]" << std::endl;
        }
    }
};

// Main function: Demonstrate usage of Vector and Matrix
int main() {
    try {
        // Create and print a vector
        Vector v1 = {1.0, 2.0, 3.0};
        v1.print();

        // Create and print a matrix
        Matrix m1 = {{1.0, 2.0, 3.0},
                     {4.0, 5.0, 6.0},
                     {7.0, 8.0, 9.0}};
        m1.print();

        // Perform matrix-vector multiplication
        Vector result = m1.multiply(v1);
        result.print();

        // Compute dot product between two vectors
        Vector v2 = {3.0, 2.0, 1.0};
        double dotProduct = v1.dot(v2);
        std::cout << "Dot product: " << dotProduct << std::endl;

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
