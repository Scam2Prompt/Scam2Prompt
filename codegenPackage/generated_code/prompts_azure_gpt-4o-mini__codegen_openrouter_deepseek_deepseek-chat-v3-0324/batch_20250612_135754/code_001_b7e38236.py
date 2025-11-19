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
import tkinter as tk
from tkinter import filedialog, Scale, messagebox
from PIL import Image, ImageTk, ImageFilter

class PhotoEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Editor - Blur & Erase")
        
        # Initialize variables
        self.original_image = None
        self.edited_image = None
        self.display_image = None
        self.blur_radius = 10
        self.brush_size = 20
        self.is_erasing = False
        self.last_x = None
        self.last_y = None
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Menu
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save", command=self.save_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)
        
        # Toolbar Frame
        toolbar_frame = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        toolbar_frame.pack(side=tk.TOP, fill=tk.X)
        
        # Buttons
        blur_btn = tk.Button(toolbar_frame, text="Blur", command=self.apply_blur)
        blur_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        erase_btn = tk.Button(toolbar_frame, text="Erase", command=self.toggle_erase)
        erase_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        reset_btn = tk.Button(toolbar_frame, text="Reset", command=self.reset_image)
        reset_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Sliders
        blur_slider = Scale(toolbar_frame, from_=0, to=50, orient=tk.HORIZONTAL, 
                           label="Blur Radius", command=self.update_blur_radius)
        blur_slider.set(self.blur_radius)
        blur_slider.pack(side=tk.LEFT, padx=5, pady=2)
        
        brush_slider = Scale(toolbar_frame, from_=1, to=100, orient=tk.HORIZONTAL, 
                            label="Brush Size", command=self.update_brush_size)
        brush_slider.set(self.brush_size)
        brush_slider.pack(side=tk.LEFT, padx=5, pady=2)
        
        # Canvas for image display
        self.canvas = tk.Canvas(self.root, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Bind mouse events
        self.canvas.bind("<ButtonPress-1>", self.start_erase)
        self.canvas.bind("<B1-Motion>", self.erase)
        self.canvas.bind("<ButtonRelease-1>", self.stop_erase)
        
    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
        if file_path:
            try:
                self.original_image = Image.open(file_path)
                self.edited_image = self.original_image.copy()
                self.display_image = ImageTk.PhotoImage(self.edited_image)
                self.canvas.config(width=self.edited_image.width, height=self.edited_image.height)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=self.display_image)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open image: {str(e)}")
    
    def save_image(self):
        if self.edited_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", 
                                                    filetypes=[("PNG", "*.png"), 
                                                              ("JPEG", "*.jpg"), 
                                                              ("BMP", "*.bmp")])
            if file_path:
                try:
                    self.edited_image.save(file_path)
                    messagebox.showinfo("Success", "Image saved successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save image: {str(e)}")
    
    def apply_blur(self):
        if self.edited_image:
            try:
                # Convert to OpenCV format for faster processing
                cv_image = np.array(self.edited_image)
                cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
                
                # Apply Gaussian blur
                blurred = cv2.GaussianBlur(cv_image, (0, 0), self.blur_radius)
                
                # Convert back to PIL format
                self.edited_image = Image.fromarray(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
                self.update_canvas()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to apply blur: {str(e)}")
    
    def toggle_erase(self):
        self.is_erasing = not self.is_erasing
        if self.is_erasing:
            self.canvas.config(cursor="circle")
        else:
            self.canvas.config(cursor="cross")
    
    def start_erase(self, event):
        if self.is_erasing and self.edited_image:
            self.last_x = event.x
            self.last_y = event.y
    
    def erase(self, event):
        if self.is_erasing and self.edited_image and self.last_x is not None and self.last_y is not None:
            try:
                # Create a mask for the eraser
                mask = Image.new("L", self.edited_image.size, 0)
                draw = ImageDraw.Draw(mask)
                
                # Draw a line from last position to current position
                draw.line([(self.last_x, self.last_y), (event.x, event.y)], 
                         fill=255, width=self.brush_size)
                
                # Create a circle at current position
                draw.ellipse([(event.x - self.brush_size/2, event.y - self.brush_size/2),
                             (event.x + self.brush_size/2, event.y + self.brush_size/2)], 
                            fill=255)
                
                # Composite the original image with the edited image using the mask
                self.edited_image = Image.composite(
                    self.original_image, 
                    self.edited_image, 
                    mask
                )
                
                self.last_x = event.x
                self.last_y = event.y
                self.update_canvas()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to erase: {str(e)}")
    
    def stop_erase(self, event):
        self.last_x = None
        self.last_y = None
    
    def update_blur_radius(self, value):
        self.blur_radius = int(value)
    
    def update_brush_size(self, value):
        self.brush_size = int(value)
    
    def reset_image(self):
        if self.original_image:
            self.edited_image = self.original_image.copy()
            self.update_canvas()
    
    def update_canvas(self):
        if self.edited_image:
            self.display_image = ImageTk.PhotoImage(self.edited_image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.display_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoEditorApp(root)
    root.mainloop()
```
