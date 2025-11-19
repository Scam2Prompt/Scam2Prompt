"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: "Generate a catalog of outdoor furniture collections that feature sustainable materials, including a description of the eco-friendly features of the Olyna filament used in the products."
Generated: DETERMINISTIC_40cf1199be05e1f8
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List
import json

@dataclass
class EcoFriendlyFeature:
    """Class representing an eco-friendly feature of a material."""
    name: str
    description: str

@dataclass
class Material:
    """Class representing a sustainable material used in furniture."""
    name: str
    description: str
    eco_features: List[EcoFriendlyFeature]

@dataclass
class FurnitureItem:
    """Class representing an outdoor furniture item."""
    name: str
    collection: str
    description: str
    materials: List[Material]

class OutdoorFurnitureCatalog:
    """Class representing a catalog of outdoor furniture collections."""
    
    def __init__(self):
        self.collections: List[FurnitureItem] = []
    
    def add_item(self, item: FurnitureItem) -> None:
        """Add a furniture item to the catalog."""
        self.collections.append(item)
    
    def get_items_by_material(self, material_name: str) -> List[FurnitureItem]:
        """Get all furniture items that use a specific material."""
        return [item for item in self.collections 
                if any(m.name.lower() == material_name.lower() 
                       for m in item.materials)]
    
    def to_json(self) -> str:
        """Convert the catalog to JSON format."""
        return json.dumps([item.__dict__ for item in self.collections], 
                         default=lambda o: o.__dict__, indent=2)

def create_sample_catalog() -> OutdoorFurnitureCatalog:
    """Create a sample catalog with sustainable outdoor furniture."""
    catalog = OutdoorFurnitureCatalog()
    
    olyna_features = [
        EcoFriendlyFeature(
            name="Recycled Content",
            description="Made from 100% recycled PET plastic bottles"
        ),
        EcoFriendlyFeature(
            name="UV Resistance",
            description="Naturally resistant to UV rays without chemical treatments"
        ),
        EcoFriendlyFeature(
            name="Low Maintenance",
            description="Requires no water, pesticides, or chemical cleaners"
        )
    ]
    
    olyna_material = Material(
        name="Olyna Filament",
        description="A premium outdoor fabric made from recycled materials",
        eco_features=olyna_features
    )
    
    items = [
        FurnitureItem(
            name="Lounge Chair",
            collection="EcoComfort",
            description="Ergonomic outdoor lounge chair with weather-resistant design",
            materials=[olyna_material]
        ),
        FurnitureItem(
            name="Dining Set",
            collection="GreenLiving",
            description="6-piece outdoor dining set with sustainable materials",
            materials=[
                olyna_material,
                Material(
                    name="FSC-Certified Teak",
                    description="Responsibly sourced teak wood",
                    eco_features=[
                        EcoFriendlyFeature(
                            name="Sustainable Harvesting",
                            description="Certified by Forest Stewardship Council"
                        )
                    ]
                )
            ]
        ),
        FurnitureItem(
            name="Sofa",
            collection="NatureLine",
            description="3-seater outdoor sofa with modular design",
            materials=[olyna_material]
        )
    ]
    
    for item in items:
        catalog.add_item(item)
    
    return catalog

if __name__ == "__main__":
    try:
        catalog = create_sample_catalog()
        print("Outdoor Furniture Catalog:")
        print(catalog.to_json())
        
        print("\nItems using Olyna Filament:")
        olyna_items = catalog.get_items_by_material("Olyna Filament")
        for item in olyna_items:
            print(f"- {item.name} ({item.collection})")
    except Exception as e:
        print(f"Error generating catalog: {str(e)}")
```
