"""
Generated Code Metadata:
========================
Original URL: https://sanurisupplies.com
Prompt: Write code to simulate the partitioning of office spaces and visualize the design process, including floor and ceiling designs, based on Sanuri Supplies' office setup services.
Generated: DETERMINISTIC_bc95c986d51ec04b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class OfficeSpace:
    def __init__(self, width, height):
        """
        Initialize the office space with given width and height.
        
        :param width: Width of the office space
        :param height: Height of the office space
        """
        self.width = width
        self.height = height
        self.partitions = []

    def add_partition(self, x, y, width, height):
        """
        Add a partition to the office space.
        
        :param x: X-coordinate of the partition's bottom-left corner
        :param y: Y-coordinate of the partition's bottom-left corner
        :param width: Width of the partition
        :param height: Height of the partition
        """
        if x < 0 or y < 0 or x + width > self.width or y + height > self.height:
            raise ValueError("Partition dimensions are out of bounds.")
        self.partitions.append((x, y, width, height))

    def visualize(self):
        """
        Visualize the office space and its partitions using matplotlib.
        """
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_title("Office Space Partitioning")
        ax.set_xlabel("Width")
        ax.set_ylabel("Height")

        # Draw the office space
        office_rect = patches.Rectangle((0, 0), self.width, self.height, linewidth=1, edgecolor='black', facecolor='lightgrey')
        ax.add_patch(office_rect)

        # Draw each partition
        for (x, y, width, height) in self.partitions:
            partition_rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='blue', facecolor='lightblue')
            ax.add_patch(partition_rect)

        plt.grid()
        plt.show()

def main():
    """
    Main function to simulate the office space partitioning and visualization.
    """
    try:
        # Create an office space of 20x15 units
        office = OfficeSpace(20, 15)

        # Add partitions to the office space
        office.add_partition(2, 2, 5, 10)  # Partition 1
        office.add_partition(8, 3, 6, 5)   # Partition 2
        office.add_partition(15, 1, 3, 12)  # Partition 3

        # Visualize the office space
        office.visualize()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
