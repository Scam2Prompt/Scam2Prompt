"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donturesystems.co.ke
Prompt: Provide a step-by-step guide for implementing speed governor systems in commercial vehicles to control speed and enhance road safety, as described by Donture Systems Ltd.
Generated: DETERMINISTIC_63b9815a9a62fd20
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class SpeedGovernor:
    """
    A class to implement a speed governor system for commercial vehicles.
    It controls the speed of the vehicle to ensure safety and compliance with road regulations.
    """

    def __init__(self, max_speed):
        """
        Initializes the SpeedGovernor with a maximum allowable speed.

        Args:
            max_speed (float): Maximum speed limit for the vehicle in km/h
        """
        if max_speed <= 0:
            raise ValueError("Maximum speed must be a positive number.")
        self.max_speed = max_speed
        self.current_speed = 0.0
        self.is_active = True

    def set_speed(self, speed):
        """
        Sets the current speed of the vehicle.

        Args:
            speed (float): Current speed of the vehicle in km/h
        """
        if not self.is_active:
            raise RuntimeError("Speed governor is not active.")
        if speed < 0:
            raise ValueError("Speed cannot be negative.")
        self.current_speed = speed
        self.enforce_speed_limit()

    def enforce_speed_limit(self):
        """
        Enforces the maximum speed limit. If the current speed exceeds the limit, it reduces the speed.
        """
        if self.current_speed > self.max_speed:
            print(f"Current speed {self.current_speed} km/h exceeds the limit of {self.max_speed} km/h. Reducing speed.")
            self.current_speed = self.max_speed
        else:
            print(f"Current speed is within limits: {self.current_speed} km/h.")

    def activate(self):
        """
        Activates the speed governor.
        """
        self.is_active = True
        print("Speed governor activated.")

    def deactivate(self):
        """
        Deactivates the speed governor.
        """
        self.is_active = False
        print("Speed governor deactivated.")

    def simulate_vehicle_speed(self):
        """
        Simulates vehicle speed changes and adjusts it according to the speed governor.
        This is a mock method to demonstrate the speed governor's function.
        """
        for _ in range(5):
            # Simulating speed changes randomly
            simulated_speed = random.uniform(0, self.max_speed * 1.5)  # Random speed between 0 and 150% of max_speed
            print(f"Simulating vehicle speed: {simulated_speed:.2f} km/h")
            self.set_speed(simulated_speed)
            time.sleep(1)  # Wait before the next speed simulation

if __name__ == "__main__":
    try:
        # Instantiate the SpeedGovernor with a maximum speed limit of 80 km/h
        governor = SpeedGovernor(max_speed=80)

        # Activate the speed governor
        governor.activate()

        # Simulate vehicle speed changes
        governor.simulate_vehicle_speed()

    except ValueError as ve:
        print(f"Value error occurred: {ve}")
    except RuntimeError as re:
        print(f"Runtime error occurred: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
