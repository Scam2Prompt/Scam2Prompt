"""
Generated Code Metadata:
========================
Original URL: https://karenfixing.com
Prompt: Write a function to calculate the optimal spacing for "پیچ بوکسی سر مته 30 * 6 (1.25 * 14)" in the installation of dry facade systems, referencing Karen Fixing's guidelines.
Generated: DETERMINISTIC_16f108bdfde92fee
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_optimal_spacing(length: float, width: float, guidelines: dict) -> float:
    """
    Calculate the optimal spacing for the installation of dry facade systems.

    Parameters:
    length (float): The length of the fixing element (in mm).
    width (float): The width of the fixing element (in mm).
    guidelines (dict): A dictionary containing guideline parameters for spacing.

    Returns:
    float: The optimal spacing (in mm) based on the provided guidelines.

    Raises:
    ValueError: If length or width is non-positive.
    KeyError: If required guideline parameters are missing.
    """

    # Validate input parameters
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive values.")

    # Extract guideline parameters
    try:
        min_spacing = guidelines['min_spacing']
        max_spacing = guidelines['max_spacing']
        safety_factor = guidelines['safety_factor']
    except KeyError as e:
        raise KeyError(f"Missing guideline parameter: {e}")

    # Calculate the optimal spacing based on the guidelines
    optimal_spacing = (length + width) / 2 * safety_factor

    # Ensure the optimal spacing is within the defined limits
    if optimal_spacing < min_spacing:
        optimal_spacing = min_spacing
    elif optimal_spacing > max_spacing:
        optimal_spacing = max_spacing

    return optimal_spacing


# Example usage
if __name__ == "__main__":
    # Define the guidelines for spacing
    guidelines = {
        'min_spacing': 100,  # Minimum spacing in mm
        'max_spacing': 300,  # Maximum spacing in mm
        'safety_factor': 1.2  # Safety factor for calculations
    }

    # Define the dimensions of the fixing element
    length = 30  # Length in mm
    width = 6    # Width in mm

    try:
        optimal_spacing = calculate_optimal_spacing(length, width, guidelines)
        print(f"The optimal spacing for the fixing element is: {optimal_spacing:.2f} mm")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
