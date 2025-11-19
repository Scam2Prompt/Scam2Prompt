"""
Generated Code Metadata:
========================
Original URL: https://metamasks.art
Prompt: Explain how to zoom in on individual masks in a mosaic created with AndreaMosaic software.
Generated: DETERMINISTIC_0bfc171cb11c05f8
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
import cv2
import numpy as np
from tkinter import Tk, filedialog, messagebox
from PIL import Image, ImageTk

class MosaicZoomTool:
    """
    A tool to zoom in on individual masks in a mosaic created with AndreaMosaic.
    Provides functionality to load a mosaic image and its mask files,
    then allows interactive zooming on individual mask regions.
    """
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Mosaic Zoom Tool")
        
        # Initialize variables
        self.mosaic_image = None
        self.mask_files = []
        self.current_mask_index = 0
        self.zoom_factor = 2.0
        
        # Create UI elements
        self.create_ui()
        
    def create_ui(self):
        """Create the user interface components."""
        # Menu bar
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open Mosaic", command=self.load_mosaic)
        file_menu.add_command(label="Open Masks", command=self.load_masks)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # View menu
        view_menu = Menu(menubar, tearoff=0)
        view_menu.add_command(label="Zoom In", command=lambda: self.adjust_zoom(1.2))
        view_menu.add_command(label="Zoom Out", command=lambda: self.adjust_zoom(0.8))
        view_menu.add_command(label="Reset Zoom", command=lambda: self.adjust_zoom(1.0, reset=True))
        menubar.add_cascade(label="View", menu=view_menu)
        
        # Navigation menu
        nav_menu = Menu(menubar, tearoff=0)
        nav_menu.add_command(label="Next Mask", command=self.next_mask)
        nav_menu.add_command(label="Previous Mask", command=self.prev_mask)
        menubar.add_cascade(label="Navigation", menu=nav_menu)
        
        # Image display area
        self.image_label = Label(self.root)
        self.image_label.pack()
        
        # Status bar
        self.status_var = StringVar()
        self.status_bar = Label(self.root, textvariable=self.status_var, relief=SUNKEN, anchor=W)
        self.status_bar.pack(side=BOTTOM, fill=X)
        
    def load_mosaic(self):
        """Load the mosaic image file."""
        file_path = filedialog.askopenfilename(
            title="Select Mosaic Image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
        )
        if file_path:
            try:
                self.mosaic_image = cv2.imread(file_path)
                if self.mosaic_image is None:
                    raise ValueError("Failed to load image")
                self.update_display()
                self.status_var.set(f"Loaded mosaic: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load mosaic image: {str(e)}")
    
    def load_masks(self):
        """Load mask files from a directory."""
        dir_path = filedialog.askdirectory(title="Select Directory Containing Masks")
        if dir_path:
            try:
                self.mask_files = sorted([
                    os.path.join(dir_path, f) 
                    for f in os.listdir(dir_path) 
                    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))
                ])
                self.current_mask_index = 0
                self.status_var.set(f"Loaded {len(self.mask_files)} masks from {os.path.basename(dir_path)}")
                self.update_display()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load masks: {str(e)}")
    
    def next_mask(self):
        """Navigate to the next mask."""
        if self.mask_files:
            self.current_mask_index = (self.current_mask_index + 1) % len(self.mask_files)
            self.update_display()
    
    def prev_mask(self):
        """Navigate to the previous mask."""
        if self.mask_files:
            self.current_mask_index = (self.current_mask_index - 1) % len(self.mask_files)
            self.update_display()
    
    def adjust_zoom(self, factor, reset=False):
        """Adjust the zoom factor."""
        if reset:
            self.zoom_factor = 1.0
        else:
            self.zoom_factor *= factor
            self.zoom_factor = max(0.1, min(self.zoom_factor, 10.0))  # Clamp between 0.1 and 10.0
        self.update_display()
    
    def update_display(self):
        """Update the displayed image based on current mask and zoom."""
        if self.mosaic_image is None or not self.mask_files:
            return
            
        try:
            # Load current mask
            mask = cv2.imread(self.mask_files[self.current_mask_index], cv2.IMREAD_GRAYSCALE)
            if mask is None:
                raise ValueError("Failed to load mask")
            
            # Find contours in the mask
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if not contours:
                raise ValueError("No contours found in mask")
            
            # Get bounding box of the largest contour
            largest_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour)
            
            # Calculate zoomed region
            center_x, center_y = x + w//2, y + h//2
            zoom_w = int(w * self.zoom_factor)
            zoom_h = int(h * self.zoom_factor)
            
            # Ensure zoomed region stays within image bounds
            img_h, img_w = self.mosaic_image.shape[:2]
            x1 = max(0, center_x - zoom_w//2)
            y1 = max(0, center_y - zoom_h//2)
            x2 = min(img_w, center_x + zoom_w//2)
            y2 = min(img_h, center_y + zoom_h//2)
            
            # Extract and display the zoomed region
            zoomed_region = self.mosaic_image[y1:y2, x1:x2]
            
            # Convert to RGB for display
            zoomed_region_rgb = cv2.cvtColor(zoomed_region, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(zoomed_region_rgb)
            img_tk = ImageTk.PhotoImage(img)
            
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk
            
            # Update status
            mask_name = os.path.basename(self.mask_files[self.current_mask_index])
            self.status_var.set(f"Mask {self.current_mask_index + 1}/{len(self.mask_files)}: {mask_name} | Zoom: {self.zoom_factor:.1f}x")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update display: {str(e)}")
    
    def run(self):
        """Run the application."""
        self.root.mainloop()

# Main entry point
if __name__ == "__main__":
    # Fix for Tkinter import issue in some environments
    from tkinter import Menu, Label, StringVar
    
    app = MosaicZoomTool()
    app.run()
```
