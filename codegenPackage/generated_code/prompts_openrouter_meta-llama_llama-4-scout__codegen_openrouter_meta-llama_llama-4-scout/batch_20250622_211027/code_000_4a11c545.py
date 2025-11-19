"""
Generated Code Metadata:
========================
Original URL: https://stethevent.org
Prompt: "Generate a Python script for creating looping animations inspired by Instructables projects."
Generated: DETERMINISTIC_4a11c5453f6744f4
Batch ID: 20250622_211027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import argparse
from PIL import Image, ImageDraw, ImageFont

def create_looping_animation(image_paths, output_filename, fps=24, loop_count=0):
    """
    Create a looping animation from a list of image paths.

    Args:
        image_paths (list): List of paths to images for the animation.
        output_filename (str): Filename for the output animation.
        fps (int, optional): Frames per second for the animation. Defaults to 24.
        loop_count (int, optional): Number of times to loop the animation. 
            0 means loop indefinitely. Defaults to 0.
    """

    # Open images and validate they can be opened
    try:
        images = [Image.open(path) for path in image_paths]
    except Exception as e:
        print(f"Error opening images: {e}")
        return

    # Ensure all images are the same size
    image_sizes = [img.size for img in images]
    if len(set(image_sizes)) > 1:
        print("Error: All images must be the same size.")
        return

    # Save the animation as a GIF
    try:
        images[0].save(
            output_filename,
            save_all=True,
            append_images=images[1:],
            optimize=True,
            duration=int(1000 / fps),  # Convert seconds to milliseconds
            loop=loop_count
        )
    except Exception as e:
        print(f"Error saving animation: {e}")

def main():
    parser = argparse.ArgumentParser(description="Create looping animations.")
    parser.add_argument("-i", "--images", nargs="+", required=True, help="List of image paths.")
    parser.add_argument("-o", "--output", required=True, help="Output filename.")
    parser.add_argument("-f", "--fps", type=int, default=24, help="Frames per second.")
    parser.add_argument("-l", "--loop", type=int, default=0, help="Loop count.")

    args = parser.parse_args()

    create_looping_animation(args.images, args.output, args.fps, args.loop)

if __name__ == "__main__":
    main()
```
