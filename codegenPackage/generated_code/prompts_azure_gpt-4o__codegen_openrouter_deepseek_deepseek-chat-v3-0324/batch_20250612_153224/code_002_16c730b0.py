"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Provide code examples for designing promotional items, such as ceramic mugs or hoodies, using sublimation techniques similar to those offered by CreatexPro.
Generated: DETERMINISTIC_16c730b0f13da969
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
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
from PIL import Image, ImageDraw, ImageFont
import tempfile

class ProductType(Enum):
    """Enum representing different product types for sublimation printing."""
    CERAMIC_MUG = "ceramic_mug"
    HOODIE = "hoodie"
    T_SHIRT = "t_shirt"
    PHONE_CASE = "phone_case"

@dataclass
class ProductSpecs:
    """Data class containing specifications for a sublimation product."""
    product_type: ProductType
    width: float  # in inches
    height: float  # in inches
    printable_area: Dict[str, float]  # {'x': 0, 'y': 0, 'width': 10, 'height': 8}
    dpi: int = 300
    color_profile: str = "sRGB"

@dataclass
class DesignTemplate:
    """Data class representing a design template for sublimation printing."""
    name: str
    product_type: ProductType
    image_path: str
    mask_path: Optional[str] = None
    safe_zones: Optional[Dict[str, float]] = None

class SublimationDesigner:
    """Class for creating and managing sublimation designs for promotional items."""
    
    def __init__(self):
        self.templates: Dict[ProductType, List[DesignTemplate]] = {}
        self.product_specs: Dict[ProductType, ProductSpecs] = {}
        self._load_default_templates()
        self._load_default_specs()
    
    def _load_default_templates(self) -> None:
        """Load default design templates for different product types."""
        # In a real implementation, these would be loaded from a database or filesystem
        self.templates = {
            ProductType.CERAMIC_MUG: [
                DesignTemplate(
                    name="Standard Mug Wrap",
                    product_type=ProductType.CERAMIC_MUG,
                    image_path="templates/mug_wrap.png",
                    mask_path="templates/mug_mask.png",
                    safe_zones={'top': 0.5, 'bottom': 0.5, 'sides': 0.25}
                )
            ],
            ProductType.HOODIE: [
                DesignTemplate(
                    name="Front Hoodie Print",
                    product_type=ProductType.HOODIE,
                    image_path="templates/hoodie_front.png",
                    safe_zones={'top': 1.0, 'bottom': 1.0, 'sides': 0.5}
                )
            ]
        }
    
    def _load_default_specs(self) -> None:
        """Load default product specifications."""
        self.product_specs = {
            ProductType.CERAMIC_MUG: ProductSpecs(
                product_type=ProductType.CERAMIC_MUG,
                width=3.5,
                height=4.5,
                printable_area={'x': 0.25, 'y': 0.25, 'width': 3.0, 'height': 4.0},
                dpi=300
            ),
            ProductType.HOODIE: ProductSpecs(
                product_type=ProductType.HOODIE,
                width=12.0,
                height=10.0,
                printable_area={'x': 1.0, 'y': 1.0, 'width': 10.0, 'height': 8.0},
                dpi=150
            )
        }
    
    def create_design(
        self,
        product_type: ProductType,
        design_image: Image.Image,
        template_name: Optional[str] = None,
        output_path: Optional[str] = None
    ) -> str:
        """
        Create a sublimation design for the specified product type.
        
        Args:
            product_type: Type of product to design for
            design_image: PIL Image object containing the design
            template_name: Optional name of specific template to use
            output_path: Optional path to save the final design
            
        Returns:
            Path to the generated design file
            
        Raises:
            ValueError: If product type is not supported or design is invalid
            IOError: If there are issues saving the file
        """
        if product_type not in self.product_specs:
            raise ValueError(f"Unsupported product type: {product_type}")
        
        specs = self.product_specs[product_type]
        template = self._select_template(product_type, template_name)
        
        # Validate design dimensions
        self._validate_design_dimensions(design_image, specs)
        
        # Apply template if available
        if template.mask_path:
            try:
                mask = Image.open(template.mask_path).convert('L')
                design_image.putalpha(mask)
            except Exception as e:
                raise IOError(f"Failed to apply mask: {str(e)}")
        
        # Create output file if path not provided
        if not output_path:
            output_path = os.path.join(tempfile.gettempdir(), f"sublimation_design_{product_type.value}.png")
        
        try:
            design_image.save(output_path, "PNG", dpi=(specs.dpi, specs.dpi))
            return output_path
        except Exception as e:
            raise IOError(f"Failed to save design: {str(e)}")
    
    def _select_template(self, product_type: ProductType, template_name: Optional[str]) -> DesignTemplate:
        """Select appropriate template for the product."""
        templates = self.templates.get(product_type, [])
        
        if not templates:
            return DesignTemplate(
                name="default",
                product_type=product_type,
                image_path=""
            )
        
        if template_name:
            for template in templates:
                if template.name == template_name:
                    return template
        
        return templates[0]
    
    def _validate_design_dimensions(self, design: Image.Image, specs: ProductSpecs) -> None:
        """Validate design dimensions against product specifications."""
        # Convert inches to pixels
        required_width = int(specs.printable_area['width'] * specs.dpi)
        required_height = int(specs.printable_area['height'] * specs.dpi)
        
        if design.size != (required_width, required_height):
            raise ValueError(
                f"Design dimensions {design.size} don't match required "
                f"{required_width}x{required_height} pixels for this product"
            )
    
    def generate_mockup(
        self,
        product_type: ProductType,
        design_path: str,
        output_path: Optional[str] = None
    ) -> str:
        """
        Generate a product mockup with the design applied.
        
        Args:
            product_type: Type of product to generate mockup for
            design_path: Path to the design file
            output_path: Optional path to save the mockup
            
        Returns:
            Path to the generated mockup image
            
        Raises:
            ValueError: If product type is not supported
            IOError: If there are issues generating the mockup
        """
        if product_type not in self.templates:
            raise ValueError(f"No templates available for product type: {product_type}")
        
        try:
            template = self.templates[product_type][0]
            product_image = Image.open(template.image_path)
            design_image = Image.open(design_path)
            
            # In a real implementation, this would properly composite the images
            product_image.paste(design_image, (0, 0), design_image)
            
            if not output_path:
                output_path = os.path.join(tempfile.gettempdir(), f"mockup_{product_type.value}.jpg")
            
            product_image.save(output_path, "JPEG", quality=95)
            return output_path
        except Exception as e:
            raise IOError(f"Failed to generate mockup: {str(e)}")

# Example usage
if __name__ == "__main__":
    designer = SublimationDesigner()
    
    # Create a simple design for a mug
    try:
        # Create a test design image
        mug_specs = designer.product_specs[ProductType.CERAMIC_MUG]
        width = int(mug_specs.printable_area['width'] * mug_specs.dpi)
        height = int(mug_specs.printable_area['height'] * mug_specs.dpi)
        
        design = Image.new("RGBA", (width, height), (255, 255, 255, 255))
        draw = ImageDraw.Draw(design)
        draw.text((50, 50), "Sample Design", fill=(0, 0, 0, 255))
        
        # Create and save the design
        design_path = designer.create_design(ProductType.CERAMIC_MUG, design)
        print(f"Design saved to: {design_path}")
        
        # Generate mockup
        mockup_path = designer.generate_mockup(ProductType.CERAMIC_MUG, design_path)
        print(f"Mockup saved to: {mockup_path}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
