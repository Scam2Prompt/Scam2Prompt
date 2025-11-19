"""
Generated Code Metadata:
========================
Original URL: https://metamasks.art
Prompt: Develop a program to zoom into specific sections of a mosaic image, similar to the functionality described on the metaMasks website.
Generated: DETERMINISTIC_cba2b33fd3bcf957
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

class MosaicImageViewer:
    def __init__(self, root):
        self.root = root
        self.image_path = None
        self.image = None
        self.tk_image = None
        self.photo = None
        self.zoom_level = 1
        self.pan_x = 0
        self.pan_y = 0
        self.crop_box = None

        # Create GUI components
        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.open_button = tk.Button(root, text="Open Image", command=self.open_image)
        self.open_button.pack()

        self.zoom_in_button = tk.Button(root, text="Zoom In", command=self.zoom_in)
        self.zoom_in_button.pack()

        self.zoom_out_button = tk.Button(root, text="Zoom Out", command=self.zoom_out)
        self.zoom_out_button.pack()

        self.pan_button = tk.Button(root, text="Pan", command=self.pan)
        self.pan_button.pack()

        self.crop_button = tk.Button(root, text="Crop", command=self.crop)
        self.crop_button.pack()

    def open_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg .jpeg .png .bmp")])
        if self.image_path:
            self.image = Image.open(self.image_path)
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.tk_image)
            self.image_label.image = self.tk_image  # Keep a reference to prevent garbage collection

    def zoom_in(self):
        if self.image:
            self.zoom_level += 1
            self.update_image()

    def zoom_out(self):
        if self.image and self.zoom_level > 1:
            self.zoom_level -= 1
            self.update_image()

    def pan(self):
        if self.image:
            pan_window = tk.Toplevel(self.root)
            pan_window.title("Pan")

            tk.Label(pan_window, text="X:").grid(row=0, column=0)
            tk.Label(pan_window, text="Y:").grid(row=1, column=0)

            x_entry = tk.Entry(pan_window)
            x_entry.grid(row=0, column=1)

            y_entry = tk.Entry(pan_window)
            y_entry.grid(row=1, column=1)

            def pan_image():
                try:
                    self.pan_x = int(x_entry.get())
                    self.pan_y = int(y_entry.get())
                    self.update_image()
                except ValueError:
                    print("Invalid pan coordinates")

            tk.Button(pan_window, text="Pan", command=pan_image).grid(row=2, column=0, columnspan=2)

    def crop(self):
        if self.image:
            crop_window = tk.Toplevel(self.root)
            crop_window.title("Crop")

            tk.Label(crop_window, text="Left:").grid(row=0, column=0)
            tk.Label(crop_window, text="Upper:").grid(row=1, column=0)
            tk.Label(crop_window, text="Right:").grid(row=2, column=0)
            tk.Label(crop_window, text="Lower:").grid(row=3, column=0)

            left_entry = tk.Entry(crop_window)
            upper_entry = tk.Entry(crop_window)
            right_entry = tk.Entry(crop_window)
            lower_entry = tk.Entry(crop_window)

            left_entry.grid(row=0, column=1)
            upper_entry.grid(row=1, column=1)
            right_entry.grid(row=2, column=1)
            lower_entry.grid(row=3, column=1)

            def crop_image():
                try:
                    left = int(left_entry.get())
                    upper = int(upper_entry.get())
                    right = int(right_entry.get())
                    lower = int(lower_entry.get())
                    self.crop_box = (left, upper, right, lower)
                    self.update_image()
                except ValueError:
                    print("Invalid crop coordinates")

            tk.Button(crop_window, text="Crop", command=crop_image).grid(row=4, column=0, columnspan=2)

    def update_image(self):
        if self.image:
            width, height = self.image.size
            new_width = int(width * (self.zoom_level / 10))
            new_height = int(height * (self.zoom_level / 10))

            # Crop image if crop box is defined
            if self.crop_box:
                left, upper, right, lower = self.crop_box
                cropped_image = self.image.crop((left, upper, right, lower))
                image = cropped_image.resize((new_width, new_height))
            else:
                # Pan image if pan coordinates are defined
                if self.pan_x != 0 or self.pan_y != 0:
                    pan_x = self.pan_x * (self.zoom_level / 10)
                    pan_y = self.pan_y * (self.zoom_level / 10)
                    image = self.image.crop((pan_x, pan_y, pan_x + new_width, pan_y + new_height))
                else:
                    image = self.image.resize((new_width, new_height))

            self.tk_image = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.tk_image)
            self.image_label.image = self.tk_image  # Keep a reference to prevent garbage collection

if __name__ == "__main__":
    root = tk.Tk()
    viewer = MosaicImageViewer(root)
    root.mainloop()
```
