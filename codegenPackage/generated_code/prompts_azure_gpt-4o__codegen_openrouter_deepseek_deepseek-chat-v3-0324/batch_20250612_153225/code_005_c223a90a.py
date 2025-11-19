"""
Generated Code Metadata:
========================
Original URL: https://vitalcs.net
Prompt: Write code to design a logo and banner using Python libraries, following the branding guidelines mentioned in Vital Corporate Solutions' graphic design services.
Generated: DETERMINISTIC_c223a90a32ba0836
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

class BrandLogoGenerator:
    """
    A class to generate logos and banners following Vital Corporate Solutions' branding guidelines.
    """
    
    def __init__(self):
        # Brand colors (RGB)
        self.primary_color = (0, 102, 204)  # Dark blue
        self.secondary_color = (255, 204, 0)  # Gold
        self.accent_color = (255, 255, 255)  # White
        self.background_color = (240, 240, 240)  # Light gray
        
        # Font paths (assuming we have these fonts available)
        self.primary_font = "arialbd.ttf"  # Bold Arial as fallback
        self.secondary_font = "arial.ttf"  # Regular Arial as fallback
        
        # Try to use more professional fonts if available
        try:
            self.primary_font = "Helvetica-Bold.ttf"
            self.secondary_font = "Helvetica.ttf"
        except:
            pass
    
    def generate_logo(self, company_name, output_path="logo.png", size=(800, 400)):
        """
        Generate a professional logo with the company name.
        
        Args:
            company_name (str): The name to display in the logo
            output_path (str): Path to save the logo image
            size (tuple): Dimensions of the logo (width, height)
        """
        try:
            # Create a new image with transparent background
            logo = Image.new("RGBA", size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(logo)
            
            # Draw a rectangle with primary color
            draw.rectangle([(0, 0), size], fill=self.primary_color)
            
            # Add a gold accent bar at the bottom
            accent_height = int(size[1] * 0.1)
            draw.rectangle(
                [(0, size[1] - accent_height), (size[0], size[1])],
                fill=self.secondary_color
            )
            
            # Calculate font size based on image height
            font_size = int(size[1] * 0.3)
            
            try:
                font = ImageFont.truetype(self.primary_font, font_size)
            except:
                font = ImageFont.load_default()
            
            # Calculate text position
            text_width, text_height = draw.textsize(company_name, font=font)
            text_x = (size[0] - text_width) // 2
            text_y = (size[1] - text_height - accent_height) // 2
            
            # Draw the company name
            draw.text(
                (text_x, text_y),
                company_name,
                font=font,
                fill=self.accent_color
            )
            
            # Save the logo
            logo.save(output_path, "PNG")
            print(f"Logo successfully saved to {output_path}")
            
        except Exception as e:
            print(f"Error generating logo: {str(e)}")
    
    def generate_banner(self, headline, subheadline="", output_path="banner.png", size=(1200, 600)):
        """
        Generate a professional banner with headline and optional subheadline.
        
        Args:
            headline (str): Main banner text
            subheadline (str): Secondary banner text
            output_path (str): Path to save the banner image
            size (tuple): Dimensions of the banner (width, height)
        """
        try:
            # Create a new image with light gray background
            banner = Image.new("RGB", size, self.background_color)
            draw = ImageDraw.Draw(banner)
            
            # Add a primary color rectangle on the left side
            rect_width = int(size[0] * 0.3)
            draw.rectangle([(0, 0), (rect_width, size[1])], fill=self.primary_color)
            
            # Calculate font sizes
            headline_font_size = int(size[1] * 0.15)
            subheadline_font_size = int(size[1] * 0.08)
            
            try:
                headline_font = ImageFont.truetype(self.primary_font, headline_font_size)
                subheadline_font = ImageFont.truetype(self.secondary_font, subheadline_font_size)
            except:
                headline_font = ImageFont.load_default()
                subheadline_font = ImageFont.load_default()
            
            # Wrap text if needed
            max_chars = int(size[0] * 0.6 / (headline_font_size * 0.6))
            wrapped_headline = textwrap.fill(headline, width=max_chars)
            
            # Calculate text positions
            text_x = rect_width + 50
            text_y_headline = (size[1] // 3) - (headline_font_size // 2)
            
            # Draw headline
            draw.text(
                (text_x, text_y_headline),
                wrapped_headline,
                font=headline_font,
                fill=self.primary_color
            )
            
            # Draw subheadline if provided
            if subheadline:
                text_y_subheadline = text_y_headline + headline_font_size + 20
                wrapped_subheadline = textwrap.fill(subheadline, width=max_chars * 2)
                draw.text(
                    (text_x, text_y_subheadline),
                    wrapped_subheadline,
                    font=subheadline_font,
                    fill=(100, 100, 100)  # Dark gray
                )
            
            # Add gold accent at the bottom
            accent_height = int(size[1] * 0.05)
            draw.rectangle(
                [(0, size[1] - accent_height), (size[0], size[1])],
                fill=self.secondary_color
            )
            
            # Save the banner
            banner.save(output_path, "PNG")
            print(f"Banner successfully saved to {output_path}")
            
        except Exception as e:
            print(f"Error generating banner: {str(e)}")

# Example usage
if __name__ == "__main__":
    brand_generator = BrandLogoGenerator()
    
    # Generate a logo
    brand_generator.generate_logo(
        company_name="Vital Corporate Solutions",
        output_path="vital_logo.png",
        size=(800, 400)
    )
    
    # Generate a banner
    brand_generator.generate_banner(
        headline="Innovative Business Solutions",
        subheadline="Driving growth through technology and strategy",
        output_path="vital_banner.png",
        size=(1200, 600)
    )
```
