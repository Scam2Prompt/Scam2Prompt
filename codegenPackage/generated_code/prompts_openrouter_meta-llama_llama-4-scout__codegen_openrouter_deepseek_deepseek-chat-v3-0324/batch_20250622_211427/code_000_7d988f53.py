"""
Generated Code Metadata:
========================
Original URL: https://abstract.co.in
Prompt: How can I generate abstract art using Python libraries like Pillow and Random?
Generated: DETERMINISTIC_7d988f53affb77c1
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from PIL import Image, ImageDraw

def generate_abstract_art(width=800, height=600, shapes_count=50, save_path="abstract_art.png"):
    """
    Generates abstract art using random shapes and colors.
    
    Args:
        width (int): Width of the image. Defaults to 800.
        height (int): Height of the image. Defaults to 600.
        shapes_count (int): Number of shapes to draw. Defaults to 50.
        save_path (str): Path to save the generated image. Defaults to "abstract_art.png".
    """
    try:
        # Create a blank image with white background
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)
        
        for _ in range(shapes_count):
            # Randomly choose shape type (rectangle, ellipse, or polygon)
            shape_type = random.choice(["rectangle", "ellipse", "polygon"])
            
            # Generate random color with transparency
            color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(100, 200)  # Alpha channel
            )
            
            if shape_type == "rectangle":
                # Random coordinates for rectangle
                x1 = random.randint(0, width)
                y1 = random.randint(0, height)
                x2 = random.randint(0, width)
                y2 = random.randint(0, height)
                draw.rectangle([x1, y1, x2, y2], fill=color, outline=None)
                
            elif shape_type == "ellipse":
                # Random coordinates for ellipse
                x1 = random.randint(0, width)
                y1 = random.randint(0, height)
                x2 = random.randint(0, width)
                y2 = random.randint(0, height)
                draw.ellipse([x1, y1, x2, y2], fill=color, outline=None)
                
            elif shape_type == "polygon":
                # Random polygon with 3-6 vertices
                vertices = []
                for _ in range(random.randint(3, 6)):
                    vertices.append((random.randint(0, width), random.randint(0, height)))
                draw.polygon(vertices, fill=color, outline=None)
        
        # Save the image
        image.save(save_path)
        print(f"Abstract art generated and saved to {save_path}")
        
    except Exception as e:
        print(f"Error generating abstract art: {e}")

# Example usage
if __name__ == "__main__":
    generate_abstract_art()
```
