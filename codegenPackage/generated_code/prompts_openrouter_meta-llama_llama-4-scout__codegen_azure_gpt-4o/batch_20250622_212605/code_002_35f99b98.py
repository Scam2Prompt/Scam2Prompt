"""
Generated Code Metadata:
========================
Original URL: https://tensor.credit
Prompt: "Write a code snippet to convert a numpy array to a tensor in PyTorch."
Generated: DETERMINISTIC_35f99b98a00b53cf
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
import torch

def numpy_to_tensor(np_array):
    """
    Converts a NumPy array to a PyTorch tensor.

    Args:
        np_array (numpy.ndarray): The input NumPy array.

    Returns:
        torch.Tensor: The converted PyTorch tensor.
    """
    try:
        # Ensure the input is a NumPy array
        if not isinstance(np_array, np.ndarray):
            raise TypeError("Input must be a NumPy array.")

        # Convert the NumPy array to a PyTorch tensor
        tensor = torch.from_numpy(np_array)

        # Return the tensor
        return tensor
    except TypeError as e:
        # Handle type errors
        print(f"TypeError: {e}")
        raise
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An error occurred: {e}")
        raise

# Example usage:
if __name__ == "__main__":
    # Create a sample NumPy array
    np_array = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)

    # Convert the NumPy array to a PyTorch tensor
    tensor = numpy_to_tensor(np_array)

    # Print the resulting tensor
    print("Converted Tensor:")
    print(tensor)
```
