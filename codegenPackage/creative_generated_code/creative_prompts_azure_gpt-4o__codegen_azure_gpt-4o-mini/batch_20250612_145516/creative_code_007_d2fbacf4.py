"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftsonopensea.com
Prompt: Generate code to simulate the heat distribution in a "一体箱式电阻炉" (integrated box-type resistance furnace) for material testing.
Generated: DETERMINISTIC_d2fbacf4695df294
Batch ID: 20250612_145516
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
from scipy.integrate import solve_ivp

class HeatDistributionSimulator:
    def __init__(self, length, width, height, num_points, initial_temp, boundary_temp):
        """
        Initialize the simulator with the furnace dimensions and parameters.

        Parameters:
        length (float): Length of the furnace in meters.
        width (float): Width of the furnace in meters.
        height (float): Height of the furnace in meters.
        num_points (int): Number of grid points per dimension.
        initial_temp (float): Initial temperature of the furnace in °C.
        boundary_temp (float): Boundary temperature of the furnace in °C.
        """
        self.length = length
        self.width = width
        self.height = height
        self.num_points = num_points
        self.initial_temp = initial_temp
        self.boundary_temp = boundary_temp

        # Initialize the temperature grid
        self.temperature_grid = np.full((num_points, num_points, num_points), initial_temp)
        self.set_boundary_conditions()

    def set_boundary_conditions(self):
        """Set the boundary conditions of the furnace."""
        # Setting the boundary temperature on all sides of the furnace
        self.temperature_grid[0, :, :] = self.boundary_temp
        self.temperature_grid[-1, :, :] = self.boundary_temp
        self.temperature_grid[:, 0, :] = self.boundary_temp
        self.temperature_grid[:, -1, :] = self.boundary_temp
        self.temperature_grid[:, :, 0] = self.boundary_temp
        self.temperature_grid[:, :, -1] = self.boundary_temp

    def simulate_heat_distribution(self, time_span, num_steps):
        """
        Simulate the heat distribution over time using the finite difference method.

        Parameters:
        time_span (tuple): Start and end time for the simulation.
        num_steps (int): Number of steps in the time span.
        """
        time_eval = np.linspace(time_span[0], time_span[1], num_steps)

        # Prepare a function to calculate the rate of temperature change
        def heat_equation(t, y):
            # Reshape the solution vector to 3D for temperature grid operations
            grid = y.reshape((self.num_points, self.num_points, self.num_points))
            dTdt = np.zeros_like(grid)

            # Finite difference method to compute temperature changes
            for i in range(1, self.num_points - 1):
                for j in range(1, self.num_points - 1):
                    for k in range(1, self.num_points - 1):
                        dTdt[i, j, k] = (
                            grid[i+1, j, k] + grid[i-1, j, k] +
                            grid[i, j+1, k] + grid[i, j-1, k] +
                            grid[i, j, k+1] + grid[i, j, k-1] -
                            6 * grid[i, j, k]
                        )

            return dTdt.flatten()

        # Flatten the initial temperature grid for the solver
        initial_conditions = self.temperature_grid.flatten()

        # Using solve_ivp to solve the differential equations
        solution = solve_ivp(heat_equation, time_span, initial_conditions, t_eval=time_eval)

        # Reshape the solution back to the grid format for visualization
        return solution.y.reshape((self.num_points, self.num_points, self.num_points, -1))

    def visualize_temperature_distribution(self, temperature_data):
        """
        Visualize the temperature distribution over time.

        Parameters:
        temperature_data (np.ndarray): The temperature data over time.
        """
        # Select a slice of the 3D temperature data for visualization
        mid_point = self.num_points // 2
        for t in range(temperature_data.shape[-1]):
            plt.imshow(temperature_data[:, :, mid_point, t], cmap='hot', interpolation='nearest')
            plt.title(f'Temperature Distribution at t={t}')
            plt.colorbar(label='Temperature (°C)')
            plt.pause(0.1)  # Pause for a brief moment to visualize the changes

if __name__ == "__main__":
    # Parameters for the simulation
    furnace_length = 1.0  # meters
    furnace_width = 1.0   # meters
    furnace_height = 1.0  # meters
    grid_points = 20      # number of points in each dimension
    initial_temperature = 25.0  # °C
    boundary_temperature = 200.0 # °C

    # Create the heat distribution simulator instance
    simulator = HeatDistributionSimulator(furnace_length, furnace_width, furnace_height,
                                           grid_points, initial_temperature, boundary_temperature)

    # Run the simulation for 10 time units with 100 steps
    time_span = (0, 10)
    num_time_steps = 100
    temperature_data = simulator.simulate_heat_distribution(time_span, num_time_steps)

    # Visualize the temperature distribution
    plt.ion()  # Turn on interactive mode
    simulator.visualize_temperature_distribution(temperature_data)
    plt.ioff()  # Turn off interactive mode
    plt.show()
```
