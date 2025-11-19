"""
Generated Code Metadata:
========================
Original URL: https://mydrones.gr
Prompt: Write Python code to simulate the speed variation of quadcopter rotors to achieve specific thrust and control, as described on the "Drone Media" website.
Generated: DETERMINISTIC_77701104826820a8
Batch ID: 20250612_152924
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

class Quadcopter:
    def __init__(self, rotor_count=4, max_thrust=10.0):
        """
        Initialize the Quadcopter with a specified number of rotors and maximum thrust.

        :param rotor_count: Number of rotors on the quadcopter (default is 4)
        :param max_thrust: Maximum thrust produced by each rotor (default is 10.0)
        """
        self.rotor_count = rotor_count
        self.max_thrust = max_thrust
        self.rotor_speeds = np.zeros(rotor_count)  # Initialize rotor speeds

    def set_rotor_speeds(self, thrusts):
        """
        Set the rotor speeds based on desired thrust values.

        :param thrusts: List of desired thrust values for each rotor
        :raises ValueError: If thrust values exceed maximum thrust
        """
        if len(thrusts) != self.rotor_count:
            raise ValueError(f"Expected {self.rotor_count} thrust values, got {len(thrusts)}.")
        
        for thrust in thrusts:
            if thrust < 0 or thrust > self.max_thrust:
                raise ValueError(f"Thrust value {thrust} is out of bounds (0 to {self.max_thrust}).")
        
        # Calculate rotor speeds based on thrust
        self.rotor_speeds = thrusts / self.max_thrust * 100  # Convert thrust to percentage of max speed

    def simulate_flight(self, duration=10, time_step=0.1):
        """
        Simulate the flight of the quadcopter over a specified duration.

        :param duration: Total time for the simulation in seconds
        :param time_step: Time step for the simulation in seconds
        :return: Time and thrust data for plotting
        """
        time_points = np.arange(0, duration, time_step)
        thrust_data = np.zeros((len(time_points), self.rotor_count))

        for i, t in enumerate(time_points):
            thrust_data[i] = self.rotor_speeds  # Record current rotor speeds

        return time_points, thrust_data

    def plot_thrust(self, time_points, thrust_data):
        """
        Plot the thrust produced by each rotor over time.

        :param time_points: Array of time points
        :param thrust_data: Array of thrust data for each rotor
        """
        plt.figure(figsize=(10, 6))
        for i in range(self.rotor_count):
            plt.plot(time_points, thrust_data[:, i], label=f'Rotor {i + 1}')
        
        plt.title('Quadcopter Rotor Thrust Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Thrust (% of max)')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        quadcopter = Quadcopter()
        desired_thrusts = [5.0, 5.0, 5.0, 5.0]  # Example thrust values for each rotor
        quadcopter.set_rotor_speeds(desired_thrusts)
        time_points, thrust_data = quadcopter.simulate_flight(duration=10, time_step=0.1)
        quadcopter.plot_thrust(time_points, thrust_data)
    except ValueError as e:
        print(f"Error: {e}")
```
