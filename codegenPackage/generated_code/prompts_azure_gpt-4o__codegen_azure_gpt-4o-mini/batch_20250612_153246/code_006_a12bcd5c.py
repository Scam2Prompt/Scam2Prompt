"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Create a script to generate custom designs for engraved trophies and medallions, including text and graphical elements, based on the engraving services described on "La Graveuse Normande."
Generated: DETERMINISTIC_a12bcd5c8ccb22e1
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
from matplotlib.patches import Rectangle, Text
import os

class TrophyDesign:
    def __init__(self, width=10, height=5, background_color='white'):
        """
        Initialize the TrophyDesign object with specified dimensions and background color.

        :param width: Width of the trophy design in inches.
        :param height: Height of the trophy design in inches.
        :param background_color: Background color of the design.
        """
        self.width = width
        self.height = height
        self.background_color = background_color
        self.fig, self.ax = plt.subplots(figsize=(self.width, self.height))
        self.ax.set_facecolor(self.background_color)
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.axis('off')  # Hide axes

    def add_text(self, text, position=(0.5, 0.5), fontsize=20, color='black', fontweight='bold'):
        """
        Add text to the trophy design.

        :param text: The text to be added.
        :param position: Tuple (x, y) for text position (0 to 1 scale).
        :param fontsize: Font size of the text.
        :param color: Color of the text.
        :param fontweight: Weight of the font (e.g., 'bold').
        """
        self.ax.text(position[0] * self.width, position[1] * self.height, text,
                     fontsize=fontsize, color=color, fontweight=fontweight,
                     ha='center', va='center')

    def add_graphic(self, graphic_path, position=(0.5, 0.5), scale=0.1):
        """
        Add a graphical element to the trophy design.

        :param graphic_path: Path to the graphic file (PNG, JPG).
        :param position: Tuple (x, y) for graphic position (0 to 1 scale).
        :param scale: Scale factor for the graphic size.
        """
        try:
            img = plt.imread(graphic_path)
            img_height, img_width, _ = img.shape
            self.ax.imshow(img, extent=[position[0] * self.width - (img_width * scale) / 2,
                                         position[0] * self.width + (img_width * scale) / 2,
                                         position[1] * self.height - (img_height * scale) / 2,
                                         position[1] * self.height + (img_height * scale) / 2])
        except FileNotFoundError:
            print(f"Error: The graphic file '{graphic_path}' was not found.")
        except Exception as e:
            print(f"An error occurred while adding the graphic: {e}")

    def save_design(self, filename):
        """
        Save the trophy design to a file.

        :param filename: The filename to save the design (should include .png).
        """
        try:
            plt.savefig(filename, bbox_inches='tight', dpi=300)
            print(f"Trophy design saved as '{filename}'.")
        except Exception as e:
            print(f"An error occurred while saving the design: {e}")

    def show_design(self):
        """
        Display the trophy design.
        """
        plt.show()

if __name__ == "__main__":
    # Example usage of the TrophyDesign class
    trophy = TrophyDesign()

    # Add custom text
    trophy.add_text("Champion", position=(0.5, 0.7), fontsize=30, color='gold')

    # Add a graphic (ensure the path is correct)
    trophy.add_graphic("path/to/graphic.png", position=(0.5, 0.4), scale=0.2)

    # Save the design
    trophy.save_design("trophy_design.png")

    # Show the design
    trophy.show_design()
```

Make sure to replace `"path/to/graphic.png"` with the actual path to your graphic file before running the script.
