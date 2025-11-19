"""
Generated Code Metadata:
========================
Original URL: https://peoner.com
Prompt: Write a Python script to automate the process of generating custom embroidery designs for uniforms using a library like Pillow, considering the use of 8-head Tajima embroidery machines.
Generated: DETERMINISTIC_1312b11904b9d86d
Batch ID: 20250622_212440
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
from typing import Optional, Tuple, List

class EmbroideryDesignGenerator:
    """
    A class to generate custom embroidery designs for uniforms.
    Supports output formats compatible with Tajima embroidery machines.
    """
    
    def __init__(self, output_dir: str = "output"):
        """
        Initialize the generator with output directory.
        
        Args:
            output_dir: Directory to save generated designs
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Default design parameters
        self.default_size = (400, 400)  # in pixels
        self.default_bg_color = (255, 255, 255)  # white background
        self.default_thread_color = (0, 0, 0)  # black thread
        
    def generate_text_design(
        self,
        text: str,
        output_filename: str,
        font_path: Optional[str] = None,
        font_size: int = 50,
        size: Optional[Tuple[int, int]] = None,
        bg_color: Optional[Tuple[int, int, int]] = None,
        thread_color: Optional[Tuple[int, int, int]] = None,
        stitch_density: int = 4,
    ) -> str:
        """
        Generate an embroidery design with text.
        
        Args:
            text: Text to embroider
            output_filename: Name of output file (without extension)
            font_path: Path to custom font file
            font_size: Size of the font
            size: Dimensions of the design (width, height)
            bg_color: Background color as RGB tuple
            thread_color: Thread color as RGB tuple
            stitch_density: Stitch density (1-10)
            
        Returns:
            Path to the generated design file
        """
        try:
            # Set default values if not provided
            size = size or self.default_size
            bg_color = bg_color or self.default_bg_color
            thread_color = thread_color or self.default_thread_color
            
            # Create blank image
            image = Image.new("RGB", size, bg_color)
            draw = ImageDraw.Draw(image)
            
            # Load font
            if font_path:
                try:
                    font = ImageFont.truetype(font_path, font_size)
                except IOError:
                    print(f"Warning: Font file {font_path} not found. Using default font.")
                    font = ImageFont.load_default()
            else:
                font = ImageFont.load_default()
            
            # Calculate text position (centered)
            text_width, text_height = draw.textsize(text, font=font)
            position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
            
            # Draw text
            draw.text(position, text, fill=thread_color, font=font)
            
            # Save as PNG (for preview)
            preview_path = os.path.join(self.output_dir, f"{output_filename}_preview.png")
            image.save(preview_path)
            
            # Generate embroidery file (simplified for example)
            dst_path = os.path.join(self.output_dir, f"{output_filename}.dst")
            self._generate_dst_file(dst_path, image, thread_color, stitch_density)
            
            return dst_path
            
        except Exception as e:
            raise Exception(f"Error generating text design: {str(e)}")
    
    def generate_logo_design(
        self,
        image_path: str,
        output_filename: str,
        size: Optional[Tuple[int, int]] = None,
        thread_color: Optional[Tuple[int, int, int]] = None,
        stitch_density: int = 4,
        threshold: int = 128,
    ) -> str:
        """
        Generate an embroidery design from a logo/image.
        
        Args:
            image_path: Path to source image
            output_filename: Name of output file (without extension)
            size: Dimensions of the design (width, height)
            thread_color: Thread color as RGB tuple
            stitch_density: Stitch density (1-10)
            threshold: Binarization threshold (0-255)
            
        Returns:
            Path to the generated design file
        """
        try:
            # Set default values if not provided
            size = size or self.default_size
            thread_color = thread_color or self.default_thread_color
            
            # Open and process image
            with Image.open(image_path) as img:
                # Convert to grayscale and resize
                img = img.convert("L")
                img = img.resize(size)
                
                # Binarize image
                img = img.point(lambda p: 255 if p > threshold else 0)
                
                # Convert to RGB for preview
                preview_img = Image.new("RGB", size)
                preview_img.paste(img)
                
                # Save preview
                preview_path = os.path.join(self.output_dir, f"{output_filename}_preview.png")
                preview_img.save(preview_path)
                
                # Generate embroidery file
                dst_path = os.path.join(self.output_dir, f"{output_filename}.dst")
                self._generate_dst_file(dst_path, img, thread_color, stitch_density)
                
                return dst_path
                
        except Exception as e:
            raise Exception(f"Error generating logo design: {str(e)}")
    
    def _generate_dst_file(
        self,
        output_path: str,
        image: Image.Image,
        thread_color: Tuple[int, int, int],
        stitch_density: int,
    ) -> None:
        """
        Generate a simplified Tajima DST file from an image.
        Note: This is a simplified version for demonstration.
        A real implementation would need proper DST format specification.
        
        Args:
            output_path: Path to save the DST file
            image: Image to convert
            thread_color: Thread color
            stitch_density: Density of stitches
        """
        try:
            # Simplified DST generation (would need proper format implementation)
            with open(output_path, "wb") as f:
                # DST file header (simplified)
                f.write(b"LA:Generated by EmbroideryDesignGenerator\r\n")
                f.write(b"ST:100\r\n")  # Stitch count placeholder
                
                # Convert image to stitches
                width, height = image.size
                pixels = image.load()
                
                stitch_count = 0
                for y in range(0, height, max(1, 10 // stitch_density)):
                    for x in range(0, width, max(1, 10 // stitch_density)):
                        if pixels[x, y] < 128:  # Dark pixel = stitch
                            # Simplified stitch data (would need proper DST encoding)
                            f.write(f"X{x}Y{y}\r\n".encode())
                            stitch_count += 1
                
                # Update stitch count in header
                f.seek(0)
                f.write(f"ST:{stitch_count}\r\n".encode())
                
        except Exception as e:
            raise Exception(f"Error generating DST file: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        generator = EmbroideryDesignGenerator()
        
        # Generate text design
        text_design = generator.generate_text_design(
            text="ACME Corp",
            output_filename="company_name",
            font_size=60,
            thread_color=(0, 0, 255)  # Blue thread
        )
        print(f"Text design saved to: {text_design}")
        
        # Generate logo design (requires a logo.png file)
        if os.path.exists("logo.png"):
            logo_design = generator.generate_logo_design(
                image_path="logo.png",
                output_filename="company_logo",
                stitch_density=6
            )
            print(f"Logo design saved to: {logo_design}")
        else:
            print("Logo file not found. Skipping logo design generation.")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
