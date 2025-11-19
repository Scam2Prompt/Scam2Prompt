"""
Generated Code Metadata:
========================
Original URL: https://chumchums.xyz
Prompt: "Develop a basic script to generate unique digital art pieces, inspired by the 'Chum Generator 3000' concept."
Generated: DETERMINISTIC_4ae0d9928b28227c
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import os
from PIL import Image, ImageDraw, ImageColor

# Constants
OUTPUT_DIR = "generated_art"
CANVAS_SIZE = (500, 500)  # Width x Height in pixels
NUM_ART_PIECES = 10  # Number of unique art pieces to generate
SHAPE_COUNT = 20  # Number of shapes per art piece
COLORS = ["#FF5733", "#33FF57", "#3357FF", "#F1C40F", "#9B59B6", "#E74C3C", "#1ABC9C", "#34495E"]

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_random_color():
    """Generate a random color from the predefined color palette."""
    return random.choice(COLORS)

def generate_random_position():
    """Generate a random position within the canvas."""
    x = random.randint(0, CANVAS_SIZE[0])
    y = random.randint(0, CANVAS_SIZE[1])
    return x, y

def generate_random_shape(draw):
    """Generate a random shape (circle, rectangle, or line) on the canvas."""
    shape_type = random.choice(["circle", "rectangle", "line"])
    color = generate_random_color()
    start_pos = generate_random_position()
    end_pos = generate_random_position()

    if shape_type == "circle":
        # Draw an ellipse (circle-like shape)
        bounding_box = [start_pos, end_pos]
        draw.ellipse(bounding_box, fill=color, outline=color)
    elif shape_type == "rectangle":
        # Draw a rectangle
        bounding_box = [start_pos, end_pos]
        draw.rectangle(bounding_box, fill=color, outline=color)
    elif shape_type == "line":
        # Draw a line
        draw.line([start_pos, end_pos], fill=color, width=3)

def generate_art_piece(index):
    """Generate a single unique art piece."""
    # Create a blank canvas
    image = Image.new("RGB", CANVAS_SIZE, "white")
    draw = ImageDraw.Draw(image)

    # Draw random shapes
    for _ in range(SHAPE_COUNT):
        generate_random_shape(draw)

    # Save the generated art piece
    file_name = f"art_piece_{index + 1}.png"
    file_path = os.path.join(OUTPUT_DIR, file_name)
    image.save(file_path)
    print(f"Art piece saved: {file_path}")

def main():
    """Main function to generate multiple unique art pieces."""
    print("Starting art generation...")
    for i in range(NUM_ART_PIECES):
        try:
            generate_art_piece(i)
        except Exception as e:
            print(f"Error generating art piece {i + 1}: {e}")
    print("Art generation complete.")

if __name__ == "__main__":
    main()
```
