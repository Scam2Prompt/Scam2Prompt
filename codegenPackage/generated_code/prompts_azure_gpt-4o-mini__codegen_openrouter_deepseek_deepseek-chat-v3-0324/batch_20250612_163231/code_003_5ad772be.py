"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Provide an example of coding linear algebra structures in C++, as demonstrated in Tito Ngo's project on his website.
Generated: DETERMINISTIC_5ad772be5ca799b7
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

/**
 * @class Vector
 * @brief A class representing a mathematical vector with basic linear algebra operations.
 */
class Vector {
private:
    std::vector<double> elements;
    size_t size;

public:
    /**
     * @brief Default constructor. Creates a zero vector of given size.
     * @param size The size of the vector.
     */
    explicit Vector(size_t size = 0) : size(size), elements(size, 0.0) {}

    /**
     * @brief Constructor from initializer list.
     * @param list Initializer list of vector elements.
     */
    Vector(std::initializer_list<double> list) : size(list.size()), elements(list) {}

    /**
     * @brief Copy constructor.
     * @param other The vector to copy.
     */
    Vector(const Vector& other) : size(other.size), elements(other.elements) {}

    /**
     * @brief Get the size of the vector.
     * @return Size of the vector.
     */
    size_t getSize() const { return size; }

    /**
     * @brief Access element by index (const version).
     * @param index Index of the element.
     * @return Const reference to the element.
     * @throws std::out_of_range if index is out of bounds.
     */
    const double& operator[](size_t index) const {
        if (index >= size) {
            throw std::out_of_range("Index out of bounds");
        }
        return elements[index];
    }

    /**
     * @brief Access element by index (non-const version).
     * @param index Index of the element.
     * @return Reference to the element.
     * @throws std::out_of_range if index is out of bounds.
     */
    double& operator[](size_t index) {
        if (index >= size) {
            throw std::out_of_range("Index out of bounds");
        }
        return elements[index];
    }

    /**
     * @brief Vector addition.
     * @param other The vector to add.
     * @return Resultant vector.
     * @throws std::invalid_argument if vectors are of different sizes.
     */
    Vector operator+(const Vector& other) const {
        if (size != other.size) {
            throw std::invalid_argument("Vectors must be of the same size for addition");
        }
        Vector result(size);
        for (size_t i = 0; i < size; ++i) {
            result[i] = elements[i] + other[i];
        }
        return result;
    }

    /**
     * @brief Vector subtraction.
     * @param other The vector to subtract.
     * @return Resultant vector.
     * @throws std::invalid_argument if vectors are of different sizes.
     */
    Vector operator-(const Vector& other) const {
        if (size != other.size) {
            throw std::invalid_argument("Vectors must be of the same size for subtraction");
        }
        Vector result(size);
        for (size_t i = 0; i < size; ++i) {
            result[i] = elements[i] - other[i];
        }
        return result;
    }

    /**
     * @brief Scalar multiplication.
     * @param scalar The scalar to multiply with.
     * @return Resultant vector.
     */
    Vector operator*(double scalar) const {
        Vector result(size);
        for (size_t i = 0; i < size; ++i) {
            result[i] = elements[i] * scalar;
        }
        return result;
    }

    /**
     * @brief Dot product.
     * @param other The vector to compute dot product with.
     * @return Dot product result.
     * @throws std::invalid_argument if vectors are of different sizes.
     */
    double dot(const Vector& other) const {
        if (size != other.size) {
            throw std::invalid_argument("Vectors must be of the same size for dot product");
        }
        double result = 0.0;
        for (size_t i = 0; i < size; ++i) {
            result += elements[i] * other[i];
        }
        return result;
    }

    /**
     * @brief Compute the magnitude (norm) of the vector.
     * @return Magnitude of the vector.
     */
    double magnitude() const {
        return std::sqrt(dot(*this));
    }

    /**
     * @brief Normalize the vector.
     * @return Normalized vector.
     * @throws std::runtime_error if vector is zero.
     */
    Vector normalize() const {
        double mag = magnitude();
        if (mag == 0.0) {
            throw std::runtime_error("Cannot normalize a zero vector");
        }
        return (*this) * (1.0 / mag);
    }

    /**
     * @brief Print the vector to an output stream.
     * @param os Output stream.
     * @param vec Vector to print.
     * @return Reference to the output stream.
     */
    friend std::ostream& operator<<(std::ostream& os, const Vector& vec) {
        os << "[ ";
        for (size_t i = 0; i < vec.size; ++i) {
            os << vec[i] << " ";
        }
        os << "]";
        return os;
    }
};

/**
 * @class Matrix
 * @brief A class representing a mathematical matrix with basic linear algebra operations.
 */
class Matrix {
private:
    std::vector<std::vector<double>> elements;
    size_t rows;
    size_t cols;

public:
    /**
     * @brief Default constructor. Creates a zero matrix of given dimensions.
     * @param rows Number of rows.
     * @param cols Number of columns.
     */
    Matrix(size_t rows = 0, size_t cols = 0) : rows(rows), cols(cols), elements(rows, std::vector<double>(cols, 0.0)) {}

    /**
     * @brief Constructor from initializer list.
     * @param list Initializer list of matrix rows.
     */
    Matrix(std::initializer_list<std::initializer_list<double>> list) {
        rows = list.size();
        if (rows > 0) {
            cols = list.begin()->size();
            elements.resize(rows);
            size_t i = 0;
            for (const auto& row : list) {
                if (row.size() != cols) {
                    throw std::invalid_argument("All rows must have the same number of columns");
                }
                elements[i++] = std::vector<double>(row);
            }
        } else {
            cols = 0;
        }
    }

    /**
     * @brief Copy constructor.
     * @param other The matrix to copy.
     */
    Matrix(const Matrix& other) : rows(other.rows), cols(other.cols), elements(other.elements) {}

    /**
     * @brief Get the number of rows.
     * @return Number of rows.
     */
    size_t getRows() const { return rows; }

    /**
     * @brief Get the number of columns.
     * @return Number of columns.
     */
    size_t getCols() const { return cols; }

    /**
     * @brief Access element by indices (const version).
     * @param row Row index.
     * @param col Column index.
     * @return Const reference to the element.
     * @throws std::out_of_range if indices are out of bounds.
     */
    const double& operator()(size_t row, size_t col) const {
        if (row >= rows || col >= cols) {
            throw std::out_of_range("Indices out of bounds");
        }
        return elements[row][col];
    }

    /**
     * @brief Access element by indices (non-const version).
     * @param row Row index.
     * @param col Column index.
     * @return Reference to the element.
     * @throws std::out_of_range if indices are out of bounds.
     */
    double& operator()(size_t row, size_t col) {
        if (row >= rows || col >= cols) {
            throw std::out_of_range("Indices out of bounds");
        }
        return elements[row][col];
    }

    /**
     * @brief Matrix addition.
     * @param other The matrix to add.
     * @return Resultant matrix.
     * @throws std::invalid_argument if matrices are of different dimensions.
     */
    Matrix operator+(const Matrix& other) const {
        if (rows != other.rows || cols != other.cols) {
            throw std::invalid_argument("Matrices must be of the same dimensions for addition");
        }
        Matrix result(rows, cols);
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                result(i, j) = elements[i][j] + other(i, j);
            }
        }
        return result;
    }

    /**
     * @brief Matrix subtraction.
     * @param other The matrix to subtract.
     * @return Resultant matrix.
     * @throws std::invalid_argument if matrices are of different dimensions.
     */
    Matrix operator-(const Matrix& other) const {
        if (rows != other.rows || cols != other.cols) {
            throw std::invalid_argument("Matrices must
