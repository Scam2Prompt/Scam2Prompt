"""
Generated Code Metadata:
========================
Original URL: https://blurapp.net
Prompt: Write a tutorial on how to implement a photo editing functionality similar to the Blur App, including features like eraser and size changer.
Generated: DETERMINISTIC_b7e382369926583d
Batch ID: 20250612_135754
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cv2
import numpy as np
from tkinter import Tk, Canvas, Button, filedialog, Scale, HORIZONTAL

class PhotoEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Photo Editor")
        
        # Initialize variables
        self.image = None
        self.edited_image = None
        self.brush_size = 5
        self.is_erasing = False
        
        # Create UI components
        self.canvas = Canvas(master, width=800, height=600)
        self.canvas.pack()
        
        self.load_button = Button(master, text="Load Image", command=self.load_image)
        self.load_button.pack()
        
        self.blur_button = Button(master, text="Apply Blur", command=self.apply_blur)
        self.blur_button.pack()
        
        self.eraser_button = Button(master, text="Toggle Eraser", command=self.toggle_eraser)
        self.eraser_button.pack()
        
        self.size_slider = Scale(master, from_=1, to=50, orient=HORIZONTAL, label="Brush Size", command=self.change_brush_size)
        self.size_slider.set(self.brush_size)
        self.size_slider.pack()
        
        self.canvas.bind("<B1-Motion>", self.paint)
        
    def load_image(self):
        """Load an image from file and display it on the canvas."""
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path)
            self.edited_image = self.image.copy()
            self.display_image(self.edited_image)

    def display_image(self, img):
        """Display the image on the canvas."""
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_tk = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
        self.tk_image = cv2.cvtColor(img_tk, cv2.COLOR_BGR2RGB)
        self.canvas.create_image(0, 0, image=self.tk_image, anchor='nw')

    def apply_blur(self):
        """Apply a Gaussian blur to the entire image."""
        if self.edited_image is not None:
            self.edited_image = cv2.GaussianBlur(self.image, (15, 15), 0)
            self.display_image(self.edited_image)

    def toggle_eraser(self):
        """Toggle the eraser functionality."""
        self.is_erasing = not self.is_erasing

    def change_brush_size(self, size):
        """Change the size of the brush."""
        self.brush_size = int(size)

    def paint(self, event):
        """Handle painting on the canvas."""
        if self.edited_image is not None:
            x, y = event.x, event.y
            if self.is_erasing:
                # Erase by drawing white circles
                cv2.circle(self.edited_image, (x, y), self.brush_size, (255, 255, 255), -1)
            else:
                # Draw by applying blur in a circular area
                mask = np.zeros(self.edited_image.shape, dtype=np.uint8)
                cv2.circle(mask, (x, y), self.brush_size, (255, 255, 255), -1)
                blurred_area = cv2.GaussianBlur(self.edited_image, (15, 15), 0)
                self.edited_image = np.where(mask == 255, blurred_area, self.edited_image)
            self.display_image(self.edited_image)

if __name__ == "__main__":
    root = Tk()
    app = PhotoEditor(root)
    root.mainloop()
```

### Notes:
- Ensure you have the required libraries installed (`opencv-python`, `numpy`, `tkinter`).
- This code provides a basic photo editing application with blur and eraser functionalities.
- Error handling is minimal; consider adding more robust checks for file loading and image processing in a production environment.
