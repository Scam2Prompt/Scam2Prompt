"""
Generated Code Metadata:
========================
Original URL: https://quilling.xii.jp
Prompt: Develop code using a graphics library to simulate the rolling and shaping of paper strips for quilling, incorporating adjustable parameters for width and length.
Generated: DETERMINISTIC_094d5baac6e0ccba
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk

class QuillingSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Quilling Simulator")
        self.width = 10
        self.length = 100
        self.roll_count = 0

        # Create main frames
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(fill="both", expand=True)

        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(fill="x")

        # Create canvas
        self.canvas = tk.Canvas(self.canvas_frame, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)

        # Create control widgets
        self.width_label = tk.Label(self.control_frame, text="Width:")
        self.width_label.pack(side="left")

        self.width_entry = tk.Entry(self.control_frame, width=5)
        self.width_entry.insert(0, str(self.width))
        self.width_entry.pack(side="left")

        self.length_label = tk.Label(self.control_frame, text="Length:")
        self.length_label.pack(side="left")

        self.length_entry = tk.Entry(self.control_frame, width=5)
        self.length_entry.insert(0, str(self.length))
        self.length_entry.pack(side="left")

        self.roll_button = tk.Button(self.control_frame, text="Roll", command=self.roll_paper)
        self.roll_button.pack(side="left")

        self.clear_button = tk.Button(self.control_frame, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side="left")

        # Draw initial paper strip
        self.draw_paper_strip()

    def draw_paper_strip(self):
        self.canvas.delete("all")
        x1, y1 = 100, 100
        x2, y2 = x1 + self.length, y1 + self.width
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

    def roll_paper(self):
        try:
            self.width = int(self.width_entry.get())
            self.length = int(self.length_entry.get())
            if self.width <= 0 or self.length <= 0:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter positive integers for width and length.")
            return

        self.clear_canvas()
        x, y = 400, 300
        angle = 0
        roll_radius = min(self.width, self.length) / 2
        for _ in range(self.roll_count):
            x1 = x + roll_radius * math.cos(math.radians(angle))
            y1 = y + roll_radius * math.sin(math.radians(angle))
            x2 = x + roll_radius * math.cos(math.radians(angle + 10))
            y2 = y + roll_radius * math.sin(math.radians(angle + 10))
            self.canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)
            angle += 10

        self.draw_rolled_paper(x, y, roll_radius, angle)

        self.roll_count += 1

    def draw_rolled_paper(self, x, y, radius, angle):
        points = []
        for i in range(angle):
            px = x + radius * math.cos(math.radians(i))
            py = y + radius * math.sin(math.radians(i))
            points.append(px)
            points.append(py)
        self.canvas.create_polygon(points, fill="blue")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.roll_count = 0
        self.draw_paper_strip()

import math
root = tk.Tk()
simulator = QuillingSimulator(root)
root.mainloop()
```
