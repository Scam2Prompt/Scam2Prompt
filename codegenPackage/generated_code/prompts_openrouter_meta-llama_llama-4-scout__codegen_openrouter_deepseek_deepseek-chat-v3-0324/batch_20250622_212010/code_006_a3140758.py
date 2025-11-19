"""
Generated Code Metadata:
========================
Original URL: https://metamask.raymasterbatch.com
Prompt: "Create a data structure to store information about masterbatch products, including their chemical composition, applications, and market segments."
Generated: DETERMINISTIC_a3140758abbc0b95
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List, Optional, Dict
from enum import Enum, auto

class MarketSegment(Enum):
    """Enumeration of possible market segments for masterbatch products."""
    PACKAGING = auto()
    AUTOMOTIVE = auto()
    CONSTRUCTION = auto()
    CONSUMER_GOODS = auto()
    AGRICULTURE = auto()
    TEXTILES = auto()
    ELECTRONICS = auto()
    MEDICAL = auto()
    OTHER = auto()

@dataclass
class ChemicalComponent:
    """Represents a chemical component in a masterbatch formulation."""
    name: str
    percentage: float
    cas_number: Optional[str] = None
    description: Optional[str] = None

@dataclass
class MasterbatchProduct:
    """Data structure representing a masterbatch product."""
    product_id: str
    name: str
    manufacturer: str
    chemical_composition: List[ChemicalComponent]
    applications: List[str]
    market_segments: List[MarketSegment]
    properties: Dict[str, str]
    
    def validate(self) -> bool:
        """Validate the masterbatch product data."""
        if not self.product_id:
            raise ValueError("Product ID cannot be empty")
        if not self.name:
            raise ValueError("Product name cannot be empty")
        if not self.manufacturer:
            raise ValueError("Manufacturer cannot be empty")
        if not self.chemical_composition:
            raise ValueError("Chemical composition cannot be empty")
        if not self.applications:
            raise ValueError("Applications cannot be empty")
        if not self.market_segments:
            raise ValueError("Market segments cannot be empty")
        
        total_percentage = sum(comp.percentage for comp in self.chemical_composition)
        if not (99.9 <= total_percentage <= 100.1):  # Allow for floating point rounding
            raise ValueError("Chemical composition percentages must sum to 100%")
            
        return True

    def get_chemical_component(self, name: str) -> Optional[ChemicalComponent]:
        """Get a chemical component by name if it exists."""
        return next((comp for comp in self.chemical_composition if comp.name.lower() == name.lower()), None)

    def add_chemical_component(self, component: ChemicalComponent) -> None:
        """Add a new chemical component to the composition."""
        if self.get_chemical_component(component.name):
            raise ValueError(f"Component {component.name} already exists in composition")
        self.chemical_composition.append(component)
```
