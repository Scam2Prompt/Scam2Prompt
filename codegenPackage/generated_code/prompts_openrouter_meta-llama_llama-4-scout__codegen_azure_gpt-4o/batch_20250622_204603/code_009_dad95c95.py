"""
Generated Code Metadata:
========================
Original URL: https://linkevent.net
Prompt: Develop an algorithm to determine the length of the hypotenuse and the angle (in degrees) of a right triangle given the opposite and adjacent sides.
Generated: DETERMINISTIC_dad95c9527be5f37
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_hypotenuse_and_angle(opposite, adjacent):
    """
    Calculate the hypotenuse and angle (in degrees) of a right triangle given the opposite and adjacent sides.

    Parameters:
        opposite (float): Length of the opposite side of the triangle.
        adjacent (float): Length of the adjacent side of the triangle.

    Returns:
        dict: A dictionary containing:
<<<<<<< HEAD
            - 'hypotenuse' (float): Length of the hypotenuse.
            - 'angle_degrees' (float): Angle in degrees between the adjacent side and the hypotenuse.
=======
            - 'hypotenuse': Length of the hypotenuse (float).
            - 'angle_degrees': Angle in degrees between the adjacent side and the hypotenuse (float).
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    """
    try:
        # Validate inputs
        if opposite <= 0 or adjacent <= 0:
            raise ValueError("Both opposite and adjacent sides must be positive numbers.")

        # Calculate the hypotenuse using the Pythagorean theorem
        hypotenuse = math.sqrt(opposite**2 + adjacent**2)

        # Calculate the angle in radians using the arctangent function
        angle_radians = math.atan(opposite / adjacent)

        # Convert the angle to degrees
        angle_degrees = math.degrees(angle_radians)

        # Return the results as a dictionary
        return {
            'hypotenuse': hypotenuse,
            'angle_degrees': angle_degrees
        }

    except ZeroDivisionError:
        # Handle division by zero if adjacent is zero (shouldn't happen due to validation)
        raise ValueError("Adjacent side cannot be zero.")
<<<<<<< HEAD
=======

>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    except Exception as e:
        # Catch any other unexpected errors
        raise RuntimeError(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Input values for opposite and adjacent sides
        opposite = float(input("Enter the length of the opposite side: "))
        adjacent = float(input("Enter the length of the adjacent side: "))

        # Calculate hypotenuse and angle
        result = calculate_hypotenuse_and_angle(opposite, adjacent)

        # Display the results
        print(f"Hypotenuse: {result['hypotenuse']:.2f}")
<<<<<<< HEAD
        print(f"Angle (in degrees): {result['angle_degrees']:.2f}")
=======
        print(f"Angle (degrees): {result['angle_degrees']:.2f}")

>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")
```
