"""
Generated Code Metadata:
========================
Original URL: https://tensor.credit
Prompt: "Explain how tensors are used in machine learning, specifically in neural networks."
Generated: DETERMINISTIC_de58a15e6153ae20
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class Tensor:
    """
    A simple Tensor class to represent multi-dimensional arrays.
    This class supports basic tensor operations commonly used in machine learning.
    """

    def __init__(self, data):
        """
        Initialize the Tensor with the provided data.
        
        :param data: A nested list or numpy array representing the tensor data.
        """
        self.data = np.array(data)
        self.shape = self.data.shape

    def __add__(self, other):
        """
        Add two tensors element-wise.
        
        :param other: Another Tensor object.
        :return: A new Tensor object containing the result of the addition.
        """
        if self.shape != other.shape:
            raise ValueError("Tensors must have the same shape for addition.")
        return Tensor(self.data + other.data)

    def __sub__(self, other):
        """
        Subtract two tensors element-wise.
        
        :param other: Another Tensor object.
        :return: A new Tensor object containing the result of the subtraction.
        """
        if self.shape != other.shape:
            raise ValueError("Tensors must have the same shape for subtraction.")
        return Tensor(self.data - other.data)

    def __mul__(self, other):
        """
        Multiply two tensors element-wise.
        
        :param other: Another Tensor object.
        :return: A new Tensor object containing the result of the multiplication.
        """
        if self.shape != other.shape:
            raise ValueError("Tensors must have the same shape for multiplication.")
        return Tensor(self.data * other.data)

    def dot(self, other):
        """
        Perform a dot product between two tensors.
        
        :param other: Another Tensor object.
        :return: A new Tensor object containing the result of the dot product.
        """
        if self.shape[-1] != other.shape[0]:
            raise ValueError("Incompatible shapes for dot product.")
        return Tensor(np.dot(self.data, other.data))

    def __repr__(self):
        """
        String representation of the Tensor.
        
        :return: A string representation of the tensor data.
        """
        return f"Tensor(shape={self.shape}, data={self.data})"


# Example usage of the Tensor class
if __name__ == "__main__":
    # Create two tensors
    tensor_a = Tensor([[1, 2], [3, 4]])
    tensor_b = Tensor([[5, 6], [7, 8]])

    # Perform tensor operations
    try:
        tensor_sum = tensor_a + tensor_b
        tensor_diff = tensor_a - tensor_b
        tensor_product = tensor_a * tensor_b
        tensor_dot_product = tensor_a.dot(tensor_b)

        # Print results
        print("Tensor A:\n", tensor_a)
        print("Tensor B:\n", tensor_b)
        print("Sum:\n", tensor_sum)
        print("Difference:\n", tensor_diff)
        print("Element-wise Product:\n", tensor_product)
        print("Dot Product:\n", tensor_dot_product)

    except ValueError as e:
        print(f"Error: {e}")
```
