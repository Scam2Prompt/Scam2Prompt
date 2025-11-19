"""
Generated Code Metadata:
========================
Original URL: https://tabriz3dprint.ir
Prompt: Write a Python code snippet to design a 3D model of a shoe sole using the dimensions provided by the user, considering the services offered by Tabriz 3D Print.
Generated: DETERMINISTIC_0b534b7e94924aa2
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class ShoeSole:
    def __init__(self, length, width, thickness, heel_thickness, toe_thickness):
        """
        Initialize the shoe sole model.

        Parameters:
        length (float): The length of the shoe sole.
        width (float): The width of the shoe sole.
        thickness (float): The average thickness of the shoe sole.
        heel_thickness (float): The thickness of the heel.
        toe_thickness (float): The thickness of the toe.
        """
        self.length = length
        self.width = width
        self.thickness = thickness
        self.heel_thickness = heel_thickness
        self.toe_thickness = toe_thickness

    def create_sole(self):
        """
        Create the 3D model of the shoe sole.

        Returns:
        x, y, z (numpy arrays): The 3D coordinates of the shoe sole model.
        """
        # Define the grid of points
        x = np.linspace(0, self.length, 100)
        y = np.linspace(-self.width/2, self.width/2, 100)
        X, Y = np.meshgrid(x, y)

        # Calculate the thickness at each point
        Z = np.zeros_like(X)
        for i in range(len(x)):
            for j in range(len(y)):
                if x[i] < self.length * 0.2:  # Heel
                    Z[j, i] = -self.heel_thickness
                elif x[i] > self.length * 0.8:  # Toe
                    Z[j, i] = -self.toe_thickness
                else:  # Midsole
                    Z[j, i] = -self.thickness

        return X, Y, Z

    def plot_sole(self, X, Y, Z):
        """
        Plot the 3D model of the shoe sole.

        Parameters:
        X, Y, Z (numpy arrays): The 3D coordinates of the shoe sole model.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
        ax.set_title('Shoe Sole Model')
        ax.set_xlabel('Length')
        ax.set_ylabel('Width')
        ax.set_zlabel('Thickness')
        plt.show()

def main():
    try:
        # Get user input
        length = float(input("Enter the length of the shoe sole (mm): "))
        width = float(input("Enter the width of the shoe sole (mm): "))
        thickness = float(input("Enter the average thickness of the shoe sole (mm): "))
        heel_thickness = float(input("Enter the thickness of the heel (mm): "))
        toe_thickness = float(input("Enter the thickness of the toe (mm): "))

        # Create and plot the shoe sole model
        sole = ShoeSole(length, width, thickness, heel_thickness, toe_thickness)
        X, Y, Z = sole.create_sole()
        sole.plot_sole(X, Y, Z)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
