"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atilumber.com
Prompt: Create a visualization tool for displaying the gallery of timber products, including softwood, hardwood, and sawn timber, as showcased on the Askar Trading International website.
Generated: DETERMINISTIC_1157180b88251125
Batch ID: 20250612_153224
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
import os
from PIL import Image, ImageTk

class TimberGalleryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Timber Products Gallery")
        
        # Set window size
        self.master.geometry("800x600")
        
        # Create a canvas for displaying images
        self.canvas = tk.Canvas(self.master, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Create a navigation frame
        self.nav_frame = tk.Frame(self.master)
        self.nav_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Buttons to load different categories of timber
        self.softwood_button = tk.Button(self.nav_frame, text="Load Softwood", command=lambda: self.load_images('softwood'))
        self.softwood_button.pack(side=tk.LEFT)
        
        self.hardwood_button = tk.Button(self.nav_frame, text="Load Hardwood", command=lambda: self.load_images('hardwood'))
        self.hardwood_button.pack(side=tk.LEFT)
        
        self.sawn_button = tk.Button(self.nav_frame, text="Load Sawn Timber", command=lambda: self.load_images('sawn'))
        self.sawn_button.pack(side=tk.LEFT)
        
        # List to hold image file paths
        self.images = []
        self.current_image_index = 0
        
        # Bind keys for navigation
        self.master.bind("<Right>", self.next_image)
        self.master.bind("<Left>", self.previous_image)

    def load_images(self, timber_type):
        """Load images from the selected timber type directory."""
        try:
            # Replace with the appropriate directory path
            directory = os.path.join('timber_gallery', timber_type)
            if not os.path.isdir(directory):
                raise FileNotFoundError(f"Directory not found: {directory}")

            # Clear previous images
            self.images.clear()
            self.current_image_index = 0
            
            # Load images from the directory
            for filename in os.listdir(directory):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    self.images.append(os.path.join(directory, filename))
            
            if not self.images:
                messagebox.showwarning("No Images", "No images found in the selected category.")
                return
            
            self.show_image()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_image(self):
        """Display the current image on the canvas."""
        if self.images:
            img_path = self.images[self.current_image_index]
            img = Image.open(img_path)
            img.thumbnail((800, 600))  # Resize image to fit canvas
            self.photo = ImageTk.PhotoImage(img)
            self.canvas.create_image(400, 300, image=self.photo)

    def next_image(self, event):
        """Show the next image in the gallery."""
        if self.images:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.show_image()

    def previous_image(self, event):
        """Show the previous image in the gallery."""
        if self.images:
            self.current_image_index = (self.current_image_index - 1) % len(self.images)
            self.show_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = TimberGalleryApp(root)
    root.mainloop()
```
