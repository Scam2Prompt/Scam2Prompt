"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Develop a program to create laser engraving designs for wedding place cards or baptism plaques, referencing the customization options mentioned on "La Graveuse Normande."
Generated: DETERMINISTIC_e5438804180e03f7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Laser Engraving Design Generator

This program generates laser engraving designs for wedding place cards or baptism plaques.
It provides customization options similar to those mentioned on "La Graveuse Normande."

Author: [Your Name]
Date: [Today's Date]
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.font_manager as fm
import numpy as np

class EngravingDesign:
    def __init__(self, width=100, height=50, font_size=20, text_color='black', background_color='white'):
        """
        Initialize the engraving design.

        Parameters:
        width (float): The width of the design in mm. Default is 100.
        height (float): The height of the design in mm. Default is 50.
        font_size (int): The font size of the text in points. Default is 20.
        text_color (str): The color of the text. Default is 'black'.
        background_color (str): The color of the background. Default is 'white'.
        """
        self.width = width
        self.height = height
        self.font_size = font_size
        self.text_color = text_color
        self.background_color = background_color

    def add_text(self, text, x=10, y=10):
        """
        Add text to the design.

        Parameters:
        text (str): The text to add.
        x (float): The x-coordinate of the text in mm. Default is 10.
        y (float): The y-coordinate of the text in mm. Default is 10.
        """
        self.text = text
        self.text_x = x
        self.text_y = y

    def add_rectangle(self, x=0, y=0, width=None, height=None):
        """
        Add a rectangle to the design.

        Parameters:
        x (float): The x-coordinate of the rectangle in mm. Default is 0.
        y (float): The y-coordinate of the rectangle in mm. Default is 0.
        width (float): The width of the rectangle in mm. Default is the design width.
        height (float): The height of the rectangle in mm. Default is the design height.
        """
        if width is None:
            width = self.width
        if height is None:
            height = self.height
        self.rectangle = Rectangle((x, y), width, height, edgecolor='black', facecolor=self.background_color)

    def generate_design(self):
        """
        Generate the engraving design.

        Returns:
        A matplotlib figure object representing the design.
        """
        fig, ax = plt.subplots()
        if hasattr(self, 'rectangle'):
            ax.add_patch(self.rectangle)
        if hasattr(self, 'text'):
            font = fm.FontProperties()
            font.set_family('sans-serif')
            font.set_size(self.font_size)
            ax.text(self.text_x, self.text_y, self.text, ha='left', va='bottom', color=self.text_color, fontproperties=font)
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect('equal')
        ax.axis('off')
        return fig

def main():
    try:
        design = EngravingDesign(width=150, height=75, font_size=30)
        design.add_rectangle()
        design.add_text('John & Jane', x=20, y=30)
        design.add_text('Wedding', x=20, y=50)
        fig = design.generate_design()
        plt.savefig('wedding_place_card.pdf', bbox_inches='tight')
        print("Design generated and saved to wedding_place_card.pdf")

        design = EngravingDesign(width=200, height=100, font_size=40, background_color='gray')
        design.add_rectangle()
        design.add_text('Baby John', x=30, y=40)
        design.add_text('Baptism', x=30, y=70)
        fig = design.generate_design()
        plt.savefig('baptism_plaque.pdf', bbox_inches='tight')
        print("Design generated and saved to baptism_plaque.pdf")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
