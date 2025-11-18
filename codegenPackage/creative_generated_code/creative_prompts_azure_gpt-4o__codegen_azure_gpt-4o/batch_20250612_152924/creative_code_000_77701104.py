"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mydrones.gr
Prompt: Write Python code to simulate the speed variation of quadcopter rotors to achieve specific thrust and control, as described on the "Drone Media" website.
Generated: DETERMINISTIC_77701104826820a8
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class Quadcopter:
    def __init__(self, max_rpm=12000, min_rpm=1000):
        """
        Initialize the quadcopter with rotor RPM limits.
        :param max_rpm: Maximum RPM a rotor can achieve.
        :param min_rpm: Minimum RPM a rotor can achieve.
        """
        self.max_rpm = max_rpm
        self.min_rpm = min_rpm
        self.rotor_speeds = [0, 0, 0, 0]  # Initial speeds for 4 rotors.

    def set_thrust_and_control(self, thrust, roll, pitch, yaw):
        """
        Adjust rotor speeds to achieve desired thrust and control parameters.
        :param thrust: Overall thrust to lift the quadcopter.
        :param roll: Roll control (rotation around the front-back axis).
        :param pitch: Pitch control (rotation around the side-to-side axis).
        :param yaw: Yaw control (rotation around the vertical axis).
        """
        try:
            # Ensure inputs are within valid ranges.
            if thrust < 0 or thrust > 1:
                raise ValueError("Thrust must be between 0 and 1.")
            if not (-1 <= roll <= 1):
                raise ValueError("Roll must be between -1 and 1.")
            if not (-1 <= pitch <= 1):
                raise ValueError("Pitch must be between -1 and 1.")
            if not (-1 <= yaw <= 1):
                raise ValueError("Yaw must be between -1 and 1.")

            # Map thrust from 0-1 to rotor RPM range.
            base_speed = self.min_rpm + thrust * (self.max_rpm - self.min_rpm)

            # Calculate individual rotor speeds based on roll, pitch, and yaw.
            # Rotor layout:
            # Rotor 1: Front-left, Rotor 2: Front-right
            # Rotor 3: Rear-right, Rotor 4: Rear-left
            rotor_1 = base_speed + roll - pitch + yaw
            rotor_2 = base_speed - roll - pitch - yaw
            rotor_3 = base_speed - roll + pitch + yaw
            rotor_4 = base_speed + roll + pitch - yaw

            # Clamp rotor speeds within the min and max RPM range.
            self.rotor_speeds = [
                max(self.min_rpm, min(self.max_rpm, rotor_1)),
                max(self.min_rpm, min(self.max_rpm, rotor_2)),
                max(self.min_rpm, min(self.max_rpm, rotor_3)),
                max(self.min_rpm, min(self.max_rpm, rotor_4))
            ]

        except ValueError as e:
            print(f"Input error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_rotor_speeds(self):
        """
        Retrieve the current rotor speeds.
        :return: List of rotor speeds in RPM.
        """
        return self.rotor_speeds


# Example usage:
if __name__ == "__main__":
    quadcopter = Quadcopter()

    # Simulate thrust and control adjustments.
    thrust = 0.7  # 70% of max thrust
    roll = 0.1    # Slight roll to the right
    pitch = -0.1  # Slight pitch downward
    yaw = 0.05    # Slight clockwise yaw

    quadcopter.set_thrust_and_control(thrust, roll, pitch, yaw)

    # Output rotor speeds.
    print("Rotor speeds (RPM):", quadcopter.get_rotor_speeds())
```
