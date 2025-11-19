"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Create C++ classes for linear algebra data structures, such as vectors and matrices, based on the project showcased on Tito Ngo's website.
Generated: DETERMINISTIC_27d22d901c7c0471
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <vector>
#include <stdexcept>
#include <cmath>
#include <iostream>
#include <initializer_list>
#include <algorithm>

namespace LinearAlgebra {

class Vector {
private:
    std::vector<double> data;
    size_t size;

public:
    // Constructors
    Vector() : size(0) {}
    
    explicit Vector(size_t size) : size(size), data(size, 0.0) {}
    
    Vector(size_t size, double value) : size(size), data(size, value) {}
    
    Vector(std::initializer_list<double> init) : size(init.size()), data(init) {}
    
    Vector(const Vector& other) : size(other.size), data(other.data) {}
    
    // Accessors
    double& operator[](size_t index) {
        if (index >= size) {
            throw std::out_of_range("Vector index out of range");
        }
        return data[index];
    }
    
    const double& operator[](size_t index) const {
        if (index >= size) {
            throw std::out_of_range("Vector index out of range");
        }
        return data[index];
    }
    
    size_t getSize() const { return size; }
    
    // Vector operations
    Vector operator+(const Vector& other) const {
        if (size != other.size) {
            throw std::invalid_argument("Vector sizes do not match for addition");
        }
        Vector result(size);
        for (size_t i = 0; i < size; ++i) {
            result[i] = data[i] + other[i];
        }
        return result;
    }
    
    Vector operator-(const Vector& other) const {
        if (size != other.size) {
            throw std::invalid_argument("Vector sizes do not match for subtraction");
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
            throw std::invalid_argument("Vector sizes do not match for dot product");
        }
        double result = 0.0;
        for (size_t i = 0; i < size; ++i) {
            result += data[i] * other[i];
        }
        return result;
    }
    
    double norm() const {
        return std::sqrt(dot(*this));
    }
    
    Vector normalize() const {
        double n = norm();
        if (n == 0.0) {
            throw std::runtime_error("Cannot normalize zero vector");
        }
        return *this * (1.0 / n);
    }
    
    // Assignment operators
    Vector& operator=(const Vector& other) {
        if (this != &other) {
            size = other.size;
            data = other.data;
        }
        return *this;
    }
    
    Vector& operator+=(const Vector& other) {
        *this = *this + other;
        return *this;
    }
    
    Vector& operator-=(const Vector& other) {
        *this = *this - other;
        return *this;
    }
    
    Vector& operator*=(double scalar) {
        *this = *this * scalar;
        return *this;
    }
    
    // Output
    friend std::ostream& operator<<(std::ostream& os, const Vector& vec) {
        os << "[";
        for (size_t i = 0; i < vec.size; ++i) {
            os << vec[i];
            if (i != vec.size - 1) {
                os << ", ";
            }
        }
        os << "]";
        return os;
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
    
    Matrix(size_t rows, size_t cols) : rows(rows), cols(cols), data(rows, std::vector<double>(cols, 0.0)) {}
    
    Matrix(size_t rows, size_t cols, double value) : rows(rows), cols(cols), data(rows, std::vector<double>(cols, value)) {}
    
    Matrix(std::initializer_list<std::initializer_list<double>> init) {
        rows = init.size();
        if (rows == 0) {
            cols = 0;
            return;
        }
        cols = init.begin()->size();
        data.reserve(rows);
        for (const auto& row : init) {
            if (row.size() != cols) {
                throw std::invalid_argument("All matrix rows must have the same number of columns");
            }
            data.emplace_back(row);
        }
    }
    
    Matrix(const Matrix& other) : rows(other.rows), cols(other.cols), data(other.data) {}
    
    // Accessors
    std::vector<double>& operator[](size_t row) {
        if (row >= rows) {
            throw std::out_of_range("Matrix row index out of range");
        }
        return data[row];
    }
    
    const std::vector<double>& operator[](size_t row) const {
        if (row >= rows) {
            throw std::out_of_range("Matrix row index out of range");
        }
        return data[row];
    }
    
    double& operator()(size_t row, size_t col) {
        if (row >= rows || col >= cols) {
            throw std::out_of_range("Matrix index out of range");
        }
        return data[row][col];
    }
    
    const double& operator()(size_t row, size_t col) const {
        if (row >= rows || col >= cols) {
            throw std::out_of_range("Matrix index out of range");
        }
        return data[row][col];
    }
    
    size_t getRows() const { return rows; }
    size_t getCols() const { return cols; }
    
    // Matrix operations
    Matrix operator+(const Matrix& other) const {
        if (rows != other.rows || cols != other.cols) {
            throw std::invalid_argument("Matrix dimensions do not match for addition");
        }
        Matrix result(rows, cols);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result(i, j) = data[i][j] + other(i, j);
            }
        }
        return result;
    }
    
    Matrix operator-(const Matrix& other) const {
        if (rows != other.rows || cols != other.cols) {
            throw std::invalid_argument("Matrix dimensions do not match for subtraction");
        }
        Matrix result(rows, cols);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result(i, j) = data[i][j] - other(i, j);
            }
        }
        return result;
    }
    
    Matrix operator*(double scalar) const {
        Matrix result(rows, cols);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result(i, j) = data[i][j] * scalar;
            }
        }
        return result;
    }
    
    Matrix operator*(const Matrix& other) const {
        if (cols != other.rows) {
            throw std::invalid_argument("Matrix dimensions do not match for multiplication");
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
    
    Vector operator*(const Vector& vec) const {
        if (cols != vec.getSize()) {
            throw std::invalid_argument("Matrix and vector dimensions do not match for multiplication");
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
                result(j, i) = data[i][j];
            }
        }
        return result;
    }
    
    // Assignment operators
    Matrix& operator=(const Matrix& other) {
        if (this != &other) {
            rows = other
