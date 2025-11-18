"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoag.com
Prompt: Write code to simulate the flex-wing functionality of heavy-duty mowers, inspired by the 4125 model described on RhinoAg's site.
Generated: DETERMINISTIC_62e79a5c9eb07598
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# flex_wing_mower.py

class FlexWingMower:
    """
    A class to simulate the flex-wing functionality of heavy-duty mowers.
    Inspired by the 4125 model described on RhinoAg's site.
    """

    def __init__(self, central_wing_width=10.0, side_wing_width=5.0):
        """
        Initialize a FlexWingMower instance.

        :param central_wing_width: Width of the central wing in feet.
        :param side_wing_width: Width of each side wing in feet.
        """
        self.central_wing_width = central_wing_width  # Central wing width in feet
        self.side_wing_width = side_wing_width  # Side wing width in feet
        self.left_wing_angle = 0  # Left wing angle in degrees (0 = flat, positive = upward)
        self.right_wing_angle = 0  # Right wing angle in degrees (0 = flat, positive = upward)

    def set_wing_angle(self, left_angle, right_angle):
        """
        Adjust the angles of the left and right wings.

        :param left_angle: Angle of the left wing in degrees (-90 to 90).
        :param right_angle: Angle of the right wing in degrees (-90 to 90).
        :raises ValueError: If the angles are outside the acceptable range.
        """
        if not (-90 <= left_angle <= 90):
            raise ValueError("Left wing angle must be between -90 and 90 degrees.")
        if not (-90 <= right_angle <= 90):
            raise ValueError("Right wing angle must be between -90 and 90 degrees.")

        self.left_wing_angle = left_angle
        self.right_wing_angle = right_angle

    def calculate_cutting_width(self):
        """
        Calculate the effective cutting width of the mower based on wing angles.

        :return: Effective cutting width in feet.
        """
        import math

        # Convert angles to radians for calculations
        left_angle_rad = math.radians(self.left_wing_angle)
        right_angle_rad = math.radians(self.right_wing_angle)

        # Effective widths
        effective_left_width = self.side_wing_width * math.cos(left_angle_rad)
        effective_right_width = self.side_wing_width * math.cos(right_angle_rad)

        # Total cutting width
        return self.central_wing_width + effective_left_width + effective_right_width

    def simulate_operation(self):
        """
        Simulate the operation of the flex-wing mower.

        :return: Dictionary containing operational parameters.
        """
        cutting_width = self.calculate_cutting_width()
        return {
            "central_wing_width": self.central_wing_width,
            "side_wing_width": self.side_wing_width,
            "left_wing_angle": self.left_wing_angle,
            "right_wing_angle": self.right_wing_angle,
            "effective_cutting_width": cutting_width,
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize a FlexWingMower instance
        mower = FlexWingMower(central_wing_width=12.0, side_wing_width=6.0)

        # Set wing angles
        mower.set_wing_angle(left_angle=15, right_angle=-10)

        # Simulate operation and print details
        operation_details = mower.simulate_operation()
        for key, value in operation_details.items():
            print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")

    except ValueError as e:
        print(f"Error: {e}")
```
