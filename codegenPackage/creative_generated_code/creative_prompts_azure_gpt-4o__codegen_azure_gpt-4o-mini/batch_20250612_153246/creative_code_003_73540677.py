"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engenhariawpj.com
Prompt: Provide code to create a visualization of design textures and color options available for construction projects, inspired by the "texturas" section of Engenharia WPJ.
Generated: DETERMINISTIC_7354067701ab4a73
Batch ID: 20250612_153246
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
import pandas as pd

class TextureVisualizer:
    """
    A class to visualize design textures and color options for construction projects.
    
    Attributes:
        textures (pd.DataFrame): A dataframe containing texture options and their colors.
    """

    def __init__(self, data):
        """
        Initializes the TextureVisualizer with texture data.

        Parameters:
            data (dict): A dictionary containing texture names and their corresponding colors.
        """
        try:
            # Convert input data to DataFrame
            self.textures = pd.DataFrame(data)
            if not all(col in self.textures.columns for col in ['Texture', 'Color']):
                raise ValueError("Data must contain 'Texture' and 'Color' columns.")
        except Exception as e:
            print(f"Error initializing TextureVisualizer: {e}")

    def plot_textures(self):
        """
        Plots the textures and their respective colors in a bar chart.
        """
        try:
            # Ensure the DataFrame is not empty
            if self.textures.empty:
                raise ValueError("No texture data available to plot.")

            # Set up plot
            plt.figure(figsize=(12, 6))
            plt.bar(self.textures['Texture'], np.zeros(len(self.textures)), color=self.textures['Color'], width=0.4)
            plt.title('Design Textures and Color Options')
            plt.xlabel('Textures')
            plt.ylabel('Visual Representation')
            plt.yticks([])  # Hide y-axis ticks

            # Show plot
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"Error while plotting textures: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for textures and their corresponding colors
    texture_data = {
        'Texture': ['Wood', 'Marble', 'Concrete', 'Brick', 'Glass'],
        'Color': ['#8B4513', '#FFFFFF', '#A9A9A9', '#B22222', '#ADD8E6']
    }

    # Create TextureVisualizer instance
    visualizer = TextureVisualizer(texture_data)

    # Plot the textures
    visualizer.plot_textures()
```
