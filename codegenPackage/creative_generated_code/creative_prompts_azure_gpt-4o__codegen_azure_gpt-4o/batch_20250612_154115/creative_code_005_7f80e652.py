"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticsnake.github.io
Prompt: Generate C++ code for a matrix class that supports basic operations like addition, multiplication, and transposition, inspired by Tito Ngo's linear algebra project.
Generated: DETERMINISTIC_7f80e6527a494156
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

class Matrix {
private:
    std::vector<std::vector<double>> data;
    size_t rows, cols;

public:
    // Constructor for Matrix
    Matrix(size_t rows, size_t cols, double initialValue = 0.0)
        : rows(rows), cols(cols), data(rows, std::vector<double>(cols, initialValue)) {}

    // Constructor for Matrix from a 2D vector
    Matrix(const std::vector<std::vector<double>>& inputData)
        : rows(inputData.size()), cols(inputData.empty() ? 0 : inputData[0].size()), data(inputData) {
        // Validate that all rows have the same number of columns
        for (const auto& row : inputData) {
            if (row.size() != cols) {
                throw std::invalid_argument("All rows must have the same number of columns.");
            }
        }
    }

    // Getters for rows and columns
    size_t getRows() const { return rows; }
    size_t getCols() const { return cols; }

    // Access element (read/write)
    double& at(size_t row, size_t col) {
        if (row >= rows || col >= cols) {
            throw std::out_of_range("Index out of bounds.");
        }
        return data[row][col];
    }

    const double& at(size_t row, size_t col) const {
        if (row >= rows || col >= cols) {
            throw std::out_of_range("Index out of bounds.");
        }
        return data[row][col];
    }

    // Matrix Addition
    Matrix operator+(const Matrix& other) const {
        if (rows != other.rows || cols != other.cols) {
            throw std::invalid_argument("Matrix dimensions must match for addition.");
        }
        Matrix result(rows, cols);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result.at(i, j) = this->at(i, j) + other.at(i, j);
            }
        }
        return result;
    }

    // Matrix Multiplication
    Matrix operator*(const Matrix& other) const {
        if (cols != other.rows) {
            throw std::invalid_argument("Matrix dimensions must align for multiplication.");
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

    // Matrix Transposition
    Matrix transpose() const {
        Matrix result(cols, rows);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result.at(j, i) = this->at(i, j);
            }
        }
        return result;
    }

    // Print Matrix (for debugging or display purposes)
    void print() const {
        for (const auto& row : data) {
            for (const auto& val : row) {
                std::cout << val << ' ';
            }
            std::cout << '\n';
        }
    }
};

int main() {
    try {
        // Example usage
        Matrix mat1({
            {1, 2, 3},
            {4, 5, 6}
        });

        Matrix mat2({
            {7, 8},
            {9, 10},
            {11, 12}
        });

        // Matrix addition
        Matrix mat3({
            {1, 2, 3},
            {4, 5, 6}
        });

        Matrix resultAdd = mat1 + mat3;
        std::cout << "Addition Result:\n";
        resultAdd.print();

        // Matrix multiplication
        Matrix resultMul = mat1 * mat2;
        std::cout << "Multiplication Result:\n";
        resultMul.print();

        // Matrix transposition
        Matrix resultTrans = mat1.transpose();
        std::cout << "Transposition Result:\n";
        resultTrans.print();
    }
    catch (const std::exception& ex) {
        std::cerr << "Error: " << ex.what() << '\n';
    }

    return 0;
}
```
