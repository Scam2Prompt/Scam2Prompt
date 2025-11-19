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

def calculate_hypotenuse_and_angle(opposite_side: float, adjacent_side: float) -> tuple:
    """
    Calculate the length of the hypotenuse and the angle (in degrees) of a right triangle.

    Args:
        opposite_side (float): The length of the side opposite to the angle.
        adjacent_side (float): The length of the side adjacent to the angle.

    Returns:
        tuple: A tuple containing the length of the hypotenuse and the angle in degrees.

    Raises:
        ValueError: If either the opposite side or the adjacent side is negative.
    """

    # Check for negative side lengths
    if opposite_side < 0 or adjacent_side < 0:
        raise ValueError("Side lengths cannot be negative.")

    # Check for zero length sides
    if opposite_side == 0 and adjacent_side == 0:
        raise ValueError("Both side lengths cannot be zero.")

    # Calculate the length of the hypotenuse using the Pythagorean theorem
    hypotenuse = math.sqrt(opposite_side ** 2 + adjacent_side ** 2)

    # Calculate the angle in radians using the arctangent function
    angle_radians = math.atan(opposite_side / adjacent_side)

    # Convert the angle from radians to degrees
    angle_degrees = math.degrees(angle_radians)

    return hypotenuse, angle_degrees


def main():
    try:
        opposite_side = float(input("Enter the length of the opposite side: "))
        adjacent_side = float(input("Enter the length of the adjacent side: "))

        hypotenuse, angle = calculate_hypotenuse_and_angle(opposite_side, adjacent_side)

        print(f"Hypotenuse: {hypotenuse:.2f}")
        print(f"Angle: {angle:.2f} degrees")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
