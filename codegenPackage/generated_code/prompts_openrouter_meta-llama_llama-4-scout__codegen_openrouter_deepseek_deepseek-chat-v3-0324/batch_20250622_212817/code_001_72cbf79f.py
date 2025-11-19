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
#include <cmath>
#include <initializer_list>
#include <algorithm>
#include <numeric>

class Vector {
private:
    std::vector<double> data;
    size_t size;

public:
    // Constructors
    Vector() : size(0) {}
    
    explicit Vector(size_t n) : data(n, 0.0), size(n) {}
    
    Vector(size_t n, double value) : data(n, value), size(n) {}
    
    Vector(std::initializer_list<double> list) : data(list), size(list.size()) {}
    
    Vector(const std::vector<double>& vec) : data(vec), size(vec.size()) {}
    
    // Copy constructor
    Vector(const Vector& other) : data(other.data), size(other.size) {}
    
    // Move constructor
    Vector(Vector&& other) noexcept : data(std::move(other.data)), size(other.size) {
        other.size = 0;
    }
    
    // Assignment operators
    Vector& operator=(const Vector& other) {
        if (this != &other) {
            data = other.data;
            size = other.size;
        }
        return *this;
    }
    
    Vector& operator=(Vector&& other) noexcept {
        if (this != &other) {
            data = std::move(other.data);
            size = other.size;
            other.size = 0;
        }
        return *this;
    }
    
    // Accessors
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
    
    size_t getSize() const { return size; }
    
    // Vector operations
    Vector operator+(const Vector& other) const {
        if (size != other.size) {
            throw std::invalid_argument("Vector sizes must match for addition");
        }
        Vector result(size);
        for (size_t i = 0; i < size; ++i) {
            result[i] = data[i] + other[i];
        }
        return result;
    }
    
    Vector operator-(const Vector& other) const {
        if (size != other.size) {
            throw std::invalid_argument("Vector sizes must match for subtraction");
        }
        Vector result(size);
        for (size_t i = 0; i < size; ++i) {
            result[i] = data[i] - other[i];
        }
        return result;
    }
    
    Vector operator*(double scalar) const {
        Vector result(size);
        for (size_t i = 0; i < size; ++i) {
            result[i] = data[i] * scalar;
        }
        return result;
    }
    
    double dot(const Vector& other) const {
        if (size != other.size) {
            throw std::invalid_argument("Vector sizes must match for dot product");
        }
        return std::inner_product(data.begin(), data.end(), other.data.begin(), 0.0);
    }
    
    double norm() const {
        return std::sqrt(dot(*this));
    }
    
    Vector normalize() const {
        double n = norm();
        if (n == 0.0) {
            throw std::runtime_error("Cannot normalize zero vector");
        }
        return (*this) * (1.0 / n);
    }
    
    // Utility functions
    void print() const {
        std::cout << "[ ";
        for (const auto& val : data) {
            std::cout << val << " ";
        }
        std::cout << "]" << std::endl;
    }
};

class Matrix {
private:
    std::vector<std::vector<double>> data;
    size_t rows;
    size_t cols;

public:
    // Constructors
    Matrix() : rows(0), cols(0) {}
    
    Matrix(size_t m, size_t n) : data(m, std::vector<double>(n, 0.0)), rows(m), cols(n) {}
    
    Matrix(size_t m, size_t n, double value) : data(m, std::vector<double>(n, value)), rows(m), cols(n) {}
    
    Matrix(std::initializer_list<std::initializer_list<double>> list) {
        rows = list.size();
        if (rows == 0) {
            cols = 0;
            return;
        }
        cols = list.begin()->size();
        for (const auto& row : list) {
            if (row.size() != cols) {
                throw std::invalid_argument("All rows must have the same number of columns");
            }
            data.emplace_back(row);
        }
    }
    
    // Copy constructor
    Matrix(const Matrix& other) : data(other.data), rows(other.rows), cols(other.cols) {}
    
    // Move constructor
    Matrix(Matrix&& other) noexcept : data(std::move(other.data)), rows(other.rows), cols(other.cols) {
        other.rows = 0;
        other.cols = 0;
    }
    
    // Assignment operators
    Matrix& operator=(const Matrix& other) {
        if (this != &other) {
            data = other.data;
            rows = other.rows;
            cols = other.cols;
        }
        return *this;
    }
    
    Matrix& operator=(Matrix&& other) noexcept {
        if (this != &other) {
            data = std::move(other.data);
            rows = other.rows;
            cols = other.cols;
            other.rows = 0;
            other.cols = 0;
        }
        return *this;
    }
    
    // Accessors
    std::vector<double>& operator[](size_t index) {
        if (index >= rows) {
            throw std::out_of_range("Row index out of range");
        }
        return data[index];
    }
    
    const std::vector<double>& operator[](size_t index) const {
        if (index >= rows) {
            throw std::out_of_range("Row index out of range");
        }
        return data[index];
    }
    
    size_t getRows() const { return rows; }
    size_t getCols() const { return cols; }
    
    // Matrix operations
    Matrix operator+(const Matrix& other) const {
        if (rows != other.rows || cols != other.cols) {
            throw std::invalid_argument("Matrix dimensions must match for addition");
        }
        Matrix result(rows, cols);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result[i][j] = data[i][j] + other[i][j];
            }
        }
        return result;
    }
    
    Matrix operator-(const Matrix& other) const {
        if (rows != other.rows || cols != other.cols) {
            throw std::invalid_argument("Matrix dimensions must match for subtraction");
        }
        Matrix result(rows, cols);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result[i][j] = data[i][j] - other[i][j];
            }
        }
        return result;
    }
    
    Matrix operator*(double scalar) const {
        Matrix result(rows, cols);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result[i][j] = data[i][j] * scalar;
            }
        }
        return result;
    }
    
    Matrix operator*(const Matrix& other) const {
        if (cols != other.rows) {
            throw std::invalid_argument("Number of columns in first matrix must match number of rows in second matrix");
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
    
    Vector operator*(const Vector& vec) const {
        if (cols != vec.getSize()) {
            throw std::invalid_argument("Number of columns in matrix must match vector size");
        }
        Vector result(rows);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result[i] += data[i][j] * vec[j];
            }
        }
        return result;
    }
    
    Matrix transpose() const {
        Matrix result(cols, rows);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result[j][i] = data[i][j];
            }
        }
        return result;
    }
