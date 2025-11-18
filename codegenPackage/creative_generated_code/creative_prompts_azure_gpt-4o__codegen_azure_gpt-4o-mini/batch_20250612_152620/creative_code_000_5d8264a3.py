"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capinaeletrica.com.br
Prompt: Write Python code to simulate the effects of Capina Elétrica's high-voltage weed removal technology on urban vegetation, ensuring the simulation models both root and shoot elimination as described on the website.
Generated: DETERMINISTIC_5d8264a3becb7215
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import numpy as np
import matplotlib.pyplot as plt

class UrbanVegetationSimulation:
    def __init__(self, grid_size, num_vegetation, root_elimination_rate, shoot_elimination_rate):
        """
        Initializes the simulation with given parameters.

        Parameters:
            grid_size (int): The size of the square grid for vegetation.
            num_vegetation (int): The number of vegetation units to simulate.
            root_elimination_rate (float): The probability of root elimination per vegetation unit.
            shoot_elimination_rate (float): The probability of shoot elimination per vegetation unit.
        """
        self.grid_size = grid_size
        self.num_vegetation = num_vegetation
        self.root_elimination_rate = root_elimination_rate
        self.shoot_elimination_rate = shoot_elimination_rate
        
        # Create a grid to represent vegetation; 1 for present, 0 for removed
        self.grid = np.zeros((grid_size, grid_size))
        self.populate_vegetation()

    def populate_vegetation(self):
        """Randomly populates the grid with vegetation units."""
        positions = random.sample(range(self.grid_size * self.grid_size), self.num_vegetation)
        for pos in positions:
            x, y = divmod(pos, self.grid_size)
            self.grid[x][y] = 1  # 1 denotes presence of vegetation

    def simulate_removal(self):
        """Simulates the removal of vegetation based on root and shoot elimination rates."""
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == 1:  # If there is vegetation
                    root_removed = random.random() < self.root_elimination_rate
                    shoot_removed = random.random() < self.shoot_elimination_rate
                    
                    if root_removed and shoot_removed:
                        self.grid[i][j] = 0  # Both root and shoot eliminated
                    elif root_removed:
                        self.grid[i][j] = 0  # Only root eliminated
                    elif shoot_removed:
                        self.grid[i][j] = 0  # Only shoot eliminated

    def display_grid(self):
        """Displays the current state of the vegetation grid."""
        plt.imshow(self.grid, cmap='Greens', interpolation='nearest')
        plt.title("Urban Vegetation Simulation")
        plt.colorbar(label='Vegetation State (1 = Present, 0 = Removed)')
        plt.show()

    def run_simulation(self, steps):
        """
        Runs the simulation for a given number of steps.

        Parameters:
            steps (int): The number of simulation steps to run.
        """
        for step in range(steps):
            self.simulate_removal()
            print(f"Step {step + 1}:")
            self.display_grid()

# Example usage
if __name__ == "__main__":
    try:
        simulation = UrbanVegetationSimulation(grid_size=10, num_vegetation=50, 
                                               root_elimination_rate=0.3, 
                                               shoot_elimination_rate=0.5)
        simulation.run_simulation(steps=5)
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
