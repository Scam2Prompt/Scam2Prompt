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
#include <initializer_list>

// Tensor class definition
template <typename T>
class Tensor {
public:
    // Constructor for creating a tensor with given dimensions
    Tensor(std::initializer_list<size_t> dims) {
        for (auto dim : dims) {
            dimensions.push_back(dim);
            totalSize *= dim;
        }
        data.resize(totalSize);
    }

    // Access element at specified indices
    T& operator()(std::initializer_list<size_t> indices) {
        size_t index = calculateIndex(indices);
        return data.at(index);
    }

    // Get the dimensions of the tensor
    const std::vector<size_t>& getDimensions() const {
        return dimensions;
    }

    // Get the total number of elements in the tensor
    size_t size() const {
        return totalSize;
    }

private:
    std::vector<T> data;          // Storage for tensor data
    std::vector<size_t> dimensions; // Dimensions of the tensor
    size_t totalSize = 1;        // Total number of elements

    // Calculate the linear index from multi-dimensional indices
    size_t calculateIndex(std::initializer_list<size_t> indices) const {
        if (indices.size() != dimensions.size()) {
            throw std::out_of_range("Number of indices does not match tensor dimensions.");
        }

        size_t index = 0;
        size_t stride = 1;

        auto it = indices.end();
        for (size_t i = 0; i < dimensions.size(); ++i) {
            --it;
            if (*it >= dimensions[i]) {
                throw std::out_of_range("Index out of bounds for dimension " + std::to_string(i));
            }
            index += (*it) * stride;
            stride *= dimensions[i];
        }
        return index;
    }
};

// Example usage of the Tensor class
int main() {
    try {
        // Create a 2x3 tensor
        Tensor<int> tensor = {2, 3};

        // Assign values to the tensor
        for (size_t i = 0; i < 2; ++i) {
            for (size_t j = 0; j < 3; ++j) {
                tensor({i, j}) = i * 3 + j; // Fill with some values
            }
        }

        // Print the tensor values
        for (size_t i = 0; i < 2; ++i) {
            for (size_t j = 0; j < 3; ++j) {
                std::cout << tensor({i, j}) << " ";
            }
            std::cout << std::endl;
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
