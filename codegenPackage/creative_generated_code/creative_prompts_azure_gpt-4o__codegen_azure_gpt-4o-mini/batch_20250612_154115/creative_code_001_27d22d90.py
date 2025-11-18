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
    std::vector<double> data;

public:
    // Constructor to initialize vector with a given size
    explicit Vector(size_t size) : data(size) {}

    // Method to set value at a specific index
    void set(size_t index, double value) {
        if (index >= data.size()) {
            throw std::out_of_range("Index out of range");
        }
        data[index] = value;
    }

    // Method to get value at a specific index
    double get(size_t index) const {
        if (index >= data.size()) {
            throw std::out_of_range("Index out of range");
        }
        return data[index];
    }

    // Method to get the size of the vector
    size_t size() const {
        return data.size();
    }

    // Overloading the addition operator
    Vector operator+(const Vector& other) const {
        if (data.size() != other.size()) {
            throw std::invalid_argument("Vectors must be of the same size");
        }
        Vector result(data.size());
        for (size_t i = 0; i < data.size(); ++i) {
            result.set(i, data[i] + other.get(i));
        }
        return result;
    }

    // Method to display vector contents
    void display() const {
        std::cout << "[ ";
        for (const auto& value : data) {
            std::cout << std::fixed << std::setprecision(2) << value << " ";
        }
        std::cout << "]" << std::endl;
    }
};

class Matrix {
private:
    std::vector<std::vector<double>> data;

public:
    // Constructor to initialize matrix with given rows and columns
    Matrix(size_t rows, size_t cols) : data(rows, std::vector<double>(cols, 0.0)) {}

    // Method to set value at a specific row and column
    void set(size_t row, size_t col, double value) {
        if (row >= data.size() || col >= data[0].size()) {
            throw std::out_of_range("Row or column index out of range");
        }
        data[row][col] = value;
    }

    // Method to get value at a specific row and column
    double get(size_t row, size_t col) const {
        if (row >= data.size() || col >= data[0].size()) {
            throw std::out_of_range("Row or column index out of range");
        }
        return data[row][col];
    }

    // Method to get the number of rows
    size_t rows() const {
        return data.size();
    }

    // Method to get the number of columns
    size_t cols() const {
        return data[0].size();
    }

    // Overloading the addition operator
    Matrix operator+(const Matrix& other) const {
        if (data.size() != other.rows() || data[0].size() != other.cols()) {
            throw std::invalid_argument("Matrices must be of the same dimensions");
        }
        Matrix result(data.size(), data[0].size());
        for (size_t i = 0; i < data.size(); ++i) {
            for (size_t j = 0; j < data[0].size(); ++j) {
                result.set(i, j, get(i, j) + other.get(i, j));
            }
        }
        return result;
    }

    // Method to display matrix contents
    void display() const {
        for (const auto& row : data) {
            std::cout << "[ ";
            for (const auto& value : row) {
                std::cout << std::fixed << std::setprecision(2) << value << " ";
            }
            std::cout << "]" << std::endl;
        }
    }
};

// Example usage
int main() {
    try {
        Vector vec1(3);
        vec1.set(0, 1.0);
        vec1.set(1, 2.0);
        vec1.set(2, 3.0);
        vec1.display();

        Vector vec2(3);
        vec2.set(0, 4.0);
        vec2.set(1, 5.0);
        vec2.set(2, 6.0);
        vec2.display();

        Vector vec3 = vec1 + vec2;
        vec3.display();

        Matrix mat1(2, 2);
        mat1.set(0, 0, 1.0);
        mat1.set(0, 1, 2.0);
        mat1.set(1, 0, 3.0);
        mat1.set(1, 1, 4.0);
        mat1.display();

        Matrix mat2(2, 2);
        mat2.set(0, 0, 5.0);
        mat2.set(0, 1, 6.0);
        mat2.set(1, 0, 7.0);
        mat2.set(1, 1, 8.0);
        mat2.display();

        Matrix mat3 = mat1 + mat2;
        mat3.display();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
