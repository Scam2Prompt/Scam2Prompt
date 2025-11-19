"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: "Create a graphic design solution for a microbrewery looking to establish a presence in the market, inspired by Lords Marketing's style."
Generated: DETERMINISTIC_35b39a84fed5ba48
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw, ImageFont
import random
import os

class MicrobreweryBranding:
    """
    A class to generate branding materials for a microbrewery inspired by Lords Marketing's style.
    Includes logo generation, color schemes, and label designs.
    """
    
    def __init__(self, brewery_name, tagline):
        """
        Initialize the branding generator with brewery details.
        
        Args:
            brewery_name (str): Name of the brewery
            tagline (str): Tagline/slogan for the brewery
        """
        self.brewery_name = brewery_name
        self.tagline = tagline
        self.color_palette = self._generate_color_palette()
        self.font_path = self._get_font()
        
    def _generate_color_palette(self):
        """
        Generate a color palette inspired by craft beer aesthetics.
        
        Returns:
            dict: Color palette with primary, secondary, and accent colors
        """
        return {
            'primary': (45, 45, 45),       # Dark gray/black
            'secondary': (214, 170, 70),   # Gold
            'accent1': (200, 60, 60),      # Deep red
            'accent2': (60, 100, 60),      # Forest green
            'background': (250, 250, 245)  # Off-white
        }
    
    def _get_font(self):
        """
        Get font path, trying to find a suitable craft beer style font.
        
        Returns:
            str: Path to font file
        """
        # Try common font locations
        possible_fonts = [
            '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf',
            '/Library/Fonts/Arial.ttf',
            'C:\\Windows\\Fonts\\Arial.ttf'
        ]
        
        for font in possible_fonts:
            if os.path.exists(font):
                return font
        
        # Fallback to default PIL font
        return None
    
    def generate_logo(self, output_path='logo.png', size=(800, 800)):
        """
        Generate a logo for the microbrewery.
        
        Args:
            output_path (str): Path to save the logo
            size (tuple): Dimensions of the logo
            
        Returns:
            str: Path to the generated logo
        """
        try:
            # Create blank image
            img = Image.new('RGB', size, self.color_palette['background'])
            draw = ImageDraw.Draw(img)
            
            # Draw circular element (common in beer logos)
            circle_pos = (size[0]//4, size[1]//4, size[0]//4*3, size[1]//4*3)
            draw.ellipse(circle_pos, fill=self.color_palette['secondary'], outline=self.color_palette['primary'], width=5)
            
            # Add text
            try:
                if self.font_path:
                    font = ImageFont.truetype(self.font_path, 40)
                else:
                    font = ImageFont.load_default()
            except:
                font = ImageFont.load_default()
                
            # Draw brewery name
            text_width, text_height = draw.textsize(self.brewery_name, font=font)
            draw.text(
                ((size[0] - text_width) // 2, size[1]//2 + 20),
                self.brewery_name,
                font=font,
                fill=self.color_palette['primary']
            )
            
            # Draw tagline with smaller font
            tagline_font = ImageFont.truetype(self.font_path, 20) if self.font_path else ImageFont.load_default()
            tagline_width, tagline_height = draw.textsize(self.tagline, font=tagline_font)
            draw.text(
                ((size[0] - tagline_width) // 2, size[1]//2 + 70),
                self.tagline,
                font=tagline_font,
                fill=self.color_palette['accent1']
            )
            
            # Save logo
            img.save(output_path)
            return output_path
            
        except Exception as e:
            print(f"Error generating logo: {e}")
            return None
    
    def generate_beer_label(self, beer_name, beer_type, abv, output_path='label.png', size=(600, 800)):
        """
        Generate a beer label design.
        
        Args:
            beer_name (str): Name of the beer
            beer_type (str): Type of beer (IPA, Stout, etc.)
            abv (str): Alcohol by volume percentage
            output_path (str): Path to save the label
            size (tuple): Dimensions of the label
            
        Returns:
            str: Path to the generated label
        """
        try:
            # Create blank image
            img = Image.new('RGB', size, self.color_palette['background'])
            draw = ImageDraw.Draw(img)
            
            # Draw border
            border_width = 10
            draw.rectangle(
                [(border_width, border_width), (size[0]-border_width, size[1]-border_width)],
                outline=self.color_palette['primary'],
                width=5
            )
            
            # Add brewery name at top
            if self.font_path:
                font = ImageFont.truetype(self.font_path, 30)
            else:
                font = ImageFont.load_default()
                
            brewery_width, brewery_height = draw.textsize(self.brewery_name, font=font)
            draw.text(
                ((size[0] - brewery_width) // 2, 30),
                self.brewery_name,
                font=font,
                fill=self.color_palette['primary']
            )
            
            # Add beer name (larger text)
            beer_font = ImageFont.truetype(self.font_path, 50) if self.font_path else ImageFont.load_default()
            beer_width, beer_height = draw.textsize(beer_name, font=beer_font)
            draw.text(
                ((size[0] - beer_width) // 2, size[1]//3),
                beer_name,
                font=beer_font,
                fill=self.color_palette['accent1']
            )
            
            # Add beer type and ABV
            details_font = ImageFont.truetype(self.font_path, 25) if self.font_path else ImageFont.load_default()
            details_text = f"{beer_type} | ABV {abv}%"
            details_width, details_height = draw.textsize(details_text, font=details_font)
            draw.text(
                ((size[0] - details_width) // 2, size[1]//3 + 70),
                details_text,
                font=details_font,
                fill=self.color_palette['primary']
            )
            
            # Add decorative elements
            hop_positions = [
                (50, 150), (size[0]-100, 200), 
                (80, size[1]-150), (size[0]-70, size[1]-100)
            ]
            for x, y in hop_positions:
                self._draw_hop_icon(draw, x, y, 40, self.color_palette['accent2'])
            
            # Save label
            img.save(output_path)
            return output_path
            
        except Exception as e:
            print(f"Error generating label: {e}")
            return None
    
    def _draw_hop_icon(self, draw, x, y, size, color):
        """
        Draw a simple hop icon (decorative element).
        
        Args:
            draw (ImageDraw): Drawing context
            x (int): X position
            y (int): Y position
            size (int): Size of the icon
            color (tuple): RGB color tuple
        """
        # Draw hop cone shape
        draw.ellipse(
            [(x, y), (x + size, y + size)],
            outline=color,
            width=3
        )
        
        # Draw leaf-like elements
        for i in range(4):
            angle = i * 90
            dx = int(size * 0.4 * (1 if i % 2 == 0 else 0.6))
            dy = int(size * 0.4 * (1 if i % 2 == 1 else 0.6))
            draw.line(
                [(x + size//2, y + size//2), (x + size//2 + dx, y + size//2 + dy)],
                fill=color,
                width=3
            )
    
    def generate_color_scheme(self):
        """
        Return the generated color scheme for reference.
        
        Returns:
            dict: Color palette dictionary
        """
        return self.color_palette


# Example usage
if __name__ == "__main__":
    branding = MicrobreweryBranding(
        brewery_name="Hoppy Trails Brewing Co.",
        tagline="Crafted with Adventure in Mind"
    )
    
    # Generate logo
    logo_path = branding.generate_logo()
    print(f"Logo generated at: {logo_path}")
    
    # Generate sample label
    label_path = branding.generate_beer_label(
        beer_name="Trail
