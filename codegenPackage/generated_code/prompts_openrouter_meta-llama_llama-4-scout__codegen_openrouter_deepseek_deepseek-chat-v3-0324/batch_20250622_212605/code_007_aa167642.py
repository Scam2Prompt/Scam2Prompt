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
# This script demonstrates the advantages of using tensors over matrices in computational physics
# through practical examples and comparisons.

import numpy as np
import torch

def tensor_vs_matrix_comparison():
    """
    Demonstrates key advantages of tensors over matrices in computational physics:
    1. Higher dimensionality support
    2. Better handling of complex operations
    3. GPU acceleration support
    4. Automatic differentiation capabilities
    """
    
    # Example 1: Higher dimensionality
    print("Example 1: Higher Dimensionality")
    matrix_2d = np.random.rand(3, 3)  # Regular 2D matrix
    tensor_3d = torch.rand(3, 3, 3)   # 3D tensor
    
    print(f"Matrix shape: {matrix_2d.shape}")
    print(f"Tensor shape: {tensor_3d.shape}\n")
    
    # Example 2: Complex operations
    print("Example 2: Complex Operations")
    tensor_a = torch.rand(2, 3, 4)
    tensor_b = torch.rand(2, 4, 3)
    
    # Tensor contraction (generalized matrix multiplication)
    tensor_result = torch.einsum('ijk,ikl->ijl', tensor_a, tensor_b)
    print(f"Tensor contraction result shape: {tensor_result.shape}\n")
    
    # Example 3: GPU acceleration
    print("Example 3: GPU Acceleration")
    if torch.cuda.is_available():
        cuda_tensor = tensor_a.cuda()
        print(f"Tensor moved to GPU: {cuda_tensor.device}\n")
    else:
        print("GPU not available, skipping GPU example\n")
    
    # Example 4: Automatic differentiation
    print("Example 4: Automatic Differentiation")
    x = torch.tensor(2.0, requires_grad=True)
    y = x**3 + 2*x + 1
    y.backward()
    print(f"Derivative of y = x³ + 2x + 1 at x=2: {x.grad}\n")

def main():
    try:
        print("=== Tensor vs Matrix in Computational Physics ===")
        tensor_vs_matrix_comparison()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
