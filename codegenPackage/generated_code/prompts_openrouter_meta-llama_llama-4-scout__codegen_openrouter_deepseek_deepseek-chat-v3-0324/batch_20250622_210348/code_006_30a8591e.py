"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: "Create a customized label design for a product with specific branding requirements, including a unique shape and printing effects."
Generated: DETERMINISTIC_30a8591e456279fa
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import svgwrite
from svgwrite import cm, mm
from typing import Tuple, Optional

class LabelDesigner:
    """
    A class to create customized label designs with branding requirements.
    Supports unique shapes, printing effects, and branding elements.
    """
    
    def __init__(self, size: Tuple[float, float], brand_name: str, brand_color: str):
        """
        Initialize the label designer with basic parameters.
        
        Args:
            size: Tuple of (width, height) in millimeters
            brand_name: Name of the brand to display on label
            brand_color: Primary brand color in hex format (e.g., '#FF0000')
        """
        self.width, self.height = size
        self.brand_name = brand_name
        self.brand_color = brand_color
        self.dwg = None
        
    def create_canvas(self, filename: str) -> None:
        """Create a new SVG canvas for the label design."""
        self.dwg = svgwrite.Drawing(filename=filename, size=(f"{self.width}mm", f"{self.height}mm"))
        self.dwg.viewbox(0, 0, self.width, self.height)
        
    def add_unique_shape(self, shape_type: str, **kwargs) -> None:
        """
        Add a unique shape to the label design.
        
        Args:
            shape_type: Type of shape ('rounded_rect', 'circle', 'custom')
            kwargs: Shape-specific parameters
        """
        if not self.dwg:
            raise ValueError("Canvas not initialized. Call create_canvas() first.")
            
        if shape_type == 'rounded_rect':
            rx = kwargs.get('rx', 5)  # x-radius of corners
            ry = kwargs.get('ry', 5)  # y-radius of corners
            self.dwg.add(self.dwg.rect(
                insert=(2*mm, 2*mm),
                size=((self.width-4)*mm, (self.height-4)*mm),
                rx=rx*mm, ry=ry*mm,
                fill='white',
                stroke=self.brand_color,
                stroke_width=0.5*mm
            ))
        elif shape_type == 'circle':
            radius = min(self.width, self.height)/2 - 2  # mm
            self.dwg.add(self.dwg.circle(
                center=(self.width/2*mm, self.height/2*mm),
                r=radius*mm,
                fill='white',
                stroke=self.brand_color,
                stroke_width=0.5*mm
            ))
        elif shape_type == 'custom':
            points = kwargs.get('points', [])
            if not points:
                raise ValueError("Custom shape requires 'points' parameter")
            self.dwg.add(self.dwg.polygon(
                points=points,
                fill='white',
                stroke=self.brand_color,
                stroke_width=0.5*mm
            ))
        else:
            raise ValueError(f"Unsupported shape type: {shape_type}")
    
    def add_branding(self, logo_path: Optional[str] = None) -> None:
        """
        Add branding elements to the label.
        
        Args:
            logo_path: Optional path to logo image file
        """
        if not self.dwg:
            raise ValueError("Canvas not initialized. Call create_canvas() first.")
            
        # Add brand name
        self.dwg.add(self.dwg.text(
            self.brand_name,
            insert=(self.width/2*mm, 10*mm),
            font_family="Arial",
            font_size=8*mm,
            fill=self.brand_color,
            text_anchor="middle"
        ))
        
        # Add logo if provided
        if logo_path:
            try:
                logo = self.dwg.image(
                    href=logo_path,
                    insert=(self.width/2*mm - 5*mm, 15*mm),
                    size=(10*mm, 10*mm)
                )
                self.dwg.add(logo)
            except Exception as e:
                print(f"Warning: Could not add logo - {str(e)}")
    
    def add_print_effect(self, effect_type: str) -> None:
        """
        Add printing effects to the label.
        
        Args:
            effect_type: Type of effect ('foil', 'emboss', 'deboss')
        """
        if not self.dwg:
            raise ValueError("Canvas not initialized. Call create_canvas() first.")
            
        if effect_type == 'foil':
            # Simulate foil effect with gradient
            gradient = self.dwg.linearGradient((0, 0), (1, 1))
            gradient.add_stop_color(0, 'gold')
            gradient.add_stop_color(1, 'white')
            self.dwg.add(self.dwg.circle(
                center=(self.width/2*mm, self.height/2*mm),
                r=5*mm,
                fill=gradient,
                opacity=0.3
            ))
        elif effect_type in ('emboss', 'deboss'):
            # Simulate 3D effect with shadows
            offset = 0.2*mm if effect_type == 'emboss' else -0.2*mm
            self.dwg.add(self.dwg.text(
                "PREMIUM",
                insert=(self.width/2*mm + offset, self.height - 5*mm + offset),
                font_family="Arial",
                font_size=3*mm,
                fill="rgba(0,0,0,0.3)",
                text_anchor="middle"
            ))
            self.dwg.add(self.dwg.text(
                "PREMIUM",
                insert=(self.width/2*mm, self.height - 5*mm),
                font_family="Arial",
                font_size=3*mm,
                fill=self.brand_color,
                text_anchor="middle"
            ))
        else:
            raise ValueError(f"Unsupported effect type: {effect_type}")
    
    def add_product_info(self, product_name: str, barcode: Optional[str] = None) -> None:
        """
        Add product information to the label.
        
        Args:
            product_name: Name of the product
            barcode: Optional barcode data
        """
        if not self.dwg:
            raise ValueError("Canvas not initialized. Call create_canvas() first.")
            
        # Add product name
        self.dwg.add(self.dwg.text(
            product_name,
            insert=(self.width/2*mm, 25*mm),
            font_family="Arial",
            font_size=5*mm,
            fill="black",
            text_anchor="middle"
        ))
        
        # Add barcode if provided
        if barcode:
            self.dwg.add(self.dwg.text(
                f"Barcode: {barcode}",
                insert=(self.width/2*mm, self.height - 2*mm),
                font_family="Arial",
                font_size=2*mm,
                fill="black",
                text_anchor="middle"
            ))
    
    def save_design(self) -> None:
        """Save the label design to file."""
        if not self.dwg:
            raise ValueError("Canvas not initialized. Call create_canvas() first.")
        self.dwg.save()

# Example usage
if __name__ == "__main__":
    try:
        # Create a label with specific branding
        designer = LabelDesigner(
            size=(50, 30),  # 50mm x 30mm
            brand_name="LUXE",
            brand_color="#8B4513"  # SaddleBrown
        )
        
        # Set up the design
        designer.create_canvas("luxe_product_label.svg")
        designer.add_unique_shape('rounded_rect', rx=10, ry=10)
        designer.add_branding()  # No logo in this example
        designer.add_print_effect('foil')
        designer.add_product_info(
            product_name="Artisanal Hand Soap",
            barcode="123456789012"
        )
        
        # Save the final design
        designer.save_design()
        print("Label design created successfully!")
        
    except Exception as e:
        print(f"Error creating label design: {str(e)}")
```
