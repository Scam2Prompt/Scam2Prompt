"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoingearapp.blogspot.com
Prompt: Write a program to simulate rodagem silenciosa (silent rolling systems) in industrial machinery and explain the physics behind it.
Generated: DETERMINISTIC_3aa97d1a9688f041
Batch ID: 20250612_154646
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

class SilentRollingSystem:
    """
    A class to simulate the silent rolling systems in industrial machinery.
    
    Attributes:
        radius (float): The radius of the rolling object.
        friction_coefficient (float): The coefficient of friction for the surface.
        mass (float): The mass of the rolling object.
    """

    def __init__(self, radius: float, mass: float, friction_coefficient: float):
        """
        Initializes the SilentRollingSystem with given parameters.
        
        Parameters:
            radius (float): The radius of the rolling object.
            mass (float): The mass of the rolling object.
            friction_coefficient (float): The coefficient of friction for the surface.
        """
        self.radius = radius
        self.mass = mass
        self.friction_coefficient = friction_coefficient
        self.gravity = 9.81  # Acceleration due to gravity (m/s^2)

    def calculate_force(self) -> float:
        """
        Calculates the frictional force acting on the rolling object.
        
        Returns:
            float: The frictional force in Newtons.
        """
        return self.friction_coefficient * self.mass * self.gravity

    def calculate_acceleration(self) -> float:
        """
        Calculates the linear acceleration of the rolling object.
        
        Returns:
            float: The linear acceleration in m/s^2.
        """
        force = self.calculate_force()
        return force / self.mass

    def simulate_rolling(self, time: float, time_step: float) -> tuple:
        """
        Simulates the rolling motion over a given period of time.
        
        Parameters:
            time (float): Total time for the simulation in seconds.
            time_step (float): Time increment for each simulation step in seconds.
        
        Returns:
            tuple: Time array and position array corresponding to the simulation.
        """
        num_steps = int(time / time_step)
        positions = np.zeros(num_steps)
        velocities = np.zeros(num_steps)
        acceleration = self.calculate_acceleration()

        for i in range(1, num_steps):
            velocities[i] = velocities[i - 1] + acceleration * time_step
            positions[i] = positions[i - 1] + velocities[i] * time_step

        return np.arange(0, time, time_step), positions

def main():
    """
    Main function to run the silent rolling system simulation.
    """
    # Parameters for the simulation
    radius = 0.1  # Radius in meters
    mass = 10.0  # Mass in kg
    friction_coefficient = 0.1  # Coefficient of friction
    total_time = 10.0  # Total simulation time in seconds
    time_step = 0.1  # Increment time step in seconds

    try:
        # Create a silent rolling system instance
        rolling_system = SilentRollingSystem(radius, mass, friction_coefficient)

        # Simulate the rolling motion
        time_array, position_array = rolling_system.simulate_rolling(total_time, time_step)

        # Plotting the results
        plt.figure(figsize=(10, 5))
        plt.plot(time_array, position_array, label='Position (m)', color='blue')
        plt.title('Silent Rolling System Simulation')
        plt.xlabel('Time (s)')
        plt.ylabel('Position (m)')
        plt.grid()
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"An error occurred during simulation: {e}")

if __name__ == "__main__":
    main()
```
