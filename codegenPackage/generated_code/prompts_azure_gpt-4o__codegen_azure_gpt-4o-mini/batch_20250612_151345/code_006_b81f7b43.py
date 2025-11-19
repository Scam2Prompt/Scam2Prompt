"""
Generated Code Metadata:
========================
Original URL: https://jsebastiao.com
Prompt: Develop a wireframe generator tool using Python that aligns with the UX design approach highlighted in J. Sebastião's portfolio.
Generated: DETERMINISTIC_b81f7b43227a6185
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class WireframeGenerator:
    def __init__(self, master):
        """Initialize the Wireframe Generator application."""
        self.master = master
        self.master.title("Wireframe Generator")
        self.canvas = tk.Canvas(master, width=800, height=600, bg='white')
        self.canvas.pack()

        # Create a menu for the application
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.clear_canvas)
        self.file_menu.add_command(label="Exit", command=master.quit)

        self.shapes = []  # List to store drawn shapes

        # Bind mouse click event to draw shapes
        self.canvas.bind("<Button-1>", self.draw_shape)

    def clear_canvas(self):
        """Clear the canvas and reset the shapes list."""
        self.canvas.delete("all")
        self.shapes.clear()

    def draw_shape(self, event):
        """Draw a random shape on the canvas at the clicked position."""
        shape_type = random.choice(['rectangle', 'oval', 'line'])
        size = random.randint(50, 150)
        x1, y1 = event.x, event.y
        x2, y2 = x1 + size, y1 + size

        try:
            if shape_type == 'rectangle':
                shape_id = self.canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='lightgray')
            elif shape_type == 'oval':
                shape_id = self.canvas.create_oval(x1, y1, x2, y2, outline='black', fill='lightblue')
            elif shape_type == 'line':
                shape_id = self.canvas.create_line(x1, y1, x2, y2, fill='black', width=2)

            self.shapes.append(shape_id)  # Store the shape ID for future reference
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while drawing the shape: {e}")

    def run(self):
        """Run the main loop of the application."""
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = WireframeGenerator(root)
    app.run()
```
