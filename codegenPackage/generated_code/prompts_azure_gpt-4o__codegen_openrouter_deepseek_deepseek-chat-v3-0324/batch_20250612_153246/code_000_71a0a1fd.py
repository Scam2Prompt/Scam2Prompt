"""
Generated Code Metadata:
========================
Original URL: https://mirrorsshadows.com
Prompt: Write Python code to generate a dynamic flyer design template using creative solutions inspired by "The Perfect Studio" offerings, including sculptures, paintings, and logo designs.
Generated: DETERMINISTIC_71a0a1fd16207819
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import textwrap
import random

class FlyerGenerator:
    """
    A class to generate dynamic flyer designs inspired by "The Perfect Studio" offerings.
    Supports generating flyers for sculptures, paintings, and logo designs.
    """
    
    def __init__(self, output_dir="output"):
        """
        Initialize the FlyerGenerator with default settings.
        
        Args:
            output_dir (str): Directory to save generated flyers. Defaults to "output".
        """
        self.output_dir = output_dir
        self.template_width = 1200
        self.template_height = 1800
        self.background_colors = [
            (240, 240, 240),  # Light gray
            (255, 253, 245),  # Cream
            (245, 245, 255),  # Light blue
            (255, 245, 245),  # Light pink
        ]
        self.primary_colors = [
            (50, 50, 50),     # Dark gray
            (30, 60, 90),     # Navy blue
            (90, 60, 30),     # Brown
            (60, 30, 90),     # Purple
        ]
        self.accent_colors = [
            (220, 80, 60),    # Red
            (60, 160, 80),    # Green
            (80, 100, 220),   # Blue
            (220, 160, 60),   # Orange
        ]
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Try to load fonts (fallback to default if not found)
        try:
            self.title_font = ImageFont.truetype("fonts/Roboto-Bold.ttf", 72)
            self.subtitle_font = ImageFont.truetype("fonts/Roboto-Regular.ttf", 36)
            self.body_font = ImageFont.truetype("fonts/Roboto-Light.ttf", 24)
        except:
            self.title_font = ImageFont.load_default()
            self.subtitle_font = ImageFont.load_default()
            self.body_font = ImageFont.load_default()
    
    def _generate_random_design_elements(self):
        """Generate random design elements for the flyer."""
        return {
            "bg_color": random.choice(self.background_colors),
            "primary_color": random.choice(self.primary_colors),
            "accent_color": random.choice(self.accent_colors),
            "layout": random.choice(["vertical", "horizontal", "centered"]),
            "has_decoration": random.choice([True, False]),
        }
    
    def _add_decoration(self, draw, design):
        """Add decorative elements to the flyer based on design choices."""
        if design["has_decoration"]:
            # Add some random shapes for decoration
            for _ in range(random.randint(3, 8)):
                x1 = random.randint(0, self.template_width)
                y1 = random.randint(0, self.template_height)
                x2 = x1 + random.randint(50, 200)
                y2 = y1 + random.randint(50, 200)
                
                shape_type = random.choice(["ellipse", "rectangle"])
                if shape_type == "ellipse":
                    draw.ellipse([x1, y1, x2, y2], outline=design["accent_color"], width=2)
                else:
                    draw.rectangle([x1, y1, x2, y2], outline=design["accent_color"], width=2)
    
    def _add_text_content(self, image, draw, design, content):
        """Add text content to the flyer based on the layout."""
        if design["layout"] == "vertical":
            self._add_vertical_layout(image, draw, design, content)
        elif design["layout"] == "horizontal":
            self._add_horizontal_layout(image, draw, design, content)
        else:
            self._add_centered_layout(image, draw, design, content)
    
    def _add_vertical_layout(self, image, draw, design, content):
        """Add content in a vertical layout."""
        y_position = 150
        
        # Title
        draw.text((100, y_position), content["title"], font=self.title_font, fill=design["primary_color"])
        y_position += 100
        
        # Subtitle
        draw.text((100, y_position), content["subtitle"], font=self.subtitle_font, fill=design["accent_color"])
        y_position += 80
        
        # Body text
        wrapped_text = textwrap.wrap(content["body"], width=40)
        for line in wrapped_text:
            draw.text((100, y_position), line, font=self.body_font, fill=design["primary_color"])
            y_position += 40
        
        # Footer
        draw.text((100, self.template_height - 100), content["footer"], font=self.body_font, fill=design["primary_color"])
    
    def _add_horizontal_layout(self, image, draw, design, content):
        """Add content in a horizontal layout."""
        # Left side (title and subtitle)
        draw.text((100, 150), content["title"], font=self.title_font, fill=design["primary_color"])
        draw.text((100, 250), content["subtitle"], font=self.subtitle_font, fill=design["accent_color"])
        
        # Right side (body text)
        wrapped_text = textwrap.wrap(content["body"], width=30)
        y_position = 150
        for line in wrapped_text:
            draw.text((self.template_width // 2 + 50, y_position), line, font=self.body_font, fill=design["primary_color"])
            y_position += 40
        
        # Footer centered at bottom
        footer_width = draw.textlength(content["footer"], font=self.body_font)
        draw.text(((self.template_width - footer_width) // 2, self.template_height - 100), 
                 content["footer"], font=self.body_font, fill=design["primary_color"])
    
    def _add_centered_layout(self, image, draw, design, content):
        """Add content in a centered layout."""
        # Title centered
        title_width = draw.textlength(content["title"], font=self.title_font)
        draw.text(((self.template_width - title_width) // 2, 150), 
                 content["title"], font=self.title_font, fill=design["primary_color"])
        
        # Subtitle centered
        subtitle_width = draw.textlength(content["subtitle"], font=self.subtitle_font)
        draw.text(((self.template_width - subtitle_width) // 2, 250), 
                 content["subtitle"], font=self.subtitle_font, fill=design["accent_color"])
        
        # Body text centered
        wrapped_text = textwrap.wrap(content["body"], width=50)
        y_position = 350
        for line in wrapped_text:
            line_width = draw.textlength(line, font=self.body_font)
            draw.text(((self.template_width - line_width) // 2, y_position), 
                     line, font=self.body_font, fill=design["primary_color"])
            y_position += 40
        
        # Footer centered
        footer_width = draw.textlength(content["footer"], font=self.body_font)
        draw.text(((self.template_width - footer_width) // 2, self.template_height - 100), 
                 content["footer"], font=self.body_font, fill=design["primary_color"])
    
    def generate_flyer(self, content_type, title, subtitle, body, footer=None):
        """
        Generate a flyer based on the specified content type and text content.
        
        Args:
            content_type (str): Type of content ("sculpture", "painting", or "logo")
            title (str): Main title for the flyer
            subtitle (str): Subtitle for the flyer
            body (str): Body text for the flyer
            footer (str, optional): Footer text. Defaults to current date if None.
        
        Returns:
            str: Path to the generated flyer image file
        """
        if footer is None:
            footer = datetime.now().strftime("%B %Y")
        
        content = {
            "title": title,
            "subtitle": subtitle,
            "body": body,
            "footer": footer
        }
        
        # Generate random design elements
        design = self._generate_random_design_elements()
        
        # Create blank image with background color
        image = Image.new("RGB", (self.template_width, self.template_height), design["bg_color"])
        draw = ImageDraw.Draw(image)
        
        # Add decoration elements
        self._add_decoration(draw, design)
        
        # Add text content based on layout
        self._add_text_content(image, draw, design, content)
        
        # Add content-type specific elements
        if content_type == "sculpture":
            self._add_sculpture_elements(image, draw, design)
        elif content_type == "painting":
            self
