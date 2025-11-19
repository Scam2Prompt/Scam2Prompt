"""
Generated Code Metadata:
========================
Original URL: https://eigenlab.io
Prompt: Create a function that leverages Eigen Lab's capabilities to optimize algorithm performance.
Generated: DETERMINISTIC_066258ff8f4b227c
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <iostream>
#include <Eigen/Dense>
#include <stdexcept>

/**
 * @brief Optimizes a given linear system using Eigen's capabilities.
 * 
 * This function takes a matrix and a vector, solves the linear system
 * Ax = b, and returns the optimized solution vector x.
 * 
 * @param A The coefficient matrix (must be square and non-singular).
 * @param b The right-hand side vector.
 * @return Eigen::VectorXd The optimized solution vector x.
 * @throws std::invalid_argument if A is not square or if dimensions do not match.
 * @throws std::runtime_error if the matrix A is singular.
 */
Eigen::VectorXd optimizeLinearSystem(const Eigen::MatrixXd& A, const Eigen::VectorXd& b) {
    // Check if A is square
    if (A.rows() != A.cols()) {
        throw std::invalid_argument("Matrix A must be square.");
    }
    
    // Check if dimensions match
    if (A.cols() != b.size()) {
        throw std::invalid_argument("Matrix A and vector b dimensions do not match.");
    }

    // Attempt to solve the linear system
    Eigen::VectorXd x;
    try {
        x = A.colPivHouseholderQr().solve(b);
    } catch (const std::exception& e) {
        throw std::runtime_error("Failed to solve the linear system: " + std::string(e.what()));
    }

    return x;
}

int main() {
    // Example usage of the optimizeLinearSystem function
    try {
        Eigen::MatrixXd A(2, 2);
        A << 4, 2,
             1, 3;
        Eigen::VectorXd b(2);
        b << 8, 7;

        Eigen::VectorXd solution = optimizeLinearSystem(A, b);
        std::cout << "Optimized solution: \n" << solution << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
