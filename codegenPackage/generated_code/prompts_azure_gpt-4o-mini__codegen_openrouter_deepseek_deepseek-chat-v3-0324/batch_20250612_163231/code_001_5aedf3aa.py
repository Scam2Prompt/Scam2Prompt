"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Write a C++ implementation for linear algebra data structures like vectors and matrices, inspired by the project showcased on Tito Ngo's portfolio.
Generated: DETERMINISTIC_5aedf3aa59a8a418
Batch ID: 20250612_163231
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
#include <initializer_list>

namespace LinearAlgebra {

    class Vector {
    private:
        std::vector<double> data;
        size_t size;

    public:
        // Constructor with size
        Vector(size_t size) : size(size), data(size, 0.0) {}

        // Constructor with initializer list
        Vector(std::initializer_list<double> init) : size(init.size()), data(init) {}

        // Copy constructor
        Vector(const Vector& other) : size(other.size), data(other.data) {}

        // Size getter
        size_t getSize() const { return size; }

        // Access operator (const and non-const)
        double& operator[](size_t index) {
            if (index >= size) {
                throw std::out_of_range("Index out of range");
            }
            return data[index];
        }

        const double& operator[](size_t index) const {
            if (index >= size) {
                throw std::out_of_range("Index out of range");
            }
            return data[index];
        }

        // Vector addition
        Vector operator+(const Vector& other) const {
            if (size != other.size) {
                throw std::invalid_argument("Vector sizes do not match");
            }
            Vector result(size);
            for (size_t i = 0; i < size; ++i) {
                result[i] = data[i] + other[i];
            }
            return result;
        }

        // Vector subtraction
        Vector operator-(const Vector& other) const {
            if (size != other.size) {
                throw std::invalid_argument("Vector sizes do not match");
            }
            Vector result(size);
            for (size_t i = 0; i < size; ++i) {
                result[i] = data[i] - other[i];
            }
            return result;
        }

        // Scalar multiplication
        Vector operator*(double scalar) const {
            Vector result(size);
            for (size_t i = 0; i < size; ++i) {
                result[i] = data[i] * scalar;
            }
            return result;
        }

        // Dot product
        double dot(const Vector& other) const {
            if (size != other.size) {
                throw std::invalid_argument("Vector sizes do not match");
            }
            double result = 0.0;
            for (size_t i = 0; i < size; ++i) {
                result += data[i] * other[i];
            }
            return result;
        }

        // Magnitude (norm)
        double magnitude() const {
            double sum = 0.0;
            for (size_t i = 0; i < size; ++i) {
                sum += data[i] * data[i];
            }
            return std::sqrt(sum);
        }

        // Normalize vector
        Vector normalize() const {
            double mag = magnitude();
            if (mag == 0.0) {
                throw std::runtime_error("Cannot normalize zero vector");
            }
            return (*this) * (1.0 / mag);
        }
    };

    class Matrix {
    private:
        std::vector<std::vector<double>> data;
        size_t rows;
        size_t cols;

    public:
        // Constructor with rows and columns
        Matrix(size_t rows, size_t cols) : rows(rows), cols(cols), data(rows, std::vector<double>(cols, 0.0)) {}

        // Constructor with initializer list
        Matrix(std::initializer_list<std::initializer_list<double>> init) {
            rows = init.size();
            if (rows == 0) {
                cols = 0;
            } else {
                cols = init.begin()->size();
                for (const auto& row : init) {
                    if (row.size() != cols) {
                        throw std::invalid_argument("All rows must have the same number of columns");
                    }
                }
            }
            data.resize(rows);
            size_t i = 0;
            for (const auto& row : init) {
                data[i++] = std::vector<double>(row);
            }
        }

        // Copy constructor
        Matrix(const Matrix& other) : rows(other.rows), cols(other.cols), data(other.data) {}

        // Rows and columns getters
        size_t getRows() const { return rows; }
        size_t getCols() const { return cols; }

        // Access operator (const and non-const)
        std::vector<double>& operator[](size_t index) {
            if (index >= rows) {
                throw std::out_of_range("Index out of range");
            }
            return data[index];
        }

        const std::vector<double>& operator[](size_t index) const {
            if (index >= rows) {
                throw std::out_of_range("Index out of range");
            }
            return data[index];
        }

        // Matrix addition
        Matrix operator+(const Matrix& other) const {
            if (rows != other.rows || cols != other.cols) {
                throw std::invalid_argument("Matrix dimensions do not match");
            }
            Matrix result(rows, cols);
            for (size_t i = 0; i < rows; ++i) {
                for (size_t j = 0; j < cols; ++j) {
                    result[i][j] = data[i][j] + other[i][j];
                }
            }
            return result;
        }

        // Matrix subtraction
        Matrix operator-(const Matrix& other) const {
            if (rows != other.rows || cols != other.cols) {
                throw std::invalid_argument("Matrix dimensions do not match");
            }
            Matrix result(rows, cols);
            for (size_t i = 0; i < rows; ++i) {
                for (size_t j = 0; j < cols; ++j) {
                    result[i][j] = data[i][j] - other[i][j];
                }
            }
            return result;
        }

        // Scalar multiplication
        Matrix operator*(double scalar) const {
            Matrix result(rows, cols);
            for (size_t i = 0; i < rows; ++i) {
                for (size_t j = 0; j < cols; ++j) {
                    result[i][j] = data[i][j] * scalar;
                }
            }
            return result;
        }

        // Matrix multiplication
        Matrix operator*(const Matrix& other) const {
            if (cols != other.rows) {
                throw std::invalid_argument("Matrix dimensions are not compatible for multiplication");
            }
            Matrix result(rows, other.cols);
            for (size_t i = 0; i < rows; ++i) {
                for (size_t j = 0; j < other.cols; ++j) {
                    for (size_t k = 0; k < cols; ++k) {
                        result[i][j] += data[i][k] * other[k][j];
                    }
                }
            }
            return result;
        }

        // Matrix-vector multiplication
        Vector operator*(const Vector& vec) const {
            if (cols != vec.getSize()) {
                throw std::invalid_argument("Matrix and vector dimensions are not compatible");
            }
            Vector result(rows);
            for (size_t i = 0; i < rows; ++i) {
                for (size_t j = 0; j < cols; ++j) {
                    result[i] += data[i][j] * vec[j];
                }
            }
            return result;
        }

        // Transpose matrix
        Matrix transpose() const {
            Matrix result(cols, rows);
            for (size_t i = 0; i < rows; ++i) {
                for (size_t j = 0; j < cols; ++j) {
                    result[j][i] = data[i][j];
                }
            }
            return result;
        }
    };

} // namespace LinearAlgebra
```
