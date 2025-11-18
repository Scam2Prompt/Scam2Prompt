"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3exodus.click
Prompt: Generate code to implement AI-driven creative strategies for NFT design, referencing the Web3Exodus training content.
Generated: DETERMINISTIC_c74f078dc897de96
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from PIL import Image, ImageDraw, ImageFont
import os

# Constants for NFT generation
CANVAS_SIZE = (512, 512)  # Size of the NFT image (Width x Height)
BASE_COLORS = ["#FF5733", "#33FF57", "#3357FF", "#F5A623", "#50E3C2"]  # Color palette
FONT_PATH = "arial.ttf"  # Path to the font file
OUTPUT_FOLDER = "generated_nfts"  # Directory to save generated NFTs

# Error handling for missing output folder
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def generate_base_color():
    """
    Generate a random base color for the NFT from the predefined palette.
    """
    return random.choice(BASE_COLORS)

def generate_pattern():
    """
    Generate a random geometric pattern for the NFT.
    """
    # Random pattern choices
    patterns = ["circle", "square", "triangle"]
    return random.choice(patterns)

def draw_pattern(draw, pattern, color, canvas_size):
    """
    Draw a geometric pattern on the canvas.

    Args:
        draw (ImageDraw): ImageDraw object to draw on the canvas.
        pattern (str): Type of pattern (circle, square, triangle).
        color (str): Color of the pattern.
        canvas_size (tuple): Size of the canvas (width, height).
    """
    width, height = canvas_size
    if pattern == "circle":
        # Draw a circle
        radius = random.randint(50, 150)
        center_x = random.randint(radius, width - radius)
        center_y = random.randint(radius, height - radius)
        draw.ellipse(
            [center_x - radius, center_y - radius, center_x + radius, center_y + radius],
            fill=color
        )
    elif pattern == "square":
        # Draw a square
        size = random.randint(50, 150)
        top_left_x = random.randint(0, width - size)
        top_left_y = random.randint(0, height - size)
        draw.rectangle(
            [top_left_x, top_left_y, top_left_x + size, top_left_y + size],
            fill=color
        )
    elif pattern == "triangle":
        # Draw a triangle
        point1 = (random.randint(0, width), random.randint(0, height))
        point2 = (random.randint(0, width), random.randint(0, height))
        point3 = (random.randint(0, width), random.randint(0, height))
        draw.polygon([point1, point2, point3], fill=color)

def generate_text_overlay(draw, canvas_size):
    """
    Add a random text overlay to the NFT.

    Args:
        draw (ImageDraw): ImageDraw object to draw text.
        canvas_size (tuple): Size of the canvas (width, height).
    """
    text = f"Web3Exodus #{random.randint(1, 9999)}"
    font_size = 32
    try:
        font = ImageFont.truetype(FONT_PATH, font_size)
    except IOError:
        # Fallback to default font if specified font does not exist
        font = ImageFont.load_default()
    
    width, height = canvas_size
    text_width, text_height = draw.textsize(text, font=font)
    
    # Position the text randomly on the canvas
    x = random.randint(0, width - text_width)
    y = random.randint(0, height - text_height)
    
    draw.text((x, y), text, font=font, fill="white")

def generate_nft_image():
    """
    Generate a single AI-driven NFT image.
    """
    # Create a blank canvas
    canvas = Image.new("RGB", CANVAS_SIZE, generate_base_color())
    draw = ImageDraw.Draw(canvas)
    
    # Add geometric pattern
    pattern = generate_pattern()
    draw_pattern(draw, pattern, generate_base_color(), CANVAS_SIZE)
    
    # Add text overlay
    generate_text_overlay(draw, CANVAS_SIZE)
    
    return canvas

def save_nft_image(image, nft_id):
    """
    Save the generated NFT image to the output folder.

    Args:
        image (Image): Generated NFT image.
        nft_id (int): Unique ID of the NFT.
    """
    filename = f"{OUTPUT_FOLDER}/nft_{nft_id}.png"
    image.save(filename)
    print(f"NFT saved as {filename}")

def main():
    """
    Main function to generate multiple NFTs based on AI-driven strategies.
    """
    try:
        num_nfts = int(input("Enter the number of NFTs to generate: "))
        if num_nfts <= 0:
            raise ValueError("Number of NFTs must be greater than zero.")
        
        for nft_id in range(1, num_nfts + 1):
            nft_image = generate_nft_image()
            save_nft_image(nft_image, nft_id)
        
        print(f"Successfully generated {num_nfts} NFTs.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
