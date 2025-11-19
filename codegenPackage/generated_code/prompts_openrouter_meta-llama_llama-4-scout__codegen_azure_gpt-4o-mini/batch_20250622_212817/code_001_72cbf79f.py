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

class Vector {
public:
    // Constructor to initialize a vector of given size
    Vector(size_t size) : data(size) {}

    // Accessor for vector size
    size_t size() const { return data.size(); }

    // Overload the subscript operator for element access
    double& operator[](size_t index) {
        if (index >= data.size()) {
            throw std::out_of_range("Index out of range");
        }
        return data[index];
    }

    // Const version of the subscript operator
    const double& operator[](size_t index) const {
        if (index >= data.size()) {
            throw std::out_of_range("Index out of range");
        }
        return data[index];
    }

    // Method to display the vector
    void display() const {
        for (const auto& value : data) {
            std::cout << std::fixed << std::setprecision(2) << value << " ";
        }
        std::cout << std::endl;
    }

private:
    std::vector<double> data; // Internal storage for vector elements
};

class Matrix {
public:
    // Constructor to initialize a matrix with given rows and columns
    Matrix(size_t rows, size_t cols) : data(rows, Vector(cols)) {}

    // Accessor for matrix dimensions
    size_t rows() const { return data.size(); }
    size_t cols() const { return data.empty() ? 0 : data[0].size(); }

    // Overload the subscript operator for element access
    Vector& operator[](size_t index) {
        if (index >= data.size()) {
            throw std::out_of_range("Row index out of range");
        }
        return data[index];
    }

    // Const version of the subscript operator
    const Vector& operator[](size_t index) const {
        if (index >= data.size()) {
            throw std::out_of_range("Row index out of range");
        }
        return data[index];
    }

    // Method to display the matrix
    void display() const {
        for (const auto& row : data) {
            row.display();
        }
    }

private:
    std::vector<Vector> data; // Internal storage for matrix rows
};

int main() {
    try {
        // Create a 3x3 matrix
        Matrix mat(3, 3);
        
        // Initialize the matrix with some values
        for (size_t i = 0; i < mat.rows(); ++i) {
            for (size_t j = 0; j < mat.cols(); ++j) {
                mat[i][j] = static_cast<double>(i * mat.cols() + j + 1);
            }
        }

        // Display the matrix
        std::cout << "Matrix:" << std::endl;
        mat.display();

        // Create a vector of size 3
        Vector vec(3);
        
        // Initialize the vector with some values
        for (size_t i = 0; i < vec.size(); ++i) {
            vec[i] = static_cast<double>(i + 1);
        }

        // Display the vector
        std::cout << "Vector:" << std::endl;
        vec.display();

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
