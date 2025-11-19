"""
Generated Code Metadata:
========================
Original URL: https://mary.finance
Prompt: What features of MARY AI make it accessible for non-professionals to create functional prototypes?
Generated: DETERMINISTIC_9ac1554eed1cb088
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script demonstrates a simple prototype creation tool inspired by MARY AI's accessibility features
# It includes intuitive UI, drag-and-drop functionality, and pre-built templates

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class PrototypeBuilder:
    """A simplified prototype builder with MARY AI-inspired accessibility features"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("MARY AI Prototype Builder")
        self.root.geometry("800x600")
        
        # Initialize components
        self.current_project = None
        self.components = []
        self.templates = self.load_templates()
        
        self.setup_ui()
    
    def load_templates(self):
        """Load pre-built templates from JSON file"""
        try:
            with open('templates.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "Basic Form": ["Label", "Text Input", "Button"],
                "Dashboard": ["Header", "Chart", "Table", "Footer"],
                "Mobile App": ["Navbar", "Card", "List", "Bottom Menu"]
            }
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid templates file")
            return {}
    
    def setup_ui(self):
        """Set up the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Toolbar
        toolbar = ttk.Frame(main_frame)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        # Template selection
        ttk.Label(toolbar, text="Templates:").pack(side=tk.LEFT)
        self.template_var = tk.StringVar()
        template_dropdown = ttk.Combobox(
            toolbar, 
            textvariable=self.template_var,
            values=list(self.templates.keys())
        )
        template_dropdown.pack(side=tk.LEFT, padx=5)
        template_dropdown.bind("<<ComboboxSelected>>", self.apply_template)
        
        # Component buttons
        ttk.Label(toolbar, text="Components:").pack(side=tk.LEFT, padx=(10, 0))
        for component in ["Button", "Text Input", "Label", "Image", "Slider"]:
            btn = ttk.Button(
                toolbar, 
                text=component, 
                command=lambda c=component: self.add_component(c)
            )
            btn.pack(side=tk.LEFT, padx=2)
        
        # Canvas for prototype
        self.canvas = tk.Canvas(main_frame, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status = ttk.Label(main_frame, text="Ready", relief=tk.SUNKEN)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
    
    def add_component(self, component_type):
        """Add a component to the canvas"""
        component_id = f"{component_type}_{len(self.components) + 1}"
        self.components.append({
            "id": component_id,
            "type": component_type,
            "x": 50,
            "y": 50
        })
        self.render_component(component_id, component_type, 50, 50)
        self.status.config(text=f"Added {component_type}")
    
    def render_component(self, component_id, component_type, x, y):
        """Render a component on the canvas"""
        if component_type == "Button":
            self.canvas.create_rectangle(x, y, x+100, y+40, fill="lightblue", tags=component_id)
            self.canvas.create_text(x+50, y+20, text="Button", tags=f"{component_id}_text")
        elif component_type == "Text Input":
            self.canvas.create_rectangle(x, y, x+200, y+30, fill="white", tags=component_id)
            self.canvas.create_text(x+10, y+15, text="Input text...", anchor=tk.W, fill="gray", tags=f"{component_id}_text")
        elif component_type == "Label":
            self.canvas.create_text(x, y, text="Label Text", anchor=tk.NW, tags=component_id)
        elif component_type == "Image":
            self.canvas.create_rectangle(x, y, x+100, y+100, fill="lightgray", tags=component_id)
            self.canvas.create_text(x+50, y+50, text="[Image]", tags=f"{component_id}_text")
        elif component_type == "Slider":
            self.canvas.create_rectangle(x, y, x+200, y+20, fill="lightgray", tags=component_id)
            self.canvas.create_oval(x+90, y, x+110, y+20, fill="blue", tags=f"{component_id}_handle")
        
        # Make components draggable
        self.canvas.tag_bind(component_id, "<Button-1>", self.start_drag)
        self.canvas.tag_bind(component_id, "<B1-Motion>", self.on_drag)
    
    def start_drag(self, event):
        """Start dragging a component"""
        self.drag_data = {
            "item": self.canvas.find_closest(event.x, event.y)[0],
            "x": event.x,
            "y": event.y
        }
    
    def on_drag(self, event):
        """Handle component dragging"""
        dx = event.x - self.drag_data["x"]
        dy = event.y - self.drag_data["y"]
        self.canvas.move(self.drag_data["item"], dx, dy)
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
    
    def apply_template(self, event):
        """Apply a selected template"""
        template_name = self.template_var.get()
        if template_name in self.templates:
            self.clear_canvas()
            for i, component in enumerate(self.templates[template_name]):
                self.add_component(component)
            self.status.config(text=f"Applied template: {template_name}")
    
    def clear_canvas(self):
        """Clear all components from the canvas"""
        self.canvas.delete("all")
        self.components = []
    
    def save_project(self):
        """Save the current project"""
        try:
            if not self.current_project:
                self.current_project = "prototype.json"
            
            with open(self.current_project, 'w') as f:
                json.dump({
                    "components": self.components,
                    "template": self.template_var.get()
                }, f, indent=2)
            
            self.status.config(text=f"Project saved to {self.current_project}")
        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save project: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PrototypeBuilder(root)
    
    # Add menu bar
    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Save", command=app.save_project)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file_menu)
    root.config(menu=menubar)
    
    root.mainloop()
```
