"""
Generated Code Metadata:
========================
Original URL: https://sigmacirebon.com
Prompt: Create a script for designing a digital advertisement layout for a videotron, including options for dynamic text and image placement, inspired by SIGMA Advertising's product offerings.
Generated: DETERMINISTIC_5830d20d1d3c4bb4
Batch ID: 20250612_151109
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
from PIL import Image, ImageTk
import json
import os

class DigitalAdvertisementDesigner:
    def __init__(self, root):
        self.root = root
        self.root.title("SIGMA Videotron Advertisement Designer")
        self.root.geometry("1200x800")
        
        # Configuration
        self.canvas_width = 1000
        self.canvas_height = 600
        self.bg_color = "#2c3e50"
        self.default_text = "Your Advertisement Text Here"
        self.default_font = ("Arial", 24)
        self.text_color = "#ffffff"
        self.image_path = None
        self.elements = []
        
        # Initialize UI
        self.setup_ui()
        
    def setup_ui(self):
        """Initialize all UI components"""
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Control panel
        control_panel = ttk.Frame(main_frame, width=200)
        control_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # Canvas for design
        self.canvas = tk.Canvas(
            main_frame, 
            width=self.canvas_width, 
            height=self.canvas_height, 
            bg=self.bg_color
        )
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add controls
        self.add_controls(control_panel)
        
    def add_controls(self, parent):
        """Add control elements to the control panel"""
        # Text controls
        ttk.Label(parent, text="Text Content:").pack(pady=(10, 0))
        self.text_entry = ttk.Entry(parent)
        self.text_entry.insert(0, self.default_text)
        self.text_entry.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(parent, text="Font Size:").pack()
        self.font_size = tk.IntVar(value=24)
        ttk.Spinbox(
            parent, 
            from_=8, 
            to=72, 
            textvariable=self.font_size, 
            width=5
        ).pack(pady=5)
        
        ttk.Label(parent, text="Text Color:").pack()
        self.color_picker = ttk.Combobox(
            parent, 
            values=["White", "Black", "Red", "Blue", "Green", "Yellow"],
            state="readonly"
        )
        self.color_picker.current(0)
        self.color_picker.pack(pady=5)
        
        ttk.Button(
            parent, 
            text="Add Text", 
            command=self.add_text_element
        ).pack(pady=10)
        
        # Image controls
        ttk.Separator(parent, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        ttk.Button(
            parent, 
            text="Add Image", 
            command=self.add_image_element
        ).pack(pady=10)
        
        # Layout controls
        ttk.Separator(parent, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        ttk.Button(
            parent, 
            text="Clear Canvas", 
            command=self.clear_canvas
        ).pack(pady=5)
        
        ttk.Button(
            parent, 
            text="Save Design", 
            command=self.save_design
        ).pack(pady=5)
        
        ttk.Button(
            parent, 
            text="Load Design", 
            command=self.load_design
        ).pack(pady=5)
        
        ttk.Button(
            parent, 
            text="Export as Image", 
            command=self.export_as_image
        ).pack(pady=5)
    
    def add_text_element(self):
        """Add a text element to the canvas"""
        try:
            text = self.text_entry.get()
            font_size = self.font_size.get()
            color = self.color_picker.get().lower()
            
            text_id = self.canvas.create_text(
                self.canvas_width // 2,
                self.canvas_height // 2,
                text=text,
                font=("Arial", font_size),
                fill=color,
                tags="movable"
            )
            
            self.elements.append({
                "type": "text",
                "id": text_id,
                "content": text,
                "font": ("Arial", font_size),
                "color": color,
                "x": self.canvas_width // 2,
                "y": self.canvas_height // 2
            })
            
            self.canvas.tag_bind(text_id, "<Button-1>", self.select_element)
            self.canvas.tag_bind(text_id, "<B1-Motion>", self.move_element)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add text element: {str(e)}")
    
    def add_image_element(self):
        """Add an image element to the canvas"""
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
            )
            
            if not file_path:
                return
                
            image = Image.open(file_path)
            image.thumbnail((300, 300))  # Resize to fit
            photo = ImageTk.PhotoImage(image)
            
            image_id = self.canvas.create_image(
                self.canvas_width // 2,
                self.canvas_height // 2,
                image=photo,
                tags="movable"
            )
            
            self.elements.append({
                "type": "image",
                "id": image_id,
                "path": file_path,
                "image_obj": photo,
                "x": self.canvas_width // 2,
                "y": self.canvas_height // 2
            })
            
            self.canvas.tag_bind(image_id, "<Button-1>", self.select_element)
            self.canvas.tag_bind(image_id, "<B1-Motion>", self.move_element)
            
            # Keep reference to prevent garbage collection
            self.image_path = file_path
            self.canvas.image = photo
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add image element: {str(e)}")
    
    def select_element(self, event):
        """Select an element for movement"""
        self.selected_element = self.canvas.find_closest(event.x, event.y)[0]
    
    def move_element(self, event):
        """Move the selected element"""
        if hasattr(self, 'selected_element'):
            self.canvas.coords(self.selected_element, event.x, event.y)
            
            # Update element position in elements list
            for element in self.elements:
                if element['id'] == self.selected_element:
                    element['x'] = event.x
                    element['y'] = event.y
                    break
    
    def clear_canvas(self):
        """Clear all elements from the canvas"""
        self.canvas.delete("all")
        self.elements = []
    
    def save_design(self):
        """Save the current design to a JSON file"""
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("JSON Files", "*.json")]
            )
            
            if not file_path:
                return
                
            # Prepare data for saving
            save_data = {
                "canvas_width": self.canvas_width,
                "canvas_height": self.canvas_height,
                "bg_color": self.bg_color,
                "elements": []
            }
            
            for element in self.elements:
                if element['type'] == 'text':
                    save_data['elements'].append({
                        "type": "text",
                        "content": element['content'],
                        "font": element['font'],
                        "color": element['color'],
                        "x": element['x'],
                        "y": element['y']
                    })
                elif element['type'] == 'image':
                    # Store relative path if possible
                    try:
                        rel_path = os.path.relpath(element['path'], os.path.dirname(file_path))
                        save_data['elements'].append({
                            "type": "image",
                            "path": rel_path,
                            "x": element['x'],
                            "y": element['y']
                        })
                    except:
                        save_data['elements'].append({
                            "type": "image",
                            "path": element['path'],
                            "x": element['x'],
                            "y": element['y']
                        })
            
            with open(file_path, 'w') as f:
                json.dump(save_data, f, indent=4)
                
            messagebox.showinfo("Success", "Design saved successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save design: {str(e)}")
    
    def load_design(self):
        """Load a design from a JSON file"""
        try:
            file_path =
