"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sameersphysicsclasses.com
Prompt: Generate a Python script that simulates physics experiments for Class XI students, incorporating concepts from CBSE Physics curriculum.
Generated: DETERMINISTIC_b245f9f7d3995591
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class PhysicsExperimentSimulator:
    def __init__(self):
        """Initialize the simulator with default parameters."""
        self.gravity = 9.81  # Acceleration due to gravity (m/s^2)

    def free_fall(self, height, time_steps=100):
        """
        Simulate the free fall of an object from a specified height.

        Parameters:
        height (float): Initial height from which the object falls (meters).
        time_steps (int): Number of time intervals for the simulation.

        Returns:
        tuple: Time array and position array of the falling object.
        """
        if height <= 0:
            raise ValueError("Height must be a positive value.")
        
        # Time array (seconds)
        time = np.linspace(0, np.sqrt(2 * height / self.gravity), time_steps)
        # Position array (meters)
        position = height - 0.5 * self.gravity * time**2
        
        return time, position

    def projectile_motion(self, initial_velocity, angle, time_steps=100):
        """
        Simulate the projectile motion of an object.

        Parameters:
        initial_velocity (float): Initial velocity of the projectile (m/s).
        angle (float): Launch angle of the projectile (degrees).
        time_steps (int): Number of time intervals for the simulation.

        Returns:
        tuple: Time array, X positions, and Y positions of the projectile.
        """
        if initial_velocity <= 0:
            raise ValueError("Initial velocity must be a positive value.")
        if not (0 <= angle <= 90):
            raise ValueError("Angle must be between 0 and 90 degrees.")

        # Convert angle to radians
        angle_rad = np.radians(angle)
        # Time of flight calculation
        time_of_flight = (2 * initial_velocity * np.sin(angle_rad)) / self.gravity
        # Time array (seconds)
        time = np.linspace(0, time_of_flight, time_steps)
        
        # X and Y positions
        x_position = initial_velocity * np.cos(angle_rad) * time
        y_position = (initial_velocity * np.sin(angle_rad) * time) - (0.5 * self.gravity * time**2)

        return time, x_position, y_position

    def plot_free_fall(self, height):
        """Plot the free fall simulation."""
        time, position = self.free_fall(height)
        plt.figure(figsize=(10, 5))
        plt.plot(time, position)
        plt.title('Free Fall Simulation')
        plt.xlabel('Time (s)')
        plt.ylabel('Height (m)')
        plt.axhline(0, color='gray', linestyle='--')
        plt.grid()
        plt.show()

    def plot_projectile_motion(self, initial_velocity, angle):
        """Plot the projectile motion simulation."""
        time, x_position, y_position = self.projectile_motion(initial_velocity, angle)
        plt.figure(figsize=(10, 5))
        plt.plot(x_position, y_position)
        plt.title('Projectile Motion Simulation')
        plt.xlabel('Distance (m)')
        plt.ylabel('Height (m)')
        plt.axhline(0, color='gray', linestyle='--')
        plt.grid()
        plt.show()

if __name__ == "__main__":
    simulator = PhysicsExperimentSimulator()

    # Free fall simulation
    try:
        height = float(input("Enter the height for free fall experiment (in meters): "))
        simulator.plot_free_fall(height)
    except ValueError as e:
        print(f"Error: {e}")

    # Projectile motion simulation
    try:
        initial_velocity = float(input("Enter the initial velocity for projectile motion (in m/s): "))
        angle = float(input("Enter the launch angle (in degrees): "))
        simulator.plot_projectile_motion(initial_velocity, angle)
    except ValueError as e:
        print(f"Error: {e}")
```
