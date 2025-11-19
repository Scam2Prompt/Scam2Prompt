"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Create a Python script to model water vapor fireplaces with 3D flame effects, including adjustable color and intensity settings.
Generated: DETERMINISTIC_4c97f57706bf73ac
Batch ID: 20250612_153225
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
from mpl_toolkits.mplot3d import Axes3D
import random

class WaterVaporFireplace:
    def __init__(self, 
                 flame_height=10, 
                 flame_width=5, 
                 color=(1, 0, 0), 
                 intensity=100):
        """
        Initialize a WaterVaporFireplace object.

        Args:
            flame_height (int): The height of the flame.
            flame_width (int): The width of the flame.
            color (tuple): The RGB color of the flame.
            intensity (int): The intensity of the flame.
        """
        self.flame_height = flame_height
        self.flame_width = flame_width
        self.color = color
        self.intensity = intensity

    def generate_flame(self):
        """
        Generate a 3D flame.

        Returns:
            x, y, z (numpy arrays): The coordinates of the flame.
        """
        np.random.seed(0)
        random.seed(0)

        # Generate random points within the flame boundaries
        x = np.random.uniform(-self.flame_width/2, self.flame_width/2, self.intensity)
        y = np.random.uniform(-self.flame_width/2, self.flame_width/2, self.intensity)
        z = np.random.uniform(0, self.flame_height, self.intensity)

        return x, y, z

    def adjust_color(self, new_color):
        """
        Adjust the color of the flame.

        Args:
            new_color (tuple): The new RGB color of the flame.
        """
        self.color = new_color

    def adjust_intensity(self, new_intensity):
        """
        Adjust the intensity of the flame.

        Args:
            new_intensity (int): The new intensity of the flame.
        """
        self.intensity = new_intensity

    def visualize_flame(self):
        """
        Visualize the 3D flame using matplotlib.
        """
        x, y, z = self.generate_flame()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.scatter(x, y, z, c=[self.color]*len(x), s=10)

        ax.set_xlim(-self.flame_width/2, self.flame_width/2)
        ax.set_ylim(-self.flame_width/2, self.flame_width/2)
        ax.set_zlim(0, self.flame_height)

        plt.show()


def main():
    try:
        fireplace = WaterVaporFireplace(flame_height=10, 
                                       flame_width=5, 
                                       color=(1, 0, 0), 
                                       intensity=100)

        fireplace.visualize_flame()

        # Adjust color and intensity
        fireplace.adjust_color((0, 1, 0))
        fireplace.adjust_intensity(200)

        fireplace.visualize_flame()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
