"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kallimos.com
Prompt: Write Python code to simulate a neighborhood design based on the "pocket neighborhoods" concept described in Kallimos Communities, where small dwellings are clustered around shared green spaces.
Generated: DETERMINISTIC_15071c34e3545a3a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class PocketNeighborhood:
    """
    A class representing a pocket neighborhood with small dwellings and shared green spaces.
    """

    def __init__(self, num_houses, neighborhood_size):
        """
        Initializes the PocketNeighborhood with the specified number of houses and neighborhood size.
        
        Parameters:
        num_houses (int): Number of houses in the neighborhood.
        neighborhood_size (tuple): Size of the neighborhood (width, height).
        """
        self.num_houses = num_houses
        self.neighborhood_size = neighborhood_size
        self.houses = []
        self.green_spaces = []

    def create_houses(self):
        """
        Creates houses within the neighborhood. Houses are randomly placed.
        """
        house_width = 2
        house_height = 2
        for _ in range(self.num_houses):
            x = random.uniform(0, self.neighborhood_size[0] - house_width)
            y = random.uniform(0, self.neighborhood_size[1] - house_height)
            self.houses.append((x, y, house_width, house_height))

    def create_green_space(self):
        """
        Creates a central green space area within the neighborhood.
        The green space is a larger rectangle in the center.
        """
        green_space_width = self.neighborhood_size[0] * 0.4
        green_space_height = self.neighborhood_size[1] * 0.4
        x = (self.neighborhood_size[0] - green_space_width) / 2
        y = (self.neighborhood_size[1] - green_space_height) / 2
        self.green_spaces.append((x, y, green_space_width, green_space_height))

    def plot_neighborhood(self):
        """
        Plots the neighborhood layout using matplotlib.
        """
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Plot green spaces
        for green_space in self.green_spaces:
            ax.add_patch(patches.Rectangle((green_space[0], green_space[1]),
                                            green_space[2], green_space[3],
                                            edgecolor='green', facecolor='lightgreen'))
        
        # Plot houses
        for house in self.houses:
            ax.add_patch(patches.Rectangle((house[0], house[1]),
                                            house[2], house[3],
                                            edgecolor='blue', facecolor='lightblue'))

        # Set limits and aspect
        ax.set_xlim(0, self.neighborhood_size[0])
        ax.set_ylim(0, self.neighborhood_size[1])
        ax.set_aspect('equal', adjustable='box')
        plt.title('Pocket Neighborhood Simulation')
        plt.xlabel('Width')
        plt.ylabel('Height')
        plt.grid()
        plt.show()

def main():
    """
    Main function to execute the pocket neighborhood simulation.
    """
    try:
        num_houses = 10  # Adjust number of houses as needed
        neighborhood_size = (20, 20)  # Width, Height of neighborhood
        neighborhood = PocketNeighborhood(num_houses, neighborhood_size)
        neighborhood.create_houses()
        neighborhood.create_green_space()
        neighborhood.plot_neighborhood()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
