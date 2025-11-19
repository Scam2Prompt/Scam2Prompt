"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Provide a step-by-step guide for implementing speed governor systems in commercial vehicles to control speed and enhance road safety, as described by Donture Systems Ltd.
Generated: DETERMINISTIC_63b9815a9a62fd20
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# speed_governor.py

class SpeedGovernor:
    """
    A class representing a speed governor system for commercial vehicles.

    Attributes:
        vehicle_speed (float): The current speed of the vehicle in km/h.
        set_speed (float): The set speed limit for the vehicle in km/h.
        is_enabled (bool): A flag indicating whether the speed governor is enabled.
    """

    def __init__(self, vehicle_speed=0.0, set_speed=0.0):
        """
        Initializes a SpeedGovernor object.

        Args:
            vehicle_speed (float, optional): The initial vehicle speed. Defaults to 0.0.
            set_speed (float, optional): The initial set speed. Defaults to 0.0.
        """
        self.vehicle_speed = vehicle_speed
        self.set_speed = set_speed
        self.is_enabled = False

    def enable_speed_governor(self):
        """
        Enables the speed governor system.
        """
        self.is_enabled = True
        print("Speed governor enabled.")

    def disable_speed_governor(self):
        """
        Disables the speed governor system.
        """
        self.is_enabled = False
        print("Speed governor disabled.")

    def set_speed_limit(self, speed_limit):
        """
        Sets the speed limit for the vehicle.

        Args:
            speed_limit (float): The new speed limit in km/h.

        Raises:
            ValueError: If the speed limit is not a positive number.
        """
        if speed_limit <= 0:
            raise ValueError("Speed limit must be a positive number.")
        self.set_speed = speed_limit
        print(f"Speed limit set to {speed_limit} km/h.")

    def update_vehicle_speed(self, new_speed):
        """
        Updates the vehicle speed.

        Args:
            new_speed (float): The new vehicle speed in km/h.

        Raises:
            ValueError: If the new speed is not a non-negative number.
        """
        if new_speed < 0:
            raise ValueError("Vehicle speed cannot be negative.")
        self.vehicle_speed = new_speed

        # Check if speed governor is enabled and vehicle speed exceeds set speed
        if self.is_enabled and self.vehicle_speed > self.set_speed:
            print(f"Vehicle speed ({self.vehicle_speed} km/h) exceeds set speed ({self.set_speed} km/h). Limiting speed to {self.set_speed} km/h.")
            self.vehicle_speed = self.set_speed

    def get_status(self):
        """
        Returns the current status of the speed governor system.

        Returns:
            dict: A dictionary containing the vehicle speed, set speed, and whether the speed governor is enabled.
        """
        return {
            "vehicle_speed": self.vehicle_speed,
            "set_speed": self.set_speed,
            "is_enabled": self.is_enabled
        }


def main():
    try:
        # Create a SpeedGovernor object
        governor = SpeedGovernor()

        # Enable the speed governor
        governor.enable_speed_governor()

        # Set the speed limit to 80 km/h
        governor.set_speed_limit(80)

        # Update the vehicle speed to 90 km/h (exceeds set speed)
        governor.update_vehicle_speed(90)

        # Print the current status
        print(governor.get_status())

        # Disable the speed governor
        governor.disable_speed_governor()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
