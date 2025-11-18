"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etiquettetout.com
Prompt: Generate code for a label preview tool that allows users to visualize personalized labels for clothing and objects before printing, inspired by Etiquettetout.com.
Generated: DETERMINISTIC_109e08c6c6f8a746
Batch ID: 20250612_154333
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
from PIL import Image, ImageDraw, ImageFont

class LabelPreviewTool:
    def __init__(self, root):
        """Initialize the Label Preview Tool."""
        self.root = root
        self.root.title("Label Preview Tool")
        self.label_text = tk.StringVar()
        self.font_size = tk.IntVar(value=20)

        self.create_widgets()

    def create_widgets(self):
        """Create and place widgets on the GUI."""
        tk.Label(self.root, text="Enter Label Text:").pack(pady=10)
        tk.Entry(self.root, textvariable=self.label_text).pack(pady=5)

        tk.Label(self.root, text="Font Size:").pack(pady=10)
        tk.Scale(self.root, variable=self.font_size, from_=10, to=100, orient=tk.HORIZONTAL).pack(pady=5)

        tk.Button(self.root, text="Preview", command=self.preview_label).pack(pady=10)
        tk.Button(self.root, text="Save as Image", command=self.save_label_image).pack(pady=10)

        self.preview_canvas = tk.Canvas(self.root, width=300, height=150, bg="white")
        self.preview_canvas.pack(pady=20)

    def preview_label(self):
        """Display the label preview on the canvas."""
        label = self.label_text.get()
        if not label:
            messagebox.showwarning("Input Error", "Please enter some text for the label.")
            return

        font_size = self.font_size.get()
        self.preview_canvas.delete("all")  # Clear previous previews
        self.draw_label(label, font_size)

    def draw_label(self, text, font_size):
        """Draw the label text on the canvas."""
        # Create an image to draw on
        img = Image.new('RGB', (300, 150), color='white')
        draw = ImageDraw.Draw(img)

        # Load a default font or fallback to a basic one
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        # Calculate text size and position
        text_width, text_height = draw.textsize(text, font)
        text_x = (img.width - text_width) / 2
        text_y = (img.height - text_height) / 2

        # Draw the text on the image
        draw.text((text_x, text_y), text, fill="black", font=font)

        # Convert the image to a format suitable for the canvas
        self.img_tk = self.pil_image_to_tk(img)
        self.preview_canvas.create_image(0, 0, anchor=tk.NW, image=self.img_tk)

    def pil_image_to_tk(self, img):
        """Convert a PIL image to a format suitable for Tkinter."""
        return ImageTk.PhotoImage(img)

    def save_label_image(self):
        """Save the current label image as a file."""
        label = self.label_text.get()
        if not label:
            messagebox.showwarning("Input Error", "Please enter some text for the label before saving.")
            return
        
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                   filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.create_and_save_image(label, self.font_size.get(), file_path)

    def create_and_save_image(self, text, font_size, file_path):
        """Create an image from the label text and save it to a file."""
        img = Image.new('RGB', (300, 150), color='white')
        draw = ImageDraw.Draw(img)

        # Load a default font or fallback to a basic one
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        # Calculate text size and position
        text_width, text_height = draw.textsize(text, font)
        text_x = (img.width - text_width) / 2
        text_y = (img.height - text_height) / 2

        # Draw the text on the image
        draw.text((text_x, text_y), text, fill="black", font=font)

        # Save the image
        img.save(file_path)
        messagebox.showinfo("Success", f"Label saved successfully as {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LabelPreviewTool(root)
    root.mainloop()
```
