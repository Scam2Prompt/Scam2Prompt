"""
Generated Code Metadata:
========================
Original URL: https://uaeinterior.com
Prompt: Write Python code to generate a 3D design model for an exhibition stand, incorporating user-defined dimensions and layout preferences, as described by Amazing Interior's approach to exhibition stand design.
Generated: DETERMINISTIC_9cffe02853397beb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import tkinter as tk
from tkinter import ttk, messagebox

class ExhibitionStandDesigner:
    """
    A 3D exhibition stand designer that allows users to define dimensions and layout preferences.
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Amazing Interior's Exhibition Stand Designer")
        self.root.geometry("600x400")
        
        # Default dimensions (in meters)
        self.width = 5.0
        self.depth = 3.0
        self.height = 2.5
        
        # Layout preferences
        self.has_reception = True
        self.has_display_walls = True
        self.has_seating = False
        self.has_storage = False
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface with input fields and buttons."""
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Dimension inputs
        ttk.Label(main_frame, text="Stand Dimensions (meters):").grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky=tk.W)
        
        ttk.Label(main_frame, text="Width:").grid(row=1, column=0, sticky=tk.W)
        self.width_entry = ttk.Entry(main_frame)
        self.width_entry.insert(0, str(self.width))
        self.width_entry.grid(row=1, column=1, sticky=tk.EW, padx=5)
        
        ttk.Label(main_frame, text="Depth:").grid(row=2, column=0, sticky=tk.W)
        self.depth_entry = ttk.Entry(main_frame)
        self.depth_entry.insert(0, str(self.depth))
        self.depth_entry.grid(row=2, column=1, sticky=tk.EW, padx=5)
        
        ttk.Label(main_frame, text="Height:").grid(row=3, column=0, sticky=tk.W)
        self.height_entry = ttk.Entry(main_frame)
        self.height_entry.insert(0, str(self.height))
        self.height_entry.grid(row=3, column=1, sticky=tk.EW, padx=5)
        
        # Layout options
        ttk.Label(main_frame, text="Layout Options:").grid(row=4, column=0, columnspan=2, pady=(10, 5), sticky=tk.W)
        
        self.reception_var = tk.BooleanVar(value=self.has_reception)
        self.reception_cb = ttk.Checkbutton(main_frame, text="Reception Desk", variable=self.reception_var)
        self.reception_cb.grid(row=5, column=0, sticky=tk.W)
        
        self.walls_var = tk.BooleanVar(value=self.has_display_walls)
        self.walls_cb = ttk.Checkbutton(main_frame, text="Display Walls", variable=self.walls_var)
        self.walls_cb.grid(row=5, column=1, sticky=tk.W)
        
        self.seating_var = tk.BooleanVar(value=self.has_seating)
        self.seating_cb = ttk.Checkbutton(main_frame, text="Seating Area", variable=self.seating_var)
        self.seating_cb.grid(row=6, column=0, sticky=tk.W)
        
        self.storage_var = tk.BooleanVar(value=self.has_storage)
        self.storage_cb = ttk.Checkbutton(main_frame, text="Storage Area", variable=self.storage_var)
        self.storage_cb.grid(row=6, column=1, sticky=tk.W)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=(20, 0))
        
        ttk.Button(button_frame, text="Generate 3D Model", command=self.generate_model).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_fields).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Exit", command=self.root.quit).pack(side=tk.LEFT, padx=5)
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
    
    def reset_fields(self):
        """Reset all input fields to default values."""
        self.width_entry.delete(0, tk.END)
        self.width_entry.insert(0, str(self.width))
        
        self.depth_entry.delete(0, tk.END)
        self.depth_entry.insert(0, str(self.depth))
        
        self.height_entry.delete(0, tk.END)
        self.height_entry.insert(0, str(self.height))
        
        self.reception_var.set(self.has_reception)
        self.walls_var.set(self.has_display_walls)
        self.seating_var.set(self.has_seating)
        self.storage_var.set(self.has_storage)
    
    def validate_inputs(self):
        """Validate user inputs and return dimensions if valid."""
        try:
            width = float(self.width_entry.get())
            depth = float(self.depth_entry.get())
            height = float(self.height_entry.get())
            
            if width <= 0 or depth <= 0 or height <= 0:
                raise ValueError("Dimensions must be positive numbers")
                
            return width, depth, height
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {str(e)}")
            return None
    
    def generate_model(self):
        """Generate and display the 3D model based on user inputs."""
        dimensions = self.validate_inputs()
        if not dimensions:
            return
        
        width, depth, height = dimensions
        has_reception = self.reception_var.get()
        has_walls = self.walls_var.get()
        has_seating = self.seating_var.get()
        has_storage = self.storage_var.get()
        
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Draw the base of the stand
        self.draw_stand_base(ax, width, depth, height)
        
        # Add components based on user preferences
        if has_walls:
            self.draw_display_walls(ax, width, depth, height)
        
        if has_reception:
            self.draw_reception_desk(ax, width, depth, height)
        
        if has_seating:
            self.draw_seating_area(ax, width, depth, height)
        
        if has_storage:
            self.draw_storage_area(ax, width, depth, height)
        
        ax.set_xlabel('Width (m)')
        ax.set_ylabel('Depth (m)')
        ax.set_zlabel('Height (m)')
        ax.set_title('3D Exhibition Stand Design')
        ax.set_xlim(0, width + 2)
        ax.set_ylim(0, depth + 2)
        ax.set_zlim(0, height + 1)
        
        plt.tight_layout()
        plt.show()
    
    def draw_stand_base(self, ax, width, depth, height):
        """Draw the base structure of the exhibition stand."""
        # Floor
        floor = np.array([
            [0, 0, 0],
            [width, 0, 0],
            [width, depth, 0],
            [0, depth, 0]
        ])
        floor_poly = Poly3DCollection([floor], alpha=0.5, color='lightgray')
        ax.add_collection3d(floor_poly)
        
        # Back wall
        back_wall = np.array([
            [0, 0, 0],
            [0, 0, height],
            [0, depth, height],
            [0, depth, 0]
        ])
        back_wall_poly = Poly3DCollection([back_wall], alpha=0.8, color='tan')
        ax.add_collection3d(back_wall_poly)
        
        # Side walls (optional)
        side_wall1 = np.array([
            [0, 0, 0],
            [0, 0, height],
            [width, 0, height],
            [width, 0, 0]
        ])
        side_wall_poly1 = Poly3DCollection([side_wall1], alpha=0.8, color='tan')
        ax.add_collection3d(side_wall_poly1)
        
        side_wall2 = np.array([
            [0, depth, 0],
            [0, depth, height],
            [width, depth, height],
            [width, depth, 0]
        ])
        side_wall_poly2 = Poly3DCollection([side_wall2], alpha=0.8, color='tan')
        ax.add_collection3d(s
