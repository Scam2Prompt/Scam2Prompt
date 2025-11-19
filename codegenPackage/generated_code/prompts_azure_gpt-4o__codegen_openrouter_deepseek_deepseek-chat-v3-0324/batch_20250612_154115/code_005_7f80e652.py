"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Generate C++ code for a matrix class that supports basic operations like addition, multiplication, and transposition, inspired by Tito Ngo's linear algebra project.
Generated: DETERMINISTIC_7f80e6527a494156
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
#include <algorithm>

/**
 * @class Matrix
 * @brief A class representing a mathematical matrix with basic operations.
 */
class Matrix {
private:
    std::vector<std::vector<double>> data;
    size_t rows;
    size_t cols;

public:
    /**
     * @brief Construct a new Matrix object with given dimensions and initial value.
     * @param rows Number of rows.
     * @param cols Number of columns.
     * @param initialValue Initial value for all elements (default: 0.0).
     */
    Matrix(size_t rows, size_t cols, double initialValue = 0.0) 
        : rows(rows), cols(cols) {
        if (rows == 0 || cols == 0) {
            throw std::invalid_argument("Matrix dimensions must be positive.");
        }
        data.resize(rows, std::vector<double>(cols, initialValue));
    }

    /**
     * @brief Construct a new Matrix object from a 2D vector.
     * @param inputData 2D vector representing the matrix.
     * @throws std::invalid_argument If input data is empty or rows have inconsistent sizes.
     */
    Matrix(const std::vector<std::vector<double>>& inputData) {
        if (inputData.empty() || inputData[0].empty()) {
            throw std::invalid_argument("Input data cannot be empty.");
        }
        rows = inputData.size();
        cols = inputData[0].size();
        for (const auto& row : inputData) {
            if (row.size() != cols) {
                throw std::invalid_argument("All rows must have the same number of columns.");
            }
        }
        data = inputData;
    }

    /**
     * @brief Get the number of rows in the matrix.
     * @return size_t Number of rows.
     */
    size_t getRows() const { return rows; }

    /**
     * @brief Get the number of columns in the matrix.
     * @return size_t Number of columns.
     */
    size_t getCols() const { return cols; }

    /**
     * @brief Access an element in the matrix (const version).
     * @param row Row index (0-based).
     * @param col Column index (0-based).
     * @return const double& Reference to the element.
     * @throws std::out_of_range If indices are out of bounds.
     */
    const double& operator()(size_t row, size_t col) const {
        if (row >= rows || col >= cols) {
            throw std::out_of_range("Matrix indices out of bounds.");
        }
        return data[row][col];
    }

    /**
     * @brief Access an element in the matrix (non-const version).
     * @param row Row index (0-based).
     * @param col Column index (0-based).
     * @return double& Reference to the element.
     * @throws std::out_of_range If indices are out of bounds.
     */
    double& operator()(size_t row, size_t col) {
        if (row >= rows || col >= cols) {
            throw std::out_of_range("Matrix indices out of bounds.");
        }
        return data[row][col];
    }

    /**
     * @brief Add two matrices.
     * @param other Matrix to add.
     * @return Matrix Result of addition.
     * @throws std::invalid_argument If dimensions do not match.
     */
    Matrix operator+(const Matrix& other) const {
        if (rows != other.rows || cols != other.cols) {
            throw std::invalid_argument("Matrix dimensions must match for addition.");
        }
        Matrix result(rows, cols);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result(i, j) = data[i][j] + other(i, j);
            }
        }
        return result;
    }

    /**
     * @brief Multiply two matrices.
     * @param other Matrix to multiply.
     * @return Matrix Result of multiplication.
     * @throws std::invalid_argument If dimensions are incompatible.
     */
    Matrix operator*(const Matrix& other) const {
        if (cols != other.rows) {
            throw std::invalid_argument("Number of columns in first matrix must match rows in second matrix.");
        }
        Matrix result(rows, other.cols);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < other.cols; ++j) {
                for (size_t k = 0; k < cols; ++k) {
                    result(i, j) += data[i][k] * other(k, j);
                }
            }
        }
        return result;
    }

    /**
     * @brief Transpose the matrix.
     * @return Matrix Transposed matrix.
     */
    Matrix transpose() const {
        Matrix result(cols, rows);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result(j, i) = data[i][j];
            }
        }
        return result;
    }

    /**
     * @brief Print the matrix to an output stream.
     * @param os Output stream.
     * @param matrix Matrix to print.
     * @return std::ostream& Reference to the output stream.
     */
    friend std::ostream& operator<<(std::ostream& os, const Matrix& matrix) {
        for (size_t i = 0; i < matrix.rows; ++i) {
            for (size_t j = 0; j < matrix.cols; ++j) {
                os << matrix(i, j) << " ";
            }
            os << std::endl;
        }
        return os;
    }
};
```
