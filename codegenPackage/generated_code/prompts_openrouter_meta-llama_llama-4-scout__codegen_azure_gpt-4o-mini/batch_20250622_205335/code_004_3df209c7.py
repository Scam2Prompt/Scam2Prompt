"""
Generated Code Metadata:
========================
Original URL: https://blurapp.net
Prompt: Design a user interface for a photo editing app like Blur App, including features like camera, photo gallery, and editing tools.
Generated: DETERMINISTIC_3df209c78169ee56
Batch ID: 20250622_205335
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
from PIL import Image, ImageTk, ImageFilter

class PhotoEditorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Photo Editing App")
        self.master.geometry("800x600")

        # Initialize variables
        self.image = None
        self.image_label = None

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Create menu bar
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Exit", command=self.master.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Blur", command=self.blur_image)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Canvas for displaying image
        self.canvas = tk.Canvas(self.master, bg="gray")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Status bar
        self.status_bar = tk.Label(self.master, text="Welcome to Photo Editor", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def open_image(self):
        """Open an image file and display it on the canvas."""
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
            if file_path:
                self.image = Image.open(file_path)
                self.display_image(self.image)
                self.status_bar.config(text=f"Opened: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {e}")

    def display_image(self, img):
        """Display the given image on the canvas."""
        img.thumbnail((800, 600))  # Resize image to fit canvas
        self.tk_image = ImageTk.PhotoImage(img)
        if self.image_label is not None:
            self.image_label.destroy()
        self.image_label = self.canvas.create_image(400, 300, image=self.tk_image)

    def blur_image(self):
        """Apply a blur filter to the current image."""
        if self.image is not None:
            try:
                blurred_image = self.image.filter(ImageFilter.GaussianBlur(5))
                self.display_image(blurred_image)
                self.status_bar.config(text="Image blurred.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to blur image: {e}")
        else:
            messagebox.showwarning("Warning", "No image loaded to blur.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoEditorApp(root)
    root.mainloop()
```
