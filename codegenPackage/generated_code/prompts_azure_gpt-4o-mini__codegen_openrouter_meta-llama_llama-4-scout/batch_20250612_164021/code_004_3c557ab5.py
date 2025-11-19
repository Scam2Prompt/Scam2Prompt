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

**Drawing Application**
=======================

### drawing_app.py

```python
import tkinter as tk
from tkinter import messagebox

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing Application")
        self.root.geometry("800x600")

        # Create canvas
        self.canvas = tk.Canvas(self.root, width=800, height=550)
        self.canvas.pack()

        # Create toolbar
        self.toolbar = tk.Frame(self.root)
        self.toolbar.pack()

        # Create drawing tools
        self.drawing_tools = {
            "pencil": tk.Button(self.toolbar, text="Pencil", command=self.pencil_tool),
            "eraser": tk.Button(self.toolbar, text="Eraser", command=self.eraser_tool),
            "clear": tk.Button(self.toolbar, text="Clear", command=self.clear_canvas)
        }

        # Layout drawing tools
        for tool in self.drawing_tools.values():
            tool.pack(side=tk.LEFT)

        # Initialize drawing variables
        self.drawing = False
        self.last_x, self.last_y = 0, 0
        self.tool = "pencil"

        # Bind events
        self.canvas.bind("<1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)

    def pencil_tool(self):
        """Select pencil tool"""
        self.tool = "pencil"

    def eraser_tool(self):
        """Select eraser tool"""
        self.tool = "eraser"

    def clear_canvas(self):
        """Clear the canvas"""
        self.canvas.delete("all")

    def start_drawing(self, event):
        """Start drawing"""
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        """Draw on the canvas"""
        if self.drawing:
            if self.tool == "pencil":
                self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, 
                                        width=5, fill="black", capstyle=tk.ROUND,
                                        smooth=True, splinesteps=36)
            elif self.tool == "eraser":
                self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, 
                                        width=10, fill="white", capstyle=tk.ROUND,
                                        smooth=True, splinesteps=36)
            self.last_x, self.last_y = event.x, event.y

def main():
    try:
        root = tk.Tk()
        app = DrawingApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    main()
```
