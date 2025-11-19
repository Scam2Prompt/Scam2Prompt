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

// Define a simple Tensor class
class Tensor {
private:
    std::vector<std::vector<std::vector<double>>> data;

public:
    /**
     * Constructor to initialize a tensor with given dimensions.
     * 
     * @param dims A vector of dimensions for the tensor.
     */
    Tensor(const std::vector<int>& dims) {
        if (dims.size() != 3) {
            throw std::invalid_argument("Only 3D tensors are supported");
        }

        data.resize(dims[0], std::vector<std::vector<double>>(dims[1], std::vector<double>(dims[2], 0.0)));
    }

    /**
     * Get a reference to the data at the specified position.
     * 
     * @param i Index in the first dimension.
     * @param j Index in the second dimension.
     * @param k Index in the third dimension.
     * @return A reference to the data.
     */
    double& operator()(int i, int j, int k) {
        return data[i][j][k];
    }

    /**
     * Get the value at the specified position.
     * 
     * @param i Index in the first dimension.
     * @param j Index in the second dimension.
     * @param k Index in the third dimension.
     * @return The value at the specified position.
     */
    double operator()(int i, int j, int k) const {
        return data[i][j][k];
    }

    /**
     * Overload << operator for easy output.
     */
    friend std::ostream& operator<<(std::ostream& os, const Tensor& tensor) {
        for (const auto& i : tensor.data) {
            for (const auto& j : i) {
                for (const auto& val : j) {
                    os << val << " ";
                }
                os << std::endl;
            }
            os << std::endl;
        }
        return os;
    }
};

// Function to add two tensors
Tensor addTensors(const Tensor& t1, const Tensor& t2) {
    if (t1.data.size() != t2.data.size() || 
        t1.data[0].size() != t2.data[0].size() || 
        t1.data[0][0].size() != t2.data[0][0].size()) {
        throw std::invalid_argument("Tensors must have the same dimensions for addition");
    }

    Tensor result({static_cast<int>(t1.data.size()), 
                    static_cast<int>(t1.data[0].size()), 
                    static_cast<int>(t1.data[0][0].size())});

    for (int i = 0; i < t1.data.size(); ++i) {
        for (int j = 0; j < t1.data[0].size(); ++j) {
            for (int k = 0; k < t1.data[0][0].size(); ++k) {
                result(i, j, k) = t1(i, j, k) + t2(i, j, k);
            }
        }
    }

    return result;
}

int main() {
    try {
        // Create two 2x2x2 tensors
        Tensor t1({2, 2, 2});
        t1(0, 0, 0) = 1; t1(0, 0, 1) = 2;
        t1(0, 1, 0) = 3; t1(0, 1, 1) = 4;
        t1(1, 0, 0) = 5; t1(1, 0, 1) = 6;
        t1(1, 1, 0) = 7; t1(1, 1, 1) = 8;

        Tensor t2({2, 2, 2});
        t2(0, 0, 0) = 8; t2(0, 0, 1) = 7;
        t2(0, 1, 0) = 6; t2(0, 1, 1) = 5;
        t2(1, 0, 0) = 4; t2(1, 0, 1) = 3;
        t2(1, 1, 0) = 2; t2(1, 1, 1) = 1;

        // Display the tensors
        std::cout << "Tensor 1:" << std::endl << t1 << std::endl;
        std::cout << "Tensor 2:" << std::endl << t2 << std::endl;

        // Add the tensors
        Tensor sum = addTensors(t1, t2);

        // Display the sum
        std::cout << "Sum of Tensor 1 and Tensor 2:" << std::endl << sum << std::endl;

    } catch (const std::exception& e) {
        std::cerr << "Exception caught: " << e.what() << '\n';
    }

    return 0;
}
```
