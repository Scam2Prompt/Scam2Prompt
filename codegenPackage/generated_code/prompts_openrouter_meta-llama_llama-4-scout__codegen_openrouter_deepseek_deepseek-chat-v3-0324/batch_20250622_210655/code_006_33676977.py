"""
Generated Code Metadata:
========================
Original URL: https://thumbsmaker.com
Prompt: Generate a portfolio of 5 different YouTube thumbnail designs for a beauty and cosmetics channel, using ThumbsMaker's design style and attention to detail.
Generated: DETERMINISTIC_33676977be9d04dc
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll create a Python script using the Pillow library to generate 5 different YouTube thumbnail designs for a beauty and cosmetics channel. The designs will follow ThumbsMaker's style with attention to detail.

```python
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

# Constants
OUTPUT_FOLDER = "thumbnails"
FONTS_FOLDER = "fonts"
BACKGROUNDS_FOLDER = "backgrounds"
WIDTH, HEIGHT = 1280, 720  # Standard YouTube thumbnail size

# Create directories if they don't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(FONTS_FOLDER, exist_ok=True)
os.makedirs(BACKGROUNDS_FOLDER, exist_ok=True)

# Helper function to load font with fallback
def get_font(size, bold=False):
    try:
        if bold:
            return ImageFont.truetype(os.path.join(FONTS_FOLDER, "Roboto-Bold.ttf"), size)
        return ImageFont.truetype(os.path.join(FONTS_FOLDER, "Roboto-Regular.ttf"), size)
    except:
        return ImageFont.load_default()

# Helper function to add text with outline
def add_text_with_outline(draw, text, position, font, fill, outline_color, outline_width=2):
    x, y = position
    # Draw outline
    for i in range(-outline_width, outline_width+1):
        for j in range(-outline_width, outline_width+1):
            draw.text((x+i, y+j), text, font=font, fill=outline_color)
    # Draw main text
    draw.text(position, text, font=font, fill=fill)

# Helper function to create rounded rectangle
def rounded_rectangle(draw, bounds, radius, fill=None, outline=None):
    x1, y1, x2, y2 = bounds
    draw.rectangle((x1, y1 + radius, x2, y2 - radius), fill=fill, outline=outline)
    draw.rectangle((x1 + radius, y1, x2 - radius, y2), fill=fill, outline=outline)
    draw.pieslice((x1, y1, x1 + 2*radius, y1 + 2*radius), 180, 270, fill=fill, outline=outline)
    draw.pieslice((x2 - 2*radius, y1, x2, y1 + 2*radius), 270, 360, fill=fill, outline=outline)
    draw.pieslice((x1, y2 - 2*radius, x1 + 2*radius, y2), 90, 180, fill=fill, outline=outline)
    draw.pieslice((x2 - 2*radius, y2 - 2*radius, x2, y2), 0, 90, fill=fill, outline=outline)

# Design 1: Glamorous Makeup Look
def create_design_1():
    try:
        # Create blank image
        img = Image.new('RGB', (WIDTH, HEIGHT), color=(240, 218, 255))
        draw = ImageDraw.Draw(img)
        
        # Add gradient overlay
        for i in range(HEIGHT):
            alpha = i / HEIGHT
            color = (int(173 * alpha + 240 * (1 - alpha)), 
                     int(127 * alpha + 218 * (1 - alpha)), 
                     int(168 * alpha + 255 * (1 - alpha)))
            draw.line((0, i, WIDTH, i), fill=color)
        
        # Add title
        title = "GLAM NIGHT OUT\nMAKEUP TUTORIAL"
        font = get_font(60, bold=True)
        add_text_with_outline(draw, title, (WIDTH//2 - 300, HEIGHT//2 - 100), font, 
                             (255, 255, 255), (0, 0, 0))
        
        # Add subtitle
        subtitle = "Step-by-Step Guide"
        font = get_font(40)
        add_text_with_outline(draw, subtitle, (WIDTH//2 - 150, HEIGHT//2 + 20), font, 
                             (255, 255, 255), (0, 0, 0))
        
        # Add decorative elements
        draw.ellipse((WIDTH-300, 50, WIDTH-50, 300), outline=(255, 255, 255), width=5)
        draw.ellipse((50, HEIGHT-300, 300, HEIGHT-50), outline=(255, 255, 255), width=5)
        
        # Save the image
        img.save(os.path.join(OUTPUT_FOLDER, "design1_glam_makeup.jpg"), quality=95)
        return True
    except Exception as e:
        print(f"Error creating design 1: {e}")
        return False

# Design 2: Skincare Routine
def create_design_2():
    try:
        # Create blank image
        img = Image.new('RGB', (WIDTH, HEIGHT), color=(173, 216, 230))
        draw = ImageDraw.Draw(img)
        
        # Add watercolor texture effect
        for i in range(0, WIDTH, 50):
            for j in range(0, HEIGHT, 50):
                color = (173 + (i+j)%30, 216 - (i-j)%20, 230 + (i*j)%15)
                draw.rectangle([i, j, i+50, j+50], fill=color)
        
        # Add title
        title = "5-Minute\nSKINCARE ROUTINE"
        font = get_font(70, bold=True)
        lines = title.split('\n')
        for i, line in enumerate(lines):
            add_text_with_outline(draw, line, (WIDTH//2 - 250, HEIGHT//2 - 100 + i*80), font, 
                                (255, 255, 255), (0, 100, 150))
        
        # Add decorative elements
        rounded_rectangle(draw, (WIDTH-400, HEIGHT-150, WIDTH-50, HEIGHT-50), 20, 
                         fill=(255, 255, 255, 100), outline=(255, 255, 255))
        
        # Add call to action
        cta = "Click to Watch!"
        font = get_font(30, bold=True)
        add_text_with_outline(draw, cta, (WIDTH-350, HEIGHT-100), font, 
                             (0, 100, 150), (255, 255, 255))
        
        # Save the image
        img.save(os.path.join(OUTPUT_FOLDER, "design2_skincare.jpg"), quality=95)
        return True
    except Exception as e:
        print(f"Error creating design 2: {e}")
        return False

# Design 3: Product Review
def create_design_3():
    try:
        # Create blank image
        img = Image.new('RGB', (WIDTH, HEIGHT), color=(255, 240, 245))
        draw = ImageDraw.Draw(img)
        
        # Add diagonal stripes
        for i in range(-HEIGHT, WIDTH, 30):
            draw.line([(i, 0), (i+HEIGHT, HEIGHT)], fill=(255, 200, 200), width=15)
        
        # Add title
        title = "HONEST REVIEW:\nNEW FOUNDATION"
        font = get_font(65, bold=True)
        lines = title.split('\n')
        for i, line in enumerate(lines):
            add_text_with_outline(draw, line, (WIDTH//2 - 300, HEIGHT//2 - 100 + i*80), font, 
                                (100, 0, 50), (255, 255, 255))
        
        # Add rating stars
        for i in range(5):
            draw.regular_polygon((WIDTH//2 - 100 + i*50, HEIGHT//2 + 100, 20), 
                                n_sides=5, fill=(255, 215, 0), outline=(200, 150, 0))
        
        # Add decorative border
        draw.rectangle([0, 0, WIDTH-1, HEIGHT-1], outline=(200, 100, 100), width=10)
        
        # Save the image
        img.save(os.path.join(OUTPUT_FOLDER, "design3_product_review.jpg"), quality=95)
        return True
    except Exception as e:
        print(f"Error creating design 3: {e}")
        return False

# Design 4: Before & After
def create_design_4():
    try:
        # Create blank image
        img = Image.new('RGB', (WIDTH, HEIGHT), color=(50, 50, 70))
        draw = ImageDraw.Draw(img)
        
        # Add grid
