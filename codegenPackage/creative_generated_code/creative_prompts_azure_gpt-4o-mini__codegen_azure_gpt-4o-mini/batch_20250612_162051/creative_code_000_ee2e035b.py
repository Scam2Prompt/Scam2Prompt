"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: Write a Python script that uses 3D simulation software to create a unique infrastructure design based on specific project requirements.
Generated: DETERMINISTIC_ee2e035bb9540620
Batch ID: 20250612_162051
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
from mpl_toolkits.mplot3d import Axes3D

class InfrastructureDesign:
    """Class to create a unique 3D infrastructure design based on project requirements."""

    def __init__(self, length, width, height):
        """
        Initializes the infrastructure design parameters.

        Args:
            length (float): Length of the infrastructure.
            width (float): Width of the infrastructure.
            height (float): Height of the infrastructure.
        """
        self.length = length
        self.width = width
        self.height = height

    def create_base(self):
        """Creates the base of the infrastructure."""
        x = np.array([0, self.length, self.length, 0])
        y = np.array([0, 0, self.width, self.width])
        z = np.zeros(4)
        return x, y, z

    def create_columns(self, num_columns):
        """Creates column positions for the infrastructure.

        Args:
            num_columns (int): Number of columns to place on the base.
        
        Returns:
            list: List of column positions (x, y, z).
        """
        positions = []
        spacing_x = self.length / (num_columns + 1)
        spacing_y = self.width / (num_columns + 1)

        for i in range(1, num_columns + 1):
            pos_x = i * spacing_x
            pos_y = i * spacing_y
            positions.append((pos_x, pos_y, self.height))
        
        return positions

    def plot_design(self, num_columns):
        """Plots the 3D design of the infrastructure.

        Args:
            num_columns (int): Number of columns to include in the design.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Create base
        x_base, y_base, z_base = self.create_base()
        ax.plot_trisurf(x_base, y_base, z_base, color='lightgrey', alpha=0.5)

        # Create columns
        columns = self.create_columns(num_columns)
        for (x, y, z) in columns:
            ax.scatter(x, y, z, color='blue', s=100)

        # Set plot limits
        ax.set_xlim(0, self.length)
        ax.set_ylim(0, self.width)
        ax.set_zlim(0, self.height)

        # Label axes
        ax.set_xlabel('Length')
        ax.set_ylabel('Width')
        ax.set_zlabel('Height')
        ax.set_title('3D Infrastructure Design')

        # Show plot
        plt.show()

def main():
    """Main function to execute the infrastructure design simulation."""
    try:
        # Define project requirements
        length = 10.0  # Length of the infrastructure
        width = 5.0    # Width of the infrastructure
        height = 15.0  # Height of the infrastructure
        num_columns = 4  # Number of columns to include

        # Create an instance of the infrastructure design
        design = InfrastructureDesign(length, width, height)

        # Plot the design
        design.plot_design(num_columns)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
