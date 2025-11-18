"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artrecast.com
Prompt: Generate code to create a personalized NFT collection with unique attributes, similar to the "Custom NFT Collections" feature described on ArtRecast.
Generated: DETERMINISTIC_af096da27a1ba1bc
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
import os
from PIL import Image, ImageDraw, ImageFont

# Constants for NFT generation
OUTPUT_DIRECTORY = "nft_collection"
NFT_COUNT = 10
IMAGE_SIZE = (500, 500)  # Width x Height in pixels
FONT_PATH = "arial.ttf"  # Path to font file for text rendering
ATTRIBUTES = {
    "Background Color": ["Red", "Blue", "Green", "Yellow", "Purple"],
    "Foreground Shape": ["Circle", "Square", "Triangle", "Hexagon"],
    "Pattern": ["Stripes", "Dots", "Solid"],
    "Rarity": ["Common", "Uncommon", "Rare", "Legendary"]
}

# Helper function to generate random attributes
def generate_attributes():
    return {key: random.choice(values) for key, values in ATTRIBUTES.items()}

# Helper function to create NFT image based on attributes
def create_nft_image(attributes, nft_id):
    # Create a blank image
    img = Image.new("RGB", IMAGE_SIZE, color=attributes["Background Color"].lower())

    draw = ImageDraw.Draw(img)

    # Draw shapes based on the foreground shape
    shape_center = (IMAGE_SIZE[0] // 2, IMAGE_SIZE[1] // 2)
    shape_size = 100  # Size of the shape
    if attributes["Foreground Shape"] == "Circle":
        draw.ellipse(
            [shape_center[0] - shape_size, shape_center[1] - shape_size,
             shape_center[0] + shape_size, shape_center[1] + shape_size],
            fill="white"
        )
    elif attributes["Foreground Shape"] == "Square":
        draw.rectangle(
            [shape_center[0] - shape_size, shape_center[1] - shape_size,
             shape_center[0] + shape_size, shape_center[1] + shape_size],
            fill="white"
        )
    elif attributes["Foreground Shape"] == "Triangle":
        draw.polygon(
            [shape_center, 
             (shape_center[0] - shape_size, shape_center[1] + shape_size),
             (shape_center[0] + shape_size, shape_center[1] + shape_size)],
            fill="white"
        )
    elif attributes["Foreground Shape"] == "Hexagon":
        draw.polygon(
            [(shape_center[0], shape_center[1] - shape_size),
             (shape_center[0] - shape_size / 2, shape_center[1] - shape_size // 2),
             (shape_center[0] - shape_size / 2, shape_center[1] + shape_size // 2),
             (shape_center[0], shape_center[1] + shape_size),
             (shape_center[0] + shape_size / 2, shape_center[1] + shape_size // 2),
             (shape_center[0] + shape_size / 2, shape_center[1] - shape_size // 2)],
            fill="white"
        )

    # Add text for rarity
    try:
        font = ImageFont.truetype(FONT_PATH, 20)
    except IOError:
        font = ImageFont.load_default()  # Fall back to default font if loading fails

    draw.text((10, IMAGE_SIZE[1] - 30), f"Rarity: {attributes['Rarity']}", font=font, fill="white")

    # Save the image
    img_path = os.path.join(OUTPUT_DIRECTORY, f"nft_{nft_id}.png")
    img.save(img_path)

    return img_path

# Main function to generate NFT collection
def generate_nft_collection():
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

    collection_metadata = []
    
    for nft_id in range(1, NFT_COUNT + 1):
        attributes = generate_attributes()
        image_path = create_nft_image(attributes, nft_id)

        nft_metadata = {
            "id": nft_id,
            "attributes": attributes,
            "image": image_path
        }
        collection_metadata.append(nft_metadata)

    # Save metadata to JSON file
    metadata_path = os.path.join(OUTPUT_DIRECTORY, "metadata.json")
    with open(metadata_path, "w") as metadata_file:
        json.dump(collection_metadata, metadata_file, indent=4)

    print(f"Generated NFT collection in '{OUTPUT_DIRECTORY}' directory.")

if __name__ == "__main__":
    try:
        generate_nft_collection()
    except Exception as e:
        print(f"An error occurred: {e}")
```
