"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdbondindia.com
Prompt: Develop a program to create banner designs and ADS boards as described in SD BOND India's latest projects, ensuring flexibility in customization.
Generated: DETERMINISTIC_f1193e1feab68425
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class Banner:
    """
    A class to create a customizable banner design.
    """

    def __init__(self, width=10, height=5, background_color='white'):
        """
        Initializes the Banner instance with width, height, and background color.
        
        :param width: Width of the banner.
        :param height: Height of the banner.
        :param background_color: Background color of the banner.
        """
        self.width = width
        self.height = height
        self.background_color = background_color
        self.fig, self.ax = self._setup_canvas()

    def _setup_canvas(self):
        """
        Sets up the canvas for the banner.
        
        :return: Figure and Axes for the banner.
        """
        fig, ax = plt.subplots(figsize=(self.width, self.height))
        ax.set_facecolor(self.background_color)
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.axis('off')  # Hide axes
        return fig, ax

    def add_text(self, text, position, fontsize=20, color='black', fontweight='bold'):
        """
        Adds text to the banner.
        
        :param text: The text to add.
        :param position: Tuple (x, y) for the text position.
        :param fontsize: Font size of the text.
        :param color: Color of the text.
        :param fontweight: Font weight of the text.
        """
        self.ax.text(position[0], position[1], text, fontsize=fontsize, color=color,
                     weight=fontweight, ha='center', va='center')

    def add_image(self, image_path, position, image_size=(1, 1)):
        """
        Adds an image to the banner.
        
        :param image_path: Path to the image file.
        :param position: Tuple (x, y) for the image position.
        :param image_size: Tuple (width, height) for the image size.
        """
        try:
            img = plt.imread(image_path)
            self.ax.imshow(img, extent=(position[0]-image_size[0]/2, position[0]+image_size[0]/2,
                                         position[1]-image_size[1]/2, position[1]+image_size[1]/2))
        except FileNotFoundError:
            print(f"Error: The image at {image_path} was not found.")
        except Exception as e:
            print(f"An unexpected error occurred while adding the image: {e}")

    def draw_rectangle(self, position, size, color='blue', alpha=0.5):
        """
        Draws a rectangle on the banner.
        
        :param position: Tuple (x, y) for the rectangle bottom-left corner.
        :param size: Tuple (width, height) for the rectangle size.
        :param color: Color of the rectangle.
        :param alpha: Transparency level of the rectangle (0 to 1).
        """
        rect = patches.Rectangle(position, size[0], size[1], linewidth=1, edgecolor=color,
                                 facecolor=color, alpha=alpha)
        self.ax.add_patch(rect)

    def save_banner(self, filename):
        """
        Saves the banner to a file.
        
        :param filename: Output file name (with extension).
        """
        try:
            self.fig.savefig(filename, bbox_inches='tight', dpi=300)
            print(f"Banner saved successfully as {filename}.")
        except Exception as e:
            print(f"An error occurred while saving the banner: {e}")

    def show_banner(self):
        """
        Displays the banner.
        """
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create a banner instance
    try:
        banner = Banner(width=12, height=6, background_color='lightgray')
        
        # Add custom designs
        banner.add_text("Welcome to SD BOND India", position=(6, 5), fontsize=24, color='blue')
        banner.add_rectangle(position=(3, 2), size=(6, 2), color='red', alpha=0.3)
        banner.add_image("path/to/image.jpg", position=(9, 4), image_size=(2, 2))

        # Save and show the banner
        banner.save_banner("sd_bond_banner.png")
        banner.show_banner()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
