"""
Generated Code Metadata:
========================
Original URL: https://sameersphysicsclasses.com
Prompt: Generate a Python script that simulates physics experiments for Class XI students, incorporating concepts from CBSE Physics curriculum.
Generated: DETERMINISTIC_b245f9f7d3995591
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# physics_experiments.py

"""
Simulates physics experiments for Class XI students, 
incorporating concepts from CBSE Physics curriculum.
"""

import math
import matplotlib.pyplot as plt

class PhysicsExperiment:
    def __init__(self):
        pass

    def simulate_uniform_motion(self, initial_velocity, acceleration, time):
        """
        Simulates uniform motion and calculates final velocity and displacement.

        Args:
            initial_velocity (float): Initial velocity in m/s
            acceleration (float): Acceleration in m/s^2
            time (float): Time in seconds

        Returns:
            tuple: Final velocity and displacement
        """
        final_velocity = initial_velocity + acceleration * time
        displacement = initial_velocity * time + 0.5 * acceleration * time**2
        return final_velocity, displacement

    def simulate_projectile_motion(self, initial_velocity, angle, g=9.81):
        """
        Simulates projectile motion and calculates range and maximum height.

        Args:
            initial_velocity (float): Initial velocity in m/s
            angle (float): Angle of projection in degrees
            g (float, optional): Acceleration due to gravity in m/s^2. Defaults to 9.81.

        Returns:
            tuple: Range and maximum height
        """
        angle_rad = math.radians(angle)
        range_of_motion = (initial_velocity**2) * math.sin(2 * angle_rad) / g
        max_height = (initial_velocity**2) * (math.sin(angle_rad)**2) / (2 * g)
        return range_of_motion, max_height

    def simulate_oscillations(self, amplitude, frequency, time):
        """
        Simulates oscillations and calculates displacement at a given time.

        Args:
            amplitude (float): Amplitude of oscillation
            frequency (float): Frequency of oscillation
            time (float): Time in seconds

        Returns:
            float: Displacement at the given time
        """
        displacement = amplitude * math.sin(2 * math.pi * frequency * time)
        return displacement

def main():
    experiment = PhysicsExperiment()

    while True:
        print("\nPhysics Experiments Menu:")
        print("1. Uniform Motion")
        print("2. Projectile Motion")
        print("3. Oscillations")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            initial_velocity = float(input("Enter initial velocity (m/s): "))
            acceleration = float(input("Enter acceleration (m/s^2): "))
            time = float(input("Enter time (s): "))
            final_velocity, displacement = experiment.simulate_uniform_motion(initial_velocity, acceleration, time)
            print(f"Final velocity: {final_velocity:.2f} m/s")
            print(f"Displacement: {displacement:.2f} m")

        elif choice == "2":
            initial_velocity = float(input("Enter initial velocity (m/s): "))
            angle = float(input("Enter angle of projection (degrees): "))
            range_of_motion, max_height = experiment.simulate_projectile_motion(initial_velocity, angle)
            print(f"Range of motion: {range_of_motion:.2f} m")
            print(f"Maximum height: {max_height:.2f} m")

        elif choice == "3":
            amplitude = float(input("Enter amplitude of oscillation: "))
            frequency = float(input("Enter frequency of oscillation (Hz): "))
            time = float(input("Enter time (s): "))
            displacement = experiment.simulate_oscillations(amplitude, frequency, time)
            print(f"Displacement at {time:.2f} s: {displacement:.2f} m")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
