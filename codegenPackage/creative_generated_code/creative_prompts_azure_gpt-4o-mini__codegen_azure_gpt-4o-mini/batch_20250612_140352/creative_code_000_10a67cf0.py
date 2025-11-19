"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Generate a code snippet for an airbrush nail art application that utilizes stencils for creating geometric designs, as described on Airstyleart.
Generated: DETERMINISTIC_10a67cf0b46ff271
Batch ID: 20250612_140352
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

class NailArtApp:
    def __init__(self, master):
        """Initialize the Nail Art Application."""
        self.master = master
        self.master.title("Airbrush Nail Art Application")
        
        # Create a canvas for drawing
        self.canvas = tk.Canvas(master, width=400, height=400, bg='white')
        self.canvas.pack()

        # Button to load stencil
        self.load_button = tk.Button(master, text="Load Stencil", command=self.load_stencil)
        self.load_button.pack()

        # Button to clear canvas
        self.clear_button = tk.Button(master, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack()

        # Initialize stencil
        self.stencil_image = None

    def load_stencil(self):
        """Load a stencil image and draw it on the canvas."""
        try:
            file_path = filedialog.askopenfilename(title="Select Stencil Image", 
                                                   filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
            if not file_path:
                return  # No file selected

            # Load stencil image
            self.stencil_image = Image.open(file_path).convert("RGBA")
            self.draw_stencil_on_canvas()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load stencil: {str(e)}")

    def draw_stencil_on_canvas(self):
        """Draw the loaded stencil on the canvas."""
        if self.stencil_image:
            # Convert image to a format suitable for the canvas
            stencil_photo = ImageTk.PhotoImage(self.stencil_image)
            self.canvas.create_image(200, 200, image=stencil_photo)
            self.canvas.image = stencil_photo  # Keep a reference to avoid garbage collection

    def clear_canvas(self):
        """Clear the canvas."""
        self.canvas.delete("all")
        self.stencil_image = None

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = NailArtApp(root)
    
    # Start the Tkinter main event loop
    root.mainloop()
```

### Requirements:
1. Install necessary packages before running the code:
   ```bash
   pip install pillow matplotlib numpy
   ```

2. Stencil images should be in PNG or JPG format for the application to process them.
