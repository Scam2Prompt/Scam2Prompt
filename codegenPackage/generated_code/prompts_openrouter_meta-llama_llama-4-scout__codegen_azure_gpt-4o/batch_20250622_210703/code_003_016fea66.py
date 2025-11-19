"""
Generated Code Metadata:
========================
Original URL: https://www.houseofolsha.com
Prompt: Design a simple Batik Kedah pattern using Python and a library like Pillow, inspired by the House of Olsha's collections.
Generated: DETERMINISTIC_016fea66e323b320
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw

def create_batik_kedah_pattern(image_size=(800, 800), pattern_color="blue", background_color="white"):
    """
    Creates a simple Batik Kedah-inspired pattern using Pillow.

    Parameters:
        image_size (tuple): Size of the image (width, height).
        pattern_color (str): Color of the pattern.
        background_color (str): Background color of the image.

    Returns:
        Image: Generated Batik Kedah pattern.
    """
    # Create a blank image with the specified background color
    img = Image.new("RGB", image_size, background_color)
    draw = ImageDraw.Draw(img)

    # Define pattern parameters
    width, height = image_size
    num_shapes = 10  # Number of shapes in the pattern
    shape_size = min(width, height) // 10  # Size of each shape

    # Draw repeating diamond shapes
    for i in range(num_shapes):
        for j in range(num_shapes):
            # Calculate the center of each shape
            center_x = i * shape_size + shape_size // 2
            center_y = j * shape_size + shape_size // 2

            # Define the diamond shape points
            diamond = [
                (center_x, center_y - shape_size // 2),  # Top
                (center_x + shape_size // 2, center_y),  # Right
                (center_x, center_y + shape_size // 2),  # Bottom
                (center_x - shape_size // 2, center_y)   # Left
            ]

            # Alternate colors for a checkerboard effect
            if (i + j) % 2 == 0:
                draw.polygon(diamond, fill=pattern_color)
            else:
                draw.polygon(diamond, fill=background_color)

    # Add decorative circles to the pattern
    for i in range(num_shapes):
        for j in range(num_shapes):
            center_x = i * shape_size + shape_size // 2
            center_y = j * shape_size + shape_size // 2
            radius = shape_size // 4

            # Draw a circle at the center of each diamond
            draw.ellipse(
                [
                    (center_x - radius, center_y - radius),
                    (center_x + radius, center_y + radius)
                ],
                outline=pattern_color,
                width=2
            )

    return img


if __name__ == "__main__":
    # Generate the Batik Kedah pattern
    pattern_image = create_batik_kedah_pattern()

    # Save the image to a file
    pattern_image.save("batik_kedah_pattern.png")

    # Optionally, display the image
    pattern_image.show()
```
