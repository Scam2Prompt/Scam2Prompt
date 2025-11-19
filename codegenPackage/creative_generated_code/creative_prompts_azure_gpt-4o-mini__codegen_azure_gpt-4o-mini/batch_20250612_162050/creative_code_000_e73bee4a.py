"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://robertoabajo.es
Prompt: Generate a code snippet that creates a virtual art gallery showcasing abstract paintings, similar to the exhibitions mentioned on Roberto Abajo's website.
Generated: DETERMINISTIC_e73bee4af1b716c7
Batch ID: 20250612_162050
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
from PIL import Image, ImageTk
import os

class VirtualArtGallery:
    def __init__(self, root):
        """Initialize the virtual art gallery."""
        self.root = root
        self.root.title("Virtual Art Gallery")
        
        # Load images from the 'artworks' directory
        self.artworks = self.load_artworks("artworks")
        self.current_index = 0
        
        # Create a canvas for displaying artworks
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        # Create navigation buttons
        self.prev_button = tk.Button(root, text="Previous", command=self.show_previous)
        self.prev_button.pack(side=tk.LEFT, padx=10)
        
        self.next_button = tk.Button(root, text="Next", command=self.show_next)
        self.next_button.pack(side=tk.RIGHT, padx=10)

        # Display the first artwork
        self.display_artwork()

    def load_artworks(self, directory):
        """Load images from the specified directory."""
        artworks = []
        try:
            for filename in os.listdir(directory):
                if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    artworks.append(os.path.join(directory, filename))
            if not artworks:
                raise FileNotFoundError("No images found in the directory.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load artworks: {e}")
        return artworks

    def display_artwork(self):
        """Display the current artwork on the canvas."""
        if self.artworks:
            img_path = self.artworks[self.current_index]
            try:
                image = Image.open(img_path)
                image = image.resize((800, 600), Image.ANTIALIAS)
                self.photo = ImageTk.PhotoImage(image)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
                self.root.title(f"Artwork {self.current_index + 1} of {len(self.artworks)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to display artwork: {e}")

    def show_next(self):
        """Show the next artwork in the gallery."""
        if self.artworks:
            self.current_index = (self.current_index + 1) % len(self.artworks)
            self.display_artwork()

    def show_previous(self):
        """Show the previous artwork in the gallery."""
        if self.artworks:
            self.current_index = (self.current_index - 1) % len(self.artworks)
            self.display_artwork()

if __name__ == "__main__":
    # Create the main window and run the gallery application
    root = tk.Tk()
    gallery = VirtualArtGallery(root)
    root.mainloop()
```

**Note**: Make sure to have a directory named "artworks" containing your abstract painting images in the same location where you run this script. The script uses the `Pillow` library for image handling, so ensure it's installed by running `pip install Pillow`.
