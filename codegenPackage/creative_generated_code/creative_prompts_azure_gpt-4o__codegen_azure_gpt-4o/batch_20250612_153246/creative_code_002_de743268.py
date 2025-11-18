"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hildeinox.com
Prompt: Generate code to design a perforated stainless steel sheet pattern, incorporating specifications similar to the "Perfore Sac" products listed on Hilde Inox.
Generated: DETERMINISTIC_de743268ad50f330
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is Python code that generates a perforated stainless steel sheet pattern:

```python
import matplotlib.pyplot as plt
import numpy as np

def generate_perforated_sheet(rows, columns, hole_diameter, hole_spacing, sheet_width, sheet_height):
    """
    Generate a perforated stainless steel sheet pattern.
    
    Args:
        rows (int): Number of rows of holes.
        columns (int): Number of columns of holes.
        hole_diameter (float): Diameter of each hole in mm.
        hole_spacing (float): Distance between hole centers in mm.
        sheet_width (float): Width of the sheet in mm.
        sheet_height (float): Height of the sheet in mm.
    
    Returns:
        None
    """
    try:
        # Validate inputs
        if rows <= 0 or columns <= 0 or hole_diameter <= 0 or hole_spacing <= 0:
            raise ValueError("Rows, columns, hole diameter, and spacing must be positive values.")
        if hole_diameter > hole_spacing:
            raise ValueError("Hole diameter cannot exceed hole spacing.")
        if sheet_width <= 0 or sheet_height <= 0:
            raise ValueError("Sheet dimensions must be positive values.")

        # Create the figure for visualization
        fig, ax = plt.subplots(figsize=(sheet_width / 100, sheet_height / 100))
        ax.set_xlim(0, sheet_width)
        ax.set_ylim(0, sheet_height)
        ax.set_aspect('equal', adjustable='box')
        ax.set_title('Perforated Stainless Steel Sheet')
        ax.set_xlabel('Width (mm)')
        ax.set_ylabel('Height (mm)')
        
        # Calculate starting positions and draw the holes
        start_x = (sheet_width - (columns - 1) * hole_spacing) / 2
        start_y = (sheet_height - (rows - 1) * hole_spacing) / 2
        for row in range(rows):
            for col in range(columns):
                x = start_x + col * hole_spacing
                y = start_y + row * hole_spacing
                circle = plt.Circle((x, y), hole_diameter / 2, color='black')
                ax.add_artist(circle)
        
        # Render the pattern
        plt.grid(True, which='both', color='lightgray', linestyle='--', linewidth=0.5)
        plt.show()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# Generate a perforated sheet with 10 rows, 15 columns, 5mm hole diameter, 15mm hole spacing, 300mm width, and 200mm height.
generate_perforated_sheet(rows=10, columns=15, hole_diameter=5, hole_spacing=15, sheet_width=300, sheet_height=200)
```

This code uses `matplotlib` to visualize a perforated stainless steel sheet pattern. It includes error handling for invalid inputs and adheres to clean coding practices.
