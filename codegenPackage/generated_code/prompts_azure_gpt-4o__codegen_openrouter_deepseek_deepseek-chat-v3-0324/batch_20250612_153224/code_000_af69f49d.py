"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Write Python code to generate a design template for textile customization using techniques like serigraphy or sublimation, as described on CreatexPro's website.
Generated: DETERMINISTIC_af69f49d63b39b3d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from enum import Enum
from typing import List, Optional, Dict
import uuid
from datetime import datetime

class PrintingTechnique(Enum):
    """Enum representing different textile printing techniques."""
    SERIGRAPHY = "Serigraphy"
    SUBLIMATION = "Sublimation"
    DIGITAL = "Digital Printing"
    SCREEN = "Screen Printing"
    HEAT_TRANSFER = "Heat Transfer"

@dataclass
class Color:
    """Represents a color in RGB format with optional name."""
    red: int
    green: int
    blue: int
    name: Optional[str] = None

    def validate(self) -> bool:
        """Validate RGB values are within 0-255 range."""
        return all(0 <= val <= 255 for val in [self.red, self.green, self.blue])

@dataclass
class DesignElement:
    """Represents a single element in the textile design."""
    element_id: str
    name: str
    position_x: float
    position_y: float
    width: float
    height: float
    rotation: float = 0.0
    colors: List[Color] = None
    technique: PrintingTechnique = PrintingTechnique.SERIGRAPHY

    def __post_init__(self):
        """Initialize colors list if not provided and validate positions."""
        if self.colors is None:
            self.colors = []
        if not (0 <= self.position_x <= 100 and 0 <= self.position_y <= 100):
            raise ValueError("Position must be between 0 and 100")
        if not all(color.validate() for color in self.colors):
            raise ValueError("Invalid RGB color values")

@dataclass
class TextileTemplate:
    """Represents a complete textile design template."""
    template_id: str
    name: str
    description: str
    width_cm: float
    height_cm: float
    elements: List[DesignElement]
    created_at: str
    updated_at: str
    author: str
    tags: List[str] = None

    def to_json(self) -> str:
        """Convert the template to JSON format."""
        return json.dumps(asdict(self), indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'TextileTemplate':
        """Create a TextileTemplate from JSON string."""
        data = json.loads(json_str)
        elements = [DesignElement(**elem) for elem in data['elements']]
        return cls(
            template_id=data['template_id'],
            name=data['name'],
            description=data['description'],
            width_cm=data['width_cm'],
            height_cm=data['height_cm'],
            elements=elements,
            created_at=data['created_at'],
            updated_at=data['updated_at'],
            author=data['author'],
            tags=data.get('tags', [])
        )

def create_new_template(
    name: str,
    description: str,
    width_cm: float,
    height_cm: float,
    author: str,
    tags: List[str] = None
) -> TextileTemplate:
    """Create a new textile template with default values."""
    if tags is None:
        tags = []
    timestamp = datetime.now().isoformat()
    return TextileTemplate(
        template_id=str(uuid.uuid4()),
        name=name,
        description=description,
        width_cm=width_cm,
        height_cm=height_cm,
        elements=[],
        created_at=timestamp,
        updated_at=timestamp,
        author=author,
        tags=tags
    )

def add_element_to_template(
    template: TextileTemplate,
    name: str,
    position_x: float,
    position_y: float,
    width: float,
    height: float,
    colors: List[Color],
    technique: PrintingTechnique = PrintingTechnique.SERIGRAPHY,
    rotation: float = 0.0
) -> TextileTemplate:
    """Add a new design element to the template."""
    element = DesignElement(
        element_id=str(uuid.uuid4()),
        name=name,
        position_x=position_x,
        position_y=position_y,
        width=width,
        height=height,
        rotation=rotation,
        colors=colors,
        technique=technique
    )
    template.elements.append(element)
    template.updated_at = datetime.now().isoformat()
    return template

def validate_template(template: TextileTemplate) -> Dict[str, List[str]]:
    """Validate the textile template and return any errors."""
    errors = {"general": [], "elements": []}
    
    if not template.name.strip():
        errors["general"].append("Template name cannot be empty")
    
    if template.width_cm <= 0 or template.height_cm <= 0:
        errors["general"].append("Width and height must be positive values")
    
    for i, element in enumerate(template.elements):
        element_errors = []
        if not element.name.strip():
            element_errors.append("Element name cannot be empty")
        if element.width <= 0 or element.height <= 0:
            element_errors.append("Element dimensions must be positive")
        if not (0 <= element.position_x <= 100 and 0 <= element.position_y <= 100):
            element_errors.append("Element position must be between 0 and 100")
        if not element.colors:
            element_errors.append("Element must have at least one color")
        
        if element_errors:
            errors["elements"].append({
                "element_index": i,
                "element_name": element.name,
                "errors": element_errors
            })
    
    return errors

def save_template_to_file(template: TextileTemplate, file_path: str) -> None:
    """Save the template to a JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(asdict(template), f, indent=2)
    except IOError as e:
        raise IOError(f"Failed to save template to file: {str(e)}")

def load_template_from_file(file_path: str) -> TextileTemplate:
    """Load a template from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return TextileTemplate.from_json(json.dumps(data))
    except IOError as e:
        raise IOError(f"Failed to load template from file: {str(e)}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {str(e)}")
    except KeyError as e:
        raise ValueError(f"Missing required field in JSON: {str(e)}")
```
