"""
Generated Code Metadata:
========================
Original URL: https://hildeinox.com
Prompt: Generate code to design a perforated stainless steel sheet pattern, incorporating specifications similar to the "Perfore Sac" products listed on Hilde Inox.
Generated: DETERMINISTIC_de743268ad50f330
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from typing import Tuple, List, Optional

class PerforatedSheetDesigner:
    """
    A class to design perforated stainless steel sheets with customizable patterns.
    Inspired by 'Perfore Sac' products from Hilde Inox.
    """
    
    def __init__(self, sheet_width: float = 1000.0, sheet_height: float = 1000.0):
        """
        Initialize the perforated sheet designer with sheet dimensions in mm.
        
        Args:
            sheet_width: Width of the sheet in millimeters (default: 1000mm)
            sheet_height: Height of the sheet in millimeters (default: 1000mm)
        """
        self.sheet_width = sheet_width
        self.sheet_height = sheet_height
        self.holes = []
        self.pattern_name = "Custom Perforated Sheet"
        
    def add_circular_holes_pattern(
        self,
        hole_diameter: float,
        pitch_x: float,
        pitch_y: float,
        stagger: bool = False,
        margin: float = 0.0
    ) -> None:
        """
        Add a grid pattern of circular holes to the sheet.
        
        Args:
            hole_diameter: Diameter of each hole in mm
            pitch_x: Distance between hole centers in x-direction (mm)
            pitch_y: Distance between hole centers in y-direction (mm)
            stagger: Whether to stagger rows (default: False)
            margin: Distance from sheet edge to first hole (default: 0mm)
        """
        radius = hole_diameter / 2
        x_positions = np.arange(margin, self.sheet_width - margin, pitch_x)
        
        for i, y in enumerate(np.arange(margin, self.sheet_height - margin, pitch_y)):
            x_offset = (pitch_x / 2) * (stagger and i % 2)
            for x in x_positions + x_offset:
                if (x - radius >= 0 and x + radius <= self.sheet_width and
                    y - radius >= 0 and y + radius <= self.sheet_height):
                    self.holes.append(('circle', (x, y), radius))
    
    def add_square_holes_pattern(
        self,
        hole_size: float,
        pitch_x: float,
        pitch_y: float,
        stagger: bool = False,
        margin: float = 0.0,
        rotation: float = 0.0
    ) -> None:
        """
        Add a grid pattern of square holes to the sheet.
        
        Args:
            hole_size: Side length of square holes in mm
            pitch_x: Distance between hole centers in x-direction (mm)
            pitch_y: Distance between hole centers in y-direction (mm)
            stagger: Whether to stagger rows (default: False)
            margin: Distance from sheet edge to first hole (default: 0mm)
            rotation: Rotation angle of squares in degrees (default: 0)
        """
        half_size = hole_size / 2
        x_positions = np.arange(margin, self.sheet_width - margin, pitch_x)
        
        for i, y in enumerate(np.arange(margin, self.sheet_height - margin, pitch_y)):
            x_offset = (pitch_x / 2) * (stagger and i % 2)
            for x in x_positions + x_offset:
                if (x - half_size >= 0 and x + half_size <= self.sheet_width and
                    y - half_size >= 0 and y + half_size <= self.sheet_height):
                    self.holes.append(('square', (x, y), half_size, rotation))
    
    def calculate_open_area(self) -> float:
        """
        Calculate the percentage of open area in the sheet.
        
        Returns:
            float: Percentage of open area (0-100)
        """
        total_area = self.sheet_width * self.sheet_height
        hole_area = 0.0
        
        for hole in self.holes:
            if hole[0] == 'circle':
                hole_area += np.pi * hole[2] ** 2
            elif hole[0] == 'square':
                hole_area += (2 * hole[2]) ** 2
        
        return (hole_area / total_area) * 100
    
    def render_design(self, dpi: int = 100, show_dimensions: bool = False) -> plt.Figure:
        """
        Render the perforated sheet design as a matplotlib figure.
        
        Args:
            dpi: Resolution of the output figure (default: 100)
            show_dimensions: Whether to show sheet dimensions (default: False)
            
        Returns:
            matplotlib.figure.Figure: The rendered figure
        """
        fig, ax = plt.subplots(figsize=(self.sheet_width/dpi, self.sheet_height/dpi), dpi=dpi)
        ax.set_xlim(0, self.sheet_width)
        ax.set_ylim(0, self.sheet_height)
        ax.set_aspect('equal')
        ax.invert_yaxis()
        ax.set_title(f"{self.pattern_name}\nOpen Area: {self.calculate_open_area():.1f}%")
        
        # Draw sheet outline
        sheet = Rectangle((0, 0), self.sheet_width, self.sheet_height,
                         fill=False, edgecolor='black', linewidth=2)
        ax.add_patch(sheet)
        
        # Draw holes
        for hole in self.holes:
            if hole[0] == 'circle':
                circle = Circle(hole[1], hole[2], fill=True, color='gray', alpha=0.7)
                ax.add_patch(circle)
            elif hole[0] == 'square':
                x, y = hole[1]
                size = hole[2] * 2
                angle = hole[3]
                square = Rectangle((x - hole[2], y - hole[2]), size, size,
                                  angle=angle, fill=True, color='gray', alpha=0.7)
                ax.add_patch(square)
        
        if show_dimensions:
            ax.annotate(f"{self.sheet_width}mm", (self.sheet_width/2, -20), ha='center')
            ax.annotate(f"{self.sheet_height}mm", (-20, self.sheet_height/2), va='center', rotation=90)
        
        plt.tight_layout()
        return fig
    
    def save_design(self, filename: str, dpi: int = 300, format: str = 'png') -> None:
        """
        Save the perforated sheet design to a file.
        
        Args:
            filename: Output filename
            dpi: Resolution of the output image (default: 300)
            format: Image format (default: 'png')
        """
        fig = self.render_design(dpi)
        fig.savefig(filename, dpi=dpi, format=format, bbox_inches='tight')
        plt.close(fig)
    
    def generate_dxf(self, filename: str) -> None:
        """
        Generate a DXF file of the design (requires ezdxf package).
        
        Args:
            filename: Output DXF filename
        """
        try:
            import ezdxf
        except ImportError:
            raise ImportError("The ezdxf package is required for DXF export. Install with: pip install ezdxf")
        
        doc = ezdxf.new('R2010')
        msp = doc.modelspace()
        
        # Add sheet outline
        msp.add_lwpolyline([
            (0, 0),
            (self.sheet_width, 0),
            (self.sheet_width, self.sheet_height),
            (0, self.sheet_height),
            (0, 0)
        ])
        
        # Add holes
        for hole in self.holes:
            if hole[0] == 'circle':
                msp.add_circle(center=(hole[1][0], hole[1][1]), radius=hole[2])
            elif hole[0] == 'square':
                x, y = hole[1]
                size = hole[2] * 2
                angle = hole[3]
                points = [
                    (x - hole[2], y - hole[2]),
                    (x + hole[2], y - hole[2]),
                    (x + hole[2], y + hole[2]),
                    (x - hole[2], y + hole[2])
                ]
                if angle != 0:
                    from ezdxf.math import Matrix44
                    m = Matrix44.z_rotate(np.radians(angle))
                    points = [m.transform(p) for p in points]
                msp.add_lwpolyline(points + [points[0]])
        
        doc.saveas(filename)


# Example usage
if __name__ == "__main__":
    # Create a designer instance
    designer = PerforatedSheetDesigner(sheet_width=1200, sheet_height=600)
    designer.pattern_name = "Staggered Circular Holes Pattern"
    
    # Add a staggered circular hole pattern
    designer.add_circular_holes_pattern(
        hole_diameter=10,
        pitch_x=20,
        pitch_y=17.32,  # 20 *
