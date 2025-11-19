"""
Generated Code Metadata:
========================
Original URL: https://sdbondindia.com
Prompt: Develop a program to create banner designs and ADS boards as described in SD BOND India's latest projects, ensuring flexibility in customization.
Generated: DETERMINISTIC_f1193e1feab68425
Batch ID: 20250612_153225
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
import json

class BannerDesigner:
    def __init__(self, root):
        self.root = root
        self.root.title("SD BOND India - Banner & ADS Designer")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        
        # Default settings
        self.settings = {
            "width": 800,
            "height": 400,
            "bg_color": "#FFFFFF",
            "text": "Sample Text",
            "text_color": "#000000",
            "font": "Arial",
            "font_size": 24,
            "image_path": "",
            "output_dir": "output",
            "recent_projects": []
        }
        
        # Load settings if config exists
        self.load_settings()
        
        # Initialize UI
        self.init_ui()
        
    def init_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Controls
        control_frame = ttk.LabelFrame(main_frame, text="Design Controls", padding="10")
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # Right panel - Preview
        preview_frame = ttk.LabelFrame(main_frame, text="Preview", padding="10")
        preview_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Preview canvas
        self.preview_canvas = tk.Canvas(preview_frame, bg="white", width=self.settings["width"], height=self.settings["height"])
        self.preview_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Size controls
        size_frame = ttk.Frame(control_frame)
        size_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(size_frame, text="Width:").pack(side=tk.LEFT)
        self.width_var = tk.IntVar(value=self.settings["width"])
        ttk.Spinbox(size_frame, from_=100, to=5000, increment=50, textvariable=self.width_var, width=8).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(size_frame, text="Height:").pack(side=tk.LEFT, padx=(10,0))
        self.height_var = tk.IntVar(value=self.settings["height"])
        ttk.Spinbox(size_frame, from_=100, to=5000, increment=50, textvariable=self.height_var, width=8).pack(side=tk.LEFT, padx=5)
        
        # Background color
        bg_frame = ttk.Frame(control_frame)
        bg_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(bg_frame, text="Background:").pack(side=tk.LEFT)
        self.bg_color_var = tk.StringVar(value=self.settings["bg_color"])
        ttk.Entry(bg_frame, textvariable=self.bg_color_var, width=10).pack(side=tk.LEFT, padx=5)
        ttk.Button(bg_frame, text="Pick", command=self.pick_bg_color).pack(side=tk.LEFT)
        
        # Text controls
        text_frame = ttk.LabelFrame(control_frame, text="Text", padding="5")
        text_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(text_frame, text="Content:").pack(anchor=tk.W)
        self.text_var = tk.StringVar(value=self.settings["text"])
        ttk.Entry(text_frame, textvariable=self.text_var).pack(fill=tk.X, pady=2)
        
        ttk.Label(text_frame, text="Color:").pack(anchor=tk.W)
        self.text_color_var = tk.StringVar(value=self.settings["text_color"])
        ttk.Entry(text_frame, textvariable=self.text_color_var, width=10).pack(side=tk.LEFT, pady=2)
        ttk.Button(text_frame, text="Pick", command=self.pick_text_color).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(text_frame, text="Font:").pack(anchor=tk.W)
        font_frame = ttk.Frame(text_frame)
        font_frame.pack(fill=tk.X)
        
        self.font_var = tk.StringVar(value=self.settings["font"])
        ttk.Combobox(font_frame, textvariable=self.font_var, values=["Arial", "Times New Roman", "Courier New", "Verdana", "Impact"], state="readonly").pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        ttk.Label(font_frame, text="Size:").pack(side=tk.LEFT, padx=(10,0))
        self.font_size_var = tk.IntVar(value=self.settings["font_size"])
        ttk.Spinbox(font_frame, from_=8, to=120, increment=2, textvariable=self.font_size_var, width=5).pack(side=tk.LEFT)
        
        # Image controls
        image_frame = ttk.LabelFrame(control_frame, text="Image", padding="5")
        image_frame.pack(fill=tk.X, pady=5)
        
        self.image_path_var = tk.StringVar(value=self.settings["image_path"])
        ttk.Button(image_frame, text="Add Image", command=self.add_image).pack(fill=tk.X, pady=2)
        ttk.Button(image_frame, text="Remove Image", command=self.remove_image).pack(fill=tk.X, pady=2)
        
        # Action buttons
        action_frame = ttk.Frame(control_frame)
        action_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(action_frame, text="Update Preview", command=self.update_preview).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)
        ttk.Button(action_frame, text="Save Design", command=self.save_design).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)
        
        # Recent projects
        recent_frame = ttk.LabelFrame(control_frame, text="Recent Projects", padding="5")
        recent_frame.pack(fill=tk.BOTH, expand=True)
        
        self.recent_listbox = tk.Listbox(recent_frame)
        self.recent_listbox.pack(fill=tk.BOTH, expand=True)
        self.update_recent_list()
        
        ttk.Button(recent_frame, text="Load Selected", command=self.load_selected_project).pack(fill=tk.X, pady=2)
        
        # Bind events
        self.width_var.trace_add("write", lambda *args: self.update_preview())
        self.height_var.trace_add("write", lambda *args: self.update_preview())
        self.bg_color_var.trace_add("write", lambda *args: self.update_preview())
        self.text_var.trace_add("write", lambda *args: self.update_preview())
        self.text_color_var.trace_add("write", lambda *args: self.update_preview())
        self.font_var.trace_add("write", lambda *args: self.update_preview())
        self.font_size_var.trace_add("write", lambda *args: self.update_preview())
        
        # Initial preview
        self.update_preview()
    
    def pick_bg_color(self):
        color = tk.colorchooser.askcolor(title="Choose Background Color", initialcolor=self.bg_color_var.get())
        if color[1]:
            self.bg_color_var.set(color[1])
    
    def pick_text_color(self):
        color = tk.colorchooser.askcolor(title="Choose Text Color", initialcolor=self.text_color_var.get())
        if color[1]:
            self.text_color_var.set(color[1])
    
    def add_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
        )
        if file_path:
            self.image_path_var.set(file_path)
            self.update_preview()
    
    def remove_image(self):
        self.image_path_var.set("")
        self.update_preview()
    
    def update_preview(self):
        try:
            # Create blank image
            width = self.width_var.get()
            height = self.height_var.get()
            bg_color = self.bg_color_var.get()
            
            img = Image.new("RGB", (width, height), bg_color)
            draw = ImageDraw.Draw(img)
            
            # Add text
            text = self.text_var.get()
            if text:
                try:
                    font = ImageFont.truetype(self.font_var.get(), self.font_size_var.get())
                except:
                    font = ImageFont.load_default()
                
                text_color =
