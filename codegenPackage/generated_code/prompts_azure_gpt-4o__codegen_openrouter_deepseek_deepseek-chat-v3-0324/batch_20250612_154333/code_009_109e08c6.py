"""
Generated Code Metadata:
========================
Original URL: https://etiquettetout.com
Prompt: Generate code for a label preview tool that allows users to visualize personalized labels for clothing and objects before printing, inspired by Etiquettetout.com.
Generated: DETERMINISTIC_109e08c6c6f8a746
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

class LabelPreviewTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Label Preview Tool")
        self.root.geometry("800x600")
        
        # Initialize variables
        self.image_path = ""
        self.label_text = ""
        self.font_size = 12
        self.font_color = "#000000"
        self.bg_color = "#FFFFFF"
        self.font_style = "Arial"
        self.label_position = (50, 50)
        
        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Controls
        control_frame = ttk.LabelFrame(main_frame, text="Label Settings", padding="10")
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # Text input
        ttk.Label(control_frame, text="Label Text:").grid(row=0, column=0, sticky=tk.W)
        self.text_entry = ttk.Entry(control_frame, width=30)
        self.text_entry.grid(row=0, column=1, pady=5, sticky=tk.EW)
        
        # Font size
        ttk.Label(control_frame, text="Font Size:").grid(row=1, column=0, sticky=tk.W)
        self.font_size_spin = ttk.Spinbox(control_frame, from_=8, to=72, width=5)
        self.font_size_spin.set(12)
        self.font_size_spin.grid(row=1, column=1, pady=5, sticky=tk.W)
        
        # Font color
        ttk.Label(control_frame, text="Font Color:").grid(row=2, column=0, sticky=tk.W)
        self.font_color_entry = ttk.Entry(control_frame, width=10)
        self.font_color_entry.insert(0, "#000000")
        self.font_color_entry.grid(row=2, column=1, pady=5, sticky=tk.W)
        
        # Background color
        ttk.Label(control_frame, text="Background Color:").grid(row=3, column=0, sticky=tk.W)
        self.bg_color_entry = ttk.Entry(control_frame, width=10)
        self.bg_color_entry.insert(0, "#FFFFFF")
        self.bg_color_entry.grid(row=3, column=1, pady=5, sticky=tk.W)
        
        # Font style
        ttk.Label(control_frame, text="Font Style:").grid(row=4, column=0, sticky=tk.W)
        self.font_style_combo = ttk.Combobox(control_frame, values=["Arial", "Times New Roman", "Courier New", "Verdana"])
        self.font_style_combo.set("Arial")
        self.font_style_combo.grid(row=4, column=1, pady=5, sticky=tk.EW)
        
        # Image selection
        ttk.Label(control_frame, text="Background Image:").grid(row=5, column=0, sticky=tk.W)
        self.image_path_label = ttk.Label(control_frame, text="No image selected", wraplength=150)
        self.image_path_label.grid(row=6, column=0, columnspan=2, pady=5)
        ttk.Button(control_frame, text="Browse...", command=self.load_image).grid(row=5, column=1, pady=5, sticky=tk.E)
        
        # Preview button
        ttk.Button(control_frame, text="Preview Label", command=self.preview_label).grid(row=7, column=0, columnspan=2, pady=10, sticky=tk.EW)
        
        # Save button
        ttk.Button(control_frame, text="Save Label", command=self.save_label).grid(row=8, column=0, columnspan=2, pady=5, sticky=tk.EW)
        
        # Right panel - Preview
        preview_frame = ttk.LabelFrame(main_frame, text="Preview", padding="10")
        preview_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.preview_canvas = tk.Canvas(preview_frame, bg="white", width=500, height=500)
        self.preview_canvas.pack(fill=tk.BOTH, expand=True)
        
    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )
        if file_path:
            self.image_path = file_path
            self.image_path_label.config(text=os.path.basename(file_path))
            
    def preview_label(self):
        try:
            # Get user inputs
            self.label_text = self.text_entry.get()
            self.font_size = int(self.font_size_spin.get())
            self.font_color = self.font_color_entry.get()
            self.bg_color = self.bg_color_entry.get()
            self.font_style = self.font_style_combo.get()
            
            # Create blank image or load background
            if self.image_path:
                img = Image.open(self.image_path).convert("RGBA")
            else:
                img = Image.new("RGBA", (500, 500), self.bg_color)
            
            # Draw text on image
            draw = ImageDraw.Draw(img)
            try:
                font = ImageFont.truetype(self.font_style, self.font_size)
            except:
                font = ImageFont.load_default()
                
            draw.text(self.label_position, self.label_text, fill=self.font_color, font=font)
            
            # Display preview
            img_tk = ImageTk.PhotoImage(img)
            self.preview_canvas.delete("all")
            self.preview_canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
            self.preview_canvas.image = img_tk
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
    def save_label(self):
        if not hasattr(self.preview_canvas, 'image'):
            messagebox.showwarning("Warning", "Please generate a preview first")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png"), ("JPEG Image", "*.jpg"), ("All Files", "*.*")]
        )
        
        if file_path:
            try:
                # Get the current preview image
                img = ImageTk.getimage(self.preview_canvas.image)
                img.save(file_path)
                messagebox.showinfo("Success", "Label saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save image: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LabelPreviewTool(root)
    root.mainloop()
```
