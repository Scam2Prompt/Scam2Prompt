"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Develop a simple application that helps users learn basic drawing skills, inspired by the drawing courses at Ânima Academia de Arte.
Generated: DETERMINISTIC_3c557ab5ad689ca7
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import messagebox

# Basic Drawing Application inspired by Ânima Academia de Arte

class DrawingApp:
    def __init__(self, root):
        """
        Initialize the drawing application.
        :param root: Tkinter root window.
        """
        self.root = root
        self.root.title("Basic Drawing Skills - Ânima Academia de Arte")
        
        # Canvas for drawing
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Instruction label
        self.instruction_label = tk.Label(
            root, text="Click and drag to draw. Press 'Clear Canvas' to start over.",
            font=("Arial", 12)
        )
        self.instruction_label.pack(pady=10)

        # Button to clear the canvas
        self.clear_button = tk.Button(root, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack(pady=5)

        # Mouse bindings
        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)

        # Initialize variables to store drawing state
        self.start_x = None
        self.start_y = None

    def start_draw(self, event):
        """
        Triggered when the user clicks on the canvas to start drawing.
        :param event: Tkinter event object containing mouse position.
        """
        self.start_x = event.x
        self.start_y = event.y

    def draw(self, event):
        """
        Triggered when the user drags the mouse on the canvas to draw.
        :param event: Tkinter event object containing mouse position.
        """
        # Draw a line from the last position to the current position
        self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill="black", width=2)
        self.start_x = event.x
        self.start_y = event.y

    def clear_canvas(self):
        """
        Clear the entire canvas.
        """
        result = messagebox.askyesno("Clear Canvas", "Are you sure you want to clear the canvas?")
        if result:  # Clear canvas only if user confirms
            self.canvas.delete("all")


# Main entry point for the application
if __name__ == "__main__":
    # Create the root Tkinter window
    root = tk.Tk()

    # Initialize and run the drawing app
    app = DrawingApp(root)
    root.mainloop()
```
