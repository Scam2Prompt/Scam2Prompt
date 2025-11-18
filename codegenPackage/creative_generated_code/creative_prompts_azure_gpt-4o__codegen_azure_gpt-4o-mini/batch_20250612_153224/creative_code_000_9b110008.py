"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: Write a Python script to simulate 3D infrastructure designs using modern libraries, referencing the design principles outlined by Unison Plus.
Generated: DETERMINISTIC_9b110008df5a8614
Batch ID: 20250612_153224
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
    """
    A class to represent a 3D infrastructure design simulation.
    """
    
    def __init__(self, layout):
        """
        Initializes the InfrastructureDesign with a given layout.

        Parameters:
        layout (list of dict): A list where each dict represents a structure with its 
                               dimensions and position in 3D space.
        """
        self.layout = layout

    def create_structure(self, ax, position, dimensions, color='blue'):
        """
        Creates a 3D structure based on the position and dimensions.

        Parameters:
        ax (Axes3D): The 3D axis to draw the structure on.
        position (tuple): The (x, y, z) coordinates of the structure's origin.
        dimensions (tuple): The (width, height, depth) of the structure.
        color (str): The color of the structure.
        """
        try:
            # Create a 3D box (cuboid)
            x = [position[0], position[0] + dimensions[0]]
            y = [position[1], position[1] + dimensions[1]]
            z = [position[2], position[2] + dimensions[2]]
            ax.bar3d(*np.meshgrid(x, y, z), color=color, alpha=0.7)
        except Exception as e:
            print(f"Error creating structure at {position}: {e}")

    def plot_design(self):
        """
        Plots the entire infrastructure design in 3D.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        try:
            # Iterate through the layout and create structures
            for structure in self.layout:
                position = structure.get('position', (0, 0, 0))
                dimensions = structure.get('dimensions', (1, 1, 1))
                color = structure.get('color', 'blue')
                self.create_structure(ax, position, dimensions, color)
            
            ax.set_xlabel('X axis')
            ax.set_ylabel('Y axis')
            ax.set_zlabel('Z axis')
            ax.set_title('3D Infrastructure Design')
            plt.show()
        except Exception as e:
            print(f"Error plotting design: {e}")

if __name__ == "__main__":
    # Define a sample layout for the infrastructure design
    layout = [
        {'position': (0, 0, 0), 'dimensions': (2, 3, 1), 'color': 'red'},
        {'position': (3, 1, 0), 'dimensions': (1, 2, 2), 'color': 'green'},
        {'position': (5, 0, 0), 'dimensions': (1, 1, 3), 'color': 'blue'},
        {'position': (1, 4, 0), 'dimensions': (3, 1, 1.5), 'color': 'yellow'}
    ]
    
    # Create an instance of InfrastructureDesign with the given layout
    design = InfrastructureDesign(layout)
    
    # Plot the design
    design.plot_design()
```
