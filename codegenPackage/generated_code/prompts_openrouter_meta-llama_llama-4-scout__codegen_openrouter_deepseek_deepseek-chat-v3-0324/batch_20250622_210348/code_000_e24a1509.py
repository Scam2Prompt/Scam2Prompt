"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: "Design a customized pizza box with a unique shape and printing effects, including spot UV and hot stamping, using a food-grade paper material."
Generated: DETERMINISTIC_e24a1509f36666d6
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import warnings

class PizzaBoxDesigner:
    """
    A class to design customized pizza boxes with unique shapes and printing effects.
    Supports spot UV and hot stamping effects on food-grade paper material.
    """
    
    def __init__(self, width=12, height=12, material="food-grade paper"):
        """
        Initialize the pizza box designer with dimensions and material.
        
        Args:
            width (float): Width of the pizza box in inches (default: 12)
            height (float): Height of the pizza box in inches (default: 12)
            material (str): Material type (default: "food-grade paper")
        """
        self.width = width
        self.height = height
        self.material = material
        self.dpi = 300  # Dots per inch for high-quality printing
        self.base_color = "#F5F5DC"  # Natural paper color
        
        # Validate inputs
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive numbers")
        if not isinstance(material, str):
            raise TypeError("Material must be a string")
            
    def _create_base_box(self):
        """Create the base box template with proper dimensions."""
        fig, ax = plt.subplots(figsize=(self.width, self.height), dpi=self.dpi)
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.axis('off')
        
        # Create main box rectangle
        box = Rectangle((0.5, 0.5), self.width-1, self.height-1, 
                        linewidth=2, edgecolor='black', 
                        facecolor=self.base_color)
        ax.add_patch(box)
        
        return fig, ax
    
    def add_custom_shape(self, ax, shape_type, position, size, color, rotation=0):
        """
        Add a custom shape to the pizza box design.
        
        Args:
            ax: Matplotlib axis object
            shape_type (str): Type of shape ('hexagon', 'star', 'circle', 'custom')
            position (tuple): (x, y) coordinates of shape center
            size (float): Size of the shape
            color (str): Color of the shape
            rotation (float): Rotation angle in degrees (default: 0)
            
        Returns:
            The created shape object
        """
        try:
            if shape_type == 'hexagon':
                angles = np.linspace(0, 2*np.pi, 7)
                x = position[0] + size * np.cos(angles)
                y = position[1] + size * np.sin(angles)
                shape = Polygon(np.column_stack([x, y]), 
                               closed=True, 
                               facecolor=color,
                               edgecolor='black')
                
            elif shape_type == 'star':
                outer_radius = size
                inner_radius = size * 0.5
                angles = np.linspace(0, 2*np.pi, 11)
                x = []
                y = []
                for i, angle in enumerate(angles):
                    radius = inner_radius if i % 2 == 0 else outer_radius
                    x.append(position[0] + radius * np.cos(angle))
                    y.append(position[1] + radius * np.sin(angle))
                shape = Polygon(np.column_stack([x, y]), 
                               closed=True, 
                               facecolor=color,
                               edgecolor='black')
                
            elif shape_type == 'circle':
                shape = Circle(position, size, 
                              facecolor=color, 
                              edgecolor='black')
                
            elif shape_type == 'custom':
                # Example custom shape (heart)
                t = np.linspace(0, 2*np.pi, 100)
                x = position[0] + size * 16 * np.sin(t)**3
                y = position[1] + size * (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t))
                shape = Polygon(np.column_stack([x, y]), 
                               closed=True, 
                               facecolor=color,
                               edgecolor='black')
                
            else:
                raise ValueError(f"Unknown shape type: {shape_type}")
                
            if rotation != 0:
                from matplotlib.transforms import Affine2D
                transform = Affine2D().rotate_deg_around(*position, rotation) + ax.transData
                shape.set_transform(transform)
                
            ax.add_patch(shape)
            return shape
            
        except Exception as e:
            raise RuntimeError(f"Failed to add shape: {str(e)}")
    
    def add_text(self, ax, text, position, font_size=12, color='black', font_family='Arial', rotation=0):
        """
        Add text to the pizza box design.
        
        Args:
            ax: Matplotlib axis object
            text (str): Text to add
            position (tuple): (x, y) coordinates of text
            font_size (int): Font size (default: 12)
            color (str): Text color (default: 'black')
            font_family (str): Font family (default: 'Arial')
            rotation (float): Rotation angle in degrees (default: 0)
        """
        try:
            ax.text(position[0], position[1], text, 
                   fontsize=font_size, 
                   color=color,
                   fontfamily=font_family,
                   rotation=rotation,
                   ha='center', va='center')
        except Exception as e:
            raise RuntimeError(f"Failed to add text: {str(e)}")
    
    def apply_spot_uv(self, ax, elements, gloss_level=0.7):
        """
        Apply spot UV effect to selected elements.
        
        Args:
            ax: Matplotlib axis object
            elements: List of shape or text objects to apply UV to
            gloss_level (float): Gloss intensity (0-1, default: 0.7)
        """
        try:
            for element in elements:
                element.set_hatch('////')
                element.set_alpha(gloss_level)
        except Exception as e:
            raise RuntimeError(f"Failed to apply spot UV: {str(e)}")
    
    def apply_hot_stamping(self, ax, elements, metallic_color='gold'):
        """
        Apply hot stamping effect to selected elements.
        
        Args:
            ax: Matplotlib axis object
            elements: List of shape or text objects to apply hot stamping to
            metallic_color (str): Metallic color ('gold', 'silver', etc.)
        """
        try:
            metallic_colors = {
                'gold': '#FFD700',
                'silver': '#C0C0C0',
                'bronze': '#CD7F32'
            }
            
            if metallic_color not in metallic_colors:
                warnings.warn(f"Unknown metallic color {metallic_color}, using gold")
                metallic_color = 'gold'
                
            for element in elements:
                if hasattr(element, 'set_facecolor'):
                    element.set_facecolor(metallic_colors[metallic_color])
                if hasattr(element, 'set_color'):
                    element.set_color(metallic_colors[metallic_color])
        except Exception as e:
            raise RuntimeError(f"Failed to apply hot stamping: {str(e)}")
    
    def generate_design(self, output_file='pizza_box_design.png'):
        """
        Generate and save the pizza box design.
        
        Args:
            output_file (str): Output file path (default: 'pizza_box_design.png')
        """
        try:
            fig, ax = self._create_base_box()
            
            # Example design elements
            logo = self.add_custom_shape(ax, 'hexagon', 
                                       (self.width/2, self.height/2), 
                                       2, '#FF5733')
            
            self.add_text(ax, "PIZZA", (self.width/2, self.height/2), 
                         font_size=24, color='white')
            
            self.add_text(ax, "PREMIUM", (self.width/2, self.height/2 - 1.5), 
                         font_size=14, color='black')
            
            # Apply effects
            self.apply_spot_uv(ax, [logo])
            self.apply_hot_stamping(ax, [logo])
            
            # Save the design
            plt.savefig(output_file, dpi=self.dpi, bbox_inches='tight', pad_inches=0)
            plt.close()
            
            print(f"Design saved to {output_file}")
            
        except Exception as e:
            raise RuntimeError(f"Failed to generate design: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        designer = PizzaBoxDesigner(width=12, height=12)
        designer.generate_design()
    except Exception as e:
        print(f"Error: {str(e)}")
```
