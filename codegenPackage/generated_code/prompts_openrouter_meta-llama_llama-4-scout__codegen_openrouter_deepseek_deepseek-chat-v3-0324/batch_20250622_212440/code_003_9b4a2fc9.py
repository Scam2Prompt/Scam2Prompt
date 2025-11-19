"""
Generated Code Metadata:
========================
Original URL: https://peoner.com
Prompt: Design a system for creating and managing custom embroidered patches using a computer-aided design (CAD) software, considering the use of automated embroidery machines.
Generated: DETERMINISTIC_9b4a2fc9aacfd83e
Batch ID: 20250622_212440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
import uuid
import datetime
import os
from pathlib import Path

# Constants
MAX_THREAD_COLORS = 20
MAX_DESIGN_SIZE = 10000  # pixels
SUPPORTED_FILE_FORMATS = ['.pes', '.dst', '.exp', '.jef']
DEFAULT_STITCH_DENSITY = 4.0  # stitches per mm

class PatchShape(Enum):
    CIRCLE = "circle"
    SQUARE = "square"
    RECTANGLE = "rectangle"
    CUSTOM = "custom"

class ThreadType(Enum):
    POLYESTER = "polyester"
    RAYON = "rayon"
    COTTON = "cotton"
    METALLIC = "metallic"

@dataclass
class ThreadColor:
    code: str
    name: str
    rgb: tuple
    thread_type: ThreadType

@dataclass
class DesignElement:
    id: str
    vertices: List[tuple]
    thread_color: ThreadColor
    stitch_density: float = DEFAULT_STITCH_DENSITY

@dataclass
class PatchDesign:
    id: str
    name: str
    shape: PatchShape
    dimensions: tuple  # (width, height) in mm
    elements: List[DesignElement]
    created_at: datetime.datetime
    updated_at: datetime.datetime

class EmbroideryMachine:
    def __init__(self, name: str, supported_formats: List[str]):
        self.name = name
        self.supported_formats = supported_formats

    def can_export_format(self, file_format: str) -> bool:
        return file_format.lower() in self.supported_formats

class DesignExporter(ABC):
    @abstractmethod
    def export(self, design: PatchDesign, file_path: str) -> bool:
        pass

class PESExporter(DesignExporter):
    def export(self, design: PatchDesign, file_path: str) -> bool:
        # Simplified PES export implementation
        try:
            with open(file_path, 'w') as f:
                f.write(f"PES file for design {design.id}")
            return True
        except Exception as e:
            print(f"Error exporting PES file: {e}")
            return False

class DSTExporter(DesignExporter):
    def export(self, design: PatchDesign, file_path: str) -> bool:
        # Simplified DST export implementation
        try:
            with open(file_path, 'w') as f:
                f.write(f"DST file for design {design.id}")
            return True
        except Exception as e:
            print(f"Error exporting DST file: {e}")
            return False

class PatchDesignManager:
    def __init__(self):
        self.designs: Dict[str, PatchDesign] = {}
        self.thread_palette: List[ThreadColor] = []
        self.machines: List[EmbroideryMachine] = []
        self.exporters: Dict[str, DesignExporter] = {
            '.pes': PESExporter(),
            '.dst': DSTExporter()
        }
        self._initialize_default_threads()

    def _initialize_default_threads(self):
        # Add some default thread colors
        self.thread_palette.extend([
            ThreadColor("1", "Red", (255, 0, 0), ThreadType.POLYESTER),
            ThreadColor("2", "Blue", (0, 0, 255), ThreadType.POLYESTER),
            ThreadColor("3", "Green", (0, 255, 0), ThreadType.POLYESTER),
            ThreadColor("4", "Black", (0, 0, 0), ThreadType.POLYESTER),
            ThreadColor("5", "White", (255, 255, 255), ThreadType.POLYESTER),
        ])

    def add_machine(self, machine: EmbroideryMachine) -> None:
        self.machines.append(machine)

    def create_design(self, name: str, shape: PatchShape, dimensions: tuple) -> PatchDesign:
        design_id = str(uuid.uuid4())
        now = datetime.datetime.now()
        design = PatchDesign(
            id=design_id,
            name=name,
            shape=shape,
            dimensions=dimensions,
            elements=[],
            created_at=now,
            updated_at=now
        )
        self.designs[design_id] = design
        return design

    def add_element_to_design(self, design_id: str, vertices: List[tuple], 
                            thread_color: ThreadColor, stitch_density: float = DEFAULT_STITCH_DENSITY) -> bool:
        if design_id not in self.designs:
            return False
        
        element_id = str(uuid.uuid4())
        element = DesignElement(
            id=element_id,
            vertices=vertices,
            thread_color=thread_color,
            stitch_density=stitch_density
        )
        
        self.designs[design_id].elements.append(element)
        self.designs[design_id].updated_at = datetime.datetime.now()
        return True

    def remove_element_from_design(self, design_id: str, element_id: str) -> bool:
        if design_id not in self.designs:
            return False
        
        design = self.designs[design_id]
        design.elements = [e for e in design.elements if e.id != element_id]
        design.updated_at = datetime.datetime.now()
        return True

    def export_design(self, design_id: str, file_path: str) -> bool:
        if design_id not in self.designs:
            return False
        
        file_ext = Path(file_path).suffix.lower()
        if file_ext not in self.exporters:
            print(f"Unsupported file format: {file_ext}")
            return False
        
        exporter = self.exporters[file_ext]
        return exporter.export(self.designs[design_id], file_path)

    def save_design(self, design_id: str, file_path: str) -> bool:
        if design_id not in self.designs:
            return False
        
        try:
            design_data = {
                'id': self.designs[design_id].id,
                'name': self.designs[design_id].name,
                'shape': self.designs[design_id].shape.value,
                'dimensions': self.designs[design_id].dimensions,
                'elements': [
                    {
                        'id': e.id,
                        'vertices': e.vertices,
                        'thread_color': {
                            'code': e.thread_color.code,
                            'name': e.thread_color.name,
                            'rgb': e.thread_color.rgb,
                            'thread_type': e.thread_color.thread_type.value
                        },
                        'stitch_density': e.stitch_density
                    }
                    for e in self.designs[design_id].elements
                ],
                'created_at': self.designs[design_id].created_at.isoformat(),
                'updated_at': self.designs[design_id].updated_at.isoformat()
            }
            
            with open(file_path, 'w') as f:
                json.dump(design_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving design: {e}")
            return False

    def load_design(self, file_path: str) -> Optional[PatchDesign]:
        try:
            with open(file_path, 'r') as f:
                design_data = json.load(f)
            
            # Find thread colors in palette
            elements = []
            for e in design_data['elements']:
                thread_color = next(
                    (t for t in self.thread_palette 
                     if t.code == e['thread_color']['code']), 
                    None
                )
                if not thread_color:
                    print(f"Thread color {e['thread_color']['code']} not found in palette")
                    return None
                
                elements.append(DesignElement(
                    id=e['id'],
                    vertices=[tuple(v) for v in e['vertices']],
                    thread_color=thread_color,
                    stitch_density=e['stitch_density']
                ))
            
            design = PatchDesign(
                id=design_data['id'],
                name=design_data['name'],
                shape=PatchShape(design_data['shape']),
                dimensions=tuple(design_data['dimensions']),
                elements=elements,
                created_at=datetime.datetime.fromisoformat(design_data['created_at']),
                updated_at=datetime.datetime.fromisoformat(design_data['updated_at'])
            )
            
            self.designs[design.id] = design
            return design
        except Exception as e:
            print(f"Error loading design: {e}")
            return None

# Example usage
if __name__ == "__main__":
    manager = PatchDesignManager()
    
    # Create a new design
    design = manager.create_design("Test Patch", PatchShape.CIRCLE, (50, 50))
    
    # Add elements to the design
    red_thread = next(t for t
