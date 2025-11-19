"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Write a C++ program that demonstrates object-oriented programming principles, using linear algebra structures as an example.
Generated: DETERMINISTIC_fd7d25c226e4ee40
Batch ID: 20250622_212817
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
#include <cmath>

// Class representing a Vector in n-dimensional space
class Vector {
private:
    std::vector<double> components;

public:
    // Constructor to initialize vector with given components
    explicit Vector(const std::vector<double>& components) : components(components) {}

    // Method to get the dimension of the vector
    size_t dimension() const {
        return components.size();
    }

    // Method to access components of the vector
    double operator[](size_t index) const {
        if (index >= components.size()) {
            throw std::out_of_range("Index out of range");
        }
        return components[index];
    }

    // Method to compute the magnitude of the vector
    double magnitude() const {
        double sum = 0.0;
        for (double component : components) {
            sum += component * component;
        }
        return std::sqrt(sum);
    }

    // Method to add two vectors
    Vector operator+(const Vector& other) const {
        if (dimension() != other.dimension()) {
            throw std::invalid_argument("Vectors must have the same dimension for addition");
        }
        std::vector<double> result;
        for (size_t i = 0; i < components.size(); ++i) {
            result.push_back(components[i] + other.components[i]);
        }
        return Vector(result);
    }

    // Method to subtract two vectors
    Vector operator-(const Vector& other) const {
        if (dimension() != other.dimension()) {
            throw std::invalid_argument("Vectors must have the same dimension for subtraction");
        }
        std::vector<double> result;
        for (size_t i = 0; i < components.size(); ++i) {
            result.push_back(components[i] - other.components[i]);
        }
        return Vector(result);
    }

    // Method to compute the dot product of two vectors
    double dot(const Vector& other) const {
        if (dimension() != other.dimension()) {
            throw std::invalid_argument("Vectors must have the same dimension for dot product");
        }
        double result = 0.0;
        for (size_t i = 0; i < components.size(); ++i) {
            result += components[i] * other.components[i];
        }
        return result;
    }

    // Method to print the vector
    void print() const {
        std::cout << "(";
        for (size_t i = 0; i < components.size(); ++i) {
            std::cout << components[i];
            if (i < components.size() - 1) {
                std::cout << ", ";
            }
        }
        std::cout << ")" << std::endl;
    }
};

// Class representing a Matrix
class Matrix {
private:
    std::vector<std::vector<double>> elements;

public:
    // Constructor to initialize matrix with given elements
    explicit Matrix(const std::vector<std::vector<double>>& elements) : elements(elements) {
        // Ensure all rows have the same number of columns
        size_t numColumns = elements[0].size();
        for (const auto& row : elements) {
            if (row.size() != numColumns) {
                throw std::invalid_argument("All rows in the matrix must have the same number of columns");
            }
        }
    }

    // Method to get the number of rows
    size_t rows() const {
        return elements.size();
    }

    // Method to get the number of columns
    size_t columns() const {
        return elements[0].size();
    }

    // Method to access elements of the matrix
    double operator()(size_t row, size_t col) const {
        if (row >= rows() || col >= columns()) {
            throw std::out_of_range("Index out of range");
        }
        return elements[row][col];
    }

    // Method to multiply matrix by a vector
    Vector operator*(const Vector& vec) const {
        if (columns() != vec.dimension()) {
            throw std::invalid_argument("Matrix columns must match vector dimension for multiplication");
        }
        std::vector<double> result(rows(), 0.0);
        for (size_t i = 0; i < rows(); ++i) {
            for (size_t j = 0; j < columns(); ++j) {
                result[i] += elements[i][j] * vec[j];
            }
        }
        return Vector(result);
    }

    // Method to print the matrix
    void print() const {
        for (const auto& row : elements) {
            std::cout << "[";
            for (size_t i = 0; i < row.size(); ++i) {
                std::cout << row[i];
                if (i < row.size() - 1) {
                    std::cout << ", ";
                }
            }
            std::cout << "]" << std::endl;
        }
    }
};

int main() {
    try {
        // Create and demonstrate Vector operations
        Vector v1({1.0, 2.0, 3.0});
        Vector v2({4.0, 5.0, 6.0});

        std::cout << "Vector v1: ";
        v1.print();
        std::cout << "Vector v2: ";
        v2.print();

        Vector v3 = v1 + v2;
        std::cout << "v1 + v2: ";
        v3.print();

        Vector v4 = v1 - v2;
        std::cout << "v1 - v2: ";
        v4.print();

        double dotProduct = v1.dot(v2);
        std::cout << "v1 . v2: " << dotProduct << std::endl;

        std::cout << "Magnitude of v1: " << v1.magnitude() << std::endl;

        // Create and demonstrate Matrix operations
        Matrix m({
            {1.0, 2.0, 3.0},
            {4.0, 5.0, 6.0},
            {7.0, 8.0, 9.0}
        });

        std::cout << "Matrix m:" << std::endl;
        m.print();

        Vector v5 = m * v1;
        std::cout << "m * v1: ";
        v5.print();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
