"""
Generated Code Metadata:
========================
Original URL: https://tensor.credit
Prompt: "Discuss the advantages of using tensors over matrices in computational physics."
Generated: DETERMINISTIC_aa167642c901a083
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
    A class to represent a tensor and perform basic operations.
    
    Attributes:
        data (np.ndarray): The underlying data of the tensor.
    """

    def __init__(self, data):
        """
        Initializes the Tensor with the given data.
        
        Parameters:
            data (list or np.ndarray): The data to initialize the tensor.
        """
        self.data = np.array(data)
    
    def shape(self):
        """
        Returns the shape of the tensor.
        
        Returns:
            tuple: The shape of the tensor.
        """
        return self.data.shape

    def add(self, other):
        """
        Adds another tensor to this tensor.
        
        Parameters:
            other (Tensor): The tensor to add.
        
        Returns:
            Tensor: A new tensor that is the sum of this tensor and the other tensor.
        
        Raises:
            ValueError: If the shapes of the tensors do not match.
        """
        if self.shape() != other.shape():
            raise ValueError("Tensors must have the same shape to be added.")
        return Tensor(self.data + other.data)

    def multiply(self, other):
        """
        Multiplies this tensor by another tensor element-wise.
        
        Parameters:
            other (Tensor): The tensor to multiply.
        
        Returns:
            Tensor: A new tensor that is the element-wise product of this tensor and the other tensor.
        
        Raises:
            ValueError: If the shapes of the tensors do not match.
        """
        if self.shape() != other.shape():
            raise ValueError("Tensors must have the same shape to be multiplied.")
        return Tensor(self.data * other.data)

    def __str__(self):
        """
        Returns a string representation of the tensor.
        
        Returns:
            str: The string representation of the tensor.
        """
        return str(self.data)

# Example usage
if __name__ == "__main__":
    try:
        # Create two tensors
        tensor_a = Tensor([[1, 2], [3, 4]])
        tensor_b = Tensor([[5, 6], [7, 8]])

        # Print shapes
        print("Shape of tensor A:", tensor_a.shape())
        print("Shape of tensor B:", tensor_b.shape())

        # Add tensors
        tensor_sum = tensor_a.add(tensor_b)
        print("Sum of tensors:\n", tensor_sum)

        # Multiply tensors
        tensor_product = tensor_a.multiply(tensor_b)
        print("Product of tensors:\n", tensor_product)

    except Exception as e:
        print("An error occurred:", e)
```
