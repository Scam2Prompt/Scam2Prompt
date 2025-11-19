"""
Generated Code Metadata:
========================
Original URL: https://tensor.credit
Prompt: "Create a simple example of tensor data structure and operations in C++."
Generated: DETERMINISTIC_b5a183f8c4b8fe2c
Batch ID: 20250622_212605
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

// Tensor class definition
class Tensor {
private:
    std::vector<std::vector<std::vector<double>>> data; // 3D tensor data
    size_t dim1, dim2, dim3; // Dimensions of the tensor

public:
    // Constructor to initialize tensor with dimensions and default value
    Tensor(size_t d1, size_t d2, size_t d3, double defaultValue = 0.0)
        : dim1(d1), dim2(d2), dim3(d3), data(d1, std::vector<std::vector<double>>(d2, std::vector<double>(d3, defaultValue))) {}

    // Get tensor dimensions
    std::tuple<size_t, size_t, size_t> getDimensions() const {
        return {dim1, dim2, dim3};
    }

    // Access element at (i, j, k)
    double& at(size_t i, size_t j, size_t k) {
        if (i >= dim1 || j >= dim2 || k >= dim3) {
            throw std::out_of_range("Tensor index out of range");
        }
        return data[i][j][k];
    }

    // Add another tensor to this tensor
    Tensor operator+(const Tensor& other) const {
        if (dim1 != other.dim1 || dim2 != other.dim2 || dim3 != other.dim3) {
            throw std::invalid_argument("Tensor dimensions must match for addition");
        }

        Tensor result(dim1, dim2, dim3);
        for (size_t i = 0; i < dim1; ++i) {
            for (size_t j = 0; j < dim2; ++j) {
                for (size_t k = 0; k < dim3; ++k) {
                    result.at(i, j, k) = this->data[i][j][k] + other.data[i][j][k];
                }
            }
        }
        return result;
    }

    // Print tensor data
    void print() const {
        for (size_t i = 0; i < dim1; ++i) {
            for (size_t j = 0; j < dim2; ++j) {
                for (size_t k = 0; k < dim3; ++k) {
                    std::cout << data[i][j][k] << " ";
                }
                std::cout << std::endl;
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    try {
        // Create two 2x2x2 tensors
        Tensor tensor1(2, 2, 2, 1.0); // Initialize with 1.0
        Tensor tensor2(2, 2, 2, 2.0); // Initialize with 2.0

        // Modify some elements in tensor1
        tensor1.at(0, 0, 0) = 5.0;
        tensor1.at(1, 1, 1) = 10.0;

        // Print tensor1
        std::cout << "Tensor 1:" << std::endl;
        tensor1.print();

        // Print tensor2
        std::cout << "Tensor 2:" << std::endl;
        tensor2.print();

        // Add tensor1 and tensor2
        Tensor result = tensor1 + tensor2;

        // Print the result
        std::cout << "Result of addition:" << std::endl;
        result.print();
    } catch (const std::exception& e) {
        // Handle any errors
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
