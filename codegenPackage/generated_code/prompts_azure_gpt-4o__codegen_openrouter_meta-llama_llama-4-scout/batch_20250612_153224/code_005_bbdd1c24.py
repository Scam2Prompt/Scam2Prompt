"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Write code to simulate the response time of a sprinkler system in reducing heat, flames, and smoke during a fire, based on the benefits outlined by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_bbdd1c249346f0ac
Batch ID: 20250612_153224
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

class SprinklerSystem:
    """
    Simulates the response time of a sprinkler system in reducing heat, flames, and smoke during a fire.

    Attributes:
        activation_time (float): Time it takes for the sprinkler system to activate (in seconds).
        heat_reduction_rate (float): Rate at which the sprinkler system reduces heat (in degrees Celsius per second).
        flame_reduction_rate (float): Rate at which the sprinkler system reduces flames (as a percentage per second).
        smoke_reduction_rate (float): Rate at which the sprinkler system reduces smoke (as a percentage per second).
    """

    def __init__(self, activation_time=30, heat_reduction_rate=2, flame_reduction_rate=5, smoke_reduction_rate=10):
        """
        Initializes the SprinklerSystem class.

        Args:
            activation_time (float, optional): Time it takes for the sprinkler system to activate (in seconds). Defaults to 30.
            heat_reduction_rate (float, optional): Rate at which the sprinkler system reduces heat (in degrees Celsius per second). Defaults to 2.
            flame_reduction_rate (float, optional): Rate at which the sprinkler system reduces flames (as a percentage per second). Defaults to 5.
            smoke_reduction_rate (float, optional): Rate at which the sprinkler system reduces smoke (as a percentage per second). Defaults to 10.
        """
        self.activation_time = activation_time
        self.heat_reduction_rate = heat_reduction_rate
        self.flame_reduction_rate = flame_reduction_rate
        self.smoke_reduction_rate = smoke_reduction_rate

    def simulate_heat_reduction(self, initial_heat, simulation_time):
        """
        Simulates the reduction of heat over time.

        Args:
            initial_heat (float): Initial heat value (in degrees Celsius).
            simulation_time (float): Time to simulate (in seconds).

        Returns:
            np.ndarray: Array of heat values over time.
        """
        if simulation_time < 0:
            raise ValueError("Simulation time must be non-negative")

        heat_values = np.zeros(int(simulation_time) + 1)
        heat_values[0] = initial_heat

        for t in range(1, int(simulation_time) + 1):
            if t < self.activation_time:
                heat_values[t] = heat_values[t - 1]
            else:
                heat_values[t] = max(0, heat_values[t - 1] - self.heat_reduction_rate)

        return heat_values

    def simulate_flame_reduction(self, initial_flame_intensity, simulation_time):
        """
        Simulates the reduction of flame intensity over time.

        Args:
            initial_flame_intensity (float): Initial flame intensity (as a percentage).
            simulation_time (float): Time to simulate (in seconds).

        Returns:
            np.ndarray: Array of flame intensity values over time.
        """
        if simulation_time < 0:
            raise ValueError("Simulation time must be non-negative")

        flame_values = np.zeros(int(simulation_time) + 1)
        flame_values[0] = initial_flame_intensity

        for t in range(1, int(simulation_time) + 1):
            if t < self.activation_time:
                flame_values[t] = flame_values[t - 1]
            else:
                flame_values[t] = max(0, flame_values[t - 1] - self.flame_reduction_rate)

        return flame_values

    def simulate_smoke_reduction(self, initial_smoke_intensity, simulation_time):
        """
        Simulates the reduction of smoke intensity over time.

        Args:
            initial_smoke_intensity (float): Initial smoke intensity (as a percentage).
            simulation_time (float): Time to simulate (in seconds).

        Returns:
            np.ndarray: Array of smoke intensity values over time.
        """
        if simulation_time < 0:
            raise ValueError("Simulation time must be non-negative")

        smoke_values = np.zeros(int(simulation_time) + 1)
        smoke_values[0] = initial_smoke_intensity

        for t in range(1, int(simulation_time) + 1):
            if t < self.activation_time:
                smoke_values[t] = smoke_values[t - 1]
            else:
                smoke_values[t] = max(0, smoke_values[t - 1] - self.smoke_reduction_rate)

        return smoke_values


def main():
    try:
        sprinkler_system = SprinklerSystem()

        initial_heat = 500  # degrees Celsius
        initial_flame_intensity = 100  # percentage
        initial_smoke_intensity = 100  # percentage
        simulation_time = 120  # seconds

        heat_values = sprinkler_system.simulate_heat_reduction(initial_heat, simulation_time)
        flame_values = sprinkler_system.simulate_flame_reduction(initial_flame_intensity, simulation_time)
        smoke_values = sprinkler_system.simulate_smoke_reduction(initial_smoke_intensity, simulation_time)

        plt.figure(figsize=(10, 6))

        plt.subplot(3, 1, 1)
        plt.plot(heat_values)
        plt.title("Heat Reduction Over Time")
        plt.ylabel("Heat (°C)")
        plt.grid(True)

        plt.subplot(3, 1, 2)
        plt.plot(flame_values)
        plt.title("Flame Reduction Over Time")
        plt.ylabel("Flame Intensity (%)")
        plt.grid(True)

        plt.subplot(3, 1, 3)
        plt.plot(smoke_values)
        plt.title("Smoke Reduction Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Smoke Intensity (%)")
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
