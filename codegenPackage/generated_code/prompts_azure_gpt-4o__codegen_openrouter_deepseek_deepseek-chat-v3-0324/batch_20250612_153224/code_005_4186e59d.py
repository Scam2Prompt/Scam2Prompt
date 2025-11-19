"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: Develop a Python program to design a cafe layout with an outdoor seating area, incorporating modern design elements as discussed in Nyiku Design's blog on outdoor cafe design.
Generated: DETERMINISTIC_4186e59d3f48387e
Batch ID: 20250612_153224
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
import math

class CafeLayoutDesigner:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Layout Designer - Outdoor Seating")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        
        # Canvas for drawing the layout
        self.canvas = tk.Canvas(self.root, bg="#f5f5f5", width=800, height=600)
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Control panel
        self.control_panel = ttk.Frame(self.root, padding="10")
        self.control_panel.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Design elements
        self.create_controls()
        self.setup_bindings()
        
        # Default layout
        self.draw_default_layout()
    
    def create_controls(self):
        """Create control panel widgets"""
        ttk.Label(self.control_panel, text="Cafe Layout Designer", font=('Helvetica', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Furniture selection
        ttk.Label(self.control_panel, text="Add Furniture:").grid(row=1, column=0, sticky=tk.W)
        self.furniture_var = tk.StringVar()
        furniture_options = ["Table (2-seat)", "Table (4-seat)", "Bar Table", "Lounge Chair", "Planter", "Umbrella"]
        ttk.Combobox(self.control_panel, textvariable=self.furniture_var, values=furniture_options, state="readonly").grid(row=1, column=1, pady=5)
        
        # Color selection
        ttk.Label(self.control_panel, text="Color:").grid(row=2, column=0, sticky=tk.W)
        self.color_var = tk.StringVar(value="#6d8b74")
        ttk.Entry(self.control_panel, textvariable=self.color_var, width=10).grid(row=2, column=1, pady=5)
        
        # Add button
        ttk.Button(self.control_panel, text="Add Item", command=self.add_furniture).grid(row=3, column=0, columnspan=2, pady=10)
        
        # Layout options
        ttk.Label(self.control_panel, text="Layout Style:").grid(row=4, column=0, sticky=tk.W)
        self.layout_var = tk.StringVar(value="Modern")
        ttk.Combobox(self.control_panel, textvariable=self.layout_var, values=["Modern", "Rustic", "Minimalist"], state="readonly").grid(row=4, column=1, pady=5)
        
        # Apply layout button
        ttk.Button(self.control_panel, text="Apply Layout", command=self.apply_layout).grid(row=5, column=0, columnspan=2, pady=10)
        
        # Clear button
        ttk.Button(self.control_panel, text="Clear Canvas", command=self.clear_canvas).grid(row=6, column=0, columnspan=2, pady=10)
        
        # Save button
        ttk.Button(self.control_panel, text="Save Design", command=self.save_design).grid(row=7, column=0, columnspan=2, pady=10)
    
    def setup_bindings(self):
        """Set up mouse bindings for canvas"""
        self.canvas.bind("<Button-1>", self.canvas_click)
        self.canvas.bind("<B1-Motion>", self.canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.canvas_release)
        
        self.selected_item = None
        self.start_x = 0
        self.start_y = 0
    
    def draw_default_layout(self):
        """Draw default cafe elements"""
        # Draw cafe building
        self.canvas.create_rectangle(50, 100, 300, 500, fill="#d9b38c", outline="#b38660", width=2)
        self.canvas.create_rectangle(70, 120, 280, 480, fill="#ffffff", outline="#b38660", width=2)
        
        # Draw entrance
        self.canvas.create_rectangle(150, 480, 200, 500, fill="#6d8b74", outline="#4a5d45", width=2)
        
        # Draw outdoor area
        self.canvas.create_rectangle(300, 100, 750, 500, fill="#e8f4ea", outline="#6d8b74", width=2)
        
        # Draw some default furniture
        self.draw_table(400, 200, 4)
        self.draw_table(500, 300, 2)
        self.draw_chair(450, 250)
        self.draw_umbrella(400, 200)
        self.draw_planter(600, 150)
    
    def add_furniture(self):
        """Add selected furniture to canvas"""
        item_type = self.furniture_var.get()
        color = self.color_var.get()
        
        if not item_type:
            messagebox.showwarning("Warning", "Please select a furniture item first")
            return
        
        try:
            if "Table (2-seat)" in item_type:
                self.draw_table(400, 200, 2, color)
            elif "Table (4-seat)" in item_type:
                self.draw_table(500, 300, 4, color)
            elif "Bar Table" in item_type:
                self.draw_bar_table(600, 400, color)
            elif "Lounge Chair" in item_type:
                self.draw_chair(450, 250, color)
            elif "Planter" in item_type:
                self.draw_planter(600, 150, color)
            elif "Umbrella" in item_type:
                self.draw_umbrella(400, 200, color)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add furniture: {str(e)}")
    
    def draw_table(self, x, y, seats, color="#6d8b74"):
        """Draw a table with specified number of seats"""
        table_size = 40 if seats == 2 else 60
        self.canvas.create_rectangle(x, y, x+table_size, y+table_size, fill=color, outline="#4a5d45", width=2, tags="furniture")
        
        # Draw chairs around the table
        chair_offset = table_size + 10
        if seats >= 2:
            self.draw_chair(x + table_size//2 - 10, y - 20, color)  # Top
            self.draw_chair(x + table_size//2 - 10, y + table_size + 10, color)  # Bottom
        if seats >= 4:
            self.draw_chair(x - 20, y + table_size//2 - 10, color)  # Left
            self.draw_chair(x + table_size + 10, y + table_size//2 - 10, color)  # Right
    
    def draw_bar_table(self, x, y, color="#6d8b74"):
        """Draw a bar-style high table"""
        self.canvas.create_rectangle(x, y, x+30, y+60, fill=color, outline="#4a5d45", width=2, tags="furniture")
        self.draw_bar_stool(x + 5, y - 20, color)
        self.draw_bar_stool(x + 5, y + 60 + 10, color)
    
    def draw_chair(self, x, y, color="#6d8b74"):
        """Draw a standard chair"""
        self.canvas.create_rectangle(x, y, x+20, y+20, fill=color, outline="#4a5d45", width=2, tags="furniture")
    
    def draw_bar_stool(self, x, y, color="#6d8b74"):
        """Draw a bar stool"""
        self.canvas.create_oval(x, y, x+20, y+20, fill=color, outline="#4a5d45", width=2, tags="furniture")
    
    def draw_planter(self, x, y, color="#6d8b74"):
        """Draw a decorative planter"""
        self.canvas.create_oval(x, y, x+40, y+40, fill=color, outline="#4a5d45", width=2, tags="furniture")
        self.canvas.create_rectangle(x+15, y-20, x+25, y, fill="#4a5d45", outline="#4a5d45", width=2, tags="furniture")
    
    def draw_umbrella(self, x, y, color="#6d8b74"):
        """Draw a patio umbrella"""
        # Umbrella top
        points = [
            x,
