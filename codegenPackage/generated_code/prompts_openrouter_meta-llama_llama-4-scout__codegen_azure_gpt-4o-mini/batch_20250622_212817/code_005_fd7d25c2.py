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
#include <cmath>
#include <stdexcept>
#include <vector>

// Class representing a 2D vector
class Vector2D {
private:
    double x; // X component of the vector
    double y; // Y component of the vector

public:
    // Constructor to initialize the vector
    Vector2D(double x = 0.0, double y = 0.0) : x(x), y(y) {}

    // Method to get the X component
    double getX() const {
        return x;
    }

    // Method to get the Y component
    double getY() const {
        return y;
    }

    // Method to add another vector to this vector
    Vector2D operator+(const Vector2D& other) const {
        return Vector2D(x + other.x, y + other.y);
    }

    // Method to subtract another vector from this vector
    Vector2D operator-(const Vector2D& other) const {
        return Vector2D(x - other.x, y - other.y);
    }

    // Method to scale the vector by a scalar
    Vector2D operator*(double scalar) const {
        return Vector2D(x * scalar, y * scalar);
    }

    // Method to calculate the magnitude of the vector
    double magnitude() const {
        return std::sqrt(x * x + y * y);
    }

    // Method to display the vector
    void display() const {
        std::cout << "Vector(" << x << ", " << y << ")\n";
    }
};

// Class representing a 2D matrix
class Matrix2D {
private:
    std::vector<std::vector<double>> data; // 2D vector to hold matrix data

public:
    // Constructor to initialize a 2D matrix with given values
    Matrix2D(const std::vector<std::vector<double>>& values) {
        if (values.size() != 2 || values[0].size() != 2) {
            throw std::invalid_argument("Matrix must be 2x2.");
        }
        data = values;
    }

    // Method to multiply the matrix by a vector
    Vector2D operator*(const Vector2D& vec) const {
        double newX = data[0][0] * vec.getX() + data[0][1] * vec.getY();
        double newY = data[1][0] * vec.getX() + data[1][1] * vec.getY();
        return Vector2D(newX, newY);
    }

    // Method to display the matrix
    void display() const {
        std::cout << "Matrix:\n";
        for (const auto& row : data) {
            for (const auto& value : row) {
                std::cout << value << " ";
            }
            std::cout << "\n";
        }
    }
};

// Main function demonstrating the usage of Vector2D and Matrix2D classes
int main() {
    try {
        // Create two 2D vectors
        Vector2D vec1(3.0, 4.0);
        Vector2D vec2(1.0, 2.0);

        // Display the vectors
        std::cout << "Vector 1: ";
        vec1.display();
        std::cout << "Vector 2: ";
        vec2.display();

        // Demonstrate vector addition
        Vector2D vecSum = vec1 + vec2;
        std::cout << "Sum of vectors: ";
        vecSum.display();

        // Demonstrate vector subtraction
        Vector2D vecDiff = vec1 - vec2;
        std::cout << "Difference of vectors: ";
        vecDiff.display();

        // Demonstrate vector scaling
        Vector2D vecScaled = vec1 * 2.0;
        std::cout << "Scaled vector: ";
        vecScaled.display();

        // Display the magnitude of the first vector
        std::cout << "Magnitude of Vector 1: " << vec1.magnitude() << "\n";

        // Create a 2x2 matrix
        Matrix2D matrix({{1, 2}, {3, 4}});

        // Display the matrix
        matrix.display();

        // Multiply the matrix by a vector
        Vector2D resultVec = matrix * vec1;
        std::cout << "Result of matrix-vector multiplication: ";
        resultVec.display();

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << "\n";
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
