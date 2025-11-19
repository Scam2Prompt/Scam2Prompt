"""
Generated Code Metadata:
========================
Original URL: https://impresionentabloide.com
Prompt: Create code to design and export vinyl cutting templates in SVG format, optimized for the specifications provided on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_dafb1cce9e03d592
Batch ID: 20250612_150417
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
import math
import argparse
import os

class VinylCutterTemplate:
    """
    A class to generate SVG templates for vinyl cutting based on specifications.
    """
    
    def __init__(self, width=432, height=279, output_file='vinyl_template.svg'):
        """
        Initialize the template with default dimensions (tabloid size in mm).
        
        Args:
            width (float): Width of the template in mm
            height (float): Height of the template in mm
            output_file (str): Output SVG filename
        """
        self.width = width
        self.height = height
        self.output_file = output_file
        self.dwg = None
        
    def create_template(self):
        """Create the SVG drawing with the specified dimensions."""
        try:
            self.dwg = svgwrite.Drawing(
                filename=self.output_file,
                size=(f'{self.width}mm', f'{self.height}mm'),
                viewBox=(f'0 0 {self.width} {self.height}')
            )
            self._add_bleed_margin()
            self._add_cutting_guides()
            self._add_registration_marks()
            return True
        except Exception as e:
            print(f"Error creating template: {e}")
            return False
    
    def _add_bleed_margin(self, margin=3):
        """
        Add bleed margin to the template.
        
        Args:
            margin (float): Bleed margin in mm
        """
        try:
            # Add bleed area rectangle
            self.dwg.add(
                self.dwg.rect(
                    insert=(margin, margin),
                    size=(self.width - 2*margin, self.height - 2*margin),
                    stroke='red',
                    stroke_width=0.1,
                    fill='none',
                    stroke_dasharray='5,5'
                )
            )
            
            # Add bleed margin text
            self.dwg.add(
                self.dwg.text(
                    f'Bleed Margin: {margin}mm',
                    insert=(margin + 5, margin + 5),
                    font_size='3mm',
                    fill='red'
                )
            )
        except Exception as e:
            print(f"Error adding bleed margin: {e}")
    
    def _add_cutting_guides(self, spacing=50):
        """
        Add cutting guides to help with alignment.
        
        Args:
            spacing (float): Spacing between guides in mm
        """
        try:
            # Horizontal guides
            for y in range(0, self.height + 1, spacing):
                self.dwg.add(
                    self.dwg.line(
                        start=(0, y),
                        end=(5, y),
                        stroke='blue',
                        stroke_width=0.2
                    )
                )
                self.dwg.add(
                    self.dwg.line(
                        start=(self.width - 5, y),
                        end=(self.width, y),
                        stroke='blue',
                        stroke_width=0.2
                    )
                )
                if y > 0 and y < self.height:
                    self.dwg.add(
                        self.dwg.text(
                            f'{y}mm',
                            insert=(10, y + 2),
                            font_size='2mm',
                            fill='blue'
                        )
                    )
            
            # Vertical guides
            for x in range(0, self.width + 1, spacing):
                self.dwg.add(
                    self.dwg.line(
                        start=(x, 0),
                        end=(x, 5),
                        stroke='blue',
                        stroke_width=0.2
                    )
                )
                self.dwg.add(
                    self.dwg.line(
                        start=(x, self.height - 5),
                        end=(x, self.height),
                        stroke='blue',
                        stroke_width=0.2
                    )
                )
                if x > 0 and x < self.width:
                    self.dwg.add(
                        self.dwg.text(
                            f'{x}mm',
                            insert=(x + 2, 10),
                            font_size='2mm',
                            fill='blue',
                            transform=f'rotate(90, {x + 2}, 10)'
                        )
                    )
        except Exception as e:
            print(f"Error adding cutting guides: {e}")
    
    def _add_registration_marks(self, size=5, offset=10):
        """
        Add registration marks for alignment.
        
        Args:
            size (float): Size of registration marks in mm
            offset (float): Offset from edges in mm
        """
        try:
            # Corners
            corners = [
                (offset, offset),
                (self.width - offset, offset),
                (offset, self.height - offset),
                (self.width - offset, self.height - offset)
            ]
            
            for x, y in corners:
                # Crosshair
                self.dwg.add(
                    self.dwg.line(
                        start=(x - size, y),
                        end=(x + size, y),
                        stroke='black',
                        stroke_width=0.3
                    )
                )
                self.dwg.add(
                    self.dwg.line(
                        start=(x, y - size),
                        end=(x, y + size),
                        stroke='black',
                        stroke_width=0.3
                    )
                )
                
                # Circle
                self.dwg.add(
                    self.dwg.circle(
                        center=(x, y),
                        r=size/2,
                        fill='none',
                        stroke='black',
                        stroke_width=0.2
                    )
                )
        except Exception as e:
            print(f"Error adding registration marks: {e}")
    
    def add_custom_shape(self, shape_type, **kwargs):
        """
        Add a custom shape to the template.
        
        Args:
            shape_type (str): Type of shape ('rectangle', 'circle', 'polygon')
            **kwargs: Shape-specific parameters
        """
        try:
            if shape_type == 'rectangle':
                self.dwg.add(
                    self.dwg.rect(
                        insert=(kwargs['x'], kwargs['y']),
                        size=(kwargs['width'], kwargs['height']),
                        fill=kwargs.get('fill', 'none'),
                        stroke=kwargs.get('stroke', 'black'),
                        stroke_width=kwargs.get('stroke_width', 0.3)
                    )
                )
            elif shape_type == 'circle':
                self.dwg.add(
                    self.dwg.circle(
                        center=(kwargs['cx'], kwargs['cy']),
                        r=kwargs['r'],
                        fill=kwargs.get('fill', 'none'),
                        stroke=kwargs.get('stroke', 'black'),
                        stroke_width=kwargs.get('stroke_width', 0.3)
                    )
                )
            elif shape_type == 'polygon':
                self.dwg.add(
                    self.dwg.polygon(
                        points=kwargs['points'],
                        fill=kwargs.get('fill', 'none'),
                        stroke=kwargs.get('stroke', 'black'),
                        stroke_width=kwargs.get('stroke_width', 0.3)
                    )
                )
        except Exception as e:
            print(f"Error adding custom shape: {e}")
    
    def save(self):
        """Save the SVG file."""
        try:
            if self.dwg:
                self.dwg.save()
                print(f"Template saved to {os.path.abspath(self.output_file)}")
                return True
            return False
        except Exception as e:
            print(f"Error saving template: {e}")
            return False

def main():
    parser = argparse.ArgumentParser(description='Generate SVG templates for vinyl cutting')
    parser.add_argument('--width', type=float, default=432, help='Width in mm (default: 432mm - tabloid)')
    parser.add_argument('--height', type=float, default=279, help='Height in mm (default: 279mm - tabloid)')
    parser.add_argument('--output', type=str, default='vinyl_template.svg', help='Output filename')
    
    args = parser.parse_args()
    
    template = VinylCutterTemplate(width=args.width, height=args.height, output_file=args.output)
    if template.create_template():
        # Example: Add a sample rectangle
        template.add_custom_shape(
            'rectangle',
            x=50, y=50,
            width=100, height=50,
            fill='none',
            stroke='green',
            stroke_width=0.5
        )
        
        # Example: Add a sample circle
        template.add_custom_shape(
            'circle',
            cx=200, cy=100,
            r=30,
            fill='none',
            stroke='purple',
            stroke_width=0.5
        )
        
        template.save()

if __name__ == '__main__':
    main()
```
