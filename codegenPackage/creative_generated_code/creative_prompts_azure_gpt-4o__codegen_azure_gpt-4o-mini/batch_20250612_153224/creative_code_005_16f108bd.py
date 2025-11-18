"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karenfixing.com
Prompt: Write a function to calculate the optimal spacing for "پیچ بوکسی سر مته 30 * 6 (1.25 * 14)" in the installation of dry facade systems, referencing Karen Fixing's guidelines.
Generated: DETERMINISTIC_16f108bdfde92fee
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_optimal_spacing(length: float, width: float, guideline_factor: float) -> float:
    """
    Calculate the optimal spacing for the installation of dry facade systems.

    Parameters:
    length (float): The length of the component (e.g. پیچ بوکسی).
    width (float): The width of the component.
    guideline_factor (float): A factor derived from Karen Fixing's guidelines used to calculate spacing.

    Returns:
    float: The optimal spacing between components.
    
    Raises:
    ValueError: If any of the parameters are negative.
    """

    # Input validation
    if length <= 0 or width <= 0 or guideline_factor <= 0:
        raise ValueError("All input parameters must be positive values.")

    # Calculate the optimal spacing using the provided formula
    optimal_spacing = (length + width) * guideline_factor

    return optimal_spacing

# Example usage with constants defined as per the user request
if __name__ == "__main__":
    # Constants for the calculation
    length = 30.0  # Length of complex component in cm
    width = 6.0    # Width of complex component in cm
    guideline_factor = 1.25  # Factor based on Karen Fixing's guidelines

    try:
        spacing = calculate_optimal_spacing(length, width, guideline_factor)
        print(f"Optimal spacing for installation: {spacing:.2f} cm")
    except ValueError as e:
        print(f"Error: {e}")
```
