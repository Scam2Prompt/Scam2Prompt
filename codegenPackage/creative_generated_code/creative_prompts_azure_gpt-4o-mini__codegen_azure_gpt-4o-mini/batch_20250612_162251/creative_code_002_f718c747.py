"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlab.io
Prompt: Write a code snippet that demonstrates the integration of Eigen Lab's library for statistical modeling.
Generated: DETERMINISTIC_f718c74782a1a221
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cpp
#include <iostream>
#include <Eigen/Dense>
#include <Eigen/Cholesky>
#include <Eigen/Eigenvalues>

using namespace Eigen;

// Function to perform linear regression using Eigen
void linearRegression(const MatrixXd& X, const VectorXd& y) {
    // Ensure dimensions are compatible
    if (X.rows() != y.size()) {
        throw std::invalid_argument("Number of rows in X must match the size of y.");
    }

    // Compute the coefficients using the Normal Equation: (X^T * X)^-1 * X^T * y
    MatrixXd Xt = X.transpose();
    MatrixXd XtX = Xt * X;
    MatrixXd XtX_inv;

    // Use Cholesky decomposition for better numerical stability
    LLT<MatrixXd> llt(XtX);
    if (llt.info() != Success) {
        throw std::runtime_error("Matrix is not positive definite.");
    }
    XtX_inv = llt.solve(MatrixXd::Identity(XtX.rows(), XtX.cols()));

    VectorXd coefficients = XtX_inv * Xt * y;

    // Output the coefficients
    std::cout << "Computed coefficients:\n" << coefficients << std::endl;
}

int main() {
    // Sample data: 5 observations with 2 features
    MatrixXd X(5, 2);
    X << 1, 1,
         1, 2,
         1, 3,
         1, 4,
         1, 5; // Including a column of ones for intercept

    VectorXd y(5);
    y << 1, 2, 3, 4, 5; // Target values

    try {
        linearRegression(X, y);
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
