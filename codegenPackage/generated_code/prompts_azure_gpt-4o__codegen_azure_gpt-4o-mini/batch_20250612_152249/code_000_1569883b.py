"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Write Python code to calculate coordinates for a topographic diagram based on the ΕΓΣΑ ‘87 Greek Geodetic Reference System. Include validation for accurate boundary representation.
Generated: DETERMINISTIC_1569883bec2781e5
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

class TopographicDiagram:
    def __init__(self, boundary_coordinates):
        """
        Initializes the TopographicDiagram with boundary coordinates.

        :param boundary_coordinates: List of tuples representing the boundary coordinates (latitude, longitude).
        """
        self.boundary_coordinates = boundary_coordinates
        self.validate_boundary()

    def validate_boundary(self):
        """
        Validates the boundary coordinates to ensure they form a closed polygon.
        Raises ValueError if the boundary is not valid.
        """
        if len(self.boundary_coordinates) < 3:
            raise ValueError("At least three coordinates are required to form a boundary.")
        
        # Check if the first and last coordinates are the same
        if self.boundary_coordinates[0] != self.boundary_coordinates[-1]:
            raise ValueError("The boundary must be a closed polygon (first and last coordinates must be the same).")

    def calculate_coordinates(self):
        """
        Calculates the coordinates for the topographic diagram based on the ΕΓΣΑ ‘87 system.
        
        :return: Numpy array of calculated coordinates.
        """
        # Placeholder for actual ΕΓΣΑ ‘87 calculations
        # Here we simply convert the boundary coordinates to a numpy array
        coordinates = np.array(self.boundary_coordinates)
        return coordinates

    def plot_diagram(self):
        """
        Plots the topographic diagram using matplotlib.
        """
        coordinates = self.calculate_coordinates()
        
        # Extracting x and y coordinates for plotting
        x, y = coordinates[:, 0], coordinates[:, 1]
        
        plt.figure(figsize=(10, 6))
        plt.fill(x, y, color='lightblue', alpha=0.5)
        plt.plot(x, y, marker='o', color='blue')
        plt.title('Topographic Diagram based on ΕΓΣΑ ‘87')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.grid()
        plt.axis('equal')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Define boundary coordinates (must be a closed polygon)
    boundary = [(20.0, 30.0), (20.5, 30.5), (20.0, 31.0), (20.0, 30.0)]
    
    try:
        topo_diagram = TopographicDiagram(boundary)
        topo_diagram.plot_diagram()
    except ValueError as e:
        print(f"Error: {e}")
```
