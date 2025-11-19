"""
Generated Code Metadata:
========================
Original URL: https://titlebelts.au
Prompt: Generate a Python script that allows users to customize their own championship belt design using the features available on Title Belts AU.
Generated: DETERMINISTIC_b6079f48652c1444
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk, colorchooser, messagebox, filedialog
from PIL import Image, ImageTk, ImageDraw
import json
import os

class ChampionshipBeltDesigner:
    """A GUI application for designing custom championship belts."""
    
    def __init__(self, root):
        """Initialize the main application window."""
        self.root = root
        self.root.title("Title Belts AU - Championship Belt Designer")
        self.root.geometry("1000x800")
        self.root.resizable(True, True)
        
        # Default belt properties
        self.belt_properties = {
            "base_color": "#FFD700",
            "plate_color": "#000000",
            "text_color": "#FFFFFF",
            "text": "CHAMPION",
            "font_size": 24,
            "plate_count": 3,
            "plate_shape": "oval",
            "badge_image": None
        }
        
        # Available plate shapes
        self.plate_shapes = ["oval", "rectangle", "diamond"]
        
        # Initialize UI
        self.create_widgets()
        self.load_defaults()
        
    def create_widgets(self):
        """Create and arrange all GUI components."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Design controls
        control_frame = ttk.LabelFrame(main_frame, text="Design Controls", padding="10")
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # Right panel - Preview
        preview_frame = ttk.LabelFrame(main_frame, text="Belt Preview", padding="10")
        preview_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Canvas for belt preview
        self.canvas = tk.Canvas(preview_frame, bg="white", width=700, height=500)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Color selection controls
        ttk.Label(control_frame, text="Base Color:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.base_color_btn = ttk.Button(control_frame, text="Choose", command=lambda: self.choose_color("base_color"))
        self.base_color_btn.grid(row=0, column=1, pady=2)
        
        ttk.Label(control_frame, text="Plate Color:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.plate_color_btn = ttk.Button(control_frame, text="Choose", command=lambda: self.choose_color("plate_color"))
        self.plate_color_btn.grid(row=1, column=1, pady=2)
        
        ttk.Label(control_frame, text="Text Color:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.text_color_btn = ttk.Button(control_frame, text="Choose", command=lambda: self.choose_color("text_color"))
        self.text_color_btn.grid(row=2, column=1, pady=2)
        
        # Text customization
        ttk.Label(control_frame, text="Belt Text:").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.text_entry = ttk.Entry(control_frame)
        self.text_entry.grid(row=3, column=1, pady=2)
        
        # Font size
        ttk.Label(control_frame, text="Font Size:").grid(row=4, column=0, sticky=tk.W, pady=2)
        self.font_size = ttk.Spinbox(control_frame, from_=8, to=72, width=5)
        self.font_size.grid(row=4, column=1, pady=2)
        
        # Plate count
        ttk.Label(control_frame, text="Plate Count:").grid(row=5, column=0, sticky=tk.W, pady=2)
        self.plate_count = ttk.Spinbox(control_frame, from_=1, to=5, width=5)
        self.plate_count.grid(row=5, column=1, pady=2)
        
        # Plate shape
        ttk.Label(control_frame, text="Plate Shape:").grid(row=6, column=0, sticky=tk.W, pady=2)
        self.plate_shape = ttk.Combobox(control_frame, values=self.plate_shapes, state="readonly")
        self.plate_shape.grid(row=6, column=1, pady=2)
        
        # Badge image
        ttk.Label(control_frame, text="Badge Image:").grid(row=7, column=0, sticky=tk.W, pady=2)
        self.badge_btn = ttk.Button(control_frame, text="Upload", command=self.upload_badge)
        self.badge_btn.grid(row=7, column=1, pady=2)
        self.clear_badge_btn = ttk.Button(control_frame, text="Clear", command=self.clear_badge)
        self.clear_badge_btn.grid(row=7, column=2, pady=2)
        
        # Action buttons
        ttk.Button(control_frame, text="Update Preview", command=self.update_preview).grid(row=8, column=0, columnspan=3, pady=10)
        ttk.Button(control_frame, text="Save Design", command=self.save_design).grid(row=9, column=0, columnspan=3, pady=5)
        ttk.Button(control_frame, text="Load Design", command=self.load_design).grid(row=10, column=0, columnspan=3, pady=5)
        ttk.Button(control_frame, text="Reset to Defaults", command=self.load_defaults).grid(row=11, column=0, columnspan=3, pady=5)
        ttk.Button(control_frame, text="Export Image", command=self.export_image).grid(row=12, column=0, columnspan=3, pady=5)
        
    def choose_color(self, color_type):
        """Open color chooser dialog and update the specified color property."""
        color = colorchooser.askcolor(title=f"Choose {color_type.replace('_', ' ').title()}")[1]
        if color:
            self.belt_properties[color_type] = color
            self.update_preview()
    
    def upload_badge(self):
        """Open file dialog to upload a badge image."""
        file_path = filedialog.askopenfilename(
            title="Select Badge Image",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
        )
        if file_path:
            try:
                # Resize and keep reference to avoid garbage collection
                img = Image.open(file_path)
                img.thumbnail((100, 100))
                self.belt_properties["badge_image"] = img
                self.update_preview()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def clear_badge(self):
        """Remove the current badge image."""
        self.belt_properties["badge_image"] = None
        self.update_preview()
    
    def update_preview(self):
        """Update the belt preview canvas with current design."""
        try:
            # Get current properties from UI
            self.belt_properties["text"] = self.text_entry.get()
            self.belt_properties["font_size"] = int(self.font_size.get())
            self.belt_properties["plate_count"] = int(self.plate_count.get())
            self.belt_properties["plate_shape"] = self.plate_shape.get()
            
            # Create a blank image for the belt
            width, height = 700, 200
            belt_img = Image.new("RGB", (width, height), self.belt_properties["base_color"])
            draw = ImageDraw.Draw(belt_img)
            
            # Draw the belt strap
            draw.rectangle([0, 50, width, 150], fill=self.belt_properties["base_color"])
            
            # Calculate plate positions
            plate_width = 100
            spacing = (width - (self.belt_properties["plate_count"] * plate_width)) // (self.belt_properties["plate_count"] + 1)
            
            # Draw plates
            for i in range(self.belt_properties["plate_count"]):
                x1 = spacing + i * (plate_width + spacing)
                y1 = 25
                x2 = x1 + plate_width
                y2 = y1 + 150
                
                # Draw plate based on shape
                if self.belt_properties["plate_shape"] == "oval":
                    draw.ellipse([x1, y1, x2, y2], fill=self.belt_properties["plate_color"])
                elif self.belt_properties["plate_shape"] == "rectangle":
