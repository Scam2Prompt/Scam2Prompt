"""
Generated Code Metadata:
========================
Original URL: https://metaforce360.com
Prompt: Create a Python script to automate the generation of tailored illustrations for branding purposes, similar to the services described by Meta Force 360.
Generated: DETERMINISTIC_72bcee89642d10cf
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import random
from PIL import Image, ImageDraw, ImageFont
from typing import List, Dict, Optional, Tuple

class BrandIllustrationGenerator:
    """
    A class to generate tailored illustrations for branding purposes.
    Supports custom text, colors, shapes, and logos.
    """

    def __init__(self, output_dir: str = "output"):
        """
        Initialize the illustration generator with output directory.
        
        Args:
            output_dir (str): Directory to save generated illustrations
        """
        self.output_dir = output_dir
        self._validate_output_dir()

    def _validate_output_dir(self) -> None:
        """Create output directory if it doesn't exist."""
        try:
            os.makedirs(self.output_dir, exist_ok=True)
        except OSError as e:
            raise RuntimeError(f"Failed to create output directory: {e}")

    def generate_illustration(
        self,
        width: int = 1200,
        height: int = 800,
        background_color: str = "#FFFFFF",
        text: Optional[str] = None,
        text_color: str = "#000000",
        font_path: Optional[str] = None,
        font_size: int = 40,
        shapes: Optional[List[Dict]] = None,
        logo_path: Optional[str] = None,
        output_filename: str = "brand_illustration.png"
    ) -> str:
        """
        Generate a branded illustration with customizable elements.
        
        Args:
            width: Width of the illustration in pixels
            height: Height of the illustration in pixels
            background_color: Background color in hex format
            text: Text to display on the illustration
            text_color: Text color in hex format
            font_path: Path to custom font file
            font_size: Size of the text
            shapes: List of shape dictionaries to draw
            logo_path: Path to logo image to overlay
            output_filename: Name of the output file
            
        Returns:
            Path to the generated illustration file
        """
        try:
            # Create blank canvas
            image = Image.new("RGB", (width, height), background_color)
            draw = ImageDraw.Draw(image)

            # Add shapes if specified
            if shapes:
                self._draw_shapes(draw, shapes)

            # Add text if specified
            if text:
                self._add_text(draw, text, text_color, font_path, font_size, width, height)

            # Add logo if specified
            if logo_path:
                self._add_logo(image, logo_path)

            # Save the final image
            output_path = os.path.join(self.output_dir, output_filename)
            image.save(output_path)
            return output_path

        except Exception as e:
            raise RuntimeError(f"Failed to generate illustration: {e}")

    def _draw_shapes(self, draw: ImageDraw.Draw, shapes: List[Dict]) -> None:
        """Draw shapes on the image based on shape specifications."""
        for shape in shapes:
            try:
                shape_type = shape.get("type", "rectangle")
                color = shape.get("color", "#000000")
                position = shape.get("position", (0, 0))
                size = shape.get("size", (100, 100))

                if shape_type == "rectangle":
                    draw.rectangle(
                        [position, (position[0] + size[0], position[1] + size[1])],
                        fill=color
                    )
                elif shape_type == "ellipse":
                    draw.ellipse(
                        [position, (position[0] + size[0], position[1] + size[1])],
                        fill=color
                    )
                elif shape_type == "polygon":
                    points = shape.get("points", [])
                    if len(points) >= 3:
                        draw.polygon(points, fill=color)

            except Exception as e:
                print(f"Warning: Failed to draw shape {shape}. Error: {e}")

    def _add_text(
        self,
        draw: ImageDraw.Draw,
        text: str,
        text_color: str,
        font_path: Optional[str],
        font_size: int,
        canvas_width: int,
        canvas_height: int
    ) -> None:
        """Add text to the illustration with optional custom font."""
        try:
            # Load font
            if font_path and os.path.exists(font_path):
                font = ImageFont.truetype(font_path, font_size)
            else:
                font = ImageFont.load_default()

            # Calculate text position (centered by default)
            text_width, text_height = draw.textsize(text, font=font)
            x = (canvas_width - text_width) // 2
            y = (canvas_height - text_height) // 2

            # Draw text
            draw.text((x, y), text, fill=text_color, font=font)

        except Exception as e:
            print(f"Warning: Failed to add text. Error: {e}")

    def _add_logo(self, image: Image.Image, logo_path: str) -> None:
        """Overlay a logo on the illustration."""
        try:
            if not os.path.exists(logo_path):
                raise FileNotFoundError(f"Logo file not found: {logo_path}")

            logo = Image.open(logo_path)
            logo_width, logo_height = logo.size
            canvas_width, canvas_height = image.size

            # Position logo at bottom right with some padding
            position = (
                canvas_width - logo_width - 20,
                canvas_height - logo_height - 20
            )

            # Paste logo onto the image
            image.paste(logo, position, logo if logo.mode == 'RGBA' else None)

        except Exception as e:
            print(f"Warning: Failed to add logo. Error: {e}")

    @staticmethod
    def generate_random_illustration(output_dir: str = "output") -> str:
        """Generate a random illustration with sample parameters."""
        generator = BrandIllustrationGenerator(output_dir)
        
        # Random parameters
        colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33F3"]
        shapes = [
            {
                "type": random.choice(["rectangle", "ellipse", "polygon"]),
                "color": random.choice(colors),
                "position": (random.randint(0, 800), random.randint(0, 600)),
                "size": (random.randint(50, 200), random.randint(50, 200))
            } for _ in range(random.randint(1, 5))
        ]
        
        return generator.generate_illustration(
            text="Sample Brand",
            text_color=random.choice(colors),
            shapes=shapes,
            background_color="#F5F5F5",
            output_filename="random_brand.png"
        )


if __name__ == "__main__":
    # Example usage
    try:
        generator = BrandIllustrationGenerator()
        
        # Generate a custom illustration
        output_path = generator.generate_illustration(
            text="My Awesome Brand",
            text_color="#2C3E50",
            background_color="#ECF0F1",
            shapes=[
                {
                    "type": "rectangle",
                    "color": "#3498DB",
                    "position": (100, 100),
                    "size": (300, 200)
                },
                {
                    "type": "ellipse",
                    "color": "#E74C3C",
                    "position": (600, 200),
                    "size": (150, 150)
                }
            ],
            output_filename="custom_brand.png"
        )
        
        print(f"Generated illustration saved to: {output_path}")
        
        # Generate a random illustration
        random_output = BrandIllustrationGenerator.generate_random_illustration()
        print(f"Random illustration saved to: {random_output}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
```
