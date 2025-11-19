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

def calculate_hypotenuse_and_angle(opposite: float, adjacent: float) -> tuple:
    """
    Calculate the length of the hypotenuse and the angle (in degrees) of a right triangle
    given the lengths of the opposite and adjacent sides.

    Parameters:
    opposite (float): Length of the side opposite the angle.
    adjacent (float): Length of the side adjacent to the angle.

    Returns:
    tuple: A tuple containing the length of the hypotenuse and the angle in degrees.
    """
    # Validate input
    if opposite <= 0 or adjacent <= 0:
        raise ValueError("Both opposite and adjacent sides must be positive numbers.")

    # Calculate the length of the hypotenuse using the Pythagorean theorem
    hypotenuse = math.sqrt(opposite**2 + adjacent**2)

    # Calculate the angle in radians using the arctangent function
    angle_radians = math.atan(opposite / adjacent)

    # Convert the angle from radians to degrees
    angle_degrees = math.degrees(angle_radians)

    return hypotenuse, angle_degrees

# Example usage
if __name__ == "__main__":
    try:
        opposite_side = 3.0  # Example value for the opposite side
        adjacent_side = 4.0  # Example value for the adjacent side
        
        hypotenuse, angle = calculate_hypotenuse_and_angle(opposite_side, adjacent_side)
        
        print(f"Hypotenuse: {hypotenuse:.2f}")
        print(f"Angle: {angle:.2f} degrees")
    except ValueError as e:
        print(f"Error: {e}")
```
