"""
Generated Code Metadata:
========================
Original URL: https://jsebastiao.com
Prompt: Develop a wireframe generator tool using Python that aligns with the UX design approach highlighted in J. Sebastião's portfolio.
Generated: DETERMINISTIC_b81f7b43227a6185
Batch ID: 20250612_151345
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
import json
import os
from PIL import Image, ImageDraw, ImageTk

class WireframeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Wireframe Generator")
        self.root.geometry("1000x700")
        
        # Initialize variables
        self.current_project = None
        self.elements = []
        self.selected_element = None
        self.canvas_width = 800
        self.canvas_height = 600
        
        # Create UI
        self.create_menu()
        self.create_toolbar()
        self.create_canvas()
        self.create_properties_panel()
        
        # Bind events
        self.bind_events()
        
    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New Project", command=self.new_project)
        file_menu.add_command(label="Open Project", command=self.open_project)
        file_menu.add_command(label="Save Project", command=self.save_project)
        file_menu.add_separator()
        file_menu.add_command(label="Export as PNG", command=self.export_png)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Delete Selected", command=self.delete_selected)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        
        self.root.config(menu=menubar)
    
    def create_toolbar(self):
        toolbar = ttk.Frame(self.root, padding=5)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        # Tool buttons
        tools = [
            ("Rectangle", "rectangle"),
            ("Button", "button"),
            ("Text Field", "text_field"),
            ("Label", "label"),
            ("Image", "image"),
            ("Checkbox", "checkbox")
        ]
        
        for tool_name, tool_id in tools:
            btn = ttk.Button(toolbar, text=tool_name, 
                           command=lambda id=tool_id: self.set_active_tool(id))
            btn.pack(side=tk.LEFT, padx=2)
        
        # Separator
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, padx=5)
        
        # Color picker
        self.color_var = tk.StringVar(value="#000000")
        color_btn = ttk.Button(toolbar, text="Color", 
                             command=self.choose_color)
        color_btn.pack(side=tk.LEFT, padx=2)
        
        self.active_tool = None
    
    def create_canvas(self):
        canvas_frame = ttk.Frame(self.root)
        canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.canvas = tk.Canvas(canvas_frame, width=self.canvas_width, 
                               height=self.canvas_height, bg="white", 
                               cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbars
        h_scroll = ttk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, 
                                command=self.canvas.xview)
        v_scroll = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, 
                                command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=h_scroll.set, 
                             yscrollcommand=v_scroll.set)
        
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    
    def create_properties_panel(self):
        properties_frame = ttk.Frame(self.root, width=200, padding=5)
        properties_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        ttk.Label(properties_frame, text="Properties").pack(anchor=tk.W)
        
        # Element properties
        self.prop_frame = ttk.Frame(properties_frame)
        self.prop_frame.pack(fill=tk.X, pady=5)
        
        # Common properties
        ttk.Label(self.prop_frame, text="X:").grid(row=0, column=0, sticky=tk.W)
        self.x_var = tk.StringVar()
        ttk.Entry(self.prop_frame, textvariable=self.x_var).grid(row=0, column=1)
        
        ttk.Label(self.prop_frame, text="Y:").grid(row=1, column=0, sticky=tk.W)
        self.y_var = tk.StringVar()
        ttk.Entry(self.prop_frame, textvariable=self.y_var).grid(row=1, column=1)
        
        ttk.Label(self.prop_frame, text="Width:").grid(row=2, column=0, sticky=tk.W)
        self.width_var = tk.StringVar()
        ttk.Entry(self.prop_frame, textvariable=self.width_var).grid(row=2, column=1)
        
        ttk.Label(self.prop_frame, text="Height:").grid(row=3, column=0, sticky=tk.W)
        self.height_var = tk.StringVar()
        ttk.Entry(self.prop_frame, textvariable=self.height_var).grid(row=3, column=1)
        
        ttk.Label(self.prop_frame, text="Text:").grid(row=4, column=0, sticky=tk.W)
        self.text_var = tk.StringVar()
        ttk.Entry(self.prop_frame, textvariable=self.text_var).grid(row=4, column=1)
        
        # Update button
        update_btn = ttk.Button(properties_frame, text="Update", 
                              command=self.update_element_properties)
        update_btn.pack(pady=5)
    
    def bind_events(self):
        self.canvas.bind("<Button-1>", self.canvas_click)
        self.canvas.bind("<B1-Motion>", self.canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.canvas_release)
        self.canvas.bind("<Button-3>", self.canvas_right_click)
        
        # Bind property changes
        self.x_var.trace_add("write", self.update_properties)
        self.y_var.trace_add("write", self.update_properties)
        self.width_var.trace_add("write", self.update_properties)
        self.height_var.trace_add("write", self.update_properties)
        self.text_var.trace_add("write", self.update_properties)
    
    def set_active_tool(self, tool_id):
        self.active_tool = tool_id
    
    def choose_color(self):
        color = tk.colorchooser.askcolor(title="Choose color")
        if color[1]:
            self.color_var.set(color[1])
    
    def canvas_click(self, event):
        if self.active_tool:
            x, y = event.x, event.y
            element = {
                "id": len(self.elements),
                "type": self.active_tool,
                "x": x,
                "y": y,
                "width": 100,
                "height": 50,
                "color": self.color_var.get(),
                "text": "",
                "canvas_id": None
            }
            
            if self.active_tool == "rectangle":
                element["canvas_id"] = self.canvas.create_rectangle(
                    x, y, x + 100, y + 50, 
                    outline=element["color"], 
                    fill="", 
                    width=2
                )
            elif self.active_tool == "button":
                element["canvas_id"] = self.canvas.create_rectangle(
                    x, y, x + 100, y + 30, 
                    outline=element["color"], 
                    fill="#f0f0f0", 
                    width=1
                )
                element["text"] = "Button"
                element["canvas_text_id"] = self.canvas.create_text(
                    x + 50, y + 15, 
                    text=element["text"], 
                    fill=element["color"]
                )
            elif self.active_tool == "text_field":
                element["canvas_id"] = self.canvas.create_rectangle(
                    x, y, x + 150, y + 25, 
                    outline=element["color"], 
                    fill="white", 
                    width=1
                )
                element["text"] = "Text Field"
                element["canvas_text_id"] = self.canvas.create_text(
                    x + 5, y + 12, 
                    text=element["text"], 
                    fill="#999999",
                    anchor=tk.W
                )
