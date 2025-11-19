"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Implement linear algebra data structures (vectors, matrices) in C++ classes, inspired by Tito Ngo's C++ project.
Generated: DETERMINISTIC_72cbf79f8ba22e45
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
#include <iomanip>

// Vector class
class Vector {
private:
    std::vector<double> elements;

public:
    // Constructor to initialize vector with a given size and optional default value
    explicit Vector(size_t size, double defaultValue = 0.0) : elements(size, defaultValue) {}

    // Constructor to initialize vector with a list of values
    explicit Vector(const std::vector<double>& values) : elements(values) {}

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

    // Overload addition operator for vector addition
    Vector operator+(const Vector& other) const {
        if (size() != other.size()) {
            throw std::invalid_argument("Vectors must be of the same size for addition");
        }
        Vector result(size());
        for (size_t i = 0; i < size(); ++i) {
            result[i] = elements[i] + other[i];
        }
        return result;
    }

    // Overload scalar multiplication
    Vector operator*(double scalar) const {
        Vector result(size());
        for (size_t i = 0; i < size(); ++i) {
            result[i] = elements[i] * scalar;
        }
        return result;
    }

    // Print the vector
    void print() const {
        std::cout << "[ ";
        for (const auto& elem : elements) {
            std::cout << std::fixed << std::setprecision(2) << elem << " ";
        }
        std::cout << "]" << std::endl;
    }
};

// Matrix class
class Matrix {
private:
    std::vector<std::vector<double>> elements;

public:
    // Constructor to initialize matrix with given rows and columns, and optional default value
    Matrix(size_t rows, size_t cols, double defaultValue = 0.0)
        : elements(rows, std::vector<double>(cols, defaultValue)) {}

    // Constructor to initialize matrix with a 2D vector
    explicit Matrix(const std::vector<std::vector<double>>& values) : elements(values) {
        // Ensure all rows have the same number of columns
        size_t cols = values[0].size();
        for (const auto& row : values) {
            if (row.size() != cols) {
                throw std::invalid_argument("All rows must have the same number of columns");
            }
        }
    }

    // Get the number of rows
    size_t rows() const {
        return elements.size();
    }

    // Get the number of columns
    size_t cols() const {
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

    // Overload matrix addition
    Matrix operator+(const Matrix& other) const {
        if (rows() != other.rows() || cols() != other.cols()) {
            throw std::invalid_argument("Matrices must have the same dimensions for addition");
        }
        Matrix result(rows(), cols());
        for (size_t i = 0; i < rows(); ++i) {
            for (size_t j = 0; j < cols(); ++j) {
                result(i, j) = elements[i][j] + other(i, j);
            }
        }
        return result;
    }

    // Overload scalar multiplication
    Matrix operator*(double scalar) const {
        Matrix result(rows(), cols());
        for (size_t i = 0; i < rows(); ++i) {
            for (size_t j = 0; j < cols(); ++j) {
                result(i, j) = elements[i][j] * scalar;
            }
        }
        return result;
    }

    // Print the matrix
    void print() const {
        for (const auto& row : elements) {
            std::cout << "[ ";
            for (const auto& elem : row) {
                std::cout << std::fixed << std::setprecision(2) << elem << " ";
            }
            std::cout << "]" << std::endl;
        }
    }
};

// Example usage
int main() {
    try {
        // Vector example
        Vector v1({1.0, 2.0, 3.0});
        Vector v2({4.0, 5.0, 6.0});
        Vector v3 = v1 + v2;
        v3.print();

        Vector v4 = v1 * 2.0;
        v4.print();

        // Matrix example
        Matrix m1({{1.0, 2.0}, {3.0, 4.0}});
        Matrix m2({{5.0, 6.0}, {7.0, 8.0}});
        Matrix m3 = m1 + m2;
        m3.print();

        Matrix m4 = m1 * 2.0;
        m4.print();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
