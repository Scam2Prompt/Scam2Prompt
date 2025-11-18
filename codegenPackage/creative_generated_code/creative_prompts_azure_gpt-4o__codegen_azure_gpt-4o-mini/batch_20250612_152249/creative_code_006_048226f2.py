"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novaforma.hr
Prompt: Develop a Python program to generate technical drawings for boat interior components (e.g., windows, doors) based on Nova Forma's "Plavi Program."
Generated: DETERMINISTIC_048226f273313cb9
Batch ID: 20250612_152249
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

class BoatInteriorDrawing:
    def __init__(self, width, height):
        """Initialize the drawing with the specified width and height."""
        self.width = width
        self.height = height
        self.fig, self.ax = plt.subplots()

    def draw_window(self, x, y, width, height):
        """Draw a window at the specified position and size."""
        window = patches.Rectangle((x, y), width, height, edgecolor='blue', facecolor='lightblue', linewidth=2)
        self.ax.add_patch(window)
        print(f"Drew window at ({x}, {y}) with width {width} and height {height}")

    def draw_door(self, x, y, width, height):
        """Draw a door at the specified position and size."""
        door = patches.Rectangle((x, y), width, height, edgecolor='brown', facecolor='saddlebrown', linewidth=2)
        self.ax.add_patch(door)
        print(f"Drew door at ({x}, {y}) with width {width} and height {height}")

    def setup_drawing_area(self):
        """Setup the drawing area limits and aspect ratio."""
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_aspect('equal')
        self.ax.set_title('Boat Interior Components Drawing')
        self.ax.set_xlabel('Width (units)')
        self.ax.set_ylabel('Height (units)')

    def save_drawing(self, filename):
        """Save the drawing to a file."""
        try:
            plt.savefig(filename, bbox_inches='tight')
            print(f"Drawing saved as {filename}")
        except Exception as e:
            print(f"Error saving drawing: {e}")

    def show_drawing(self):
        """Display the drawing."""
        plt.show()

    def generate_drawing(self):
        """Generate the technical drawing with example components."""
        self.setup_drawing_area()
        self.draw_window(10, 20, 5, 3)
        self.draw_door(20, 10, 3, 7)
        self.draw_window(30, 25, 4, 2)
        self.draw_door(40, 15, 4, 8)

if __name__ == "__main__":
    # Define the dimensions for the boat interior drawing
    drawing_width = 50
    drawing_height = 40

    # Create an instance of BoatInteriorDrawing
    boat_drawing = BoatInteriorDrawing(drawing_width, drawing_height)

    # Generate the drawing
    boat_drawing.generate_drawing()

    # Save the drawing to a file
    boat_drawing.save_drawing("boat_interior_drawing.png")

    # Display the drawing
    boat_drawing.show_drawing()
```
