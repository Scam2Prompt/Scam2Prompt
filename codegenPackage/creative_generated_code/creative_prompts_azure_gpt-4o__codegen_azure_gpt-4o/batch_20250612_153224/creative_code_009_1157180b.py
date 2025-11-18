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
# Import necessary libraries
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Define the main application class
class TimberGalleryApp:
    def __init__(self, root):
        """
        Initialize the application, create the GUI components, and load the gallery.
        
        :param root: The Tkinter root window.
        """
        self.root = root
        self.root.title("Timber Products Gallery - Askar Trading International")
        self.root.geometry("800x600")
        
        # Create a frame for navigation
        self.nav_frame = tk.Frame(self.root, bg="#f0f0f0", height=50)
        self.nav_frame.pack(side=tk.TOP, fill=tk.X)
        
        # Create a frame for the gallery
        self.gallery_frame = tk.Frame(self.root, bg="white")
        self.gallery_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
        # Buttons for navigation
        self.btn_softwood = tk.Button(self.nav_frame, text="Softwood", command=lambda: self.load_gallery("softwood"))
        self.btn_softwood.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.btn_hardwood = tk.Button(self.nav_frame, text="Hardwood", command=lambda: self.load_gallery("hardwood"))
        self.btn_hardwood.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.btn_sawn_timber = tk.Button(self.nav_frame, text="Sawn Timber", command=lambda: self.load_gallery("sawn_timber"))
        self.btn_sawn_timber.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Default gallery display
        self.current_category = None
        self.image_labels = []
        self.load_gallery("softwood")
    
    def load_gallery(self, category):
        """
        Load and display images for the selected category.

        :param category: The category of timber products (softwood, hardwood, sawn_timber)
        """
        self.current_category = category
        self.clear_gallery()
        
        # Path to images (you can customize this based on your directory structure)
        image_folder = os.path.join("timber_images", category)
        
        try:
            # Get all image files in the specified directory
            image_files = [f for f in os.listdir(image_folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
            
            if not image_files:
                messagebox.showinfo("No Images Found", f"No images found for category: {category}")
                return
            
            # Display images in gallery
            for img_file in image_files:
                img_path = os.path.join(image_folder, img_file)
                self.display_image(img_path)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def clear_gallery(self):
        """
        Clear the gallery frame to prepare for new images.
        """
        for widget in self.gallery_frame.winfo_children():
            widget.destroy()
        self.image_labels.clear()
        
    def display_image(self, img_path):
        """
        Display a single image in the gallery.

        :param img_path: Path to the image file.
        """
        try:
            # Open image and resize it to fit in the gallery
            img = Image.open(img_path)
            img.thumbnail((200, 200))  # Resize to thumbnail
            img_tk = ImageTk.PhotoImage(img)
            
            # Create a label to display the image
            img_label = tk.Label(self.gallery_frame, image=img_tk, bg="white")
            img_label.image = img_tk  # Reference to avoid garbage collection
            img_label.pack(side=tk.LEFT, padx=10, pady=10)
            
            self.image_labels.append(img_label)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load image {img_path}: {str(e)}")

# Main driver code
if __name__ == "__main__":
    # Create the application window
    root = tk.Tk()
    
    # Create an instance of the gallery application
    app = TimberGalleryApp(root)
    
    # Start the main loop
    root.mainloop()
```

### Notes:
1. You need to ensure that the directory structure exists, with subdirectories `softwood`, `hardwood`, and `sawn_timber` under `timber_images` containing the relevant images.
2. The dependencies `Pillow` (for image handling) must be installed. Use `pip install pillow` if not already installed.
3. The code includes error handling for file operations and unexpected issues with image loading.
