"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wealthbhai.com
Prompt: Write a script to simulate the bending and stretching processes for stainless steel pipe manufacturing, incorporating techniques like rolling and extrusion described on the website.
Generated: DETERMINISTIC_06fbe5fca9730702
Batch ID: 20250612_153526
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

class SteelPipe:
    """
    A class representing a stainless steel pipe and its manufacturing processes.
    """

    def __init__(self, diameter, length, thickness):
        """
        Initializes a new SteelPipe object with specified diameter, length, and thickness.
        
        :param diameter: Diameter of the pipe (in mm).
        :param length: Length of the pipe (in mm).
        :param thickness: Thickness of the pipe wall (in mm).
        """
        self.diameter = diameter
        self.length = length
        self.thickness = thickness

    def roll(self, radius, angle):
        """
        Simulates the rolling process of the pipe.
        
        :param radius: Radius of the rolling machine (in mm).
        :param angle: Angle of bend (in degrees).
        :return: New dimensions of the pipe after rolling.
        """
        if radius <= 0 or angle <= 0:
            raise ValueError("Radius and angle must be positive values.")
        
        rolled_length = self.length * (1 + angle / 360)
        rolled_diameter = self.diameter + (angle / 360) * self.diameter
        
        print(f"Rolling: New length = {rolled_length:.2f} mm, New diameter = {rolled_diameter:.2f} mm")
        return rolled_length, rolled_diameter

    def extrude(self, new_diameter):
        """
        Simulates the extrusion process of the pipe.
        
        :param new_diameter: New diameter of the pipe after extrusion (in mm).
        :return: New dimensions of the pipe after extrusion.
        """
        if new_diameter <= self.thickness:
            raise ValueError("New diameter must be greater than wall thickness.")
        
        extruded_length = self.length
        extruded_diameter = new_diameter
        
        print(f"Extruding: New length = {extruded_length:.2f} mm, New diameter = {extruded_diameter:.2f} mm")
        return extruded_length, extruded_diameter

def main():
    """
    Main function to execute the simulation of pipe manufacturing.
    """
    try:
        # Initialize a stainless steel pipe with specific dimensions
        pipe = SteelPipe(diameter=100, length=1000, thickness=5)

        # Simulate rolling process
        rolled_length, rolled_diameter = pipe.roll(radius=300, angle=90)

        # Simulate extrusion process
        extruded_length, extruded_diameter = pipe.extrude(new_diameter=120)

        # Visualization of pipe changes
        plt.figure(figsize=(10, 6))
        pipe_dimensions = [pipe.diameter, rolled_diameter, extruded_diameter]
        processes = ['Original', 'After Rolling', 'After Extrusion']
        
        plt.bar(processes, pipe_dimensions, color=['blue', 'orange', 'green'])
        plt.ylabel('Diameter (mm)')
        plt.title('Stainless Steel Pipe Manufacturing Processes')
        plt.ylim(0, max(pipe_dimensions) + 20)
        plt.grid(axis='y')
        plt.show()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
