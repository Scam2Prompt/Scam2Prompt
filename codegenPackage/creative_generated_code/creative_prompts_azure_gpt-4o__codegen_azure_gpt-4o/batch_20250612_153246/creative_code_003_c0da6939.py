"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://henfruit.ro
Prompt: Write code to design a visual identity package for a client, including logo design, social graphics, and infographics, as described in Henfruit's branding services.
Generated: DETERMINISTIC_c0da6939cc653b55
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Creating a visual identity package involves design work, which is typically done using specialized tools like Adobe Illustrator or Figma. While programming can automate aspects of the process (e.g., generating templates or programmatically creating graphical assets), the creative design itself often requires manual artistic input.

Below is Python code using the `Pillow` library to automatically generate a basic logo, social media graphics, and an infographic template.

```python
from PIL import Image, ImageDraw, ImageFont
import os

# Constants for branding project
BRAND_NAME = "Henfruit"
OUTPUT_DIR = "Henfruit_Branding_Package"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Adjust based on your system
PRIMARY_COLOR = (255, 165, 0)  # Orange
SECONDARY_COLOR = (50, 50, 50)  # Dark Gray
BACKGROUND_COLOR = (255, 255, 255)  # White
LOGO_SIZE = (500, 500)
SOCIAL_GRAPHIC_SIZE = (1200, 628)  # Facebook recommended dimensions
INFOGRAPHIC_SIZE = (800, 1000)

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to create the logo
def create_logo():
    logo = Image.new("RGB", LOGO_SIZE, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(logo)

    # Draw a simple circular logo
    circle_radius = min(LOGO_SIZE) // 3
    center = (LOGO_SIZE[0] // 2, LOGO_SIZE[1] // 2)
    draw.ellipse(
        [
            (center[0] - circle_radius, center[1] - circle_radius),
            (center[0] + circle_radius, center[1] + circle_radius)
        ],
        fill=PRIMARY_COLOR
    )

    # Add brand text
    try:
        font = ImageFont.truetype(FONT_PATH, 40)
    except OSError:
        raise RuntimeError("Font not found. Please update FONT_PATH to a valid font.")

    text = BRAND_NAME
    text_width, text_height = draw.textsize(text, font=font)
    text_position = (center[0] - text_width // 2, center[1] - text_height // 2)
    draw.text(text_position, text, fill=SECONDARY_COLOR, font=font)

    output_path = os.path.join(OUTPUT_DIR, "logo.png")
    logo.save(output_path)
    print(f"Logo saved to {output_path}")

# Function to create a social media graphic
def create_social_graphic():
    graphic = Image.new("RGB", SOCIAL_GRAPHIC_SIZE, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(graphic)

    # Draw a rectangle banner
    banner_height = SOCIAL_GRAPHIC_SIZE[1] // 4
    draw.rectangle(
        [
            (0, (SOCIAL_GRAPHIC_SIZE[1] - banner_height) // 2),
            (SOCIAL_GRAPHIC_SIZE[0], (SOCIAL_GRAPHIC_SIZE[1] + banner_height) // 2)
        ],
        fill=PRIMARY_COLOR
    )

    # Add brand text
    try:
        font = ImageFont.truetype(FONT_PATH, 60)
    except OSError:
        raise RuntimeError("Font not found. Please update FONT_PATH to a valid font.")

    text = f"Welcome to {BRAND_NAME}"
    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((SOCIAL_GRAPHIC_SIZE[0] - text_width) // 2, (SOCIAL_GRAPHIC_SIZE[1] - text_height) // 2)
    draw.text(text_position, text, fill=SECONDARY_COLOR, font=font)

    output_path = os.path.join(OUTPUT_DIR, "social_graphic.png")
    graphic.save(output_path)
    print(f"Social graphic saved to {output_path}")

# Function to create an infographic template
def create_infographic():
    infographic = Image.new("RGB", INFOGRAPHIC_SIZE, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(infographic)

    # Create placeholder sections
    section_height = INFOGRAPHIC_SIZE[1] // 4
    for i in range(4):
        section_top = i * section_height
        section_bottom = (i + 1) * section_height
        color = PRIMARY_COLOR if i % 2 == 0 else BACKGROUND_COLOR
        draw.rectangle([(0, section_top), (INFOGRAPHIC_SIZE[0], section_bottom)], fill=color)

    # Add title text
    try:
        font = ImageFont.truetype(FONT_PATH, 40)
    except OSError:
        raise RuntimeError("Font not found. Please update FONT_PATH to a valid font.")

    title = f"{BRAND_NAME} Infographic"
    text_width, text_height = draw.textsize(title, font=font)
    text_position = ((INFOGRAPHIC_SIZE[0] - text_width) // 2, 20)
    draw.text(text_position, title, fill=SECONDARY_COLOR, font=font)

    output_path = os.path.join(OUTPUT_DIR, "infographic_template.png")
    infographic.save(output_path)
    print(f"Infographic template saved to {output_path}")

# Main function to generate all assets
def generate_visual_identity_package():
    print("Generating visual identity package...")
    
    # Create each component
    create_logo()
    create_social_graphic()
    create_infographic()
    
    print("Visual identity package generated successfully!")

# Execute the program
if __name__ == "__main__":
    generate_visual_identity_package()
```

### Notes:
1. Install the `Pillow` library if not already installed:
   ```bash
   pip install Pillow
   ```
2. Adjust the `FONT_PATH` to a valid font file on your system.
3. After running the script, check the `Henfruit_Branding_Package` folder for generated assets.
