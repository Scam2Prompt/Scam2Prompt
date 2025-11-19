"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.art-blocks.site
Prompt: Generate a code snippet for creating generative art using the Art Blocks platform.
Generated: DETERMINISTIC_1d3079d1e00182e2
Batch ID: 20250612_164049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Generative Artwork Script for Art Blocks Platform
This script uses the p5.js Python mode to create generative art compatible with platforms like Art Blocks.
"""

import random
from p5 import *

# Global variables for canvas dimensions
canvas_width = 800
canvas_height = 800

# Seed for reproducibility across runs
seed_value = 12345


def setup():
    """
    Setup the canvas and initialize random seed for deterministic art generation.
    """
    # Set the canvas size
    size(canvas_width, canvas_height)
    
    # Seed the random generator
    random.seed(seed_value)

    # Set background color
    background(255)  # White background


def draw():
    """
    Main draw function to generate the artwork.
    """
    # No continuous redraw, only draw once
    no_loop()

    # Define the number and characteristics of shapes
    num_shapes = 50

    for i in range(num_shapes):
        # Generate random position inside the canvas
        x = random.randint(0, canvas_width)
        y = random.randint(0, canvas_height)

        # Random size for the shape
        size_factor = random.randint(20, 100)

        # Randomize colors for each shape
        fill(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 150)  # RGBA

        # Randomize shape types and draw
        if random.randint(0, 1):  # 50% chance of circle
            ellipse(x, y, size_factor, size_factor)
        else:  # 50% chance of rectangle
            rect(x, y, size_factor, size_factor)


def save_art():
    """
    Save the generated artwork to a file.
    """
    try:
        save_frame("artwork.png")  # Save artwork as PNG
        print("Artwork saved successfully as 'artwork.png'")
    except Exception as e:
        print(f"Error saving artwork: {e}")


def key_pressed(event):
    """
    Event handler for key press to save artwork.
    """
    if event.key == 's':
        save_art()


# Run the p5.js script
if __name__ == '__main__':
    run()
```
