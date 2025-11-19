"""
Generated Code Metadata:
========================
Original URL: https://thumbsmaker.com
Prompt: Write a Python script to automate the process of creating custom YouTube thumbnails using the ThumbsMaker design strategy, including a consultation and concept phase.
Generated: DETERMINISTIC_9dcb25ae238241b6
Batch ID: 20250622_210655
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
from PIL import Image, ImageDraw, ImageFont
import textwrap
import argparse
from typing import Tuple, Optional

class ThumbnailGenerator:
    """
    A class to generate custom YouTube thumbnails following the ThumbsMaker design strategy.
    Handles image composition, text overlay, and styling.
    """
    
    def __init__(self, output_dir: str = "output"):
        """
        Initialize the ThumbnailGenerator with default settings.
        
        Args:
            output_dir (str): Directory to save generated thumbnails. Defaults to "output".
        """
        self.output_dir = output_dir
        self.default_font = "arial.ttf"
        self.default_bg_color = (30, 30, 30)
        self.default_text_color = (255, 255, 255)
        self.default_accent_color = (255, 0, 0)
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
    
    def create_thumbnail(
        self,
        title: str,
        output_filename: str,
        bg_image_path: Optional[str] = None,
        width: int = 1280,
        height: int = 720,
        font_size: int = 60,
        accent_font_size: int = 80,
        max_title_width: int = 25
    ) -> str:
        """
        Create a YouTube thumbnail with the given title and optional background image.
        
        Args:
            title (str): The title text to display on the thumbnail
            output_filename (str): Name for the output file (without extension)
            bg_image_path (Optional[str]): Path to background image. If None, uses solid color.
            width (int): Width of thumbnail in pixels. Default 1280 (YouTube recommended).
            height (int): Height of thumbnail in pixels. Default 720 (YouTube recommended).
            font_size (int): Font size for main text. Default 60.
            accent_font_size (int): Font size for emphasized words. Default 80.
            max_title_width (int): Maximum characters per line before wrapping. Default 25.
            
        Returns:
            str: Path to the generated thumbnail file
            
        Raises:
            ValueError: If title is empty or output filename is invalid
            FileNotFoundError: If background image path is provided but doesn't exist
            OSError: If there's an issue saving the image
        """
        if not title:
            raise ValueError("Title cannot be empty")
        if not output_filename:
            raise ValueError("Output filename cannot be empty")
        
        # Create blank image with background color
        if bg_image_path:
            if not os.path.exists(bg_image_path):
                raise FileNotFoundError(f"Background image not found: {bg_image_path}")
            image = Image.open(bg_image_path).convert("RGBA")
            image = image.resize((width, height))
        else:
            image = Image.new("RGBA", (width, height), self.default_bg_color)
        
        draw = ImageDraw.Draw(image)
        
        # Process title to identify emphasized words (surrounded by *)
        processed_title, emphasized_words = self._process_title(title)
        
        # Wrap text to fit thumbnail
        wrapped_text = textwrap.fill(processed_title, width=max_title_width)
        
        # Calculate text position (centered)
        font = ImageFont.truetype(self.default_font, font_size)
        accent_font = ImageFont.truetype(self.default_font, accent_font_size)
        text_width, text_height = self._get_multiline_text_size(wrapped_text, font)
        x = (width - text_width) // 2
        y = (height - text_height) // 2
        
        # Draw each line of text
        current_y = y
        for line in wrapped_text.split('\n'):
            line_width = self._get_text_width(line, font)
            line_x = (width - line_width) // 2
            
            # Split line into words and draw each word separately
            words = line.split()
            current_x = line_x
            
            for word in words:
                if word in emphasized_words:
                    word_font = accent_font
                    word_color = self.default_accent_color
                else:
                    word_font = font
                    word_color = self.default_text_color
                
                # Draw the word
                draw.text((current_x, current_y), word, fill=word_color, font=word_font)
                
                # Update x position for next word
                current_x += self._get_text_width(word + " ", word_font)
            
            current_y += text_height // len(wrapped_text.split('\n'))
        
        # Add branding or logo if needed
        # self._add_branding(image)
        
        # Save the image
        output_path = os.path.join(self.output_dir, f"{output_filename}.png")
        try:
            image.save(output_path, "PNG")
        except OSError as e:
            raise OSError(f"Failed to save thumbnail: {e}")
        
        return output_path
    
    def _process_title(self, title: str) -> Tuple[str, list]:
        """
        Process the title to identify emphasized words (surrounded by *) and clean the title.
        
        Args:
            title (str): The original title text
            
        Returns:
            Tuple[str, list]: (processed_title, emphasized_words)
        """
        emphasized_words = []
        words = title.split()
        processed_words = []
        
        for word in words:
            if word.startswith('*') and word.endswith('*'):
                emphasized_word = word[1:-1]
                emphasized_words.append(emphasized_word)
                processed_words.append(emphasized_word)
            else:
                processed_words.append(word)
        
        return ' '.join(processed_words), emphasized_words
    
    def _get_text_width(self, text: str, font: ImageFont.FreeTypeFont) -> int:
        """
        Get the width of text in pixels using the given font.
        
        Args:
            text (str): Text to measure
            font (ImageFont.FreeTypeFont): Font to use
            
        Returns:
            int: Width of the text in pixels
        """
        return font.getlength(text)
    
    def _get_multiline_text_size(self, text: str, font: ImageFont.FreeTypeFont) -> Tuple[int, int]:
        """
        Get the size of multiline text in pixels.
        
        Args:
            text (str): Multiline text to measure
            font (ImageFont.FreeTypeFont): Font to use
            
        Returns:
            Tuple[int, int]: (width, height) of the text in pixels
        """
        lines = text.split('\n')
        max_width = max(self._get_text_width(line, font) for line in lines)
        total_height = len(lines) * font.size
        return (max_width, total_height)

def main():
    """
    Command-line interface for the Thumbnail Generator.
    """
    parser = argparse.ArgumentParser(description="YouTube Thumbnail Generator")
    parser.add_argument("title", help="Title text for the thumbnail (use *word* to emphasize)")
    parser.add_argument("output_filename", help="Output filename (without extension)")
    parser.add_argument("-b", "--background", help="Path to background image")
    parser.add_argument("-w", "--width", type=int, default=1280, help="Thumbnail width")
    parser.add_argument("-H", "--height", type=int, default=720, help="Thumbnail height")
    parser.add_argument("--font_size", type=int, default=60, help="Main font size")
    parser.add_argument("--accent_size", type=int, default=80, help="Emphasized word font size")
    parser.add_argument("--max_width", type=int, default=25, help="Max characters per line")
    
    args = parser.parse_args()
    
    try:
        generator = ThumbnailGenerator()
        output_path = generator.create_thumbnail(
            title=args.title,
            output_filename=args.output_filename,
            bg_image_path=args.background,
            width=args.width,
            height=args.height,
            font_size=args.font_size,
            accent_font_size=args.accent_size,
            max_title_width=args.max_width
        )
        print(f"Thumbnail successfully created: {output_path}")
    except Exception as e:
        print(f"Error creating thumbnail: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
