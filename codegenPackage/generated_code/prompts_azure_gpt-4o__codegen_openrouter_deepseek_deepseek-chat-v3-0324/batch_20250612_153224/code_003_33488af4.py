"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: Suggest tools or libraries for designing eye-catching marketing materials for pubs and bars, and write code to generate sample designs using those tools.
Generated: DETERMINISTIC_33488af408b11879
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script generates sample marketing materials for pubs and bars using the Pillow library for image manipulation.
It creates a promotional poster and a social media post with customizable text and styling.
"""

from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

# Constants
OUTPUT_DIR = "output"
FONT_PATH = "arial.ttf"  # Default font, can be replaced with custom fonts
BACKGROUND_IMAGE = "background.jpg"  # Sample background image

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_poster(title, subtitle, offer_text, output_filename):
    """
    Generates a promotional poster for a pub/bar.
    
    Args:
        title (str): Main title text
        subtitle (str): Subtitle text
        offer_text (str): Special offer text
        output_filename (str): Name for the output file
    """
    try:
        # Create a blank image or use a background
        try:
            img = Image.open(BACKGROUND_IMAGE)
        except FileNotFoundError:
            img = Image.new('RGB', (1200, 1800), color=(20, 20, 40))  # Dark background if no image
        
        draw = ImageDraw.Draw(img)
        
        # Load fonts with fallbacks
        try:
            title_font = ImageFont.truetype(FONT_PATH, 80)
            subtitle_font = ImageFont.truetype(FONT_PATH, 50)
            offer_font = ImageFont.truetype(FONT_PATH, 60)
        except IOError:
            # Use default fonts if custom font not found
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            offer_font = ImageFont.load_default()
        
        # Calculate text positions
        width, height = img.size
        title_position = (width//2, height//4)
        subtitle_position = (width//2, height//3)
        offer_position = (width//2, height//2)
        
        # Draw text with outline effect
        def draw_outlined_text(draw, text, position, font, fill, outline_color, outline_width=2):
            x, y = position
            for adj in range(outline_width):
                # Draw outline
                draw.text((x-adj, y-adj), text, font=font, fill=outline_color)
                draw.text((x+adj, y-adj), text, font=font, fill=outline_color)
                draw.text((x-adj, y+adj), text, font=font, fill=outline_color)
                draw.text((x+adj, y+adj), text, font=font, fill=outline_color)
            # Draw main text
            draw.text(position, text, font=font, fill=fill)
        
        # Draw title
        draw_outlined_text(draw, title, title_position, title_font, (255, 215, 0), (0, 0, 0))
        
        # Draw subtitle
        draw_outlined_text(draw, subtitle, subtitle_position, subtitle_font, (255, 255, 255), (0, 0, 0))
        
        # Wrap and draw offer text
        offer_lines = textwrap.wrap(offer_text, width=20)
        for i, line in enumerate(offer_lines):
            y_offset = offer_position[1] + i * 70
            draw_outlined_text(draw, line, (offer_position[0], y_offset), offer_font, (255, 100, 100), (0, 0, 0))
        
        # Save the image
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        img.save(output_path)
        print(f"Poster saved to {output_path}")
        
    except Exception as e:
        print(f"Error generating poster: {e}")

def generate_social_media_post(headline, details, output_filename):
    """
    Generates a square social media post for promotions.
    
    Args:
        headline (str): Main headline text
        details (str): Additional details text
        output_filename (str): Name for the output file
    """
    try:
        # Create a square image
        img = Image.new('RGB', (1080, 1080), color=(40, 20, 20))  # Dark red background
        
        draw = ImageDraw.Draw(img)
        
        # Load fonts with fallbacks
        try:
            headline_font = ImageFont.truetype(FONT_PATH, 70)
            details_font = ImageFont.truetype(FONT_PATH, 40)
        except IOError:
            headline_font = ImageFont.load_default()
            details_font = ImageFont.load_default()
        
        # Draw headline
        headline_lines = textwrap.wrap(headline, width=20)
        for i, line in enumerate(headline_lines):
            draw.text((540, 300 + i * 80), line, font=headline_font, fill=(255, 255, 255), anchor="mm")
        
        # Draw details
        details_lines = textwrap.wrap(details, width=30)
        for i, line in enumerate(details_lines):
            draw.text((540, 500 + i * 50), line, font=details_font, fill=(200, 200, 200), anchor="mm")
        
        # Add decorative elements
        draw.rectangle([(200, 200), (880, 880)], outline=(255, 215, 0), width=5)
        
        # Save the image
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        img.save(output_path)
        print(f"Social media post saved to {output_path}")
        
    except Exception as e:
        print(f"Error generating social media post: {e}")

# Example usage
if __name__ == "__main__":
    # Generate sample materials
    generate_poster(
        title="Happy Hour!",
        subtitle="The Rusty Barrel",
        offer_text="2-for-1 Cocktails\n5-7pm Weekdays",
        output_filename="happy_hour_poster.jpg"
    )
    
    generate_social_media_post(
        headline="Live Music Friday Night",
        details="Join us for great drinks and live music from 8pm!\nNo cover charge before 9pm.",
        output_filename="live_music_post.jpg"
    )
```
