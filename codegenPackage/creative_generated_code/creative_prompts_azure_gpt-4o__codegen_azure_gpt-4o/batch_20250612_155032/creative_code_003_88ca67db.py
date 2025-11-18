"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://euler-works.com
Prompt: Create a function to visualize Euler's identity in Python, using methods or examples similar to those on EulerWorks.
Generated: DETERMINISTIC_88ca67dbec7fb48d
Batch ID: 20250612_155032
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np

def visualize_eulers_identity():
    """
    Visualizes Euler's Identity: e^(i*pi) + 1 = 0 on the complex plane.
    
    Euler's Identity is one of the most beautiful equations in mathematics, 
    demonstrating the deep relationship between exponential functions, imaginary numbers, 
    and fundamental constants (e, i, pi).
    """
    try:
        # Define the range of theta values (angle in radians)
        theta = np.linspace(0, np.pi, 500)  # From 0 to pi
        
        # Calculate e^(i*theta)
        e_i_theta = np.exp(1j * theta)  # Complex exponential using NumPy
        
        # Extract real and imaginary parts for visualization
        real_part = e_i_theta.real
        imag_part = e_i_theta.imag
        
        # Create the plot
        plt.figure(figsize=(8, 8))
        plt.plot(real_part, imag_part, label=r'$e^{i\theta}$', color='blue')
        plt.scatter([-1], [0], color='red', label=r'$e^{i\pi}$ = -1 (Euler\'s Identity)')
        
        # Add annotations
        plt.title("Visualization of Euler's Identity: $e^{i\pi} + 1 = 0$", fontsize=14)
        plt.xlabel("Real Part", fontsize=12)
        plt.ylabel("Imaginary Part", fontsize=12)
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
        
        # Add legend
        plt.legend(fontsize=12)
        
        # Ensure equal aspect ratio for proper visualization of the complex plane
        plt.axis('equal')
        
        # Show plot
        plt.show()
    
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred while visualizing Euler's Identity: {e}")

# Execute the function
visualize_eulers_identity()
```
