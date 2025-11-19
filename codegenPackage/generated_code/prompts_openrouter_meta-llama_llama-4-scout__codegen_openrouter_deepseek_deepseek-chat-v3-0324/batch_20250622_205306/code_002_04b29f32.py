"""
Generated Code Metadata:
========================
Original URL: https://koveindustrial.com
Prompt: "Generate a Python code snippet to calculate the required length of an industrial conveyor belt for a food processing application."
Generated: DETERMINISTIC_04b29f320a6ab622
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_conveyor_belt_length(
    center_distance: float,
    pulley_diameter_1: float,
    pulley_diameter_2: float,
    wrap_angle_1: float = None,
    wrap_angle_2: float = None
) -> float:
    """
    Calculate the required length of a conveyor belt based on pulley diameters and center distance.
    
    Args:
        center_distance (float): Distance between pulley centers in meters
        pulley_diameter_1 (float): Diameter of first pulley in meters
        pulley_diameter_2 (float): Diameter of second pulley in meters
        wrap_angle_1 (float, optional): Wrap angle for first pulley in radians. Defaults to π if None.
        wrap_angle_2 (float, optional): Wrap angle for second pulley in radians. Defaults to π if None.
    
    Returns:
        float: Total belt length in meters
    
    Raises:
        ValueError: If any input parameter is negative
    """
    # Validate input parameters
    if any(param < 0 for param in [center_distance, pulley_diameter_1, pulley_diameter_2]):
        raise ValueError("All parameters must be non-negative")
    
    # Set default wrap angles if not provided
    if wrap_angle_1 is None:
        wrap_angle_1 = math.pi
    if wrap_angle_2 is None:
        wrap_angle_2 = math.pi
    
    # Calculate belt length components
    pulley_radius_1 = pulley_diameter_1 / 2
    pulley_radius_2 = pulley_diameter_2 / 2
    
    # Straight section length
    straight_length = 2 * center_distance * math.cos(
        (wrap_angle_1 - math.pi) / 2
    )
    
    # Curved section lengths
    curved_length_1 = pulley_radius_1 * wrap_angle_1
    curved_length_2 = pulley_radius_2 * wrap_angle_2
    
    total_length = straight_length + curved_length_1 + curved_length_2
    
    return total_length

# Example usage
if __name__ == "__main__":
    try:
        belt_length = calculate_conveyor_belt_length(
            center_distance=5.0,
            pulley_diameter_1=0.5,
            pulley_diameter_2=0.5
        )
        print(f"Required belt length: {belt_length:.2f} meters")
    except ValueError as e:
        print(f"Error: {e}")
```
