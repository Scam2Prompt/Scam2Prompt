"""
Generated Code Metadata:
========================
Original URL: https://art-blocks.site
Prompt: "Generate Python code for creating digital art blocks using the Pillow library."
Generated: DETERMINISTIC_b5d68be31131bbb5
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw
import random
import os

def generate_art_block(width=800, height=600, blocks=10, output_path="art_block.png"):
    """
    Generate a digital art block image with random colored rectangles.
    
    Args:
        width (int): Width of the output image in pixels.
        height (int): Height of the output image in pixels.
        blocks (int): Number of colored blocks to generate.
        output_path (str): Path to save the generated image.
        
    Returns:
        str: Path to the saved image file.
    """
    try:
        # Create a blank white image
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)
        
        # Generate random blocks
        for _ in range(blocks):
            # Random position and size
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(x1, width)
            y2 = random.randint(y1, height)
            
            # Random color
            color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            
            # Draw the rectangle
            draw.rectangle([x1, y1, x2, y2], fill=color, outline="black")
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        
        # Save the image
        image.save(output_path)
        return output_path
    
    except Exception as e:
        print(f"Error generating art block: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    output_file = generate_art_block(
        width=1024,
        height=768,
        blocks=15,
        output_path="output/art_block.png"
    )
    print(f"Art block generated at: {output_file}")
```
