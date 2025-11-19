"""
Generated Code Metadata:
========================
Original URL: https://slidesgeek.com
Prompt: Write a script to generate circular infographic designs for educational presentations, inspired by the templates available on SlidesGeek.
Generated: DETERMINISTIC_27e738a68ca88cac
Batch ID: 20250612_152739
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
from matplotlib.patches import Circle, Wedge
from matplotlib.collections import PatchCollection
import random

class CircularInfographic:
    """
    Generate circular infographic designs for educational presentations.
    Inspired by SlidesGeek templates.
    """
    
    def __init__(self, title="Circular Infographic", size=8, dpi=100):
        """
        Initialize the infographic with basic parameters.
        
        Args:
            title (str): Title of the infographic
            size (int): Figure size in inches
            dpi (int): Dots per inch for the figure
        """
        self.fig, self.ax = plt.subplots(figsize=(size, size), dpi=dpi)
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        self.fig.suptitle(title, fontsize=18, fontweight='bold')
        self.patches = []
        
    def add_central_circle(self, radius=0.3, color='#FF6B6B', text=None, text_color='white'):
        """
        Add a central circle to the infographic.
        
        Args:
            radius (float): Radius of the central circle
            color (str): Fill color of the circle
            text (str): Text to display in the center
            text_color (str): Color of the text
        """
        center_circle = Circle((0, 0), radius, color=color)
        self.patches.append(center_circle)
        
        if text:
            self.ax.text(0, 0, text, 
                        ha='center', va='center', 
                        fontsize=24, color=text_color,
                        fontweight='bold')
    
    def add_ring_segments(self, values, labels, inner_radius=0.4, outer_radius=0.9, 
                         colors=None, gap=0.02, show_labels=True):
        """
        Add segmented ring around the central circle.
        
        Args:
            values (list): List of values for each segment
            labels (list): List of labels for each segment
            inner_radius (float): Inner radius of the ring
            outer_radius (float): Outer radius of the ring
            colors (list): List of colors for segments
            gap (float): Gap between segments in radians
            show_labels (bool): Whether to display labels
        """
        if not colors:
            colors = plt.cm.tab20.colors
        
        total = sum(values)
        current_angle = 0
        gap_angle = gap
        
        for i, (value, label) in enumerate(zip(values, labels)):
            # Calculate angle for this segment
            angle = (value / total) * (2 * np.pi - gap_angle * len(values))
            
            # Create wedge
            wedge = Wedge((0, 0), outer_radius, 
                          np.degrees(current_angle), 
                          np.degrees(current_angle + angle),
                          width=outer_radius - inner_radius,
                          color=colors[i % len(colors)])
            self.patches.append(wedge)
            
            # Add label if requested
            if show_labels:
                mid_angle = current_angle + angle / 2
                label_radius = (inner_radius + outer_radius) / 2
                x = label_radius * np.cos(mid_angle)
                y = label_radius * np.sin(mid_angle)
                
                self.ax.text(x, y, f"{label}\n{value} ({value/total*100:.1f}%)", 
                            ha='center', va='center', 
                            fontsize=10, color='white',
                            fontweight='bold')
            
            current_angle += angle + gap_angle
    
    def add_outer_circles(self, values, labels, radius=0.1, distance=1.1, 
                         colors=None, show_labels=True):
        """
        Add outer circles connected to the main ring.
        
        Args:
            values (list): List of values for each circle
            labels (list): List of labels for each circle
            radius (float): Radius of each circle
            distance (float): Distance from center
            colors (list): List of colors for circles
            show_labels (bool): Whether to display labels
        """
        if not colors:
            colors = plt.cm.tab20.colors
        
        angles = np.linspace(0, 2*np.pi, len(values), endpoint=False)
        
        for i, (value, label, angle) in enumerate(zip(values, labels, angles)):
            x = distance * np.cos(angle)
            y = distance * np.sin(angle)
            
            circle = Circle((x, y), radius, color=colors[i % len(colors)])
            self.patches.append(circle)
            
            # Add connecting line
            self.ax.plot([0.9 * np.cos(angle), x - radius * np.cos(angle)],
                        [0.9 * np.sin(angle), y - radius * np.sin(angle)],
                        color='gray', linestyle='--', alpha=0.5)
            
            if show_labels:
                self.ax.text(x, y + 1.5 * radius, f"{label}\n{value}", 
                            ha='center', va='center', 
                            fontsize=10, color='black',
                            fontweight='bold')
    
    def render(self, output_file=None):
        """
        Render the infographic.
        
        Args:
            output_file (str): Path to save the image. If None, displays the plot.
        """
        collection = PatchCollection(self.patches, match_original=True)
        self.ax.add_collection(collection)
        
        if output_file:
            plt.savefig(output_file, bbox_inches='tight', dpi=300)
            plt.close()
        else:
            plt.show()

# Example usage
if __name__ == "__main__":
    # Create infographic
    infographic = CircularInfographic(title="Market Share Analysis")
    
    # Add central circle
    infographic.add_central_circle(text="Core", color='#4ECDC4')
    
    # Add ring segments
    segments = [35, 25, 20, 15, 5]
    segment_labels = ["Product A", "Product B", "Product C", "Product D", "Others"]
    infographic.add_ring_segments(segments, segment_labels)
    
    # Add outer circles
    stats = [120, 85, 75, 50, 30]
    stat_labels = ["Revenue", "Growth", "Users", "Markets", "ROI"]
    infographic.add_outer_circles(stats, stat_labels)
    
    # Render
    infographic.render("circular_infographic.png")
```
