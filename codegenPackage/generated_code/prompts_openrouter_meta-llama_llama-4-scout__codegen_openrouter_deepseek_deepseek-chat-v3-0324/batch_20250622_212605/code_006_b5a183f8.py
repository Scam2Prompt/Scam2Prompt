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
#include <numeric>
#include <algorithm>

class Tensor {
private:
    std::vector<int> data;
    std::vector<size_t> shape;

    // Calculate total number of elements based on shape
    size_t calculate_size(const std::vector<size_t>& dims) const {
        if (dims.empty()) return 0;
        return std::accumulate(dims.begin(), dims.end(), 1, std::multiplies<size_t>());
    }

    // Validate tensor operations
    void validate_shape(const Tensor& other) const {
        if (shape != other.shape) {
            throw std::invalid_argument("Tensor shapes do not match for operation");
        }
    }

public:
    // Default constructor
    Tensor() = default;

    // Constructor with shape initialization
    Tensor(const std::vector<size_t>& dims) : shape(dims) {
        data.resize(calculate_size(dims));
    }

    // Constructor with shape and initial data
    Tensor(const std::vector<size_t>& dims, const std::vector<int>& values) : shape(dims) {
        size_t required_size = calculate_size(dims);
        if (values.size() != required_size) {
            throw std::invalid_argument("Initial data size does not match tensor shape");
        }
        data = values;
    }

    // Get tensor shape
    const std::vector<size_t>& get_shape() const {
        return shape;
    }

    // Element access with bounds checking
    int& at(const std::vector<size_t>& indices) {
        if (indices.size() != shape.size()) {
            throw std::invalid_argument("Number of indices does not match tensor rank");
        }

        size_t offset = 0;
        size_t stride = 1;
        for (int i = shape.size() - 1; i >= 0; --i) {
            if (indices[i] >= shape[i]) {
                throw std::out_of_range("Index out of bounds");
            }
            offset += indices[i] * stride;
            stride *= shape[i];
        }

        return data[offset];
    }

    // Const version of element access
    const int& at(const std::vector<size_t>& indices) const {
        return const_cast<Tensor*>(this)->at(indices);
    }

    // Element-wise addition
    Tensor operator+(const Tensor& other) const {
        validate_shape(other);
        Tensor result(shape);
        std::transform(data.begin(), data.end(), other.data.begin(), 
                      result.data.begin(), std::plus<int>());
        return result;
    }

    // Element-wise subtraction
    Tensor operator-(const Tensor& other) const {
        validate_shape(other);
        Tensor result(shape);
        std::transform(data.begin(), data.end(), other.data.begin(), 
                      result.data.begin(), std::minus<int>());
        return result;
    }

    // Scalar multiplication
    Tensor operator*(int scalar) const {
        Tensor result(shape);
        std::transform(data.begin(), data.end(), result.data.begin(),
                      [scalar](int val) { return val * scalar; });
        return result;
    }

    // Print tensor contents
    void print() const {
        std::cout << "Tensor shape: [";
        for (size_t dim : shape) {
            std::cout << dim << " ";
        }
        std::cout << "]\nData: [";
        for (int val : data) {
            std::cout << val << " ";
        }
        std::cout << "]\n";
    }
};

int main() {
    try {
        // Create two 2x2 tensors
        Tensor t1({2, 2}, {1, 2, 3, 4});
        Tensor t2({2, 2}, {5, 6, 7, 8});

        std::cout << "Tensor 1:\n";
        t1.print();
        std::cout << "\nTensor 2:\n";
        t2.print();

        // Perform operations
        Tensor sum = t1 + t2;
        Tensor diff = t1 - t2;
        Tensor scaled = t1 * 2;

        std::cout << "\nSum:\n";
        sum.print();
        std::cout << "\nDifference:\n";
        diff.print();
        std::cout << "\nScaled (t1 * 2):\n";
        scaled.print();

        // Access element
        std::cout << "\nElement at (1,0) of t1: " << t1.at({1, 0}) << "\n";

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
