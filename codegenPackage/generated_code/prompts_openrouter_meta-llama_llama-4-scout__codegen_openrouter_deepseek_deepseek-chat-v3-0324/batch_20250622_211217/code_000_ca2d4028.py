"""
Generated Code Metadata:
========================
Original URL: https://theog.io
Prompt: Write a Python script to generate OG images for Twitter using a customizable template, similar to Senja's offerings.
Generated: DETERMINISTIC_ca2d40287cb09286
Batch ID: 20250622_211217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import textwrap
from datetime import datetime
from typing import Optional, Tuple

from PIL import Image, ImageDraw, ImageFont, ImageOps

# Configuration Constants
DEFAULT_BG_COLOR = "#1DA1F2"  # Twitter blue
DEFAULT_TEXT_COLOR = "#FFFFFF"
DEFAULT_FONT_PATH = "arial.ttf"
DEFAULT_TITLE_FONT_SIZE = 60
DEFAULT_BODY_FONT_SIZE = 40
DEFAULT_AUTHOR_FONT_SIZE = 30
DEFAULT_IMAGE_SIZE = (1200, 630)  # Twitter recommended OG image size
DEFAULT_PADDING = 50
DEFAULT_LINE_SPACING = 10
MAX_TITLE_LINES = 3
MAX_BODY_LINES = 4
OUTPUT_DIR = "output"
TEMPLATE_DIR = "templates"

# Ensure directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(TEMPLATE_DIR, exist_ok=True)


class TwitterOGGenerator:
    def __init__(
        self,
        bg_color: str = DEFAULT_BG_COLOR,
        text_color: str = DEFAULT_TEXT_COLOR,
        font_path: str = DEFAULT_FONT_PATH,
        image_size: Tuple[int, int] = DEFAULT_IMAGE_SIZE,
    ):
        """
        Initialize the Twitter OG image generator.

        Args:
            bg_color: Background color in hex format
            text_color: Text color in hex format
            font_path: Path to the font file
            image_size: Tuple of (width, height) for the output image
        """
        self.bg_color = bg_color
        self.text_color = text_color
        self.font_path = font_path
        self.image_size = image_size

    def _get_font(self, size: int) -> ImageFont.FreeTypeFont:
        """Get a font object with the specified size."""
        try:
            return ImageFont.truetype(self.font_path, size)
        except IOError:
            # Fallback to default font if specified font is not found
            return ImageFont.load_default()

    def _wrap_text(
        self, text: str, font: ImageFont.FreeTypeFont, max_width: int, max_lines: int
    ) -> str:
        """Wrap text to fit within specified width and line count."""
        lines = textwrap.wrap(text, width=max_width // (font.size // 2))
        if len(lines) > max_lines:
            lines = lines[:max_lines]
            lines[-1] = lines[-1] + "..."
        return "\n".join(lines)

    def _draw_text(
        self,
        draw: ImageDraw.Draw,
        text: str,
        position: Tuple[int, int],
        font: ImageFont.FreeTypeFont,
        max_width: Optional[int] = None,
        max_lines: Optional[int] = None,
    ) -> None:
        """Draw text on the image with optional wrapping."""
        if max_width and max_lines:
            text = self._wrap_text(text, font, max_width, max_lines)
        draw.text(position, text, fill=self.text_color, font=font)

    def generate(
        self,
        title: str,
        body: Optional[str] = None,
        author: Optional[str] = None,
        logo_path: Optional[str] = None,
        template_path: Optional[str] = None,
    ) -> Image.Image:
        """
        Generate a Twitter OG image.

        Args:
            title: Main title text
            body: Optional body text
            author: Optional author attribution
            logo_path: Optional path to logo image
            template_path: Optional path to background template image

        Returns:
            Generated PIL Image object
        """
        # Create base image
        if template_path and os.path.exists(template_path):
            img = Image.open(template_path).convert("RGB")
            img = ImageOps.fit(img, self.image_size)
        else:
            img = Image.new("RGB", self.image_size, color=self.bg_color)

        draw = ImageDraw.Draw(img)
        padding = DEFAULT_PADDING
        current_y = padding

        # Add logo if provided
        if logo_path and os.path.exists(logo_path):
            try:
                logo = Image.open(logo_path)
                logo_width, logo_height = logo.size
                max_logo_height = self.image_size[1] // 5
                if logo_height > max_logo_height:
                    ratio = max_logo_height / logo_height
                    logo = logo.resize(
                        (int(logo_width * ratio), int(logo_height * ratio))
                    )
                img.paste(logo, (padding, padding), logo if logo.mode == "RGBA" else None)
                current_y += logo.size[1] + padding
            except IOError:
                pass  # Skip logo if there's an error loading it

        # Calculate available width for text
        text_width = self.image_size[0] - (2 * padding)

        # Add title
        title_font = self._get_font(DEFAULT_TITLE_FONT_SIZE)
        self._draw_text(
            draw,
            title,
            (padding, current_y),
            title_font,
            text_width,
            MAX_TITLE_LINES,
        )
        title_height = len(title.split("\n")) * (DEFAULT_TITLE_FONT_SIZE + DEFAULT_LINE_SPACING)
        current_y += title_height + padding

        # Add body if provided
        if body:
            body_font = self._get_font(DEFAULT_BODY_FONT_SIZE)
            self._draw_text(
                draw,
                body,
                (padding, current_y),
                body_font,
                text_width,
                MAX_BODY_LINES,
            )
            body_height = len(body.split("\n")) * (DEFAULT_BODY_FONT_SIZE + DEFAULT_LINE_SPACING)
            current_y += body_height + padding

        # Add author if provided
        if author:
            author_font = self._get_font(DEFAULT_AUTHOR_FONT_SIZE)
            author_text = f"— {author}"
            self._draw_text(
                draw,
                author_text,
                (padding, self.image_size[1] - padding - DEFAULT_AUTHOR_FONT_SIZE),
                author_font,
            )

        return img

    def save(
        self,
        image: Image.Image,
        filename: Optional[str] = None,
        format: str = "JPEG",
        quality: int = 90,
    ) -> str:
        """
        Save the generated image to a file.

        Args:
            image: PIL Image object to save
            filename: Optional filename (default: timestamp-based)
            format: Image format (JPEG, PNG, etc.)
            quality: Image quality (1-100)

        Returns:
            Path to the saved image
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"twitter_og_{timestamp}.{format.lower()}"
        output_path = os.path.join(OUTPUT_DIR, filename)
        image.save(output_path, format=format, quality=quality)
        return output_path


# Example usage
if __name__ == "__main__":
    try:
        generator = TwitterOGGenerator()
        image = generator.generate(
            title="Introducing Our New Product",
            body="This revolutionary product will change the way you work forever. Try it today!",
            author="Jane Doe",
        )
        saved_path = generator.save(image)
        print(f"Image saved to: {saved_path}")
    except Exception as e:
        print(f"Error generating image: {e}")
```
