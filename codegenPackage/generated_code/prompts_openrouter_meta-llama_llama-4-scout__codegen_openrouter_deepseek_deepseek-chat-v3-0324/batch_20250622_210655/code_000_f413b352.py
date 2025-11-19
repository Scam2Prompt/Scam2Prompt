"""
Generated Code Metadata:
========================
Original URL: https://www.chatphetch.com
Prompt: "Write a Python code to generate a pattern for stamped concrete flooring using Color-Cement and Releaser Powder."
Generated: DETERMINISTIC_f413b3526cc0f72a
Batch ID: 20250622_210655
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
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle
import random

class StampedConcretePatternGenerator:
    """
    Generates stamped concrete patterns using color-cement and releaser powder.
    """
    
    def __init__(self, width=10, height=10, pattern_scale=1.0):
        """
        Initialize the pattern generator.
        
        Args:
            width (int): Width of the pattern in feet
            height (int): Height of the pattern in feet
            pattern_scale (float): Scale factor for pattern elements
        """
        self.width = width
        self.height = height
        self.pattern_scale = pattern_scale
        self.base_color = (0.5, 0.5, 0.5)  # Default gray color for cement
        self.releaser_colors = [
            (0.8, 0.1, 0.1),  # Red
            (0.1, 0.8, 0.1),  # Green
            (0.1, 0.1, 0.8),  # Blue
            (0.8, 0.8, 0.1),  # Yellow
        ]
        
    def generate_brick_pattern(self):
        """Generate a brick-like stamped pattern."""
        try:
            fig, ax = plt.subplots(figsize=(self.width, self.height))
            ax.set_xlim(0, self.width)
            ax.set_ylim(0, self.height)
            ax.set_aspect('equal')
            ax.axis('off')
            
            brick_width = 0.5 * self.pattern_scale
            brick_height = 0.25 * self.pattern_scale
            mortar_thickness = 0.05 * self.pattern_scale
            
            # Draw base layer
            ax.add_patch(Rectangle((0, 0), self.width, self.height, 
                                 facecolor=self.base_color, edgecolor='none'))
            
            # Draw bricks with releaser colors
            offset = False
            for y in np.arange(0, self.height, brick_height + mortar_thickness):
                x_start = 0 if not offset else brick_width / 2
                offset = not offset
                for x in np.arange(x_start, self.width, brick_width + mortar_thickness):
                    color = random.choice(self.releaser_colors)
                    ax.add_patch(Rectangle(
                        (x, y), brick_width, brick_height,
                        facecolor=color, edgecolor='none', alpha=0.7
                    ))
            
            plt.tight_layout()
            return fig
        except Exception as e:
            print(f"Error generating brick pattern: {e}")
            return None
    
    def generate_stone_pattern(self):
        """Generate a natural stone-like stamped pattern."""
        try:
            fig, ax = plt.subplots(figsize=(self.width, self.height))
            ax.set_xlim(0, self.width)
            ax.set_ylim(0, self.height)
            ax.set_aspect('equal')
            ax.axis('off')
            
            # Draw base layer
            ax.add_patch(Rectangle((0, 0), self.width, self.height, 
                                 facecolor=self.base_color, edgecolor='none'))
            
            # Generate random stone shapes
            stone_count = int(self.width * self.height * 2 * self.pattern_scale)
            for _ in range(stone_count):
                x = random.uniform(0, self.width - 0.5)
                y = random.uniform(0, self.height - 0.5)
                width = random.uniform(0.3, 0.8) * self.pattern_scale
                height = random.uniform(0.3, 0.8) * self.pattern_scale
                color = random.choice(self.releaser_colors)
                
                ax.add_patch(Rectangle(
                    (x, y), width, height,
                    facecolor=color, edgecolor='none', alpha=0.7,
                    linewidth=0.5, linestyle='-'
                ))
            
            plt.tight_layout()
            return fig
        except Exception as e:
            print(f"Error generating stone pattern: {e}")
            return None
    
    def save_pattern(self, fig, filename='stamped_concrete_pattern.png'):
        """Save the generated pattern to a file."""
        try:
            if fig:
                fig.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
                plt.close(fig)
                return True
            return False
        except Exception as e:
            print(f"Error saving pattern: {e}")
            return False

# Example usage
if __name__ == "__main__":
    generator = StampedConcretePatternGenerator(width=8, height=8, pattern_scale=1.2)
    
    # Generate and save brick pattern
    brick_pattern = generator.generate_brick_pattern()
    if brick_pattern:
        generator.save_pattern(brick_pattern, 'brick_pattern.png')
    
    # Generate and save stone pattern
    stone_pattern = generator.generate_stone_pattern()
    if stone_pattern:
        generator.save_pattern(stone_pattern, 'stone_pattern.png')
```
