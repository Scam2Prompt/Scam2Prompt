"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jsebastiao.com
Prompt: Develop a wireframe generator tool using Python that aligns with the UX design approach highlighted in J. Sebastião's portfolio.
Generated: DETERMINISTIC_b81f7b43227a6185
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import colorchooser
from PIL import Image, ImageDraw

class WireframeGenerator:
    def __init__(self, master):
        """Initialize the WireframeGenerator with a Tkinter window."""
        self.master = master
        self.master.title("Wireframe Generator")
        self.canvas = tk.Canvas(master, width=800, height=600, bg='white')
        self.canvas.pack()

        # Menu bar
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Save", command=self.save_wireframe)
        self.file_menu.add_command(label="Clear", command=self.clear_canvas)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)

        # Bind mouse events for drawing
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_rectangle)

        self.start_x = None
        self.start_y = None
        self.current_rectangle = None
        self.rectangles = []

    def start_draw(self, event):
        """Start drawing a rectangle on mouse click."""
        self.start_x = event.x
        self.start_y = event.y
        self.current_rectangle = None

    def draw_rectangle(self, event):
        """Draw a rectangle based on mouse movement."""
        if self.current_rectangle is not None:
            self.canvas.delete(self.current_rectangle)

        # Create the rectangle
        self.current_rectangle = self.canvas.create_rectangle(
            self.start_x, self.start_y, event.x, event.y, outline='black'
        )

    def save_wireframe(self):
        """Save the current wireframe as an image file."""
        try:
            # Create an image from the canvas
            self.canvas.update()  # Ensure canvas is updated
            x = self.master.winfo_x() + self.canvas.winfo_x()
            y = self.master.winfo_y() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()

            # Create a PIL image
            image = Image.new("RGB", (self.canvas.winfo_width(), self.canvas.winfo_height()), "white")
            draw = ImageDraw.Draw(image)

            # Draw all rectangles
            for rect in self.rectangles:
                draw.rectangle(rect, outline="black")

            # Save the image
            file_path = simpledialog.askstring("Save Image", "Enter file name (without extension):")
            if file_path:
                file_path += ".png"
                image.save(file_path)
                messagebox.showinfo("Success", f"Wireframe saved as {file_path}")
            else:
                messagebox.showwarning("Warning", "File name cannot be empty.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving: {e}")

    def clear_canvas(self):
        """Clear the canvas and reset the wireframe."""
        self.canvas.delete("all")
        self.rectangles.clear()

if __name__ == "__main__":
    root = tk.Tk()
    wireframe_generator = WireframeGenerator(root)
    root.mainloop()
```
