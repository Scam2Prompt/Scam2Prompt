"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unapatches.com
Prompt: Generate code to simulate welding enclosures, pipe manifolds, and duct work using AWS-certified standards, as described by Jupiter Design & Manufacturing's welding services.
Generated: DETERMINISTIC_dda8971b64f311f8
Batch ID: 20250612_154412
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
from scipy.spatial import ConvexHull

class WeldingSimulation:
    """
    A class to simulate welding enclosures, pipe manifolds, and duct work.
    """

    def __init__(self, dimensions):
        """
        Initializes the welding simulation with given dimensions.

        Parameters:
            dimensions (dict): A dictionary with keys 'length', 'width', and 'height'.
        """
        self.dimensions = dimensions
        self.validate_dimensions()

    def validate_dimensions(self):
        """
        Validates the provided dimensions to ensure they are positive numbers.
        Raises ValueError if any dimension is invalid.
        """
        for key in ['length', 'width', 'height']:
            if key not in self.dimensions or self.dimensions[key] <= 0:
                raise ValueError(f"Invalid dimension for {key}: must be a positive number.")

    def generate_enclosure(self):
        """
        Generates the coordinates of a rectangular enclosure based on the dimensions.
        
        Returns:
            np.ndarray: Array of shape (8, 3) with the vertices of the enclosure.
        """
        length = self.dimensions['length']
        width = self.dimensions['width']
        height = self.dimensions['height']
        
        # Define the vertices of the enclosure
        points = np.array([[0, 0, 0], [length, 0, 0], [length, width, 0], [0, width, 0],
                           [0, 0, height], [length, 0, height], [length, width, height], [0, width, height]])
        
        return points

    def plot_enclosure(self, points):
        """
        Plots the enclosure using 3D plotting.

        Parameters:
            points (np.ndarray): Array containing the vertices of the enclosure.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        # Create a convex hull for the points
        hull = ConvexHull(points)
        
        # Plot the vertices
        ax.scatter(points[:, 0], points[:, 1], points[:, 2])

        # Plot the edges of the hull
        for simplex in hull.simplices:
            ax.plot3D(points[simplex, 0], points[simplex, 1], points[simplex, 2], 'k-')

        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        plt.title('Welding Enclosure Simulation')
        plt.show()

def main():
    """
    Main function to run the welding simulation.
    """
    try:
        # Define the dimensions of the enclosure
        dimensions = {
            'length': 5.0,  # Length in meters
            'width': 3.0,   # Width in meters
            'height': 2.0   # Height in meters
        }
        
        # Create a welding simulation instance
        welding_sim = WeldingSimulation(dimensions)
        enclosure_points = welding_sim.generate_enclosure()
        
        # Plot the enclosure
        welding_sim.plot_enclosure(enclosure_points)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
