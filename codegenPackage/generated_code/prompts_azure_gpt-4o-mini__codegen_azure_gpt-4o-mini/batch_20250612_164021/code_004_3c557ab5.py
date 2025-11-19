"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: Develop a simple application that helps users learn basic drawing skills, inspired by the drawing courses at Ânima Academia de Arte.
Generated: DETERMINISTIC_3c557ab5ad689ca7
Batch ID: 20250612_164021
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

class DrawingApp:
    def __init__(self, master):
        """Initialize the drawing application."""
        self.master = master
        self.master.title("Basic Drawing Skills App")
        
        # Create a canvas for drawing
        self.canvas = tk.Canvas(master, bg="white", width=800, height=600)
        self.canvas.pack()

        # Initialize drawing variables
        self.last_x, self.last_y = None, None
        self.color = "black"
        self.brush_size = 2

        # Bind mouse events to canvas
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        # Create a menu for additional options
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)

        # Add options to the menu
        self.options_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Options", menu=self.options_menu)
        self.options_menu.add_command(label="Change Color", command=self.change_color)
        self.options_menu.add_command(label="Change Brush Size", command=self.change_brush_size)
        self.options_menu.add_separator()
        self.options_menu.add_command(label="Clear Canvas", command=self.clear_canvas)

    def start_drawing(self, event):
        """Start drawing on the canvas."""
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        """Draw on the canvas while the mouse is moved with the button pressed."""
        if self.last_x is not None and self.last_y is not None:
            try:
                self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.color, width=self.brush_size)
                self.last_x, self.last_y = event.x, event.y
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while drawing: {e}")

    def stop_drawing(self, event):
        """Stop drawing when the mouse button is released."""
        self.last_x, self.last_y = None, None

    def change_color(self):
        """Change the drawing color."""
        color = simpledialog.askstring("Input", "Enter a color name or hex code (e.g., 'red' or '#ff0000'):")
        if color:
            self.color = color

    def change_brush_size(self):
        """Change the brush size."""
        size = simpledialog.askinteger("Input", "Enter brush size (1-10):", minvalue=1, maxvalue=10)
        if size:
            self.brush_size = size

    def clear_canvas(self):
        """Clear the canvas."""
        self.canvas.delete("all")

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = DrawingApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while starting the application: {e}")
```
