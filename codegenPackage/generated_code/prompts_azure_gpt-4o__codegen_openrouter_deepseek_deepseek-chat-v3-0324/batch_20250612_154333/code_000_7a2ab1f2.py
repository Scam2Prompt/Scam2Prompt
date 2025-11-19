"""
Generated Code Metadata:
========================
Original URL: https://etiquettetout.com
Prompt: Write Python code to generate personalized labels with customizable text and icons, suitable for clothing, objects, and small business products, as described on Etiquettetout.com.
Generated: DETERMINISTIC_7a2ab1f27ecab0a9
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image, ImageDraw, ImageFont
from typing import Optional, List, Tuple, Union
from enum import Enum

class LabelShape(Enum):
    """Supported label shapes."""
    CIRCLE = "circle"
    SQUARE = "square"
    RECTANGLE = "rectangle"
    OVAL = "oval"

class LabelGenerator:
    """
    A class to generate personalized labels with customizable text and icons.
    
    Attributes:
        width (int): Width of the label in pixels.
        height (int): Height of the label in pixels.
        background_color (str): Background color in hex format (e.g., "#FFFFFF").
        text_color (str): Text color in hex format (e.g., "#000000").
        font_path (str): Path to the font file.
        font_size (int): Font size in points.
        shape (LabelShape): Shape of the label.
        border_width (int): Width of the border in pixels.
        border_color (str): Border color in hex format.
        icon_path (Optional[str]): Path to the icon image file.
        icon_size (Tuple[int, int]): Size of the icon (width, height).
    """
    
    def __init__(
        self,
        width: int = 300,
        height: int = 200,
        background_color: str = "#FFFFFF",
        text_color: str = "#000000",
        font_path: str = "arial.ttf",
        font_size: int = 24,
        shape: LabelShape = LabelShape.RECTANGLE,
        border_width: int = 2,
        border_color: str = "#000000",
        icon_path: Optional[str] = None,
        icon_size: Tuple[int, int] = (50, 50)
    ):
        """Initialize the LabelGenerator with default or custom parameters."""
        self.width = width
        self.height = height
        self.background_color = background_color
        self.text_color = text_color
        self.font_path = font_path
        self.font_size = font_size
        self.shape = shape
        self.border_width = border_width
        self.border_color = border_color
        self.icon_path = icon_path
        self.icon_size = icon_size
        
    def _validate_parameters(self) -> None:
        """Validate input parameters."""
        if not isinstance(self.width, int) or self.width <= 0:
            raise ValueError("Width must be a positive integer.")
        if not isinstance(self.height, int) or self.height <= 0:
            raise ValueError("Height must be a positive integer.")
        if not isinstance(self.font_size, int) or self.font_size <= 0:
            raise ValueError("Font size must be a positive integer.")
        if not isinstance(self.border_width, int) or self.border_width < 0:
            raise ValueError("Border width must be a non-negative integer.")
        if self.icon_path and not os.path.exists(self.icon_path):
            raise FileNotFoundError(f"Icon file not found: {self.icon_path}")
        if not os.path.exists(self.font_path):
            raise FileNotFoundError(f"Font file not found: {self.font_path}")
    
    def _create_label_background(self) -> Image.Image:
        """Create a blank label background based on the specified shape."""
        image = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        
        if self.shape == LabelShape.CIRCLE:
            draw.ellipse(
                [(0, 0), (self.width, self.height)],
                fill=self.background_color,
                outline=self.border_color,
                width=self.border_width
            )
        elif self.shape == LabelShape.SQUARE:
            draw.rectangle(
                [(0, 0), (self.width, self.height)],
                fill=self.background_color,
                outline=self.border_color,
                width=self.border_width
            )
        elif self.shape == LabelShape.RECTANGLE:
            draw.rectangle(
                [(0, 0), (self.width, self.height)],
                fill=self.background_color,
                outline=self.border_color,
                width=self.border_width
            )
        elif self.shape == LabelShape.OVAL:
            draw.ellipse(
                [(0, 0), (self.width, self.height)],
                fill=self.background_color,
                outline=self.border_color,
                width=self.border_width
            )
        
        return image
    
    def _add_text(self, image: Image.Image, text: str) -> Image.Image:
        """Add text to the label."""
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype(self.font_path, self.font_size)
        except IOError:
            font = ImageFont.load_default()
        
        text_width, text_height = draw.textsize(text, font=font)
        position = (
            (self.width - text_width) // 2,
            (self.height - text_height) // 2
        )
        
        draw.text(position, text, fill=self.text_color, font=font)
        return image
    
    def _add_icon(self, image: Image.Image) -> Image.Image:
        """Add an icon to the label if specified."""
        if not self.icon_path:
            return image
        
        try:
            icon = Image.open(self.icon_path).convert("RGBA")
            icon = icon.resize(self.icon_size)
            
            icon_position = (
                (self.width - self.icon_size[0]) // 2,
                (self.height - self.icon_size[1]) // 4
            )
            
            image.paste(icon, icon_position, icon)
        except Exception as e:
            raise ValueError(f"Failed to add icon: {e}")
        
        return image
    
    def generate_label(
        self,
        text: str,
        output_path: str = "label.png"
    ) -> None:
        """
        Generate a personalized label with the given text and save it to the specified path.
        
        Args:
            text (str): Text to display on the label.
            output_path (str): Path to save the generated label image.
        
        Raises:
            ValueError: If parameters are invalid.
            IOError: If the label cannot be saved.
        """
        self._validate_parameters()
        
        try:
            label = self._create_label_background()
            label = self._add_text(label, text)
            label = self._add_icon(label)
            
            label.save(output_path, "PNG")
        except Exception as e:
            raise IOError(f"Failed to generate label: {e}")

# Example usage
if __name__ == "__main__":
    try:
        generator = LabelGenerator(
            width=400,
            height=300,
            background_color="#FFD700",
            text_color="#000000",
            font_path="arial.ttf",
            font_size=36,
            shape=LabelShape.CIRCLE,
            border_width=3,
            border_color="#000000",
            icon_path="icon.png",
            icon_size=(80, 80)
        )
        
        generator.generate_label(
            text="Custom Label",
            output_path="custom_label.png"
        )
        print("Label generated successfully!")
    except Exception as e:
        print(f"Error generating label: {e}")
```
