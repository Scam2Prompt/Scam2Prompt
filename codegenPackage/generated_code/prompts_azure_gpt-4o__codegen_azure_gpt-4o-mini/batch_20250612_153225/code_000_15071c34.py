"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Write Python code to simulate a neighborhood design based on the "pocket neighborhoods" concept described in Kallimos Communities, where small dwellings are clustered around shared green spaces.
Generated: DETERMINISTIC_15071c34e3545a3a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class PocketNeighborhood:
    def __init__(self, num_houses, neighborhood_size, green_space_size):
        """
        Initialize the PocketNeighborhood with the number of houses, 
        the size of the neighborhood, and the size of the green space.
        
        :param num_houses: Number of houses in the neighborhood
        :param neighborhood_size: Size of the neighborhood (width, height)
        :param green_space_size: Size of the green space (width, height)
        """
        self.num_houses = num_houses
        self.neighborhood_size = neighborhood_size
        self.green_space_size = green_space_size
        self.houses = []
        self.green_space = None

    def create_green_space(self):
        """Create a green space in the center of the neighborhood."""
        x_center = self.neighborhood_size[0] / 2
        y_center = self.neighborhood_size[1] / 2
        self.green_space = patches.Rectangle(
            (x_center - self.green_space_size[0] / 2, 
             y_center - self.green_space_size[1] / 2),
            self.green_space_size[0],
            self.green_space_size[1],
            color='green',
            alpha=0.5
        )

    def create_houses(self):
        """Randomly place houses around the green space."""
        for _ in range(self.num_houses):
            x = random.uniform(0, self.neighborhood_size[0])
            y = random.uniform(0, self.neighborhood_size[1])
            # Ensure houses are not placed in the green space
            while self.is_in_green_space(x, y):
                x = random.uniform(0, self.neighborhood_size[0])
                y = random.uniform(0, self.neighborhood_size[1])
            self.houses.append((x, y))

    def is_in_green_space(self, x, y):
        """Check if a given point is within the green space."""
        if (self.green_space is None):
            raise ValueError("Green space has not been created.")
        return (self.green_space.get_x() <= x <= self.green_space.get_x() + self.green_space.get_width() and
                self.green_space.get_y() <= y <= self.green_space.get_y() + self.green_space.get_height())

    def plot_neighborhood(self):
        """Plot the neighborhood layout with houses and green space."""
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.neighborhood_size[0])
        ax.set_ylim(0, self.neighborhood_size[1])
        ax.add_patch(self.green_space)

        # Plot houses
        for house in self.houses:
            ax.plot(house[0], house[1], 'ro')  # 'ro' means red color, circle marker

        plt.title("Pocket Neighborhood Design")
        plt.xlabel("Width")
        plt.ylabel("Height")
        plt.grid()
        plt.show()

def main():
    """Main function to simulate the neighborhood design."""
    try:
        num_houses = 10
        neighborhood_size = (100, 100)  # Width, Height
        green_space_size = (40, 40)      # Width, Height

        # Create a pocket neighborhood
        neighborhood = PocketNeighborhood(num_houses, neighborhood_size, green_space_size)
        neighborhood.create_green_space()
        neighborhood.create_houses()
        neighborhood.plot_neighborhood()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
