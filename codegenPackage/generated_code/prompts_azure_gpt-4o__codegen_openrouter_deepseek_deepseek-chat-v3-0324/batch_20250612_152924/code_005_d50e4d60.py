"""
Generated Code Metadata:
========================
Original URL: https://kroonation.com
Prompt: Create a branding-focused logo design script using Python, suitable for the services offered by Kroo Nation's graphic design team.
Generated: DETERMINISTIC_d50e4d60a9e6e8ab
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import turtle
import random
import math
from PIL import Image, ImageDraw, ImageFont
import os

class LogoDesigner:
    """
    A branding-focused logo design generator for Kroo Nation's graphic design team.
    This script creates customizable logos with text and geometric elements.
    """
    
    def __init__(self, output_dir="logos"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def _validate_color(self, color):
        """Validate and convert color input to RGB tuple."""
        if isinstance(color, str):
            if color.startswith('#'):
                try:
                    return tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
                except ValueError:
                    raise ValueError("Invalid hex color format. Use '#RRGGBB'.")
            else:
                raise ValueError("Color must be RGB tuple or hex string starting with '#'")
        elif isinstance(color, tuple) and len(color) == 3:
            return color
        else:
            raise ValueError("Color must be RGB tuple or hex string starting with '#'")

    def _generate_random_palette(self):
        """Generate a random but harmonious color palette."""
        base_hue = random.random()
        return [
            self._hsv_to_rgb(base_hue, 0.9, 0.7),
            self._hsv_to_rgb((base_hue + 0.2) % 1.0, 0.7, 0.8),
            self._hsv_to_rgb((base_hue + 0.4) % 1.0, 0.5, 0.9)
        ]

    def _hsv_to_rgb(self, h, s, v):
        """Convert HSV color to RGB."""
        h_i = int(h * 6)
        f = h * 6 - h_i
        p = v * (1 - s)
        q = v * (1 - f * s)
        t = v * (1 - (1 - f) * s)
        
        if h_i == 0:
            r, g, b = v, t, p
        elif h_i == 1:
            r, g, b = q, v, p
        elif h_i == 2:
            r, g, b = p, v, t
        elif h_i == 3:
            r, g, b = p, q, v
        elif h_i == 4:
            r, g, b = t, p, v
        else:
            r, g, b = v, p, q
            
        return (int(r * 255), int(g * 255), int(b * 255))

    def _draw_geometric_logo(self, filename, size=500, bg_color="#FFFFFF"):
        """Create a geometric logo using turtle graphics."""
        try:
            bg_color = self._validate_color(bg_color)
            palette = self._generate_random_palette()
            
            screen = turtle.Screen()
            screen.setup(size, size)
            screen.bgcolor(bg_color)
            screen.delay(0)
            
            t = turtle.Turtle()
            t.speed(0)
            t.hideturtle()
            
            # Draw geometric pattern
            for i in range(36):
                t.color(random.choice(palette))
                t.width(2)
                t.penup()
                t.goto(0, 0)
                t.setheading(i * 10)
                t.pendown()
                t.forward(size * 0.4)
                t.left(90)
                t.circle(size * 0.1)
                
            # Save the drawing
            ts = turtle.getscreen()
            ts.getcanvas().postscript(file=os.path.join(self.output_dir, f"{filename}_geo.eps"))
            
            # Convert EPS to PNG
            img = Image.open(os.path.join(self.output_dir, f"{filename}_geo.eps"))
            img.save(os.path.join(self.output_dir, f"{filename}_geo.png"), "PNG")
            
            turtle.bye()
            return os.path.join(self.output_dir, f"{filename}_geo.png")
            
        except Exception as e:
            turtle.bye()
            raise RuntimeError(f"Error generating geometric logo: {str(e)}")

    def _draw_text_logo(self, filename, text="Kroo Nation", size=500, 
                       bg_color="#FFFFFF", text_color="#000000", font_path=None):
        """Create a text-based logo with custom styling."""
        try:
            bg_color = self._validate_color(bg_color)
            text_color = self._validate_color(text_color)
            
            img = Image.new("RGB", (size, size), bg_color)
            draw = ImageDraw.Draw(img)
            
            # Try to load custom font or fall back to default
            try:
                if font_path and os.path.exists(font_path):
                    font = ImageFont.truetype(font_path, size // 4)
                else:
                    font = ImageFont.load_default()
            except Exception:
                font = ImageFont.load_default()
            
            # Calculate text position
            text_width, text_height = draw.textsize(text, font=font)
            position = ((size - text_width) // 2, (size - text_height) // 2)
            
            # Draw text with outline
            outline_size = max(2, size // 100)
            for x in range(-outline_size, outline_size + 1):
                for y in range(-outline_size, outline_size + 1):
                    if x != 0 or y != 0:
                        draw.text(
                            (position[0] + x, position[1] + y),
                            text,
                            font=font,
                            fill=(50, 50, 50)
                        )
            
            draw.text(position, text, fill=text_color, font=font)
            
            # Save the image
            output_path = os.path.join(self.output_dir, f"{filename}_text.png")
            img.save(output_path, "PNG")
            return output_path
            
        except Exception as e:
            raise RuntimeError(f"Error generating text logo: {str(e)}")

    def generate_logo(self, filename="kroo_logo", logo_type="combined", 
                     text="Kroo Nation", size=1000, bg_color="#FFFFFF", 
                     text_color="#000000", font_path=None):
        """
        Generate a logo with specified parameters.
        
        Args:
            filename: Base name for output files
            logo_type: 'geometric', 'text', or 'combined'
            text: Text to display (for text or combined logos)
            size: Output image size in pixels
            bg_color: Background color (hex or RGB tuple)
            text_color: Text color (hex or RGB tuple)
            font_path: Path to custom font file
            
        Returns:
            Path to generated logo file
        """
        try:
            if logo_type not in ['geometric', 'text', 'combined']:
                raise ValueError("logo_type must be 'geometric', 'text', or 'combined'")
                
            if logo_type == "geometric":
                return self._draw_geometric_logo(filename, size, bg_color)
            elif logo_type == "text":
                return self._draw_text_logo(filename, text, size, bg_color, text_color, font_path)
            else:
                # Generate both and combine
                geo_path = self._draw_geometric_logo(filename, size, bg_color)
                text_path = self._draw_text_logo(filename, text, size, (0, 0, 0, 0), text_color, font_path)
                
                # Combine images
                geo_img = Image.open(geo_path)
                text_img = Image.open(text_path)
                
                # Ensure text image has alpha channel
                if text_img.mode != 'RGBA':
                    text_img = text_img.convert('RGBA')
                
                combined = Image.alpha_composite(geo_img.convert('RGBA'), text_img)
                combined_path = os.path.join(self.output_dir, f"{filename}_combined.png")
                combined.save(combined_path, "PNG")
                
                # Clean up temporary files
                os.remove(geo_path)
                os.remove(text_path)
                
                return combined_path
                
        except Exception as e:
            raise RuntimeError(f"Error generating logo: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        designer = LogoDesigner()
        
        # Generate a geometric logo
        geo_logo = designer.generate_logo(
            filename="kroo_geo",
            logo_type="geometric",
            size=800,
            bg_color="#F5F5F5"
        )
        print(f"Geometric logo saved to: {geo_logo}")
        
        # Generate a text logo
        text_logo = designer.generate_logo(
            filename="kroo_text",
            logo_type="text",
            text="Kroo Nation",
            size=800,
            bg_color="#FFFFFF",
            text_color="#3366CC"
        )
        print(f"Text logo saved to: {text_logo}")
        
        # Generate a combined logo
        combined_logo = designer.generate_logo(
            filename="kroo_combined",
            logo_type="
