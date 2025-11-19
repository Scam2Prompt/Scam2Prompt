"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Generate a code snippet for an airbrush nail art application that utilizes stencils for creating geometric designs, as described on Airstyleart.
Generated: DETERMINISTIC_10a67cf0b46ff271
Batch ID: 20250612_140352
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
from PIL import Image, ImageTk, ImageDraw

class AirbrushNailArtApp:
    def __init__(self, root):
        """
        Initialize the Airbrush Nail Art Application.
        :param root: The main Tkinter window.
        """
        self.root = root
        self.root.title("Airbrush Nail Art Application")
        self.canvas_width = 400
        self.canvas_height = 400

        # Initialize canvas and stencil variables
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()
        self.stencil_image = None
        self.stencil_path = None

        # Add buttons for user interaction
        self.create_buttons()

    def create_buttons(self):
        """
        Create buttons for loading stencils and applying designs.
        """
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        load_stencil_button = tk.Button(button_frame, text="Load Stencil", command=self.load_stencil)
        load_stencil_button.pack(side=tk.LEFT, padx=5)

        apply_design_button = tk.Button(button_frame, text="Apply Design", command=self.apply_design)
        apply_design_button.pack(side=tk.LEFT, padx=5)

        clear_canvas_button = tk.Button(button_frame, text="Clear Canvas", command=self.clear_canvas)
        clear_canvas_button.pack(side=tk.LEFT, padx=5)

    def load_stencil(self):
        """
        Load a stencil image from the user's file system.
        """
        try:
            self.stencil_path = filedialog.askopenfilename(
                title="Select Stencil Image",
                filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")]
            )
            if not self.stencil_path:
                return  # User canceled the file dialog

            # Load and display the stencil image
            stencil = Image.open(self.stencil_path)
            stencil.thumbnail((self.canvas_width, self.canvas_height))  # Resize to fit canvas
            self.stencil_image = ImageTk.PhotoImage(stencil)
            self.canvas.create_image(self.canvas_width // 2, self.canvas_height // 2, image=self.stencil_image)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load stencil: {e}")

    def apply_design(self):
        """
        Apply a geometric design using the loaded stencil.
        """
        if not self.stencil_path:
            messagebox.showwarning("Warning", "Please load a stencil first.")
            return

        try:
            # Create a new image for the design
            design_image = Image.new("RGBA", (self.canvas_width, self.canvas_height), (255, 255, 255, 0))
            draw = ImageDraw.Draw(design_image)

            # Draw geometric shapes (example: circles and rectangles)
            draw.rectangle([50, 50, 150, 150], fill="blue", outline="black")
            draw.ellipse([200, 200, 300, 300], fill="red", outline="black")

            # Overlay the stencil on the design
            stencil = Image.open(self.stencil_path).convert("RGBA")
            stencil.thumbnail((self.canvas_width, self.canvas_height))
            design_image.paste(stencil, (0, 0), stencil)

            # Display the final design on the canvas
            final_design = ImageTk.PhotoImage(design_image)
            self.canvas.create_image(self.canvas_width // 2, self.canvas_height // 2, image=final_design)
            self.canvas.image = final_design  # Keep a reference to avoid garbage collection
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply design: {e}")

    def clear_canvas(self):
        """
        Clear the canvas to start a new design.
        """
        self.canvas.delete("all")
        self.stencil_image = None
        self.stencil_path = None

if __name__ == "__main__":
    root = tk.Tk()
    app = AirbrushNailArtApp(root)
    root.mainloop()
```
