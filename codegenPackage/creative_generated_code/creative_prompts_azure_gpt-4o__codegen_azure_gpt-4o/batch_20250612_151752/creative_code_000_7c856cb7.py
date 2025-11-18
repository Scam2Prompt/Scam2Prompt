"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foundation.ru
Prompt: Write Python code to simulate geotechnical tasks using numerical modeling techniques, specifically for evaluating the influence of new construction on surrounding structures, as described by the services of the Научно-образовательный центр «Геотехника».
Generated: DETERMINISTIC_7c856cb749a853d0
Batch ID: 20250612_151752
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

class GeotechnicalModel:
    """
    A class to simulate geotechnical tasks using numerical modeling techniques.
    Specifically evaluates influence of new construction on surrounding structures.
    """

    def __init__(self, soil_properties, construction_load, grid_size=100):
        """
        Initializes the geotechnical model.

        Args:
            soil_properties (dict): Dictionary containing soil properties like modulus and density.
            construction_load (float): Load of the new construction in kPa.
            grid_size (int): Size of the numerical grid for the simulation.
        """
        self.soil_properties = soil_properties
        self.construction_load = construction_load
        self.grid_size = grid_size
        self.grid = np.zeros((grid_size, grid_size))  # Stress distribution grid

    def apply_construction_load(self, x, y):
        """
        Applies construction load at the specified location on the grid.

        Args:
            x (int): X-coordinate of the construction site on the grid.
            y (int): Y-coordinate of the construction site on the grid.
        """
        try:
            if x < 0 or x >= self.grid_size or y < 0 or y >= self.grid_size:
                raise ValueError("Construction site coordinates are out of bounds.")

            # Apply load with Gaussian distribution to simulate spreading
            sigma = 10  # Standard deviation for load spreading
            for i in range(self.grid_size):
                for j in range(self.grid_size):
                    distance = np.sqrt((x - i)**2 + (y - j)**2)
                    self.grid[i, j] += self.construction_load * np.exp(-distance**2 / (2 * sigma**2))

        except Exception as e:
            print(f"Error applying construction load: {e}")

    def calculate_influence_on_surroundings(self):
        """
        Calculates the influence of the construction load on surrounding structures.

        Returns:
            stress_distribution (np.array): The grid showing stress distribution.
        """
        try:
            # Normalize the stress distribution
            stress_distribution = self.grid / np.max(self.grid)
            return stress_distribution
        except Exception as e:
            print(f"Error calculating stress distribution: {e}")
            return None

    def plot_stress_distribution(self):
        """
        Plots the stress distribution grid.
        """
        try:
            plt.imshow(self.grid, cmap='hot', interpolation='nearest')
            plt.colorbar(label='Stress (Normalized)')
            plt.title('Stress Distribution Due to Construction')
            plt.xlabel('Grid X')
            plt.ylabel('Grid Y')
            plt.show()
        except Exception as e:
            print(f"Error plotting stress distribution: {e}")


# Example usage
if __name__ == "__main__":
    # Define soil properties and construction load
    soil_properties = {
        "modulus": 15e3,  # Modulus of elasticity in kPa
        "density": 1.8e3  # Density in kg/m^3
    }
    construction_load = 50  # Construction load in kPa

    # Initialize model
    model = GeotechnicalModel(soil_properties, construction_load)

    # Apply construction load at the center of the grid
    center_x = model.grid_size // 2
    center_y = model.grid_size // 2
    model.apply_construction_load(center_x, center_y)

    # Calculate and plot stress distribution
    stress_distribution = model.calculate_influence_on_surroundings()
    if stress_distribution is not None:
        model.plot_stress_distribution()
```
