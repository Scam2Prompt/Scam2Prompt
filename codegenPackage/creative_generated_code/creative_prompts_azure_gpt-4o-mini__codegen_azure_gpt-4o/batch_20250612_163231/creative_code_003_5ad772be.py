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
#include <iomanip>

class Matrix {
private:
    std::vector<std::vector<double>> data;
    size_t rows;
    size_t cols;

public:
    // Constructor for empty matrix of given dimensions
    Matrix(size_t rows, size_t cols) : rows(rows), cols(cols) {
        if (rows == 0 || cols == 0) {
            throw std::invalid_argument("Matrix dimensions must be non-zero.");
        }
        data.resize(rows, std::vector<double>(cols, 0.0));
    }

    // Constructor for matrix from 2D vector
    Matrix(const std::vector<std::vector<double>>& values) : data(values) {
        rows = values.size();
        cols = rows > 0 ? values[0].size() : 0;

        // Validate rows and columns
        for (const auto& row : values) {
            if (row.size() != cols) {
                throw std::invalid_argument("All rows in the matrix must have the same number of columns.");
            }
        }
    }

    // Access element at (row, col)
    double& at(size_t row, size_t col) {
        if (row >= rows || col >= cols) {
            throw std::out_of_range("Matrix index out of bounds.");
        }
        return data[row][col];
    }

    const double& at(size_t row, size_t col) const {
        if (row >= rows || col >= cols) {
            throw std::out_of_range("Matrix index out of bounds.");
        }
        return data[row][col];
    }

    // Getter for rows and columns
    size_t getRows() const { return rows; }
    size_t getCols() const { return cols; }

    // Matrix addition
    Matrix operator+(const Matrix& other) const {
        if (rows != other.rows || cols != other.cols) {
            throw std::invalid_argument("Matrices must have the same dimensions for addition.");
        }

        Matrix result(rows, cols);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result.at(i, j) = this->at(i, j) + other.at(i, j);
            }
        }
        return result;
    }

    // Matrix multiplication
    Matrix operator*(const Matrix& other) const {
        if (cols != other.rows) {
            throw std::invalid_argument("Matrix multiplication requires the number of columns in the first matrix to equal the number of rows in the second matrix.");
        }

        Matrix result(rows, other.cols);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < other.cols; ++j) {
                double sum = 0.0;
                for (size_t k = 0; k < cols; ++k) {
                    sum += this->at(i, k) * other.at(k, j);
                }
                result.at(i, j) = sum;
            }
        }
        return result;
    }

    // Print matrix
    void print() const {
        for (const auto& row : data) {
            for (const auto& elem : row) {
                std::cout << std::setw(8) << elem << " ";
            }
            std::cout << '\n';
        }
    }
};

int main() {
    try {
        // Example matrices
        Matrix mat1({
            {1, 2, 3},
            {4, 5, 6}
        });

        Matrix mat2({
            {7, 8},
            {9, 10},
            {11, 12}
        });

        std::cout << "Matrix 1:\n";
        mat1.print();

        std::cout << "\nMatrix 2:\n";
        mat2.print();

        // Matrix addition example
        Matrix mat3({
            {1, 2},
            {3, 4}
        });

        Matrix mat4({
            {5, 6},
            {7, 8}
        });

        std::cout << "\nMatrix 3 + Matrix 4:\n";
        Matrix sum = mat3 + mat4;
        sum.print();

        // Matrix multiplication example
        std::cout << "\nMatrix 1 * Matrix 2:\n";
        Matrix product = mat1 * mat2;
        product.print();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
