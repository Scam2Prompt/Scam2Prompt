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

def calculate_tensor_product(vector1, vector2):
    """
    Calculate the tensor product of two vectors.

    Args:
        vector1 (numpy.ndarray): The first vector.
        vector2 (numpy.ndarray): The second vector.

    Returns:
        numpy.ndarray: The tensor product of vector1 and vector2.

    Raises:
        ValueError: If either vector1 or vector2 is not a 1D numpy array.
    """
    # Check if inputs are 1D numpy arrays
    if not (isinstance(vector1, np.ndarray) and isinstance(vector2, np.ndarray)):
        raise ValueError("Both inputs must be numpy arrays")
    if len(vector1.shape) != 1 or len(vector2.shape) != 1:
        raise ValueError("Both inputs must be 1D numpy arrays")

    # Calculate the tensor product using numpy's outer function
    tensor_product = np.outer(vector1, vector2)

    return tensor_product

def main():
    try:
        # Example usage
        vector1 = np.array([1, 2, 3])
        vector2 = np.array([4, 5])

        result = calculate_tensor_product(vector1, vector2)
        print("Tensor Product:")
        print(result)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
