"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyikudesign.com
Prompt: Write a script to simulate lighting effects in an interior design project, focusing on creating a functional and aesthetic ambiance as emphasized by Nyiku Design.
Generated: DETERMINISTIC_70b272da43e63037
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np
import random

# Simulate lighting effects in an interior design project
class LightingSimulator:
    def __init__(self, room_width, room_height):
        """
        Initialize the LightingSimulator class.
        
        Parameters:
        room_width (int): Width of the room in units.
        room_height (int): Height of the room in units.
        """
        self.room_width = room_width
        self.room_height = room_height
        self.light_sources = []  # List to store light sources
    
    def add_light_source(self, x, y, intensity, color):
        """
        Add a light source to the room.
        
        Parameters:
        x (float): X-coordinate of the light source.
        y (float): Y-coordinate of the light source.
        intensity (float): Intensity of the light source (0.1 to 1.0).
        color (tuple): RGB color of the light source (values between 0 and 1).
        """
        if not (0 <= x <= self.room_width and 0 <= y <= self.room_height):
            raise ValueError("Light source position must be within room boundaries.")
        if not (0.1 <= intensity <= 1.0):
            raise ValueError("Intensity must be between 0.1 and 1.0.")
        if not all(0 <= c <= 1 for c in color):
            raise ValueError("Color values must be between 0 and 1.")
        
        self.light_sources.append({'x': x, 'y': y, 'intensity': intensity, 'color': color})
    
    def simulate_lighting(self):
        """
        Simulate the lighting effects in the room.
        """
        # Create a grid representing the room
        x = np.linspace(0, self.room_width, 100)
        y = np.linspace(0, self.room_height, 100)
        X, Y = np.meshgrid(x, y)
        
        # Initialize intensity and color grids
        intensity_grid = np.zeros_like(X)
        color_grid = np.zeros((100, 100, 3))
        
        # Calculate light intensity and color effects from each light source
        for light in self.light_sources:
            distance = np.sqrt((X - light['x'])**2 + (Y - light['y'])**2)
            effect = light['intensity'] / (1 + distance**2)  # Lighting attenuation formula
            intensity_grid += effect
            color_grid += np.array(light['color']) * np.expand_dims(effect, axis=-1)
        
        # Normalize grids to prevent oversaturation
        intensity_grid = np.clip(intensity_grid, 0, 1)
        color_grid = np.clip(color_grid, 0, 1)
        
        # Visualize the lighting effects
        plt.figure(figsize=(8, 6))
        plt.imshow(color_grid, extent=(0, self.room_width, 0, self.room_height), origin='lower')
        plt.colorbar(label='Light Intensity')
        plt.title("Simulated Lighting Effects")
        plt.xlabel("Room Width")
        plt.ylabel("Room Height")
        plt.show()


# Example usage
if __name__ == "__main__":
    try:
        # Initialize a room with dimensions 10x8 units
        simulator = LightingSimulator(room_width=10, room_height=8)

        # Add light sources (position, intensity, color)
        simulator.add_light_source(x=3, y=4, intensity=0.8, color=(1, 0.5, 0))  # Warm light
        simulator.add_light_source(x=7, y=6, intensity=0.6, color=(0.5, 0.5, 1))  # Cool light
        simulator.add_light_source(x=5, y=2, intensity=0.4, color=(0, 1, 0.5))  # Soft green light

        # Simulate and visualize the lighting effects
        simulator.simulate_lighting()
    except Exception as e:
        print(f"Error: {e}")
```
