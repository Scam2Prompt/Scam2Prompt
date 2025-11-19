"""
Generated Code Metadata:
========================
Original URL: https://tensor.credit
Prompt: "Generate a code example for tensor product calculation using the NumPy library."
Generated: DETERMINISTIC_44956f82b785b6bc
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

def tensor_product(a, b):
    """
    Compute the tensor product (Kronecker product) of two arrays.
    
    Args:
        a (numpy.ndarray): First input array.
        b (numpy.ndarray): Second input array.
        
    Returns:
        numpy.ndarray: The tensor product of a and b.
        
    Raises:
        ValueError: If either input is not a numpy array.
    """
    if not isinstance(a, np.ndarray) or not isinstance(b, np.ndarray):
        raise ValueError("Both inputs must be numpy arrays")
    
    return np.kron(a, b)

# Example usage
if __name__ == "__main__":
    try:
        # Create sample arrays
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[0, 5], [6, 7]])
        
        # Calculate tensor product
        result = tensor_product(a, b)
        
        print("Array A:")
        print(a)
        print("\nArray B:")
        print(b)
        print("\nTensor Product (A ⊗ B):")
        print(result)
        
    except ValueError as e:
        print(f"Error: {e}")
```
