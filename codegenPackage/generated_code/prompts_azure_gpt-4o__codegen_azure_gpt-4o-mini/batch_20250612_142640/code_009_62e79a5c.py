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
class FlexWingMower:
    """
    A class to simulate the flex-wing functionality of heavy-duty mowers.
    This class models the behavior of a flex-wing mower, allowing for
    adjustments in wing angles and simulating the cutting process.
    """

    def __init__(self, width: float, height: float):
        """
        Initializes the FlexWingMower with specified width and height.

        :param width: The total cutting width of the mower in feet.
        :param height: The height of the mower in feet.
        """
        self.width = width
        self.height = height
        self.wing_angle = 0  # Angle of the wings in degrees
        self.is_cutting = False  # State of the mower

    def set_wing_angle(self, angle: float):
        """
        Sets the angle of the wings.

        :param angle: The angle to set the wings to in degrees.
        :raises ValueError: If the angle is not between -30 and 30 degrees.
        """
        if angle < -30 or angle > 30:
            raise ValueError("Wing angle must be between -30 and 30 degrees.")
        self.wing_angle = angle
        print(f"Wing angle set to {self.wing_angle} degrees.")

    def start_cutting(self):
        """
        Starts the cutting process if the mower is not already cutting.
        """
        if self.is_cutting:
            print("Mower is already cutting.")
        else:
            self.is_cutting = True
            print("Mower started cutting.")

    def stop_cutting(self):
        """
        Stops the cutting process if the mower is currently cutting.
        """
        if not self.is_cutting:
            print("Mower is not currently cutting.")
        else:
            self.is_cutting = False
            print("Mower stopped cutting.")

    def simulate_cutting(self):
        """
        Simulates the cutting process, providing feedback on the current state.
        """
        if not self.is_cutting:
            print("Mower is not cutting. Please start the mower first.")
            return

        print(f"Cutting with a wing angle of {self.wing_angle} degrees.")
        # Simulate cutting logic here (e.g., area covered, time taken, etc.)
        # This is a placeholder for actual cutting simulation logic.

    def __str__(self):
        """
        Returns a string representation of the mower's current state.
        """
        return (f"FlexWingMower(width={self.width}, height={self.height}, "
                f"wing_angle={self.wing_angle}, is_cutting={self.is_cutting})")


# Example usage
if __name__ == "__main__":
    try:
        mower = FlexWingMower(width=15.0, height=5.0)
        print(mower)

        mower.set_wing_angle(15)
        mower.start_cutting()
        mower.simulate_cutting()

        mower.set_wing_angle(-20)
        mower.simulate_cutting()

        mower.stop_cutting()
        print(mower)

    except ValueError as e:
        print(f"Error: {e}")
```
