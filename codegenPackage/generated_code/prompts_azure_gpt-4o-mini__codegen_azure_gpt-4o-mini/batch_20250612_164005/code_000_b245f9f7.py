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
import numpy as np
import matplotlib.pyplot as plt

class PhysicsExperimentSimulator:
    """
    A class to simulate basic physics experiments for Class XI students.
    This simulator covers concepts such as projectile motion and simple harmonic motion.
    """

    def __init__(self):
        """Initialize the simulator with default parameters."""
        self.gravity = 9.81  # Acceleration due to gravity (m/s^2)

    def simulate_projectile_motion(self, initial_velocity, launch_angle, time_of_flight):
        """
        Simulate projectile motion given initial velocity and launch angle.

        Parameters:
        initial_velocity (float): The initial velocity of the projectile (m/s).
        launch_angle (float): The launch angle of the projectile (degrees).
        time_of_flight (float): The total time of flight (s).

        Returns:
        tuple: Arrays of x and y coordinates of the projectile.
        """
        # Convert angle to radians
        angle_rad = np.radians(launch_angle)

        # Calculate time intervals
        t = np.linspace(0, time_of_flight, num=100)

        # Calculate x and y coordinates
        x = initial_velocity * np.cos(angle_rad) * t
        y = (initial_velocity * np.sin(angle_rad) * t) - (0.5 * self.gravity * t**2)

        return x, y

    def plot_projectile_motion(self, x, y):
        """Plot the projectile motion trajectory."""
        plt.figure(figsize=(10, 5))
        plt.plot(x, y)
        plt.title('Projectile Motion')
        plt.xlabel('Distance (m)')
        plt.ylabel('Height (m)')
        plt.xlim(0, max(x) * 1.1)
        plt.ylim(0, max(y) * 1.1)
        plt.grid()
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.show()

    def simulate_simple_harmonic_motion(self, amplitude, frequency, time_period):
        """
        Simulate simple harmonic motion.

        Parameters:
        amplitude (float): The maximum displacement from the equilibrium position (m).
        frequency (float): The frequency of the motion (Hz).
        time_period (float): The total time for the simulation (s).

        Returns:
        tuple: Arrays of time and displacement.
        """
        # Calculate time intervals
        t = np.linspace(0, time_period, num=100)

        # Calculate displacement using the formula: x(t) = A * cos(2 * pi * f * t)
        displacement = amplitude * np.cos(2 * np.pi * frequency * t)

        return t, displacement

    def plot_simple_harmonic_motion(self, t, displacement):
        """Plot the simple harmonic motion."""
        plt.figure(figsize=(10, 5))
        plt.plot(t, displacement)
        plt.title('Simple Harmonic Motion')
        plt.xlabel('Time (s)')
        plt.ylabel('Displacement (m)')
        plt.grid()
        plt.axhline(0, color='black', lw=0.5, ls='--')
        plt.show()

def main():
    """Main function to run the physics experiment simulator."""
    simulator = PhysicsExperimentSimulator()

    # Simulate and plot projectile motion
    try:
        initial_velocity = 20  # m/s
        launch_angle = 45      # degrees
        time_of_flight = 2 * initial_velocity * np.sin(np.radians(launch_angle)) / simulator.gravity

        x, y = simulator.simulate_projectile_motion(initial_velocity, launch_angle, time_of_flight)
        simulator.plot_projectile_motion(x, y)

    except Exception as e:
        print(f"Error during projectile motion simulation: {e}")

    # Simulate and plot simple harmonic motion
    try:
        amplitude = 1.0  # m
        frequency = 1.0  # Hz
        time_period = 2  # seconds

        t, displacement = simulator.simulate_simple_harmonic_motion(amplitude, frequency, time_period)
        simulator.plot_simple_harmonic_motion(t, displacement)

    except Exception as e:
        print(f"Error during simple harmonic motion simulation: {e}")

if __name__ == "__main__":
    main()
```
