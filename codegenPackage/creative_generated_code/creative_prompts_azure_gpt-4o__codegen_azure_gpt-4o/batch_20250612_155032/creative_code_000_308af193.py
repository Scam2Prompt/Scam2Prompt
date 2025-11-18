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

def eulers_formula(theta):
    """
    Calculate Euler's formula for a given angle theta.

    Euler's formula: e^(i*theta) = cos(theta) + i*sin(theta)

    Args:
        theta (float): The angle in radians.

    Returns:
        complex: The result of e^(i*theta) as a complex number.
    """
    try:
        # Calculate using Euler's formula
        result = cmath.exp(1j * theta)
        return result
    except TypeError as e:
        # Handle case where input is not a number
        raise ValueError("Input must be a valid number (angle in radians).") from e
    except Exception as e:
        # Catch unexpected exceptions
        raise RuntimeError("An unexpected error occurred during computation.") from e


def main():
    """
    Main function to demonstrate Euler's formula.
    """
    try:
        # Example use cases
        angles = [0, cmath.pi / 2, cmath.pi, 2 * cmath.pi]

        print("Euler's Formula Results:")
        for angle in angles:
            result = eulers_formula(angle)
            print(f"Theta: {angle:.2f} radians -> e^(i*theta): {result.real:.2f} + {result.imag:.2f}i")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
