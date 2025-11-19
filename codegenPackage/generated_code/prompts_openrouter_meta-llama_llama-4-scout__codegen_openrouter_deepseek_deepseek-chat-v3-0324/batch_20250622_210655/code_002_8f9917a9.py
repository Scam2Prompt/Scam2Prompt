"""
Generated Code Metadata:
========================
Original URL: https://blackhillsports.com
Prompt: "Generate code to automate the process of creating custom sublimation designs for activewear and uniforms using a library like Pillow or OpenCV."
Generated: DETERMINISTIC_8f9917a9f9114491
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
from PIL import Image, ImageDraw, ImageFont
from typing import Optional, Tuple, List, Dict
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SublimationDesignGenerator:
    """
    A class to generate custom sublimation designs for activewear and uniforms.
    """
    
    def __init__(self, output_dir: str = "output_designs"):
        """
        Initialize the design generator.
        
        Args:
            output_dir (str): Directory to save generated designs
        """
        self.output_dir = output_dir
        self._create_output_dir()
        
    def _create_output_dir(self) -> None:
        """Create output directory if it doesn't exist."""
        try:
            os.makedirs(self.output_dir, exist_ok=True)
        except OSError as e:
            logger.error(f"Error creating output directory: {e}")
            raise
            
    def _validate_image(self, image_path: str) -> bool:
        """Validate that the image exists and is readable."""
        if not os.path.exists(image_path):
            logger.error(f"Image file not found: {image_path}")
            return False
        try:
            with Image.open(image_path) as img:
                img.verify()
            return True
        except Exception as e:
            logger.error(f"Invalid image file: {image_path}. Error: {e}")
            return False
    
    def _get_timestamp(self) -> str:
        """Generate a timestamp for unique filenames."""
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def create_design(
        self,
        base_image_path: str,
        logo_path: Optional[str] = None,
        text: Optional[str] = None,
        text_position: Tuple[int, int] = (100, 100),
        text_color: Tuple[int, int, int] = (0, 0, 0),
        text_font: str = "arial.ttf",
        text_size: int = 40,
        logo_position: Tuple[int, int] = (50, 50),
        logo_size: Tuple[int, int] = (200, 200),
        output_format: str = "PNG"
    ) -> str:
        """
        Create a custom sublimation design by combining base image with logo and text.
        
        Args:
            base_image_path: Path to the base image
            logo_path: Path to logo image (optional)
            text: Text to add to design (optional)
            text_position: (x,y) position of text
            text_color: RGB color of text
            text_font: Font file path
            text_size: Font size in points
            logo_position: (x,y) position of logo
            logo_size: (width, height) of logo
            output_format: Output image format (PNG, JPEG, etc.)
            
        Returns:
            Path to the generated design file
        """
        try:
            # Validate base image
            if not self._validate_image(base_image_path):
                raise ValueError("Invalid base image")
                
            # Open base image
            base_image = Image.open(base_image_path).convert("RGBA")
            
            # Create a blank canvas with the same size as base image
            design = Image.new("RGBA", base_image.size)
            design.paste(base_image, (0, 0))
            
            # Add logo if provided
            if logo_path:
                if not self._validate_image(logo_path):
                    raise ValueError("Invalid logo image")
                    
                logo = Image.open(logo_path).convert("RGBA")
                logo = logo.resize(logo_size)
                design.paste(logo, logo_position, logo)
            
            # Add text if provided
            if text:
                try:
                    font = ImageFont.truetype(text_font, text_size)
                except IOError:
                    font = ImageFont.load_default()
                    logger.warning(f"Font {text_font} not found. Using default font.")
                
                draw = ImageDraw.Draw(design)
                draw.text(text_position, text, fill=text_color, font=font)
            
            # Generate output filename
            timestamp = self._get_timestamp()
            output_filename = f"design_{timestamp}.{output_format.lower()}"
            output_path = os.path.join(self.output_dir, output_filename)
            
            # Save the design
            design.save(output_path, format=output_format)
            logger.info(f"Design saved to: {output_path}")
            
            return output_path
            
        except Exception as e:
            logger.error(f"Error creating design: {e}")
            raise
            
    def batch_create_designs(
        self,
        base_image_paths: List[str],
        design_configs: List[Dict],
        output_format: str = "PNG"
    ) -> List[str]:
        """
        Create multiple designs in batch.
        
        Args:
            base_image_paths: List of base image paths
            design_configs: List of configuration dictionaries
            output_format: Output image format
            
        Returns:
            List of paths to generated designs
        """
        if len(base_image_paths) != len(design_configs):
            raise ValueError("Number of base images must match number of configs")
            
        output_paths = []
        for img_path, config in zip(base_image_paths, design_configs):
            try:
                output_path = self.create_design(
                    base_image_path=img_path,
                    logo_path=config.get("logo_path"),
                    text=config.get("text"),
                    text_position=config.get("text_position", (100, 100)),
                    text_color=config.get("text_color", (0, 0, 0)),
                    text_font=config.get("text_font", "arial.ttf"),
                    text_size=config.get("text_size", 40),
                    logo_position=config.get("logo_position", (50, 50)),
                    logo_size=config.get("logo_size", (200, 200)),
                    output_format=output_format
                )
                output_paths.append(output_path)
            except Exception as e:
                logger.error(f"Error processing {img_path}: {e}")
                continue
                
        return output_paths


# Example usage
if __name__ == "__main__":
    try:
        generator = SublimationDesignGenerator()
        
        # Single design example
        design_path = generator.create_design(
            base_image_path="base.jpg",
            logo_path="logo.png",
            text="Team Name",
            text_position=(200, 200),
            text_color=(255, 255, 255),
            text_size=60
        )
        print(f"Generated design: {design_path}")
        
        # Batch design example
        base_images = ["base1.jpg", "base2.jpg"]
        configs = [
            {"text": "Team A", "text_color": (255, 0, 0)},
            {"text": "Team B", "text_color": (0, 0, 255), "logo_path": "logo.png"}
        ]
        output_paths = generator.batch_create_designs(base_images, configs)
        print(f"Batch generated designs: {output_paths}")
        
    except Exception as e:
        logger.error(f"Application error: {e}")
```
