"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: "Create a custom outdoor furniture project for a luxury resort using Nodo Italia's contract services, specifying materials, colors, and designs that reflect the brand's aesthetic and commitment to sustainability."
Generated: DETERMINISTIC_e8390ce72a0f5159
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Custom Outdoor Furniture Project for Luxury Resort using Nodo Italia's Contract Services

This script generates a custom outdoor furniture project specification based on Nodo Italia's
contract services, materials, colors, and designs that reflect their brand aesthetic and
sustainability commitment.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
import json
import datetime

class MaterialType(Enum):
    """Sustainable materials offered by Nodo Italia"""
    RECYCLED_ALUMINUM = auto()
    FSC_CERTIFIED_TEAK = auto()
    RECYCLED_POLYETHYLENE = auto()
    STAINLESS_STEEL = auto()
    RECLAIMED_WOOD = auto()

class ColorPalette(Enum):
    """Nodo Italia's signature color palette"""
    SAND = "#D2B48C"
    OCEAN = "#008B8B"
    STORM = "#4F4F4F"
    CLOUD = "#F5F5F5"
    EARTH = "#8B4513"

class DesignStyle(Enum):
    """Design styles matching Nodo Italia's aesthetic"""
    MODERN = auto()
    MINIMALIST = auto()
    ORGANIC = auto()
    COASTAL = auto()
    MEDITERRANEAN = auto()

@dataclass
class FurnitureItem:
    """Class representing a single furniture item specification"""
    item_name: str
    material: MaterialType
    color: ColorPalette
    design: DesignStyle
    dimensions: dict
    quantity: int
    custom_notes: Optional[str] = None

@dataclass
class ProjectSpecification:
    """Complete project specification for Nodo Italia"""
    project_name: str
    client_name: str
    delivery_date: datetime.date
    items: List[FurnitureItem]
    sustainability_features: List[str]
    special_requests: Optional[str] = None

class ProjectGenerator:
    """Generates and manages outdoor furniture projects for Nodo Italia"""
    
    def __init__(self):
        self.sustainability_features = [
            "100% recyclable materials",
            "Low-carbon production process",
            "10-year warranty for reduced replacement",
            "Locally sourced where possible"
        ]
    
    def create_project(self, project_name: str, client_name: str, delivery_date: datetime.date) -> ProjectSpecification:
        """Initialize a new project with basic information"""
        return ProjectSpecification(
            project_name=project_name,
            client_name=client_name,
            delivery_date=delivery_date,
            items=[],
            sustainability_features=self.sustainability_features
        )
    
    def add_furniture_item(
        self,
        project: ProjectSpecification,
        item_name: str,
        material: MaterialType,
        color: ColorPalette,
        design: DesignStyle,
        dimensions: dict,
        quantity: int,
        custom_notes: Optional[str] = None
    ) -> None:
        """Add a furniture item to the project"""
        item = FurnitureItem(
            item_name=item_name,
            material=material,
            color=color,
            design=design,
            dimensions=dimensions,
            quantity=quantity,
            custom_notes=custom_notes
        )
        project.items.append(item)
    
    def generate_project_report(self, project: ProjectSpecification) -> str:
        """Generate a JSON report of the project specification"""
        try:
            report = {
                "projectName": project.project_name,
                "clientName": project.client_name,
                "deliveryDate": project.delivery_date.isoformat(),
                "sustainabilityFeatures": project.sustainability_features,
                "specialRequests": project.special_requests,
                "items": [
                    {
                        "itemName": item.item_name,
                        "material": item.material.name,
                        "color": {
                            "name": item.color.name,
                            "hex": item.color.value
                        },
                        "design": item.design.name,
                        "dimensions": item.dimensions,
                        "quantity": item.quantity,
                        "customNotes": item.custom_notes
                    }
                    for item in project.items
                ]
            }
            return json.dumps(report, indent=2)
        except Exception as e:
            raise ValueError(f"Error generating project report: {str(e)}")

def example_usage():
    """Example usage of the ProjectGenerator for a luxury resort"""
    generator = ProjectGenerator()
    
    # Create a new project
    project = generator.create_project(
        project_name="Azure Sands Resort Outdoor Collection",
        client_name="Azure Sands Luxury Resorts",
        delivery_date=datetime.date(2024, 5, 15)
    )
    
    # Add furniture items
    generator.add_furniture_item(
        project=project,
        item_name="Sunset Lounge Chair",
        material=MaterialType.FSC_CERTIFIED_TEAK,
        color=ColorPalette.SAND,
        design=DesignStyle.COASTAL,
        dimensions={"length": 180, "width": 80, "height": 70},
        quantity=24,
        custom_notes="Extra-wide version for resort comfort"
    )
    
    generator.add_furniture_item(
        project=project,
        item_name="Ocean View Dining Table",
        material=MaterialType.RECYCLED_ALUMINUM,
        color=ColorPalette.OCEAN,
        design=DesignStyle.MODERN,
        dimensions={"length": 220, "width": 100, "height": 75},
        quantity=8,
        custom_notes="Weather-resistant powder coating required"
    )
    
    # Add special requests
    project.special_requests = "All pieces must include discreet resort branding on lower right corner"
    
    # Generate and print the project report
    try:
        report = generator.generate_project_report(project)
        print(report)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    example_usage()
```
