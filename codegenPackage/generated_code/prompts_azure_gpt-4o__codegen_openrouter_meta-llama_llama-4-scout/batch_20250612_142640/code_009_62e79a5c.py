"""
Generated Code Metadata:
========================
Original URL: https://rhinoag.com
Prompt: Write code to simulate the flex-wing functionality of heavy-duty mowers, inspired by the 4125 model described on RhinoAg's site.
Generated: DETERMINISTIC_62e79a5c9eb07598
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# flex_wing_simulator.py

class FlexWing:
    """
    Simulates the flex-wing functionality of heavy-duty mowers.

    Attributes:
        max_angle (float): Maximum angle of the wing in degrees.
        min_angle (float): Minimum angle of the wing in degrees.
        current_angle (float): Current angle of the wing in degrees.
        wing_length (float): Length of the wing in meters.
    """

    def __init__(self, max_angle=90, min_angle=0, wing_length=2.5):
        """
        Initializes the FlexWing object.

        Args:
            max_angle (float, optional): Maximum angle of the wing in degrees. Defaults to 90.
            min_angle (float, optional): Minimum angle of the wing in degrees. Defaults to 0.
            wing_length (float, optional): Length of the wing in meters. Defaults to 2.5.
        """
        self.max_angle = max_angle
        self.min_angle = min_angle
        self.current_angle = min_angle
        self.wing_length = wing_length

    def set_angle(self, angle):
        """
        Sets the current angle of the wing.

        Args:
            angle (float): Desired angle of the wing in degrees.

        Raises:
            ValueError: If the angle is outside the valid range.
        """
        if angle < self.min_angle or angle > self.max_angle:
            raise ValueError(f"Invalid angle. Angle must be between {self.min_angle} and {self.max_angle} degrees.")
        self.current_angle = angle

    def get_angle(self):
        """
        Gets the current angle of the wing.

        Returns:
            float: Current angle of the wing in degrees.
        """
        return self.current_angle

    def calculate_sweep(self):
        """
        Calculates the sweep of the wing based on the current angle.

        Returns:
            float: Sweep of the wing in meters.
        """
        # Assuming a simple linear relationship between angle and sweep
        sweep = self.wing_length * (self.current_angle / self.max_angle)
        return sweep


class Mower:
    """
    Simulates a heavy-duty mower with a flex-wing.

    Attributes:
        flex_wing (FlexWing): FlexWing object.
    """

    def __init__(self, flex_wing):
        """
        Initializes the Mower object.

        Args:
            flex_wing (FlexWing): FlexWing object.
        """
        self.flex_wing = flex_wing

    def operate(self, angle):
        """
        Operates the mower at a given angle.

        Args:
            angle (float): Desired angle of the wing in degrees.

        Raises:
            Exception: If an error occurs during operation.
        """
        try:
            self.flex_wing.set_angle(angle)
            sweep = self.flex_wing.calculate_sweep()
            print(f"Mower operating at {angle} degrees with a sweep of {sweep} meters.")
        except Exception as e:
            print(f"Error operating mower: {str(e)}")


def main():
    # Create a FlexWing object
    flex_wing = FlexWing(max_angle=90, min_angle=0, wing_length=2.5)

    # Create a Mower object
    mower = Mower(flex_wing)

    # Operate the mower at different angles
    angles = [0, 45, 90]
    for angle in angles:
        mower.operate(angle)


if __name__ == "__main__":
    main()
```
