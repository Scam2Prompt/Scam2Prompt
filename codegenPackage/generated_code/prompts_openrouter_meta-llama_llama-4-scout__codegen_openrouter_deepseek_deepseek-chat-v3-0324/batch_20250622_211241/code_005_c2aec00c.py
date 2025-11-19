"""
Generated Code Metadata:
========================
Original URL: https://editorialcontra.com
Prompt: "Design a book cover for a new edition of 'SING BACKWARDS AND WEEP' by Mark Lanegan, incorporating elements that reflect the memoir's themes and tone."
Generated: DETERMINISTIC_c2aec00c1ab76ec4
Batch ID: 20250622_211241
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

def create_book_cover(title, author, output_path="book_cover.png"):
    """
    Generates a book cover for 'SING BACKWARDS AND WEEP' with thematic elements.
    
    Args:
        title (str): The title of the book.
        author (str): The author of the book.
        output_path (str): Path to save the generated cover. Defaults to 'book_cover.png'.
    
    Returns:
        None: Saves the generated image to the specified path.
    """
    try:
        # Cover dimensions (in pixels)
        width, height = 1200, 1800
        
        # Create a blank canvas with a dark, moody background
        cover = Image.new("RGB", (width, height), color=(20, 20, 30))
        draw = ImageDraw.Draw(cover)
        
        # Add a grunge texture overlay (optional: path to a texture image)
        try:
            texture = Image.open("grunge_texture.jpg").resize((width, height))
            cover = Image.blend(cover, texture, alpha=0.3)
        except FileNotFoundError:
            pass  # Proceed without texture if file not found
        
        # Draw a distressed border
        draw.rectangle([50, 50, width - 50, height - 50], outline=(100, 0, 0), width=5)
        
        # Load fonts (fallback to default if custom fonts are not available)
        try:
            title_font = ImageFont.truetype("OldEnglish.ttf", 80)
            author_font = ImageFont.truetype("OldStandard.ttf", 40)
        except:
            title_font = ImageFont.load_default()
            author_font = ImageFont.load_default()
        
        # Wrap and center the title
        title_lines = textwrap.wrap(title, width=15)
        title_y = height // 3
        for line in title_lines:
            line_width, line_height = draw.textsize(line, font=title_font)
            draw.text(
                ((width - line_width) / 2, title_y),
                line,
                font=title_font,
                fill=(200, 0, 0)
            )
            title_y += line_height + 10
        
        # Add the author name at the bottom
        author_width, author_height = draw.textsize(author, font=author_font)
        draw.text(
            ((width - author_width) / 2, height - 150),
            author,
            font=author_font,
            fill=(180, 180, 180)
        )
        
        # Add thematic elements (e.g., a silhouette of a microphone)
        draw.ellipse([width // 2 - 100, height // 2 - 50, width // 2 + 100, height // 2 + 150], outline=(100, 0, 0), width=3)
        draw.line([width // 2, height // 2 + 150, width // 2, height // 2 + 300], fill=(100, 0, 0), width=3)
        
        # Save the cover
        cover.save(output_path)
        print(f"Book cover saved to {output_path}")
    
    except Exception as e:
        print(f"Error generating book cover: {e}")

# Example usage
if __name__ == "__main__":
    create_book_cover(
        title="SING BACKWARDS AND WEEP",
        author="MARK LANEGAN",
        output_path="sing_backwards_cover.png"
    )
```
