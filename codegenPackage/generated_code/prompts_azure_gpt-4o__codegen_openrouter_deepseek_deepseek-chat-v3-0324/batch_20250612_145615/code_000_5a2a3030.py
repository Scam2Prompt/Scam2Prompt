"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Write code to generate a printable template for customized clothing labels, incorporating user input for name, font style, and label size, as described on Labelmystuff.com.
Generated: DETERMINISTIC_5a2a3030a09be6ce
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import font, messagebox, filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os

class ClothingLabelGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Clothing Label Generator")
        self.root.geometry("800x600")
        
        # Default values
        self.name_text = "Your Name"
        self.font_style = "Arial"
        self.font_size = 24
        self.label_width = 300
        self.label_height = 150
        self.text_color = "#000000"
        self.bg_color = "#FFFFFF"
        
        # Initialize UI
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Controls
        control_frame = tk.Frame(main_frame)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        # Name input
        tk.Label(control_frame, text="Name:").pack(anchor=tk.W)
        self.name_entry = tk.Entry(control_frame, width=30)
        self.name_entry.pack(pady=5)
        self.name_entry.insert(0, self.name_text)
        
        # Font style
        tk.Label(control_frame, text="Font Style:").pack(anchor=tk.W)
        self.font_style_var = tk.StringVar(value=self.font_style)
        font_styles = ["Arial", "Times New Roman", "Courier New", "Helvetica", "Verdana"]
        self.font_menu = tk.OptionMenu(control_frame, self.font_style_var, *font_styles)
        self.font_menu.pack(pady=5)
        
        # Font size
        tk.Label(control_frame, text="Font Size:").pack(anchor=tk.W)
        self.font_size_slider = tk.Scale(
            control_frame, from_=10, to=72, orient=tk.HORIZONTAL, 
            command=self.update_preview
        )
        self.font_size_slider.set(self.font_size)
        self.font_size_slider.pack(pady=5)
        
        # Label size
        tk.Label(control_frame, text="Label Width:").pack(anchor=tk.W)
        self.width_slider = tk.Scale(
            control_frame, from_=100, to=500, orient=tk.HORIZONTAL,
            command=self.update_preview
        )
        self.width_slider.set(self.label_width)
        self.width_slider.pack(pady=5)
        
        tk.Label(control_frame, text="Label Height:").pack(anchor=tk.W)
        self.height_slider = tk.Scale(
            control_frame, from_=50, to=300, orient=tk.HORIZONTAL,
            command=self.update_preview
        )
        self.height_slider.set(self.label_height)
        self.height_slider.pack(pady=5)
        
        # Color selection
        tk.Label(control_frame, text="Text Color:").pack(anchor=tk.W)
        self.text_color_entry = tk.Entry(control_frame, width=10)
        self.text_color_entry.insert(0, self.text_color)
        self.text_color_entry.pack(pady=5)
        
        tk.Label(control_frame, text="Background Color:").pack(anchor=tk.W)
        self.bg_color_entry = tk.Entry(control_frame, width=10)
        self.bg_color_entry.insert(0, self.bg_color)
        self.bg_color_entry.pack(pady=5)
        
        # Generate button
        generate_btn = tk.Button(
            control_frame, text="Generate Label", 
            command=self.generate_label
        )
        generate_btn.pack(pady=20)
        
        # Right panel - Preview
        preview_frame = tk.Frame(main_frame, relief=tk.SUNKEN, borderwidth=2)
        preview_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)
        
        self.preview_label = tk.Label(preview_frame)
        self.preview_label.pack(expand=True, padx=10, pady=10)
        
        # Initial preview update
        self.update_preview()
        
        # Bind events
        self.name_entry.bind("<KeyRelease>", lambda e: self.update_preview())
        self.font_style_var.trace_add("write", lambda *args: self.update_preview())
        self.text_color_entry.bind("<KeyRelease>", lambda e: self.update_preview())
        self.bg_color_entry.bind("<KeyRelease>", lambda e: self.update_preview())
    
    def update_preview(self, *args):
        try:
            # Get current values
            self.name_text = self.name_entry.get()
            self.font_style = self.font_style_var.get()
            self.font_size = self.font_size_slider.get()
            self.label_width = self.width_slider.get()
            self.label_height = self.height_slider.get()
            self.text_color = self.text_color_entry.get()
            self.bg_color = self.bg_color_entry.get()
            
            # Create preview image
            img = Image.new("RGB", (self.label_width, self.label_height), self.bg_color)
            draw = ImageDraw.Draw(img)
            
            try:
                font_obj = ImageFont.truetype(self.font_style, self.font_size)
            except:
                font_obj = ImageFont.load_default()
            
            # Calculate text position
            text_width, text_height = draw.textsize(self.name_text, font=font_obj)
            x = (self.label_width - text_width) / 2
            y = (self.label_height - text_height) / 2
            
            # Draw text
            draw.text((x, y), self.name_text, fill=self.text_color, font=font_obj)
            
            # Convert to Tkinter PhotoImage
            img_tk = ImageTk.PhotoImage(img)
            self.preview_label.config(image=img_tk)
            self.preview_label.image = img_tk
            
        except Exception as e:
            messagebox.showerror("Error", f"Error updating preview: {str(e)}")
    
    def generate_label(self):
        try:
            # Get save location
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
                title="Save Label As"
            )
            
            if not file_path:
                return
                
            # Create final image
            img = Image.new("RGB", (self.label_width, self.label_height), self.bg_color)
            draw = ImageDraw.Draw(img)
            
            try:
                font_obj = ImageFont.truetype(self.font_style, self.font_size)
            except:
                font_obj = ImageFont.load_default()
            
            # Calculate text position
            text_width, text_height = draw.textsize(self.name_text, font=font_obj)
            x = (self.label_width - text_width) / 2
            y = (self.label_height - text_height) / 2
            
            # Draw text
            draw.text((x, y), self.name_text, fill=self.text_color, font=font_obj)
            
            # Save image
            img.save(file_path)
            messagebox.showinfo("Success", f"Label saved successfully to:\n{file_path}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error generating label: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ClothingLabelGenerator(root)
    root.mainloop()
```
