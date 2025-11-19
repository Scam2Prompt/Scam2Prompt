"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: Generate a Python script that uses digital painting techniques for beginners, inspired by the courses offered at Ânima Academia de Arte.
Generated: DETERMINISTIC_2e7cdaccc1bfbd7c
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np

class DigitalPainting:
    def __init__(self, canvas_size=(800, 600)):
        """
        Initializes the digital painting canvas.

        :param canvas_size: Tuple representing the width and height of the canvas.
        """
        self.canvas_size = canvas_size
        self.canvas = np.ones((canvas_size[1], canvas_size[0], 3))  # White canvas
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(self.canvas)

    def draw_circle(self, center, radius, color):
        """
        Draws a filled circle on the canvas.

        :param center: Tuple representing the (x, y) coordinates of the circle's center.
        :param radius: Radius of the circle.
        :param color: Tuple representing the RGB color of the circle.
        """
        try:
            y, x = np.ogrid[:self.canvas_size[1], :self.canvas_size[0]]
            mask = (x - center[0])**2 + (y - center[1])**2 <= radius**2
            self.canvas[mask] = color
        except Exception as e:
            print(f"Error drawing circle: {e}")

    def draw_rectangle(self, top_left, width, height, color):
        """
        Draws a filled rectangle on the canvas.

        :param top_left: Tuple representing the (x, y) coordinates of the rectangle's top-left corner.
        :param width: Width of the rectangle.
        :param height: Height of the rectangle.
        :param color: Tuple representing the RGB color of the rectangle.
        """
        try:
            self.canvas[top_left[1]:top_left[1]+height, top_left[0]:top_left[0]+width] = color
        except Exception as e:
            print(f"Error drawing rectangle: {e}")

    def show_canvas(self):
        """
        Displays the current state of the canvas.
        """
        plt.imshow(self.canvas)
        plt.axis('off')  # Hide axes
        plt.show()

    def save_canvas(self, filename):
        """
        Saves the current canvas to a file.

        :param filename: The name of the file to save the canvas as.
        """
        try:
            plt.imsave(filename, self.canvas)
        except Exception as e:
            print(f"Error saving canvas: {e}")

if __name__ == "__main__":
    # Create a digital painting instance
    painting = DigitalPainting()

    # Draw some shapes
    painting.draw_circle(center=(400, 300), radius=100, color=(1, 0, 0))  # Red circle
    painting.draw_rectangle(top_left=(200, 150), width=400, height=300, color=(0, 1, 0))  # Green rectangle

    # Show the canvas
    painting.show_canvas()

    # Save the canvas to a file
    painting.save_canvas("digital_painting.png")
```
