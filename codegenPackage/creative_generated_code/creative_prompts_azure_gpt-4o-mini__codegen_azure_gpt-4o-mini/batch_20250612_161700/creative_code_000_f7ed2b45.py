"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kroonation.com
Prompt: Generate a code snippet for a graphic design application that incorporates UI/UX principles as described by Kroo Nation.
Generated: DETERMINISTIC_f7ed2b45e6c8584d
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

class GraphicDesignApp:
    def __init__(self, master):
        """Initialize the main window and its components."""
        self.master = master
        self.master.title("Graphic Design Application")
        self.master.geometry("800x600")

        # Create the menu
        self.menu = tk.Menu(master)
        self.master.config(menu=self.menu)

        # Add File menu with Open and Exit options
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_image)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)
        self.menu.add_cascade(label="File", menu=self.file_menu)

        # Canvas for drawing or displaying images
        self.canvas = tk.Canvas(master, bg="white", width=800, height=500)
        self.canvas.pack(pady=20)

        # Add a button to clear the canvas
        self.clear_button = tk.Button(master, text="Clear", command=self.clear_canvas)
        self.clear_button.pack()

        # Initialize image variable
        self.image = None
        self.image_on_canvas = None

    def open_image(self):
        """Open an image file and display it on the canvas."""
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
            if file_path:
                # Open and display the selected image
                self.image = Image.open(file_path)
                self.display_image()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {e}")

    def display_image(self):
        """Display the loaded image on the canvas."""
        if self.image:
            # Resize image to fit the canvas
            self.image.thumbnail((800, 500))
            self.tk_image = ImageTk.PhotoImage(self.image)

            # Clear the canvas before displaying new image
            self.canvas.delete("all")
            self.image_on_canvas = self.canvas.create_image(400, 250, image=self.tk_image)

    def clear_canvas(self):
        """Clear the canvas and remove any displayed images."""
        self.canvas.delete("all")
        self.image = None

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = GraphicDesignApp(root)
    root.mainloop()
```
