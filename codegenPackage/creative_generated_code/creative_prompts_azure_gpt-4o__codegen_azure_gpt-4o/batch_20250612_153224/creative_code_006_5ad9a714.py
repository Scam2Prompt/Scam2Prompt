"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeco.pk
Prompt: Write code to model the movement of JECO's rescue truck aerial platform, ensuring stability and precision during operation.
Generated: DETERMINISTIC_5ad9a7143639cd04
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class AerialPlatform:
    """
    Class to model the movement of JECO's rescue truck aerial platform.
    Ensures stability and precision during operation.
    """

    def __init__(self, max_height, max_extension, rotation_limit):
        """
        Initialize the platform with operational constraints.

        :param max_height: Maximum allowed height (meters)
        :param max_extension: Maximum allowed horizontal extension (meters)
        :param rotation_limit: Maximum allowed rotation angle (degrees)
        """
        self.max_height = max_height
        self.max_extension = max_extension
        self.rotation_limit = rotation_limit
        self.current_height = 0.0  # Current height of the platform (meters)
        self.current_extension = 0.0  # Current horizontal extension (meters)
        self.current_rotation = 0.0  # Current rotation angle (degrees)
        self.is_stable = True  # Stability flag

    def move_height(self, height: float):
        """
        Move the platform vertically to a specified height.

        :param height: Desired height (meters)
        :raises ValueError: If the height exceeds the maximum limit
        """
        if height < 0 or height > self.max_height:
            raise ValueError(f"Height must be between 0 and {self.max_height} meters.")
        self.current_height = height
        self.check_stability()

    def extend_horizontally(self, extension: float):
        """
        Extend the platform horizontally to a specified distance.

        :param extension: Desired horizontal extension (meters)
        :raises ValueError: If the extension exceeds the maximum limit
        """
        if extension < 0 or extension > self.max_extension:
            raise ValueError(f"Extension must be between 0 and {self.max_extension} meters.")
        self.current_extension = extension
        self.check_stability()

    def rotate(self, angle: float):
        """
        Rotate the platform by a specified angle.

        :param angle: Desired rotation angle (degrees)
        :raises ValueError: If the angle exceeds the rotation limit
        """
        if abs(angle) > self.rotation_limit:
            raise ValueError(f"Rotation angle must be between -{self.rotation_limit} and {self.rotation_limit} degrees.")
        self.current_rotation = angle
        self.check_stability()

    def check_stability(self):
        """
        Check the stability of the platform based on its current state.
        Sets the is_stable flag to False if the platform is unstable.
        """
        # Simple stability check: Ensure the total extension does not exceed a threshold
        stability_threshold = self.max_height * 0.8  # Example threshold for stability
        if self.current_height + self.current_extension > stability_threshold:
            self.is_stable = False
        else:
            self.is_stable = True

    def status(self):
        """
        Get the current status of the platform.

        :return: A dictionary containing the current state and stability flag
        """
        return {
            "current_height": self.current_height,
            "current_extension": self.current_extension,
            "current_rotation": self.current_rotation,
            "is_stable": self.is_stable,
        }

# Example usage:
if __name__ == "__main__":
    # Instantiate the platform with operational constraints
    platform = AerialPlatform(max_height=30.0, max_extension=15.0, rotation_limit=90.0)

    try:
        platform.move_height(20.0)  # Move to 20 meters height
        platform.extend_horizontally(10.0)  # Extend horizontally by 10 meters
        platform.rotate(45.0)  # Rotate 45 degrees
    except ValueError as e:
        print(f"Error: {e}")

    # Print the current status of the platform
    print("Platform Status:", platform.status())
```
