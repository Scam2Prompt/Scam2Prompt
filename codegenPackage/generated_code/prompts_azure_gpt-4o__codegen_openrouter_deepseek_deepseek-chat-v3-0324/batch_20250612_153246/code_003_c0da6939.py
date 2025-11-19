"""
Generated Code Metadata:
========================
Original URL: https://henfruit.ro
Prompt: Write code to design a visual identity package for a client, including logo design, social graphics, and infographics, as described in Henfruit's branding services.
Generated: DETERMINISTIC_c0da6939cc653b55
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Visual Identity Package Generator for Henfruit Branding Services

This script generates a visual identity package including:
- Logo design variations
- Social media graphics
- Infographics

The package is created using Python with Pillow for image manipulation.
"""

from PIL import Image, ImageDraw, ImageFont
import os
import random
import textwrap
from datetime import datetime

class VisualIdentityGenerator:
    def __init__(self, brand_name, primary_color, secondary_color, font_path='arial.ttf'):
        """
        Initialize the visual identity generator with brand parameters.
        
        Args:
            brand_name (str): Name of the brand/client
            primary_color (tuple): RGB tuple for primary color
            secondary_color (tuple): RGB tuple for secondary color
            font_path (str): Path to font file (default: arial.ttf)
        """
        self.brand_name = brand_name
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.font_path = font_path
        self.output_dir = f"visual_identity_{brand_name}_{datetime.now().strftime('%Y%m%d')}"
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
    def generate_logo(self, variations=3):
        """
        Generate logo variations for the brand.
        
        Args:
            variations (int): Number of logo variations to generate
        """
        for i in range(1, variations + 1):
            try:
                # Create a blank image with white background
                img = Image.new('RGB', (800, 400), color='white')
                d = ImageDraw.Draw(img)
                
                # Choose a random logo style
                style = random.choice(['text_only', 'icon_left', 'icon_top'])
                
                # Load font
                try:
                    font = ImageFont.truetype(self.font_path, 60)
                except IOError:
                    font = ImageFont.load_default()
                
                if style == 'text_only':
                    # Simple text logo
                    d.text((50, 150), self.brand_name, fill=self.primary_color, font=font)
                elif style == 'icon_left':
                    # Logo with icon on left
                    d.ellipse((50, 100, 200, 250), fill=self.secondary_color)
                    d.text((250, 150), self.brand_name, fill=self.primary_color, font=font)
                else:
                    # Logo with icon on top
                    d.ellipse((300, 50, 500, 250), fill=self.secondary_color)
                    d.text((200, 270), self.brand_name, fill=self.primary_color, font=font)
                
                # Save the logo
                img.save(f'{self.output_dir}/logo_variation_{i}.png')
                print(f'Generated logo variation {i}')
                
            except Exception as e:
                print(f'Error generating logo variation {i}: {str(e)}')
    
    def generate_social_graphics(self, platforms=['facebook', 'twitter', 'instagram'], count=2):
        """
        Generate social media graphics for specified platforms.
        
        Args:
            platforms (list): List of platforms to generate graphics for
            count (int): Number of graphics per platform
        """
        sizes = {
            'facebook': (1200, 630),
            'twitter': (1024, 512),
            'instagram': (1080, 1080)
        }
        
        for platform in platforms:
            if platform not in sizes:
                print(f'Unsupported platform: {platform}')
                continue
                
            for i in range(1, count + 1):
                try:
                    size = sizes[platform]
                    img = Image.new('RGB', size, color='white')
                    d = ImageDraw.Draw(img)
                    
                    # Add platform-specific design elements
                    if platform == 'facebook':
                        # Facebook cover style
                        d.rectangle((0, 0, size[0], size[1]//3), fill=self.primary_color)
                        try:
                            font = ImageFont.truetype(self.font_path, 40)
                        except IOError:
                            font = ImageFont.load_default()
                        d.text((50, size[1]//2), f"Welcome to {self.brand_name}", fill='black', font=font)
                    
                    elif platform == 'twitter':
                        # Twitter header style
                        d.rectangle((0, 0, size[0], size[1]), fill=self.secondary_color)
                        try:
                            font = ImageFont.truetype(self.font_path, 60)
                        except IOError:
                            font = ImageFont.load_default()
                        d.text((50, 50), f"Follow us on Twitter\n@{self.brand_name}", fill='white', font=font)
                    
                    elif platform == 'instagram':
                        # Instagram square post
                        d.rectangle((0, 0, size[0], size[1]), fill=self.primary_color)
                        try:
                            font = ImageFont.truetype(self.font_path, 80)
                        except IOError:
                            font = ImageFont.load_default()
                        d.text((size[0]//4, size[1]//3), f"#{self.brand_name}", fill='white', font=font)
                    
                    img.save(f'{self.output_dir}/{platform}_graphic_{i}.png')
                    print(f'Generated {platform} graphic {i}')
                    
                except Exception as e:
                    print(f'Error generating {platform} graphic {i}: {str(e)}')
    
    def generate_infographic(self, data_points, title="Our Services"):
        """
        Generate an infographic with provided data points.
        
        Args:
            data_points (list): List of tuples (label, value)
            title (str): Title for the infographic
        """
        try:
            img = Image.new('RGB', (1000, 1500), color='white')
            d = ImageDraw.Draw(img)
            
            # Add title
            try:
                title_font = ImageFont.truetype(self.font_path, 60)
                body_font = ImageFont.truetype(self.font_path, 30)
            except IOError:
                title_font = ImageFont.load_default()
                body_font = ImageFont.load_default()
            
            d.text((100, 50), title, fill=self.primary_color, font=title_font)
            d.text((100, 120), f"Presented by {self.brand_name}", fill=self.secondary_color, font=body_font)
            
            # Add data points as bars
            y_position = 200
            max_value = max([value for _, value in data_points])
            
            for label, value in data_points:
                # Draw bar
                bar_width = int(800 * (value / max_value))
                d.rectangle((100, y_position, 100 + bar_width, y_position + 50), fill=self.primary_color)
                
                # Draw label and value
                d.text((100, y_position + 60), label, fill='black', font=body_font)
                d.text((100 + bar_width + 20, y_position), f"{value}%", fill=self.secondary_color, font=body_font)
                
                y_position += 120
            
            # Save the infographic
            img.save(f'{self.output_dir}/infographic.png')
            print('Generated infographic')
            
        except Exception as e:
            print(f'Error generating infographic: {str(e)}')
    
    def generate_full_package(self):
        """Generate the complete visual identity package."""
        print(f"Generating visual identity package for {self.brand_name}")
        self.generate_logo()
        self.generate_social_graphics()
        
        # Sample data for infographic
        sample_data = [
            ("Customer Satisfaction", 95),
            ("Market Growth", 78),
            ("Product Quality", 92),
            ("Brand Recognition", 85)
        ]
        self.generate_infographic(sample_data)
        print(f"Package generated in {self.output_dir}")

# Example usage
if __name__ == "__main__":
    try:
        # Customize these parameters for your client
        brand_name = "Henfruit"
        primary_color = (34, 139, 34)  # Forest green
        secondary_color = (255, 215, 0)  # Gold
        
        generator = VisualIdentityGenerator(brand_name, primary_color, secondary_color)
        generator.generate_full_package()
    except Exception as e:
        print(f"Error generating visual identity package: {str(e)}")
```
