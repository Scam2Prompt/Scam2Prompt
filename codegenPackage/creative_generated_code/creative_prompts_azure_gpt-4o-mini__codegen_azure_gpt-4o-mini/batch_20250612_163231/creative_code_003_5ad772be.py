"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticsnake.github.io
Prompt: Provide an example of coding linear algebra structures in C++, as demonstrated in Tito Ngo's project on his website.
Generated: DETERMINISTIC_5ad772be5ca799b7
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
#include <cmath>

// Class representing a vector in linear algebra
class Vector {
public:
    // Constructor to initialize the vector with given size
    Vector(size_t size) : data(size, 0.0) {
        if (size == 0) {
            throw std::invalid_argument("Vector size must be greater than zero.");
        }
    }

    // Access element at a specific index
    double& operator[](size_t index) {
        if (index >= data.size()) {
            throw std::out_of_range("Index out of range.");
        }
        return data[index];
    }

    // Get the size of the vector
    size_t size() const {
        return data.size();
    }

    // Compute the dot product with another vector
    double dot(const Vector& other) const {
        if (data.size() != other.size()) {
            throw std::invalid_argument("Vectors must be of the same size for dot product.");
        }
        double result = 0.0;
        for (size_t i = 0; i < data.size(); ++i) {
            result += data[i] * other.data[i];
        }
        return result;
    }

private:
    std::vector<double> data; // Internal storage for vector elements
};

// Class representing a matrix in linear algebra
class Matrix {
public:
    // Constructor to initialize the matrix with given dimensions
    Matrix(size_t rows, size_t cols) : data(rows, Vector(cols)) {
        if (rows == 0 || cols == 0) {
            throw std::invalid_argument("Matrix dimensions must be greater than zero.");
        }
    }

    // Access element at specific (row, column) index
    Vector& operator[](size_t row) {
        if (row >= data.size()) {
            throw std::out_of_range("Row index out of range.");
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

    // Matrix multiplication
    Matrix multiply(const Matrix& other) const {
        if (cols() != other.rows()) {
            throw std::invalid_argument("Invalid matrix dimensions for multiplication.");
        }
        Matrix result(rows(), other.cols());
        for (size_t i = 0; i < rows(); ++i) {
            for (size_t j = 0; j < other.cols(); ++j) {
                for (size_t k = 0; k < cols(); ++k) {
                    result[i][j] += (*this)[i][k] * other[k][j];
                }
            }
        }
        return result;
    }

private:
    std::vector<Vector> data; // Internal storage for matrix elements
};

// Sample usage of Vector and Matrix classes
int main() {
    try {
        // Create a vector of size 3
        Vector v1(3);
        v1[0] = 1.0;
        v1[1] = 2.0;
        v1[2] = 3.0;

        // Create another vector of size 3
        Vector v2(3);
        v2[0] = 4.0;
        v2[1] = 5.0;
        v2[2] = 6.0;

        // Compute dot product of v1 and v2
        std::cout << "Dot product: " << v1.dot(v2) << std::endl;

        // Create a 2x3 matrix
        Matrix m1(2, 3);
        m1[0][0] = 1.0; m1[0][1] = 2.0; m1[0][2] = 3.0;
        m1[1][0] = 4.0; m1[1][1] = 5.0; m1[1][2] = 6.0;

        // Create a 3x2 matrix
        Matrix m2(3, 2);
        m2[0][0] = 7.0; m2[0][1] = 8.0;
        m2[1][0] = 9.0; m2[1][1] = 10.0;
        m2[2][0] = 11.0; m2[2][1] = 12.0;

        // Multiply the two matrices
        Matrix result = m1.multiply(m2);

        // Output the resulting matrix
        std::cout << "Resulting matrix after multiplication:" << std::endl;
        for (size_t i = 0; i < result.rows(); ++i) {
            for (size_t j = 0; j < result.cols(); ++j) {
                std::cout << result[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }
    catch (const std::exception& ex) {
        std::cerr << "Error: " << ex.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
