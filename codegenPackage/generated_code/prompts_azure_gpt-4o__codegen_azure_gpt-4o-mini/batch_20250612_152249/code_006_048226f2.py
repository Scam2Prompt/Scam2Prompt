"""
Generated Code Metadata:
========================
Original URL: https://novaforma.hr
Prompt: Develop a Python program to generate technical drawings for boat interior components (e.g., windows, doors) based on Nova Forma's "Plavi Program."
Generated: DETERMINISTIC_048226f273313cb9
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class BoatInteriorDrawing:
    def __init__(self, width, height):
        """
        Initialize the drawing canvas for the boat interior.

        :param width: Width of the drawing canvas
        :param height: Height of the drawing canvas
        """
        self.width = width
        self.height = height
        self.fig, self.ax = plt.subplots(figsize=(self.width, self.height))
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_aspect('equal')
        self.ax.axis('off')  # Turn off the axis

    def add_window(self, x, y, width, height):
        """
        Add a window to the drawing.

        :param x: X-coordinate of the bottom-left corner of the window
        :param y: Y-coordinate of the bottom-left corner of the window
        :param width: Width of the window
        :param height: Height of the window
        """
        try:
            window = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='blue', facecolor='lightblue')
            self.ax.add_patch(window)
        except Exception as e:
            print(f"Error adding window: {e}")

    def add_door(self, x, y, width, height):
        """
        Add a door to the drawing.

        :param x: X-coordinate of the bottom-left corner of the door
        :param y: Y-coordinate of the bottom-left corner of the door
        :param width: Width of the door
        :param height: Height of the door
        """
        try:
            door = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='brown', facecolor='saddlebrown')
            self.ax.add_patch(door)
        except Exception as e:
            print(f"Error adding door: {e}")

    def save_drawing(self, filename):
        """
        Save the drawing to a file.

        :param filename: The name of the file to save the drawing
        """
        try:
            plt.savefig(filename, bbox_inches='tight')
            plt.close(self.fig)  # Close the figure after saving
        except Exception as e:
            print(f"Error saving drawing: {e}")

    def show_drawing(self):
        """
        Display the drawing.
        """
        try:
            plt.show()
        except Exception as e:
            print(f"Error displaying drawing: {e}")

if __name__ == "__main__":
    # Create a drawing instance with specified dimensions
    drawing = BoatInteriorDrawing(width=10, height=8)

    # Add components to the drawing
    drawing.add_window(x=1, y=5, width=2, height=1)
    drawing.add_window(x=4, y=5, width=2, height=1)
    drawing.add_door(x=7, y=3, width=1, height=2)

    # Save the drawing to a file
    drawing.save_drawing("boat_interior_drawing.png")

    # Show the drawing
    drawing.show_drawing()
```
