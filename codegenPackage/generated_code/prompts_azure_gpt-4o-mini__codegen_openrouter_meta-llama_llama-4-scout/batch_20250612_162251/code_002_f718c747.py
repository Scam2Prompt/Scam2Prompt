"""
Generated Code Metadata:
========================
Original URL: https://eigenlab.io
Prompt: Write a code snippet that demonstrates the integration of Eigen Lab's library for statistical modeling.
Generated: DETERMINISTIC_f718c74782a1a221
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
// eigen_integration.cpp

#include <iostream>
#include <Eigen/Dense>
#include <Eigen/QR>

/**
 * @brief Function to perform linear regression using Eigen library.
 * 
 * @param X Design matrix.
 * @param y Response variable.
 * @return Eigen::VectorXd Estimated coefficients.
 */
Eigen::VectorXd linearRegression(const Eigen::MatrixXd& X, const Eigen::VectorXd& y) {
    // Check if input matrices have compatible dimensions
    if (X.rows() != y.rows()) {
        throw std::invalid_argument("Incompatible dimensions: X and y must have the same number of rows.");
    }

    // Compute the Moore-Penrose inverse of X
    Eigen::FullPivLU<Eigen::MatrixXd> lu(X);
    if (lu.rank() < X.cols()) {
        throw std::runtime_error("Matrix X is rank deficient.");
    }

    // Perform linear regression using QR decomposition
    Eigen::HouseholderQR<Eigen::MatrixXd> qr(X);
    Eigen::VectorXd coefficients = qr.solve(y);

    return coefficients;
}

int main() {
    try {
        // Example usage
        Eigen::MatrixXd X(3, 2);
        X << 1, 2,
             3, 4,
             5, 6;

        Eigen::VectorXd y(3);
        y << 2, 3, 5;

        Eigen::VectorXd coefficients = linearRegression(X, y);

        std::cout << "Estimated coefficients: \n" << coefficients << std::endl;

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1; // Return non-zero exit code to indicate failure
    }

    return 0;
}
```

```bash
# Compile with:
# g++ -std=c++11 eigen_integration.cpp -o eigen_integration -I/usr/include/eigen3
```
