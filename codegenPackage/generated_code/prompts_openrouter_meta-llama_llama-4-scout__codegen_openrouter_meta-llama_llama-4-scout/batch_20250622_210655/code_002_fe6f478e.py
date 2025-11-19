"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Write a Python code snippet to calculate the volume of soil excavated by a Yanmar SV100 mini excavator given its bucket volume and excavation depth.
Generated: DETERMINISTIC_fe6f478e0b88c0f8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates the volume of soil excavated by a Yanmar SV100 mini excavator.

Given the bucket volume and excavation depth, this script provides the total volume of soil excavated.
"""

def calculate_excavated_volume(bucket_volume, excavation_depth, swing_angle=180):
    """
    Calculates the volume of soil excavated.

    Args:
        bucket_volume (float): The volume of the excavator's bucket in cubic meters (m³).
        excavation_depth (float): The depth of excavation in meters (m).
        swing_angle (float, optional): The swing angle of the excavator in degrees. Defaults to 180.

    Returns:
        float: The total volume of soil excavated in cubic meters (m³).

    Raises:
        ValueError: If bucket volume or excavation depth is not a positive number.
    """
    if bucket_volume <= 0 or excavation_depth <= 0:
        raise ValueError("Bucket volume and excavation depth must be positive numbers.")

    # Convert swing angle from degrees to radians for calculation
    swing_angle_rad = swing_angle * (3.14159 / 180)

    # Calculate the excavated volume using the formula: V = B * D * (θ / 360)
    excavated_volume = bucket_volume * excavation_depth * (swing_angle / 360)

    return excavated_volume


def main():
    try:
        bucket_volume = float(input("Enter the bucket volume (m³): "))
        excavation_depth = float(input("Enter the excavation depth (m): "))
        swing_angle = float(input("Enter the swing angle (degrees), default is 180: ") or 180)

        excavated_volume = calculate_excavated_volume(bucket_volume, excavation_depth, swing_angle)
        print(f"The total volume of soil excavated is: {excavated_volume:.2f} m³")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
