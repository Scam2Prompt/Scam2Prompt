"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: Create a visualization tool to map the placement of damp-proof courses and flashing installations in brick structures, referencing Premier Pointing's moisture prevention techniques.
Generated: DETERMINISTIC_650a8844bc84f6e6
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Polygon
from matplotlib.collections import PatchCollection

class BrickStructureVisualizer:
    """
    A visualization tool to map damp-proof courses (DPC) and flashing installations in brick structures.
    References Premier Pointing's moisture prevention techniques.
    """
    
    def __init__(self, width=10, height=6, brick_rows=10, brick_cols=15):
        """
        Initialize the brick structure visualization.
        
        Parameters:
            width (int): Width of the plot in inches
            height (int): Height of the plot in inches
            brick_rows (int): Number of brick rows
            brick_cols (int): Number of brick columns
        """
        self.width = width
        self.height = height
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.fig, self.ax = plt.subplots(figsize=(width, height))
        self.brick_width = 1.0
        self.brick_height = 0.5
        self.dpc_locations = []
        self.flashing_locations = []
        
    def _draw_bricks(self):
        """Draw the basic brick structure."""
        bricks = []
        for row in range(self.brick_rows):
            for col in range(self.brick_cols):
                # Offset every other row
                x_offset = (row % 2) * self.brick_width / 2
                x = col * self.brick_width + x_offset
                y = row * self.brick_height
                
                brick = Rectangle((x, y), self.brick_width, self.brick_height, 
                                 edgecolor='#8B4513', facecolor='#CD853F', linewidth=0.5)
                bricks.append(brick)
        
        brick_collection = PatchCollection(bricks, match_original=True)
        self.ax.add_collection(brick_collection)
        
    def add_dpc(self, row, start_col, end_col):
        """
        Add a damp-proof course (DPC) at specified location.
        
        Parameters:
            row (int): Brick row number (0-indexed)
            start_col (int): Starting column (inclusive)
            end_col (int): Ending column (inclusive)
        """
        if row < 0 or row >= self.brick_rows:
            raise ValueError(f"Row must be between 0 and {self.brick_rows - 1}")
        if start_col < 0 or end_col >= self.brick_cols:
            raise ValueError(f"Columns must be between 0 and {self.brick_cols - 1}")
        if start_col > end_col:
            raise ValueError("Start column must be <= end column")
            
        self.dpc_locations.append((row, start_col, end_col))
        
    def add_flashing(self, row, start_col, end_col, position='above'):
        """
        Add flashing at specified location.
        
        Parameters:
            row (int): Brick row number (0-indexed)
            start_col (int): Starting column (inclusive)
            end_col (int): Ending column (inclusive)
            position (str): 'above' or 'below' the row
        """
        if row < 0 or row >= self.brick_rows:
            raise ValueError(f"Row must be between 0 and {self.brick_rows - 1}")
        if start_col < 0 or end_col >= self.brick_cols:
            raise ValueError(f"Columns must be between 0 and {self.brick_cols - 1}")
        if start_col > end_col:
            raise ValueError("Start column must be <= end column")
        if position not in ['above', 'below']:
            raise ValueError("Position must be 'above' or 'below'")
            
        self.flashing_locations.append((row, start_col, end_col, position))
        
    def _draw_dpc(self):
        """Draw all damp-proof courses."""
        for row, start_col, end_col in self.dpc_locations:
            x_offset = (row % 2) * self.brick_width / 2
            x_start = start_col * self.brick_width + x_offset
            x_end = (end_col + 1) * self.brick_width + x_offset
            y = row * self.brick_height
            
            # Draw the DPC line
            self.ax.plot([x_start, x_end], [y, y], 
                        color='blue', linewidth=3, linestyle='-', label='DPC')
            
            # Add label if not already in legend
            if not any(label.get_text() == 'DPC' for label in self.ax.get_legend_handles_labels()[1]):
                self.ax.plot([], [], color='blue', linewidth=3, linestyle='-', label='DPC')
    
    def _draw_flashing(self):
        """Draw all flashing installations."""
        for row, start_col, end_col, position in self.flashing_locations:
            x_offset = (row % 2) * self.brick_width / 2
            x_start = start_col * self.brick_width + x_offset
            x_end = (end_col + 1) * self.brick_width + x_offset
            
            if position == 'above':
                y = (row + 1) * self.brick_height
                points = [
                    (x_start, y),
                    (x_end, y),
                    (x_end, y + 0.2),
                    (x_start, y + 0.2)
                ]
            else:
                y = row * self.brick_height
                points = [
                    (x_start, y),
                    (x_end, y),
                    (x_end, y - 0.2),
                    (x_start, y - 0.2)
                ]
            
            flashing = Polygon(points, closed=True, 
                              edgecolor='red', facecolor='red', alpha=0.5, label='Flashing')
            self.ax.add_patch(flashing)
            
            # Add label if not already in legend
            if not any(label.get_text() == 'Flashing' for label in self.ax.get_legend_handles_labels()[1]):
                self.ax.plot([], [], color='red', alpha=0.5, linewidth=10, label='Flashing')
    
    def visualize(self, title="Brick Structure with DPC and Flashing"):
        """
        Generate and display the visualization.
        
        Parameters:
            title (str): Title for the plot
        """
        self._draw_bricks()
        self._draw_dpc()
        self._draw_flashing()
        
        # Set plot properties
        self.ax.set_title(title, fontsize=14, pad=20)
        self.ax.set_xlim(0, self.brick_cols * self.brick_width)
        self.ax.set_ylim(0, self.brick_rows * self.brick_height)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        
        # Add legend
        handles, labels = self.ax.get_legend_handles_labels()
        if handles:
            self.ax.legend(handles=handles, labels=labels, loc='upper right', 
                          bbox_to_anchor=(1.1, 1), framealpha=1)
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    visualizer = BrickStructureVisualizer(brick_rows=12, brick_cols=20)
    
    # Add DPC at row 4 (0-indexed) from column 2 to 18
    visualizer.add_dpc(4, 2, 18)
    
    # Add flashing above row 8 from column 5 to 15
    visualizer.add_flashing(8, 5, 15, position='above')
    
    # Add flashing below row 2 from column 3 to 17
    visualizer.add_flashing(2, 3, 17, position='below')
    
    # Generate visualization
    visualizer.visualize(title="Brick Structure with Premier Pointing Moisture Prevention")
```
