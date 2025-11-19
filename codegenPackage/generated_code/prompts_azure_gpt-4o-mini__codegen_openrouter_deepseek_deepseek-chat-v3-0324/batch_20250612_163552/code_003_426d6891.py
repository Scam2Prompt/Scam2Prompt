"""
Generated Code Metadata:
========================
Original URL: https://penguinbookspublishers.com
Prompt: Create a sample book cover design using a graphic design library, inspired by the captivating cover design services offered by Penguin Books Publishers.
Generated: DETERMINISTIC_426d6891e25aacf0
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Book Cover Design Generator
Inspired by Penguin Books' classic cover designs
Uses the Pillow library for image manipulation
"""

from PIL import Image, ImageDraw, ImageFont
import random
import os
import textwrap

class BookCoverGenerator:
    """
    Generates a book cover with:
    - Solid color background with vertical stripe
    - Title and author text in a clean layout
    - Random color scheme based on classic Penguin styles
    """
    
    def __init__(self, title, author, output_path="cover.png"):
        """
        Initialize book cover generator
        
        Args:
            title (str): Book title
            author (str): Author name
            output_path (str): Output file path
        """
        self.title = title
        self.author = author
        self.output_path = output_path
        self.width = 1800
        self.height = 2700
        
        # Classic Penguin-inspired color schemes
        self.color_palettes = [
            # (background, stripe, text)
            ("#FF4136", "#85144b", "#FFFFFF"),  # Red/Purple/White
            ("#2ECC40", "#3D9970", "#111111"),  # Green/Teal/Black
            ("#0074D9", "#7FDBFF", "#FFFFFF"),  # Blue/Aqua/White
            ("#FFDC00", "#FF851B", "#111111"),  # Yellow/Orange/Black
            ("#AAAAAA", "#FFFFFF", "#111111"),  # Gray/White/Black
        ]
        
        # Validate inputs
        if not title or not author:
            raise ValueError("Title and author must be provided")
            
    def generate_cover(self):
        """Generate and save the book cover image"""
        try:
            # Select random color scheme
            bg_color, stripe_color, text_color = random.choice(self.color_palettes)
            
            # Create blank image
            cover = Image.new("RGB", (self.width, self.height), bg_color)
            draw = ImageDraw.Draw(cover)
            
            # Add vertical stripe (classic Penguin design element)
            stripe_width = self.width // 3
            draw.rectangle(
                [(0, 0), (stripe_width, self.height)],
                fill=stripe_color,
                outline=None
            )
            
            # Load font (fallback to default if custom font not found)
            try:
                font_path = os.path.join(os.path.dirname(__file__), "fonts", "GillSans.ttf")
                title_font = ImageFont.truetype(font_path, 120)
                author_font = ImageFont.truetype(font_path, 60)
            except:
                title_font = ImageFont.load_default()
                author_font = ImageFont.load_default()
            
            # Wrap title text if needed
            wrapped_title = "\n".join(textwrap.wrap(self.title, width=20))
            
            # Calculate text positions
            title_position = (self.width * 0.4, self.height * 0.4)
            author_position = (self.width * 0.4, self.height * 0.7)
            
            # Add title and author text
            draw.text(
                title_position,
                wrapped_title,
                font=title_font,
                fill=text_color,
                spacing=30
            )
            
            draw.text(
                author_position,
                f"by {self.author}",
                font=author_font,
                fill=text_color,
                spacing=10
            )
            
            # Save the final image
            cover.save(self.output_path)
            print(f"Cover generated successfully at {self.output_path}")
            
            return True
            
        except Exception as e:
            print(f"Error generating cover: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    cover = BookCoverGenerator(
        title="The Art of Programming",
        author="Donald Knuth",
        output_path="sample_cover.png"
    )
    cover.generate_cover()
```
