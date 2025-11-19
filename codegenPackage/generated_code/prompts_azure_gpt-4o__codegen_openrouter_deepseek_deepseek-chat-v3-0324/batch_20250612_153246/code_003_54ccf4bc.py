"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: Write a program that simulates a custom furniture design tool, allowing users to select materials (e.g., Olyna), colors, and shapes for outdoor furniture, inspired by Nodo Italia's customization options.
Generated: DETERMINISTIC_54ccf4bc3d0f6f1c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import json
import os

class FurnitureDesignTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Furniture Design Tool")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        
        # Load configuration
        self.load_config()
        
        # Initialize UI
        self.setup_ui()
        
        # Current design state
        self.current_design = {
            "material": "",
            "color": "",
            "shape": "",
            "accessories": []
        }
        
    def load_config(self):
        """Load configuration from JSON file"""
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        try:
            with open(config_path, "r") as f:
                self.config = json.load(f)
        except FileNotFoundError:
            messagebox.showerror("Error", "Configuration file not found")
            self.root.destroy()
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid configuration file")
            self.root.destroy()
    
    def setup_ui(self):
        """Set up the main UI components"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - customization options
        left_panel = ttk.Frame(main_frame, padding="10", width=300)
        left_panel.pack(side=tk.LEFT, fill=tk.Y)
        
        # Right panel - preview
        right_panel = ttk.Frame(main_frame, padding="10")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Material selection
        ttk.Label(left_panel, text="Material", font=('Helvetica', 12, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        self.material_var = tk.StringVar()
        material_combo = ttk.Combobox(
            left_panel, 
            textvariable=self.material_var,
            values=[mat["name"] for mat in self.config["materials"]],
            state="readonly"
        )
        material_combo.pack(fill=tk.X, pady=(0, 10))
        material_combo.bind("<<ComboboxSelected>>", self.update_material)
        
        # Color selection
        ttk.Label(left_panel, text="Color", font=('Helvetica', 12, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        self.color_var = tk.StringVar()
        self.color_combo = ttk.Combobox(
            left_panel, 
            textvariable=self.color_var,
            state="readonly"
        )
        self.color_combo.pack(fill=tk.X, pady=(0, 10))
        self.color_combo.bind("<<ComboboxSelected>>", self.update_color)
        
        # Shape selection
        ttk.Label(left_panel, text="Shape", font=('Helvetica', 12, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        self.shape_var = tk.StringVar()
        shape_combo = ttk.Combobox(
            left_panel, 
            textvariable=self.shape_var,
            values=[shape["name"] for shape in self.config["shapes"]],
            state="readonly"
        )
        shape_combo.pack(fill=tk.X, pady=(0, 10))
        shape_combo.bind("<<ComboboxSelected>>", self.update_shape)
        
        # Accessories
        ttk.Label(left_panel, text="Accessories", font=('Helvetica', 12, 'bold')).pack(anchor=tk.W, pady=(0, 5))
        self.accessory_vars = {}
        for accessory in self.config["accessories"]:
            var = tk.BooleanVar()
            cb = ttk.Checkbutton(
                left_panel, 
                text=accessory["name"], 
                variable=var,
                command=lambda a=accessory, v=var: self.update_accessories(a, v)
            )
            cb.pack(anchor=tk.W, pady=2)
            self.accessory_vars[accessory["id"]] = var
        
        # Save button
        save_btn = ttk.Button(
            left_panel, 
            text="Save Design", 
            command=self.save_design
        )
        save_btn.pack(side=tk.BOTTOM, pady=(20, 0), fill=tk.X)
        
        # Preview area
        self.preview_canvas = tk.Canvas(right_panel, bg="#f0f0f0", width=500, height=500)
        self.preview_canvas.pack(expand=True, fill=tk.BOTH)
        
        # Default preview image
        self.default_img = Image.new("RGB", (500, 500), "#f0f0f0")
        self.default_photo = ImageTk.PhotoImage(self.default_img)
        self.preview_image = self.preview_canvas.create_image(250, 250, image=self.default_photo)
        
        # Design summary
        self.summary_text = tk.Text(right_panel, height=8, wrap=tk.WORD, state=tk.DISABLED)
        self.summary_text.pack(fill=tk.X, pady=(10, 0))
    
    def update_material(self, event):
        """Update material selection and available colors"""
        selected_material = self.material_var.get()
        self.current_design["material"] = selected_material
        
        # Update available colors for this material
        material = next((m for m in self.config["materials"] if m["name"] == selected_material), None)
        if material:
            self.color_combo["values"] = material["colors"]
            self.color_combo.set("")
            self.current_design["color"] = ""
        
        self.update_preview()
        self.update_summary()
    
    def update_color(self, event):
        """Update color selection"""
        self.current_design["color"] = self.color_var.get()
        self.update_preview()
        self.update_summary()
    
    def update_shape(self, event):
        """Update shape selection"""
        self.current_design["shape"] = self.shape_var.get()
        self.update_preview()
        self.update_summary()
    
    def update_accessories(self, accessory, var):
        """Update accessory selection"""
        if var.get():
            if accessory["id"] not in self.current_design["accessories"]:
                self.current_design["accessories"].append(accessory["id"])
        else:
            if accessory["id"] in self.current_design["accessories"]:
                self.current_design["accessories"].remove(accessory["id"])
        
        self.update_preview()
        self.update_summary()
    
    def update_preview(self):
        """Update the preview canvas with the current design"""
        # In a real application, this would load appropriate images based on selections
        # For this demo, we'll just create a colored rectangle
        
        # Clear canvas
        self.preview_canvas.delete("all")
        
        # Get color (default to light gray if not selected)
        color = "#cccccc"
        if self.current_design["color"]:
            color = self.current_design["color"]
        
        # Draw basic shape
        shape = "rectangle"  # default
        if self.current_design["shape"]:
            shape = self.current_design["shape"].lower()
        
        if "round" in shape or "circular" in shape:
            self.preview_canvas.create_oval(100, 100, 400, 400, fill=color, outline="black")
        else:
            self.preview_canvas.create_rectangle(100, 100, 400, 400, fill=color, outline="black")
        
        # Draw accessories
        for accessory_id in self.current_design["accessories"]:
            accessory = next((a for a in self.config["accessories"] if a["id"] == accessory_id), None)
            if accessory:
                # Simple representation of accessories
                if "cushion" in accessory["name"].lower():
                    self.preview_canvas.create_rectangle(150, 150, 350, 350, fill="#ffffff", outline="black")
                elif "umbrella" in accessory["name"].lower():
                    self.preview_canvas.create_polygon(250, 50, 200, 150, 300, 150, fill="#555555")
    
    def update_summary(self):
        """Update the design summary text"""
        self.summary_text.config(state=tk.NORMAL)
        self.summary_text.delete(1.0, tk.END)
        
        summary = "Current Design:\n\n"
        summary += f"Material: {self.current_design['material'] or 'Not selected'}\n"
        summary += f"Color: {self.current_design['color'] or 'Not selected'}\n"
