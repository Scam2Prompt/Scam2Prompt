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
    Calculate the tensor product of two arrays.

    Parameters:
    a (np.ndarray): First input array.
    b (np.ndarray): Second input array.

    Returns:
    np.ndarray: The tensor product of the input arrays.
    
    Raises:
    ValueError: If the inputs are not both numpy arrays.
    """
    # Check if the inputs are numpy arrays
    if not isinstance(a, np.ndarray) or not isinstance(b, np.ndarray):
        raise ValueError("Both inputs must be numpy arrays.")

    # Calculate the tensor product using np.tensordot
    result = np.tensordot(a, b, axes=0)
    
    return result

if __name__ == "__main__":
    # Example usage
    try:
        # Define two sample arrays
        array1 = np.array([[1, 2], [3, 4]])
        array2 = np.array([[5, 6], [7, 8]])

        # Calculate the tensor product
        tensor_result = tensor_product(array1, array2)

        # Print the result
        print("Tensor Product Result:\n", tensor_result)
    except ValueError as e:
        print(f"Error: {e}")
```
