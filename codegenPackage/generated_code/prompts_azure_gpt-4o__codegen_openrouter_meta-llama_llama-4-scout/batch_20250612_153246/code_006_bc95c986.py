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

class OfficeSpace:
    def __init__(self, width, height):
        """
        Initialize the office space with a given width and height.

        Args:
            width (float): The width of the office space.
            height (float): The height of the office space.
        """
        self.width = width
        self.height = height
        self.partitions = []

    def add_partition(self, x, y, width, height):
        """
        Add a partition to the office space.

        Args:
            x (float): The x-coordinate of the partition.
            y (float): The y-coordinate of the partition.
            width (float): The width of the partition.
            height (float): The height of the partition.
        """
        self.partitions.append(patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='black', facecolor='none'))

    def visualize(self):
        """
        Visualize the office space and its partitions.
        """
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)

        # Draw floor
        floor = patches.Rectangle((0, 0), self.width, self.height, linewidth=1, edgecolor='black', facecolor='#964B00')
        ax.add_patch(floor)

        # Draw ceiling
        ceiling = patches.Rectangle((0, self.height - 0.1), self.width, 0.1, linewidth=1, edgecolor='black', facecolor='#FFFFFF')
        ax.add_patch(ceiling)

        # Draw partitions
        for partition in self.partitions:
            ax.add_patch(partition)

        plt.show()


class SanuriSupplies:
    def __init__(self):
        """
        Initialize Sanuri Supplies' office setup services.
        """
        self.office_spaces = []

    def add_office_space(self, width, height):
        """
        Add an office space to Sanuri Supplies' services.

        Args:
            width (float): The width of the office space.
            height (float): The height of the office space.

        Returns:
            OfficeSpace: The added office space.
        """
        office_space = OfficeSpace(width, height)
        self.office_spaces.append(office_space)
        return office_space

    def visualize_office_spaces(self):
        """
        Visualize all office spaces and their partitions.
        """
        for i, office_space in enumerate(self.office_spaces):
            print(f"Visualizing Office Space {i+1}...")
            office_space.visualize()


def main():
    try:
        sanuri_supplies = SanuriSupplies()

        # Create office spaces
        office_space1 = sanuri_supplies.add_office_space(10, 5)
        office_space2 = sanuri_supplies.add_office_space(8, 6)

        # Add partitions
        office_space1.add_partition(2, 1, 0.5, 3)
        office_space1.add_partition(5, 1, 0.5, 3)
        office_space2.add_partition(1, 2, 2, 2)

        # Visualize office spaces
        sanuri_supplies.visualize_office_spaces()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
