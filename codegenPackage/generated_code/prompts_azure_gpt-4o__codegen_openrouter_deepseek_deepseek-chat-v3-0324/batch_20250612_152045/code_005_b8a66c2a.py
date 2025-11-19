"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: Write code to generate a catalog of industrial brushes with customizable features, including EU-standardized dimensions and client-specific models, as detailed on the VIRCOMEM website.
Generated: DETERMINISTIC_b8a66c2a9b29be2e
Batch ID: 20250612_152045
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

class BrushType(Enum):
    """Enum representing different types of industrial brushes."""
    CYLINDRICAL = "Cylindrical"
    DISC = "Disc"
    END = "End"
    STRIP = "Strip"
    SPECIAL = "Special"

class Material(Enum):
    """Enum representing brush materials."""
    STEEL = "Steel"
    STAINLESS_STEEL = "Stainless Steel"
    NYLON = "Nylon"
    POLYPROPYLENE = "Polypropylene"
    HORSEHAIR = "Horsehair"
    TAMPICO = "Tampico"

class EUStandard(Enum):
    """Enum representing EU standardized dimensions."""
    EN_ISO_9001 = "EN ISO 9001"
    EN_ISO_14001 = "EN ISO 14001"
    EN_ISO_45001 = "EN ISO 45001"

@dataclass
class BrushDimension:
    """Dataclass representing brush dimensions."""
    diameter: float  # in mm
    length: float    # in mm
    width: Optional[float] = None  # in mm, optional for non-strip brushes

@dataclass
class BrushSpecification:
    """Dataclass representing brush specifications."""
    type: BrushType
    material: Material
    dimensions: BrushDimension
    standards: List[EUStandard]
    custom_features: Dict[str, str]  # Key-value pairs for custom features

@dataclass
class ClientModel:
    """Dataclass representing client-specific brush models."""
    model_id: str
    name: str
    description: str
    specifications: BrushSpecification

class BrushCatalog:
    """Class representing a catalog of industrial brushes."""
    
    def __init__(self):
        self.catalog: List[ClientModel] = []
    
    def add_model(self, model: ClientModel) -> None:
        """Add a brush model to the catalog."""
        self.catalog.append(model)
    
    def remove_model(self, model_id: str) -> bool:
        """Remove a brush model from the catalog by ID."""
        for i, model in enumerate(self.catalog):
            if model.model_id == model_id:
                self.catalog.pop(i)
                return True
        return False
    
    def get_model(self, model_id: str) -> Optional[ClientModel]:
        """Get a brush model by ID."""
        for model in self.catalog:
            if model.model_id == model_id:
                return model
        return None
    
    def filter_by_type(self, brush_type: BrushType) -> List[ClientModel]:
        """Filter models by brush type."""
        return [model for model in self.catalog if model.specifications.type == brush_type]
    
    def filter_by_material(self, material: Material) -> List[ClientModel]:
        """Filter models by material."""
        return [model for model in self.catalog if model.specifications.material == material]
    
    def filter_by_standard(self, standard: EUStandard) -> List[ClientModel]:
        """Filter models by EU standard."""
        return [model for model in self.catalog if standard in model.specifications.standards]
    
    def to_json(self) -> str:
        """Convert catalog to JSON string."""
        return json.dumps([asdict(model) for model in self.catalog], indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'BrushCatalog':
        """Create catalog from JSON string."""
        catalog = cls()
        data = json.loads(json_str)
        
        for item in data:
            # Convert enums back from strings
            item['specifications']['type'] = BrushType(item['specifications']['type'])
            item['specifications']['material'] = Material(item['specifications']['material'])
            item['specifications']['standards'] = [EUStandard(s) for s in item['specifications']['standards']]
            
            # Recreate dimension object
            dim_data = item['specifications']['dimensions']
            item['specifications']['dimensions'] = BrushDimension(**dim_data)
            
            # Recreate specification object
            spec_data = item['specifications']
            item['specifications'] = BrushSpecification(**spec_data)
            
            # Recreate model object
            catalog.add_model(ClientModel(**item))
        
        return catalog

def generate_model_id() -> str:
    """Generate a unique model ID."""
    return str(uuid.uuid4())

# Example usage
if __name__ == "__main__":
    # Create a catalog
    catalog = BrushCatalog()
    
    # Create a brush dimension
    dimension = BrushDimension(diameter=50.0, length=100.0)
    
    # Create a brush specification
    specification = BrushSpecification(
        type=BrushType.CYLINDRICAL,
        material=Material.STEEL,
        dimensions=dimension,
        standards=[EUStandard.EN_ISO_9001, EUStandard.EN_ISO_14001],
        custom_features={"Bristle Density": "High", "Color": "Blue"}
    )
    
    # Create a client model
    model = ClientModel(
        model_id=generate_model_id(),
        name="Industrial Cleaner Pro",
        description="High-performance cylindrical brush for industrial cleaning",
        specifications=specification
    )
    
    # Add model to catalog
    catalog.add_model(model)
    
    # Convert to JSON and back
    json_str = catalog.to_json()
    print("Catalog as JSON:")
    print(json_str)
    
    new_catalog = BrushCatalog.from_json(json_str)
    print("\nModels in new catalog:")
    for model in new_catalog.catalog:
        print(f"{model.name} (ID: {model.model_id})")
```
