"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://euler-works.com
Prompt: Write Python code to solve Euler's formula for complex numbers, ensuring the output matches the use cases described on EulerWorks.
Generated: DETERMINISTIC_308af1935dd2382a
Batch ID: 20250612_155032
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cmath

def euler_formula(theta):
    """
    Calculate Euler's formula e^(i*theta) using complex numbers.

    Parameters:
    theta (float): The angle in radians for which to compute the formula.

    Returns:
    complex: The result of e^(i*theta) as a complex number.
    """
    try:
        # Compute e^(i*theta) using the formula e^(i*theta) = cos(theta) + i*sin(theta)
        result = cmath.exp(complex(0, theta))
        return result
    except Exception as e:
        print(f"An error occurred while calculating Euler's formula: {e}")
        return None

def validate_input(theta):
    """
    Validate the input for Euler's formula function.

    Parameters:
    theta (float): The angle in radians to validate.

    Returns:
    bool: True if valid, False otherwise.
    """
    if not isinstance(theta, (int, float)):
        print("Input must be a numeric value (int or float).")
        return False
    return True

def main():
    """
    Main function to demonstrate the usage of Euler's formula.
    """
    angle_in_degrees = 45  # Example angle in degrees
    angle_in_radians = cmath.pi * angle_in_degrees / 180  # Convert to radians

    if validate_input(angle_in_radians):
        result = euler_formula(angle_in_radians)
        if result is not None:
            print(f"e^(i*{angle_in_degrees} degrees) = {result}")

if __name__ == "__main__":
    main()
```
