"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: Write a tutorial on how to create a comic book page layout, referencing the comic art courses available at Ânima.
Generated: DETERMINISTIC_47f39ba35b21d63d
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# comic_page_layout.py

"""
This script provides a simple tutorial on how to create a comic book page layout.
It references comic art courses available at Ânima for further learning.
"""

class ComicPage:
    def __init__(self, width, height):
        """
        Initializes a new comic page with specified dimensions.

        Parameters:
        width (int): The width of the comic page in pixels.
        height (int): The height of the comic page in pixels.
        """
        self.width = width
        self.height = height
        self.panels = []

    def add_panel(self, x, y, width, height):
        """
        Adds a panel to the comic page.

        Parameters:
        x (int): The x-coordinate of the panel's top-left corner.
        y (int): The y-coordinate of the panel's top-left corner.
        width (int): The width of the panel in pixels.
        height (int): The height of the panel in pixels.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Panel dimensions must be positive values.")
        if x < 0 or y < 0 or x + width > self.width or y + height > self.height:
            raise ValueError("Panel position and size must fit within the comic page dimensions.")
        
        panel = {'x': x, 'y': y, 'width': width, 'height': height}
        self.panels.append(panel)

    def display_layout(self):
        """
        Displays the layout of the comic page with its panels.
        """
        print(f"Comic Page Layout ({self.width}x{self.height}):")
        for i, panel in enumerate(self.panels):
            print(f"Panel {i + 1}: Position ({panel['x']}, {panel['y']}), Size ({panel['width']}x{panel['height']})")

def main():
    """
    Main function to create a comic page and add panels to it.
    """
    try:
        # Create a comic page of size 800x1200 pixels
        comic_page = ComicPage(800, 1200)

        # Add panels to the comic page
        comic_page.add_panel(50, 50, 300, 400)  # Panel 1
        comic_page.add_panel(400, 50, 300, 400)  # Panel 2
        comic_page.add_panel(50, 500, 650, 600)  # Panel 3

        # Display the layout of the comic page
        comic_page.display_layout()

        # Reference to comic art courses at Ânima
        print("\nFor more detailed tutorials on comic art, check out the courses available at Ânima.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
