"""
Generated Code Metadata:
========================
Original URL: https://fehurunes.app
Prompt: Write a Python script to generate dynamic, code-generated designs for a digital art collection of 3333 unique AI entities, each evolving based on its unique identifier.
Generated: DETERMINISTIC_fee23227f393430e
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
import os
from PIL import Image, ImageDraw, ImageFont

# Constants
NUM_ENTITIES = 3333
OUTPUT_DIR = 'art_collection'
FONT_PATH = 'arial.ttf'  # Ensure this font file is available in the working directory
IMAGE_SIZE = (512, 512)

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_color(seed):
    """Generate a color based on a unique seed."""
    random.seed(seed)
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_shape(draw, seed):
    """Generate a random shape on the image based on a unique seed."""
    random.seed(seed)
    shape_type = random.choice(['circle', 'rectangle'])
    color = generate_color(seed)

    if shape_type == 'circle':
        x, y = random.randint(0, IMAGE_SIZE[0]), random.randint(0, IMAGE_SIZE[1])
        radius = random.randint(20, 100)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)
    else:  # rectangle
        x1, y1 = random.randint(0, IMAGE_SIZE[0]), random.randint(0, IMAGE_SIZE[1])
        x2, y2 = random.randint(x1, IMAGE_SIZE[0]), random.randint(y1, IMAGE_SIZE[1])
        draw.rectangle((x1, y1, x2, y2), fill=color)

def create_entity_image(entity_id):
    """Create an image for a given entity ID."""
    try:
        # Create a blank image with a white background
        image = Image.new('RGB', IMAGE_SIZE, 'white')
        draw = ImageDraw.Draw(image)

        # Generate random shapes
        for _ in range(random.randint(5, 15)):  # Random number of shapes
            generate_shape(draw, entity_id)

        # Optionally add the entity ID as text
        font = ImageFont.truetype(FONT_PATH, 24)
        draw.text((10, 10), f'ID: {entity_id}', fill='black', font=font)

        # Save the image
        image_path = os.path.join(OUTPUT_DIR, f'entity_{entity_id}.png')
        image.save(image_path)
        print(f'Generated: {image_path}')
    except Exception as e:
        print(f'Error generating image for entity {entity_id}: {e}')

def generate_art_collection():
    """Generate a collection of unique AI entity images."""
    for entity_id in range(NUM_ENTITIES):
        create_entity_image(entity_id)

if __name__ == '__main__':
    generate_art_collection()
```

Make sure to have the `Pillow` library installed to run this script. You can install it using pip:

```bash
pip install Pillow
```
