"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Create a Python script to model water vapor fireplaces with 3D flame effects, including adjustable color and intensity settings.
Generated: DETERMINISTIC_4c97f57706bf73ac
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import colorchooser
import random


class WaterVaporFireplace:
    def __init__(self, root):
        """
        Initialize the Water Vapor Fireplace object.

        :param root: Tkinter root window
        """
        self.root = root
        self.root.title("Water Vapor Fireplace with 3D Flame Effects")

        # Canvas for rendering flames
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="black")
        self.canvas.pack()

        # Default flame color and intensity
        self.flame_color = "#FF4500"  # Default orange flame color
        self.flame_intensity = 5  # Default intensity (1-10 scale)

        # Control Panel
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack()

        # Add controls for adjusting color and intensity
        self.color_button = tk.Button(
            self.control_frame, text="Choose Flame Color", command=self.change_flame_color
        )
        self.color_button.pack(side=tk.LEFT, padx=10)

        self.intensity_label = tk.Label(self.control_frame, text="Flame Intensity:")
        self.intensity_label.pack(side=tk.LEFT)

        self.intensity_scale = tk.Scale(
            self.control_frame, from_=1, to=10, orient=tk.HORIZONTAL, command=self.change_flame_intensity
        )
        self.intensity_scale.set(self.flame_intensity)
        self.intensity_scale.pack(side=tk.LEFT)

        # Start drawing flames
        self.update_flame()

    def change_flame_color(self):
        """
        Open a color chooser dialog to change the flame color.
        """
        color_code = colorchooser.askcolor(title="Choose Flame Color")[1]
        if color_code:  # Check if color was selected
            self.flame_color = color_code

    def change_flame_intensity(self, value):
        """
        Change the flame intensity based on the slider value.

        :param value: The new intensity value from the slider
        """
        self.flame_intensity = int(value)

    def draw_flame(self):
        """
        Draw the flames on the canvas.
        """
        self.canvas.delete("flames")  # Clear previous flames

        # Generate flame particles
        for _ in range(self.flame_intensity * 20):  # Particle count based on intensity
            x = random.randint(200, 600)  # Random x position within a range
            y = random.randint(400, 600)  # Random y position near the bottom
            radius = random.randint(5, 15)  # Random radius for flame particles
            alpha = random.randint(50, 100) / 100  # Transparency (mocked via color blending)

            # Create flame color with transparency effect
            blended_color = self.canvas.winfo_rgb(self.flame_color)
            blended_color = f"#{int(blended_color[0] * alpha):02x}{int(blended_color[1] * alpha):02x}{int(blended_color[2] * alpha):02x}"

            # Draw flame particle
            self.canvas.create_oval(
                x - radius, y - radius, x + radius, y + radius, fill=blended_color, tags="flames"
            )

    def update_flame(self):
        """
        Update the flame effects continuously.
        """
        self.draw_flame()
        self.root.after(50, self.update_flame)  # Refresh every 50ms


if __name__ == "__main__":
    try:
        root = tk.Tk()
        fireplace = WaterVaporFireplace(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")
```
