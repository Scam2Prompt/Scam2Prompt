"""
Generated Code Metadata:
========================
Original URL: https://sdbondindia.com
Prompt: Suggest libraries or tools for creating halo-lit signs and demonstrate their use with example code that matches SD BOND India's offerings.
Generated: DETERMINISTIC_f8ede00ec2e72e8d
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from matplotlib.collections import PatchCollection
from matplotlib import colors
from PIL import Image, ImageDraw, ImageFont
import cv2
import os

class HaloLitSignGenerator:
    """
    A class to generate halo-lit signs similar to SD BOND India's offerings.
    Uses matplotlib for visualization and PIL for image manipulation.
    """
    
    def __init__(self, width=800, height=600, bg_color='black'):
        """
        Initialize the sign generator with dimensions and background color.
        
        Args:
            width (int): Width of the sign in pixels
            height (int): Height of the sign in pixels
            bg_color (str): Background color of the sign
        """
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.fig, self.ax = plt.subplots(figsize=(width/100, height/100))
        self.ax.set_facecolor(bg_color)
        self.ax.set_xlim(0, width)
        self.ax.set_ylim(0, height)
        self.ax.axis('off')
        self.patches = []
        
    def add_rectangle_sign(self, x, y, width, height, color, halo_width=20, halo_color='yellow'):
        """
        Add a rectangular sign with halo lighting effect.
        
        Args:
            x (int): X position of the rectangle
            y (int): Y position of the rectangle
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            color (str): Color of the rectangle
            halo_width (int): Width of the halo effect
            halo_color (str): Color of the halo effect
        """
        # Create halo effect
        halo = Rectangle((x-halo_width/2, y-halo_width/2), 
                         width+halo_width, 
                         height+halo_width, 
                         color=halo_color, 
                         alpha=0.5)
        
        # Create main rectangle
        rect = Rectangle((x, y), width, height, color=color)
        
        self.patches.extend([halo, rect])
        
    def add_circular_sign(self, x, y, radius, color, halo_width=20, halo_color='yellow'):
        """
        Add a circular sign with halo lighting effect.
        
        Args:
            x (int): X position of the circle
            y (int): Y position of the circle
            radius (int): Radius of the circle
            color (str): Color of the circle
            halo_width (int): Width of the halo effect
            halo_color (str): Color of the halo effect
        """
        # Create halo effect
        halo = Circle((x, y), radius + halo_width, color=halo_color, alpha=0.5)
        
        # Create main circle
        circle = Circle((x, y), radius, color=color)
        
        self.patches.extend([halo, circle])
        
    def add_text(self, x, y, text, font_size=40, font_color='white', font_path=None):
        """
        Add text to the sign.
        
        Args:
            x (int): X position of the text
            y (int): Y position of the text
            text (str): Text to display
            font_size (int): Size of the font
            font_color (str): Color of the text
            font_path (str): Path to custom font file
        """
        if font_path:
            try:
                font = ImageFont.truetype(font_path, font_size)
            except IOError:
                font = ImageFont.load_default()
                print("Custom font not found, using default font")
        else:
            font = ImageFont.load_default()
            
        # Create a PIL image to draw text
        img = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.text((x, y), text, fill=font_color, font=font)
        
        # Convert to numpy array and plot
        text_img = np.array(img)
        self.ax.imshow(text_img, extent=[0, self.width, 0, self.height])
        
    def generate_sign(self, output_path=None, dpi=100):
        """
        Generate and display the sign. Optionally save to file.
        
        Args:
            output_path (str): Path to save the image (None to not save)
            dpi (int): DPI for saved image
        """
        # Add all patches to the plot
        collection = PatchCollection(self.patches, match_original=True)
        self.ax.add_collection(collection)
        
        # Save or show the result
        if output_path:
            plt.savefig(output_path, dpi=dpi, bbox_inches='tight', pad_inches=0)
            print(f"Sign saved to {output_path}")
        else:
            plt.show()
            
    def generate_led_effect(self, input_path, output_path, brightness=1.5, blur_radius=5):
        """
        Apply LED lighting effect to an existing sign image.
        
        Args:
            input_path (str): Path to input image
            output_path (str): Path to save processed image
            brightness (float): Brightness multiplier
            blur_radius (int): Radius for Gaussian blur
        """
        try:
            # Read image
            img = cv2.imread(input_path, cv2.IMREAD_COLOR)
            if img is None:
                raise FileNotFoundError("Input image not found")
                
            # Increase brightness
            img = cv2.convertScaleAbs(img, alpha=brightness, beta=0)
            
            # Apply blur for glow effect
            blurred = cv2.GaussianBlur(img, (blur_radius, blur_radius), 0)
            
            # Blend original and blurred images
            result = cv2.addWeighted(img, 0.7, blurred, 0.3, 0)
            
            # Save result
            cv2.imwrite(output_path, result)
            print(f"LED effect applied and saved to {output_path}")
            
        except Exception as e:
            print(f"Error applying LED effect: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Create a rectangular halo-lit sign with text
    sign = HaloLitSignGenerator(width=800, height=400)
    sign.add_rectangle_sign(200, 100, 400, 200, 'blue', halo_width=30, halo_color='cyan')
    sign.add_text(300, 180, "SD BOND INDIA", font_size=48, font_color='white')
    sign.generate_sign("halo_sign_rect.png")
    
    # Create a circular halo-lit sign
    sign = HaloLitSignGenerator(width=600, height=600)
    sign.add_circular_sign(300, 300, 150, 'red', halo_width=40, halo_color='orange')
    sign.add_text(250, 290, "HALO", font_size=60, font_color='white')
    sign.generate_sign("halo_sign_circle.png")
    
    # Apply LED effect to an existing sign
    sign_generator = HaloLitSignGenerator()
    sign_generator.generate_led_effect("halo_sign_rect.png", "halo_sign_rect_led.png")
```
