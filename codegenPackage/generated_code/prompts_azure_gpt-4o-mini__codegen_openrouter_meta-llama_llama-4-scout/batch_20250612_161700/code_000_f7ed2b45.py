"""
Generated Code Metadata:
========================
Original URL: https://kroonation.com
Prompt: Generate a code snippet for a graphic design application that incorporates UI/UX principles as described by Kroo Nation.
Generated: DETERMINISTIC_f7ed2b45e6c8584d
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import tkinter as tk
from tkinter import filedialog, messagebox

class GraphicDesignApp:
    """
    A simple graphic design application that incorporates UI/UX principles.

    Attributes:
        root (tkinter.Tk): The root window of the application.
        canvas (tkinter.Canvas): The canvas for drawing and designing.
        filename (str): The filename of the current design file.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Graphic Design App")
        self.root.geometry("800x600")

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Create a file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_design)
        self.file_menu.add_command(label="Open", command=self.open_design)
        self.file_menu.add_command(label="Save", command=self.save_design)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Create a canvas for drawing and designing
        self.canvas = tk.Canvas(self.root, width=800, height=550)
        self.canvas.pack()

        # Initialize the filename
        self.filename = None

        # Bind events to the canvas
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<Button-1>", self.start_drawing)

        # Initialize the drawing variables
        self.drawing = False
        self.last_x, self.last_y = 0, 0

    def new_design(self):
        """
        Create a new design file.
        """
        self.filename = None
        self.canvas.delete("all")

    def open_design(self):
        """
        Open an existing design file.
        """
        self.filename = filedialog.askopenfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg *.jpeg")],
        )
        if self.filename:
            try:
                # Load the image and display it on the canvas
                # For simplicity, this example assumes that the image can be loaded using PIL
                from PIL import Image, ImageTk
                image = Image.open(self.filename)
                photo = ImageTk.PhotoImage(image)
                self.canvas.create_image(0, 0, image=photo, anchor="nw")
                self.canvas.image = photo  # Keep a reference to prevent garbage collection
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def save_design(self):
        """
        Save the current design file.
        """
        if not self.filename:
            self.filename = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg *.jpeg")],
            )
        if self.filename:
            try:
                # Save the canvas as an image
                # For simplicity, this example assumes that the image can be saved using PIL
                from PIL import ImageGrab
                x = self.root.winfo_rootx() + self.canvas.winfo_x()
                y = self.root.winfo_rooty() + self.canvas.winfo_y()
                x1 = x + self.canvas.winfo_width()
                y1 = y + self.canvas.winfo_height()
                ImageGrab.grab().crop((x, y, x1, y1)).save(self.filename)
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def start_drawing(self, event):
        """
        Start drawing on the canvas.

        Args:
            event (tkinter.Event): The event that triggered this method.
        """
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        """
        Draw a line on the canvas.

        Args:
            event (tkinter.Event): The event that triggered this method.
        """
        if self.drawing:
            self.canvas.create_line((self.last_x, self.last_y, event.x, event.y),
                                    width=5, fill="black", capstyle=tk.ROUND,
                                    smooth=True, splinesteps=36)
            self.last_x, self.last_y = event.x, event.y

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphicDesignApp(root)
    root.mainloop()
```
