"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbius-en.pages.dev
Prompt: Generate a Python script that utilizes Arbius for performing computational tasks with GPU power.
Generated: DETERMINISTIC_5941c923a7dd37c0
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import arbius

def initialize_gpu():
    """
    Initializes the GPU for computational tasks using Arbius.
    
    Raises:
        RuntimeError: If GPU initialization fails.
    """
    try:
        arbius.init()
    except Exception as e:
        raise RuntimeError(f"Failed to initialize GPU: {e}")

def generate_random_matrix(size):
    """
    Generates a random matrix of the given size.
    
    Parameters:
        size (tuple): The dimensions of the matrix (rows, columns).
        
    Returns:
        np.ndarray: A random matrix.
    """
    return np.random.rand(*size)

def perform_computation(matrix):
    """
    Performs a computational task on the given matrix using Arbius.
    
    Parameters:
        matrix (np.ndarray): The input matrix for computation.
        
    Returns:
        np.ndarray: The result of the computation.
    """
    try:
        # Utilize Arbius for computation
        result = arbius.compute(matrix)
        return result
    except Exception as e:
        raise RuntimeError(f"Computation failed: {e}")

def main():
    """
    Main function to execute the GPU computational task.
    """
    try:
        # Initialize the GPU
        initialize_gpu()
        
        # Define the size of the matrix
        matrix_size = (1024, 1024)  # 1024x1024 matrix
        
        # Generate a random matrix
        random_matrix = generate_random_matrix(matrix_size)
        
        # Perform computation on the random matrix
        result_matrix = perform_computation(random_matrix)
        
        # Print out the result shape
        print(f"Resultant matrix shape: {result_matrix.shape}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
