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

# Constants
FURNACE_WIDTH = 1.0  # Width of the furnace (meters)
FURNACE_HEIGHT = 1.0  # Height of the furnace (meters)
GRID_SIZE = 50       # Number of grid points per axis
INITIAL_TEMP = 25.0  # Ambient temperature (Celsius)
HEATER_TEMP = 800.0  # Heater temperature (Celsius)
TIME_STEP = 0.01     # Time step (seconds)
SIMULATION_TIME = 10.0  # Total simulation time (seconds)
THERMAL_DIFFUSIVITY = 0.0001  # Thermal diffusivity (m^2/s)

# Initialize the furnace grid
temperature = np.full((GRID_SIZE, GRID_SIZE), INITIAL_TEMP)

# Define heater regions (adjust as needed)
heater_zone = [(20, 30), (20, 30)]  # Heater coordinates (start_row, end_row, start_col, end_col)

# Set initial heater temperatures
temperature[heater_zone[0][0]:heater_zone[0][1], heater_zone[1][0]:heater_zone[1][1]] = HEATER_TEMP

def simulate_heat_distribution(temperature, diffusivity, time_step, simulation_time):
    """
    Simulates heat distribution in the furnace over time.

    Args:
        temperature (np.ndarray): 2D array of initial temperature values.
        diffusivity (float): Thermal diffusivity (m^2/s).
        time_step (float): Simulation time step (seconds).
        simulation_time (float): Total simulation time (seconds).

    Returns:
        np.ndarray: Final temperature distribution after simulation.
    """
    rows, cols = temperature.shape
    temp_copy = temperature.copy()
    num_steps = int(simulation_time / time_step)

    for step in range(num_steps):
        # Iterate over each grid point (excluding boundaries)
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                # Skip heater zones to maintain constant temperature
                if heater_zone[0][0] <= i < heater_zone[0][1] and heater_zone[1][0] <= j < heater_zone[1][1]:
                    continue

                # Apply the heat equation (finite difference method)
                temp_copy[i, j] = temperature[i, j] + diffusivity * time_step * (
                    (temperature[i + 1, j] - 2 * temperature[i, j] + temperature[i - 1, j]) +
                    (temperature[i, j + 1] - 2 * temperature[i, j] + temperature[i, j - 1])
                )

        # Update temperature array for the next iteration
        temperature[:] = temp_copy

        # Optional: print progress every 100 steps
        if step % 100 == 0:
            print(f"Simulation progress: {step}/{num_steps} steps completed.")

    return temperature

# Run the simulation
final_temperature = simulate_heat_distribution(temperature, THERMAL_DIFFUSIVITY, TIME_STEP, SIMULATION_TIME)

# Plot the final temperature distribution
plt.figure(figsize=(8, 6))
plt.title("Final Temperature Distribution in Furnace")
plt.xlabel("Width (grid points)")
plt.ylabel("Height (grid points)")
plt.imshow(final_temperature, cmap="hot", origin="lower")
plt.colorbar(label="Temperature (Celsius)")
plt.show()
```
