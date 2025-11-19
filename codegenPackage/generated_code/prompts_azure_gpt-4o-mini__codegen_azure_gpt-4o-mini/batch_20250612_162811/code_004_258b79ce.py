"""
Generated Code Metadata:
========================
Original URL: https://monadmakeyournft.vercel.app
Prompt: Generate a script that allows users to save their drawings as PNG or JPG files using the Monad Whiteboard NFT tools.
Generated: DETERMINISTIC_258b79ce1eaacc53
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monad Whiteboard NFT Tool")
        
        # Canvas for drawing
        self.canvas = tk.Canvas(root, bg='white', width=800, height=600)
        self.canvas.pack()

        # Initialize drawing variables
        self.last_x, self.last_y = None, None
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Save button
        self.save_button = tk.Button(root, text="Save Drawing", command=self.save_drawing)
        self.save_button.pack()

    def start_draw(self, event):
        """Start drawing on the canvas."""
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        """Draw on the canvas."""
        if self.last_x is not None and self.last_y is not None:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill='black', width=2)
            self.last_x, self.last_y = event.x, event.y

    def reset(self, event):
        """Reset the last coordinates after drawing."""
        self.last_x, self.last_y = None, None

    def save_drawing(self):
        """Save the current drawing as a PNG or JPG file."""
        # Get file format from user
        file_format = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"),
                                                                ("JPEG files", "*.jpg;*.jpeg"),
                                                                ("All files", "*.*")])
        if not file_format:
            return  # User cancelled the save dialog

        # Create an image from the canvas
        try:
            self.canvas.update()  # Ensure the canvas is updated
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()

            # Capture the canvas as an image
            image = Image.new("RGB", (self.canvas.winfo_width(), self.canvas.winfo_height()), "white")
            draw = ImageDraw.Draw(image)
            for item in self.canvas.find_all():
                coords = self.canvas.coords(item)
                if self.canvas.type(item) == "line":
                    draw.line(coords, fill='black', width=2)

            # Save the image
            image.save(file_format)
            messagebox.showinfo("Success", "Drawing saved successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the drawing: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
```
