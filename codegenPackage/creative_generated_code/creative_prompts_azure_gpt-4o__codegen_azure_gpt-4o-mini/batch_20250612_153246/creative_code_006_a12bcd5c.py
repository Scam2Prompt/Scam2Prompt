"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Create a script to generate custom designs for engraved trophies and medallions, including text and graphical elements, based on the engraving services described on "La Graveuse Normande."
Generated: DETERMINISTIC_a12bcd5c8ccb22e1
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
from matplotlib.patches import Rectangle, Circle
import matplotlib.patches as patches

class EngravingDesign:
    def __init__(self, text, shape, dimensions, output_file):
        """
        Initializes the EngravingDesign object with specified text, shape, dimensions, and output file.
        
        :param text: The text to engrave on the trophy/medallion
        :param shape: The shape of the trophy/medallion ('rect' for rectangle, 'circ' for circle)
        :param dimensions: A tuple specifying the dimensions (width, height) or radius
        :param output_file: The filename for the output image
        """
        self.text = text
        self.shape = shape
        self.dimensions = dimensions
        self.output_file = output_file

    def create_design(self):
        """Creates the engraving design based on the initialized properties."""
        # Create figure and axis
        fig, ax = plt.subplots()

        # Draw the shape based on user input
        if self.shape == 'rect':
            self._draw_rectangle(ax)
        elif self.shape == 'circ':
            self._draw_circle(ax)
        else:
            raise ValueError("Shape must be 'rect' or 'circ'.")

        # Add text to the shape
        self._add_text(ax)

        # Set limits and hide axes
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.axis('off')

        # Save the design to a file
        plt.savefig(self.output_file, bbox_inches='tight', pad_inches=0.5)
        plt.close(fig)

    def _draw_rectangle(self, ax):
        """Draws a rectangle on the provided axis."""
        width, height = self.dimensions
        rect = Rectangle((-width/2, -height/2), width, height, linewidth=1, edgecolor='black', facecolor='lightgrey')
        ax.add_patch(rect)

    def _draw_circle(self, ax):
        """Draws a circle on the provided axis."""
        radius = self.dimensions[0]  # dimensions is a tuple with only radius value
        circle = Circle((0, 0), radius, linewidth=1, edgecolor='black', facecolor='lightgrey')
        ax.add_patch(circle)

    def _add_text(self, ax):
        """Adds the specified text to the shape."""
        # Add text to the center of the shape
        ax.text(0, 0, self.text, fontsize=12, ha='center', va='center', fontweight='bold', color='black')

def main():
    try:
        # Sample parameters for the engraving design
        text = "Champion"
        shape = "circ"  # Options: "rect", "circ"
        dimensions = (5,)  # For circle, just the radius; for rectangle, pass (width, height)
        output_file = "engraving_design.png"

        # Initialize the engraving design
        design = EngravingDesign(text, shape, dimensions, output_file)

        # Create and save the design
        design.create_design()
        print(f"Design saved as {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
