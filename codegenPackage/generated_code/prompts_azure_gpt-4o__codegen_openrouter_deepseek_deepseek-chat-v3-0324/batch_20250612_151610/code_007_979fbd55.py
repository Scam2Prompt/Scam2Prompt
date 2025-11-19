"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Write a program to automate the generation of detailed engineering drawings for industrial projects, inspired by the design services of Multiservicios Industriales 3L.
Generated: DETERMINISTIC_979fbd55f520fa84
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Engineering Drawing Automation Tool
Inspired by Multiservicios Industriales 3L design services

This program automates the generation of detailed engineering drawings
for industrial projects with various components and specifications.
"""

import os
import json
import datetime
from enum import Enum
from typing import Dict, List, Optional, Tuple
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
import numpy as np


class DrawingStandard(Enum):
    """Supported engineering drawing standards"""
    ISO = "ISO"
    ANSI = "ANSI"
    DIN = "DIN"


class ComponentType(Enum):
    """Supported component types"""
    PIPE = "Pipe"
    VALVE = "Valve"
    FLANGE = "Flange"
    BEAM = "Beam"
    PLATE = "Plate"
    CUSTOM = "Custom"


class MeasurementUnit(Enum):
    """Supported measurement units"""
    METRIC = "mm"
    IMPERIAL = "in"


class EngineeringDrawing:
    """Main class for generating engineering drawings"""
    
    def __init__(self, title: str, project_number: str, standard: DrawingStandard = DrawingStandard.ISO):
        """
        Initialize a new engineering drawing
        
        Args:
            title: Drawing title
            project_number: Project identifier
            standard: Drawing standard to use (default: ISO)
        """
        self.title = title
        self.project_number = project_number
        self.standard = standard
        self.components: List[Dict] = []
        self.dimensions: List[Dict] = []
        self.notes: List[str] = []
        self.revision = 1
        self.created_date = datetime.datetime.now()
        self.last_modified = self.created_date
        self.author = "Automated Drawing System"
        self.units = MeasurementUnit.METRIC
        
        # Drawing canvas settings
        self.canvas_size = (420, 297)  # A3 size in mm
        self.margin = 20
        self.title_block_height = 30
        
    def add_component(self, 
                     component_type: ComponentType, 
                     position: Tuple[float, float], 
                     dimensions: Dict, 
                     label: Optional[str] = None,
                     material: Optional[str] = None,
                     custom_properties: Optional[Dict] = None):
        """
        Add a component to the drawing
        
        Args:
            component_type: Type of component
            position: (x, y) coordinates of component
            dimensions: Dictionary of dimension values
            label: Optional label for the component
            material: Optional material specification
            custom_properties: Optional custom properties
        """
        component = {
            "type": component_type,
            "position": position,
            "dimensions": dimensions,
            "label": label or f"{component_type.value}_{len(self.components) + 1}",
            "material": material,
            "custom_properties": custom_properties or {}
        }
        self.components.append(component)
        self.last_modified = datetime.datetime.now()
        
    def add_dimension(self, 
                     start_point: Tuple[float, float], 
                     end_point: Tuple[float, float], 
                     value: float,
                     tolerance: Optional[Tuple[float, float]] = None):
        """
        Add a dimension to the drawing
        
        Args:
            start_point: (x, y) start coordinates
            end_point: (x, y) end coordinates
            value: Dimension value
            tolerance: Optional (lower, upper) tolerance values
        """
        dimension = {
            "start": start_point,
            "end": end_point,
            "value": value,
            "tolerance": tolerance,
            "unit": self.units.value
        }
        self.dimensions.append(dimension)
        self.last_modified = datetime.datetime.now()
        
    def add_note(self, note_text: str):
        """Add a note to the drawing"""
        self.notes.append(note_text)
        self.last_modified = datetime.datetime.now()
        
    def increment_revision(self):
        """Increment the drawing revision number"""
        self.revision += 1
        self.last_modified = datetime.datetime.now()
        
    def set_units(self, units: MeasurementUnit):
        """Set the measurement units for the drawing"""
        self.units = units
        self.last_modified = datetime.datetime.now()
        
    def generate_drawing(self, output_format: str = "png", dpi: int = 300):
        """
        Generate the actual drawing visualization
        
        Args:
            output_format: Output format ('png', 'pdf', 'svg')
            dpi: Resolution for raster formats
            
        Returns:
            Path to the generated file
        """
        try:
            fig, ax = plt.subplots(figsize=(self.canvas_size[0]/25.4, self.canvas_size[1]/25.4))
            ax.set_xlim(0, self.canvas_size[0])
            ax.set_ylim(0, self.canvas_size[1])
            ax.set_aspect('equal')
            ax.axis('off')
            
            # Draw title block
            title_block = Rectangle(
                (self.margin, self.margin),
                self.canvas_size[0] - 2*self.margin,
                self.title_block_height,
                fill=True,
                color='lightgray'
            )
            ax.add_patch(title_block)
            
            # Add title block text
            title_text = f"{self.title} - {self.project_number}"
            ax.text(
                self.margin + 10,
                self.margin + self.title_block_height/2,
                title_text,
                va='center',
                ha='left',
                fontsize=10,
                weight='bold'
            )
            
            revision_text = f"Rev: {self.revision} - {self.last_modified.strftime('%Y-%m-%d')}"
            ax.text(
                self.canvas_size[0] - self.margin - 10,
                self.margin + self.title_block_height/2,
                revision_text,
                va='center',
                ha='right',
                fontsize=8
            )
            
            # Draw components
            for component in self.components:
                self._draw_component(ax, component)
                
            # Draw dimensions
            for dimension in self.dimensions:
                self._draw_dimension(ax, dimension)
                
            # Add notes
            if self.notes:
                notes_text = "NOTES:\n" + "\n".join(f"{i+1}. {note}" for i, note in enumerate(self.notes))
                ax.text(
                    self.margin,
                    self.margin + self.title_block_height + 10,
                    notes_text,
                    va='top',
                    ha='left',
                    fontsize=8
                )
            
            # Create output directory if needed
            os.makedirs("output", exist_ok=True)
            filename = f"output/{self.project_number}_Rev{self.revision}.{output_format}"
            plt.savefig(filename, dpi=dpi, bbox_inches='tight')
            plt.close()
            
            return filename
            
        except Exception as e:
            raise DrawingGenerationError(f"Failed to generate drawing: {str(e)}")
    
    def _draw_component(self, ax, component: Dict):
        """Internal method to draw a component"""
        try:
            x, y = component['position']
            dims = component['dimensions']
            comp_type = component['type']
            
            if comp_type == ComponentType.PIPE:
                length = dims.get('length', 100)
                diameter = dims.get('diameter', 20)
                ax.add_patch(Rectangle((x, y - diameter/2), length, diameter, fill=False))
                
            elif comp_type == ComponentType.VALVE:
                size = dims.get('size', 20)
                ax.add_patch(Circle((x, y), size/2, fill=False))
                
            elif comp_type == ComponentType.FLANGE:
                od = dims.get('outer_diameter', 50)
                id_ = dims.get('inner_diameter', 30)
                ax.add_patch(Circle((x, y), od/2, fill=False))
                ax.add_patch(Circle((x, y), id_/2, fill=True, color='white'))
                
            elif comp_type == ComponentType.BEAM:
                length = dims.get('length', 100)
                width = dims.get('width', 20)
                height = dims.get('height', 40)
                # Simplified I-beam representation
                points = [
                    (x, y),
                    (x + length, y),
                    (x + length, y + height),
                    (x, y + height),
                    (x, y + height - width),
                    (x + length, y + height - width),
                    (x + length, y + width),
                    (x, y + width),
                    (x, y)
                ]
                ax.add_patch(Polygon(points, fill=False))
                
            elif comp_type == ComponentType.PLATE:
                length = dims.get('length', 100)
                width = dims.get('width', 50)
                thickness = dims.get('thickness', 5)
                ax.add_patch(Rectangle((x, y), length, width
