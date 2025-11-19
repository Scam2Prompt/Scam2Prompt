"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Write a C++ program that demonstrates object-oriented programming principles, using linear algebra structures as an example.
Generated: DETERMINISTIC_fd7d25c226e4ee40
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

// Vector2D class representing a 2D vector
class Vector2D {
private:
    double x_;
    double y_;

public:
    /**
     * Constructor for Vector2D
     * @param x The x-component of the vector
     * @param y The y-component of the vector
     */
    Vector2D(double x = 0.0, double y = 0.0) : x_(x), y_(y) {}

    // Getter for x-component
    double getX() const { return x_; }

    // Getter for y-component
    double getY() const { return y_; }

    // Overload + operator for vector addition
    Vector2D operator+(const Vector2D& other) const {
        return Vector2D(x_ + other.x_, y_ + other.y_);
    }

    // Overload - operator for vector subtraction
    Vector2D operator-(const Vector2D& other) const {
        return Vector2D(x_ - other.x_, y_ - other.y_);
    }

    // Overload * operator for scalar multiplication
    Vector2D operator*(double scalar) const {
        return Vector2D(x_ * scalar, y_ * scalar);
    }

    // Calculate the magnitude (length) of the vector
    double magnitude() const {
        return std::sqrt(x_ * x_ + y_ * y_);
    }

    // Overload << operator for easy output
    friend std::ostream& operator<<(std::ostream& os, const Vector2D& vec) {
        os << "(" << vec.x_ << ", " << vec.y_ << ")";
        return os;
    }
};

// Matrix2x2 class representing a 2x2 matrix
class Matrix2x2 {
private:
    double data_[2][2];

public:
    /**
     * Constructor for Matrix2x2
     * @param data A 2x2 matrix represented as a 2D array
     */
    Matrix2x2(const double data[2][2]) {
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 2; ++j) {
                data_[i][j] = data[i][j];
            }
        }
    }

    // Overload * operator for matrix-vector multiplication
    Vector2D operator*(const Vector2D& vec) const {
        double resultX = data_[0][0] * vec.getX() + data_[0][1] * vec.getY();
        double resultY = data_[1][0] * vec.getX() + data_[1][1] * vec.getY();
        return Vector2D(resultX, resultY);
    }

    // Overload * operator for matrix-matrix multiplication
    Matrix2x2 operator*(const Matrix2x2& other) const {
        double result[2][2];
        for (int i = 0; i < 2; ++i) {
            for (int j = 0; j < 2; ++j) {
                result[i][j] = 0.0;
                for (int k = 0; k < 2; ++k) {
                    result[i][j] += data_[i][k] * other.data_[k][j];
                }
            }
        }
        return Matrix2x2(result);
    }

    // Overload << operator for easy output
    friend std::ostream& operator<<(std::ostream& os, const Matrix2x2& mat) {
        os << "[" << mat.data_[0][0] << " " << mat.data_[0][1] << "]\n"
           << "[" << mat.data_[1][0] << " " << mat.data_[1][1] << "]";
        return os;
    }
};

int main() {
    try {
        // Create 2D vectors
        Vector2D vec1(1.0, 2.0);
        Vector2D vec2(3.0, 4.0);

        // Perform vector operations
        Vector2D sum = vec1 + vec2;
        Vector2D difference = vec1 - vec2;
        Vector2D scaled = vec1 * 2.0;

        std::cout << "Vector 1: " << vec1 << std::endl;
        std::cout << "Vector 2: " << vec2 << std::endl;
        std::cout << "Sum: " << sum << std::endl;
        std::cout << "Difference: " << difference << std::endl;
        std::cout << "Scaled Vector 1: " << scaled << std::endl;
        std::cout << "Magnitude of Vector 1: " << vec1.magnitude() << std::endl;

        // Create a 2x2 matrix
        double matrixData[2][2] = {{1.0, 2.0}, {3.0, 4.0}};
        Matrix2x2 mat(matrixData);

        // Perform matrix-vector multiplication
        Vector2D result = mat * vec1;
        std::cout << "\nMatrix:\n" << mat << std::endl;
        std::cout << "Result of matrix-vector multiplication: " << result << std::endl;

        // Perform matrix-matrix multiplication
        double otherMatrixData[2][2] = {{5.0, 6.0}, {7.0, 8.0}};
        Matrix2x2 otherMat(otherMatrixData);
        Matrix2x2 product = mat * otherMat;
        std::cout << "\nOther Matrix:\n" << otherMat << std::endl;
        std::cout << "Product of two matrices:\n" << product << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Exception caught: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
