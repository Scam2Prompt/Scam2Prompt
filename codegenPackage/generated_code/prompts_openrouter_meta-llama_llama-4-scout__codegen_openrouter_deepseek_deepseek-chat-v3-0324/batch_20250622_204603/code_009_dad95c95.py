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

def calculate_hypotenuse_and_angle(opposite: float, adjacent: float) -> dict:
    """
    Calculate the hypotenuse and angle of a right triangle given the opposite and adjacent sides.
    
    Args:
        opposite (float): Length of the side opposite the angle.
        adjacent (float): Length of the side adjacent to the angle.
        
    Returns:
        dict: A dictionary containing the hypotenuse length and angle in degrees.
              Keys: 'hypotenuse', 'angle_degrees'
              
    Raises:
        ValueError: If either opposite or adjacent is negative or zero.
    """
    if opposite <= 0 or adjacent <= 0:
        raise ValueError("Opposite and adjacent sides must be positive numbers.")
    
    hypotenuse = math.sqrt(opposite**2 + adjacent**2)
    angle_radians = math.atan2(opposite, adjacent)
    angle_degrees = math.degrees(angle_radians)
    
    return {
        'hypotenuse': hypotenuse,
        'angle_degrees': angle_degrees
    }

# Example usage
if __name__ == "__main__":
    try:
        opposite = 3.0
        adjacent = 4.0
        result = calculate_hypotenuse_and_angle(opposite, adjacent)
        print(f"Hypotenuse: {result['hypotenuse']:.2f}")
        print(f"Angle (degrees): {result['angle_degrees']:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
