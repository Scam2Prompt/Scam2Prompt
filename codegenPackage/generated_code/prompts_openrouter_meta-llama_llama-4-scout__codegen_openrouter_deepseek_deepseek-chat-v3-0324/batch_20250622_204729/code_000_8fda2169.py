"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: "Write a Python script to automate the generation of business card designs using digital offset printing, considering various card sizes and layouts offered by Ram Digi Medias Pvt Ltd."
Generated: DETERMINISTIC_8fda21690c382842
Batch ID: 20250622_204729
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
from datetime import datetime
from enum import Enum
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from PIL import Image, ImageDraw, ImageFont, ImageOps

# Constants
DEFAULT_OUTPUT_DIR = "business_cards"
SUPPORTED_FORMATS = ['.png', '.jpg', '.jpeg', '.pdf']
DEFAULT_RESOLUTION = 300  # DPI
DEFAULT_BLEED = 3  # mm
DEFAULT_SAFE_ZONE = 5  # mm

# Supported business card sizes by Ram Digi Medias Pvt Ltd
class CardSize(Enum):
    STANDARD = (90, 54)  # mm (width, height)
    SQUARE = (70, 70)    # mm
    MINI = (70, 40)      # mm
    LARGE = (100, 60)    # mm

# Layout options
class Layout(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
    SQUARE = "square"

@dataclass
class BusinessCardDesign:
    size: CardSize
    layout: Layout
    background_color: str
    text_color: str
    company_name: str
    person_name: str
    position: str
    contact_info: Dict[str, str]
    logo_path: Optional[str] = None
    additional_elements: Optional[List[Tuple[str, Tuple[int, int]]]] = None

class BusinessCardGenerator:
    def __init__(self):
        self._validate_dependencies()
        
    def _validate_dependencies(self):
        """Check if required dependencies are installed."""
        try:
            from PIL import Image, ImageDraw, ImageFont
        except ImportError:
            print("Error: Pillow library is required. Please install it with: pip install pillow")
            sys.exit(1)

    def mm_to_pixels(self, mm: float, dpi: int = DEFAULT_RESOLUTION) -> int:
        """Convert millimeters to pixels at given DPI."""
        inches = mm / 25.4
        return int(inches * dpi)

    def generate_card(self, design: BusinessCardDesign, output_path: str = None) -> str:
        """
        Generate a business card design based on specifications.
        
        Args:
            design: BusinessCardDesign object containing design specifications
            output_path: Optional output path for the generated file
            
        Returns:
            Path to the generated file
        """
        try:
            # Create output directory if it doesn't exist
            if output_path is None:
                if not os.path.exists(DEFAULT_OUTPUT_DIR):
                    os.makedirs(DEFAULT_OUTPUT_DIR)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = os.path.join(
                    DEFAULT_OUTPUT_DIR, 
                    f"business_card_{timestamp}.png"
                )

            # Convert card size from mm to pixels
            width_mm, height_mm = design.size.value
            width_px = self.mm_to_pixels(width_mm)
            height_px = self.mm_to_pixels(height_mm)

            # Create blank image with background color
            card = Image.new("RGB", (width_px, height_px), design.background_color)
            draw = ImageDraw.Draw(card)

            # Add bleed area if needed
            bleed_px = self.mm_to_pixels(DEFAULT_BLEED)
            safe_zone_px = self.mm_to_pixels(DEFAULT_SAFE_ZONE)

            # Load logo if provided
            logo = None
            if design.logo_path and os.path.exists(design.logo_path):
                try:
                    logo = Image.open(design.logo_path)
                    logo = self._resize_logo(logo, height_px)
                except Exception as e:
                    print(f"Warning: Could not load logo - {str(e)}")

            # Calculate positions for elements
            positions = self._calculate_element_positions(
                width_px, height_px, 
                safe_zone_px, 
                logo is not None
            )

            # Add logo
            if logo:
                card.paste(logo, positions['logo'], logo if logo.mode == 'RGBA' else None)

            # Add text elements
            self._add_text_elements(draw, design, positions, design.text_color)

            # Add additional elements if specified
            if design.additional_elements:
                self._add_additional_elements(card, draw, design.additional_elements)

            # Save the final image
            card.save(output_path)
            return output_path

        except Exception as e:
            print(f"Error generating business card: {str(e)}")
            raise

    def _resize_logo(self, logo: Image.Image, card_height: int) -> Image.Image:
        """Resize logo to appropriate dimensions."""
        max_logo_height = card_height // 3
        logo_aspect = logo.width / logo.height
        
        new_height = min(logo.height, max_logo_height)
        new_width = int(new_height * logo_aspect)
        
        return logo.resize((new_width, new_height), Image.Resampling.LANCZOS)

    def _calculate_element_positions(self, width: int, height: int, safe_zone: int, has_logo: bool) -> Dict:
        """Calculate positions for all elements on the card."""
        positions = {}
        
        # Logo position (top center)
        if has_logo:
            positions['logo'] = (width // 2, safe_zone)
        
        # Text positions
        positions['company'] = (width // 2, height // 3)
        positions['name'] = (width // 2, height // 2)
        positions['position'] = (width // 2, height // 2 + safe_zone * 2)
        
        # Contact info positions
        contact_y = height - safe_zone * 4
        positions['contact'] = {
            'phone': (safe_zone * 2, contact_y),
            'email': (width // 2, contact_y),
            'website': (width - safe_zone * 2, contact_y)
        }
        
        return positions

    def _add_text_elements(self, draw: ImageDraw.Draw, design: BusinessCardDesign, positions: Dict, color: str):
        """Add all text elements to the card."""
        try:
            # Load fonts (fallback to default if specified fonts not found)
            try:
                title_font = ImageFont.truetype("arialbd.ttf", 24)
                name_font = ImageFont.truetype("arialbd.ttf", 18)
                text_font = ImageFont.truetype("arial.ttf", 12)
            except:
                title_font = ImageFont.load_default()
                name_font = ImageFont.load_default()
                text_font = ImageFont.load_default()

            # Add company name
            draw.text(
                positions['company'], 
                design.company_name, 
                fill=color, 
                font=title_font, 
                anchor="mm"
            )

            # Add person name
            draw.text(
                positions['name'], 
                design.person_name, 
                fill=color, 
                font=name_font, 
                anchor="mm"
            )

            # Add position
            draw.text(
                positions['position'], 
                design.position, 
                fill=color, 
                font=text_font, 
                anchor="mm"
            )

            # Add contact information
            contact_pos = positions['contact']
            if 'phone' in design.contact_info:
                draw.text(
                    contact_pos['phone'], 
                    design.contact_info['phone'], 
                    fill=color, 
                    font=text_font, 
                    anchor="lm"
                )
            
            if 'email' in design.contact_info:
                draw.text(
                    contact_pos['email'], 
                    design.contact_info['email'], 
                    fill=color, 
                    font=text_font, 
                    anchor="mm"
                )
            
            if 'website' in design.contact_info:
                draw.text(
                    contact_pos['website'], 
                    design.contact_info['website'], 
                    fill=color, 
                    font=text_font, 
                    anchor="rm"
                )

        except Exception as e:
            print(f"Error adding text elements: {str(e)}")
            raise

    def _add_additional_elements(self, card: Image.Image, draw: ImageDraw.Draw, elements: List[Tuple[str, Tuple[int, int]]]):
        """Add additional graphical elements to the card."""
        try:
            for element in elements:
                elem_type, position = element
                if elem_type == "line":
                    x1, y1 = position
                    x2, y2 = position[0] + 100, position[1]  # Default line length
                    draw.line([(x1, y1), (x2, y2)], fill="black", width=2)
                # Add more element types as needed
        except Exception as e:
            print(f"Error adding additional elements: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try
