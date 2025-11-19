"""
Generated Code Metadata:
========================
Original URL: https://mydrones.gr
Prompt: Write a Python script to control a quadcopter drone for aerial photography, considering the independent variation of rotor speeds for thrust and control.
Generated: DETERMINISTIC_bf923cf7fac90248
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np
from typing import Tuple

class Quadcopter:
    """
    A class representing a quadcopter drone.

    Attributes:
    - mass (float): The mass of the quadcopter in kg.
    - L (float): The distance from the center of the quadcopter to the center of a rotor in meters.
    - g (float): The acceleration due to gravity in m/s^2.
    - b (float): The thrust coefficient.
    - k (float): The drag coefficient.
    """

    def __init__(self, mass: float, L: float, g: float = 9.81, b: float = 1.0, k: float = 0.01):
        """
        Initialize the quadcopter.

        Args:
        - mass (float): The mass of the quadcopter in kg.
        - L (float): The distance from the center of the quadcopter to the center of a rotor in meters.
        - g (float, optional): The acceleration due to gravity in m/s^2. Defaults to 9.81.
        - b (float, optional): The thrust coefficient. Defaults to 1.0.
        - k (float, optional): The drag coefficient. Defaults to 0.01.
        """
        self.mass = mass
        self.L = L
        self.g = g
        self.b = b
        self.k = k

    def calculate_rotor_speeds(self, thrust: float, roll: float, pitch: float, yaw: float) -> Tuple[float, float, float, float]:
        """
        Calculate the rotor speeds required to achieve the desired thrust, roll, pitch, and yaw.

        Args:
        - thrust (float): The desired thrust in Newtons.
        - roll (float): The desired roll angle in radians.
        - pitch (float): The desired pitch angle in radians.
        - yaw (float): The desired yaw rate in radians per second.

        Returns:
        - Tuple[float, float, float, float]: The rotor speeds in radians per second.
        """
        # Calculate the total thrust
        w1 = np.sqrt((thrust / (4 * self.b)) + (self.k * yaw * self.L) / (self.b) + (self.g * self.mass / (4 * self.b)))
        w2 = np.sqrt((thrust / (4 * self.b)) - (self.k * yaw * self.L) / (self.b) - (self.g * self.mass / (4 * self.b)) * np.sin(roll) / np.cos(pitch))
        w3 = np.sqrt((thrust / (4 * self.b)) - (self.k * yaw * self.L) / (self.b) + (self.g * self.mass / (4 * self.b)) * np.sin(roll) / np.cos(pitch))
        w4 = np.sqrt((thrust / (4 * self.b)) + (self.k * yaw * self.L) / (self.b) - (self.g * self.mass / (4 * self.b)) * np.sin(pitch))

        return w1, w2, w3, w4

    def validate_rotor_speeds(self, w1: float, w2: float, w3: float, w4: float) -> bool:
        """
        Validate the rotor speeds.

        Args:
        - w1 (float): The speed of rotor 1 in radians per second.
        - w2 (float): The speed of rotor 2 in radians per second.
        - w3 (float): The speed of rotor 3 in radians per second.
        - w4 (float): The speed of rotor 4 in radians per second.

        Returns:
        - bool: True if the rotor speeds are valid, False otherwise.
        """
        # Check if all rotor speeds are positive
        return all(w >= 0 for w in [w1, w2, w3, w4])

def main():
    try:
        # Create a quadcopter instance
        quadcopter = Quadcopter(mass=1.5, L=0.2)

        # Desired thrust, roll, pitch, and yaw
        thrust = 15.0  # Newtons
        roll = np.radians(10)  # Radians
        pitch = np.radians(5)  # Radians
        yaw = np.radians(5)  # Radians per second

        # Calculate rotor speeds
        w1, w2, w3, w4 = quadcopter.calculate_rotor_speeds(thrust, roll, pitch, yaw)

        # Validate rotor speeds
        if quadcopter.validate_rotor_speeds(w1, w2, w3, w4):
            print(f"Rotor speeds: w1 = {w1:.2f} rad/s, w2 = {w2:.2f} rad/s, w3 = {w3:.2f} rad/s, w4 = {w4:.2f} rad/s")
        else:
            print("Invalid rotor speeds")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
