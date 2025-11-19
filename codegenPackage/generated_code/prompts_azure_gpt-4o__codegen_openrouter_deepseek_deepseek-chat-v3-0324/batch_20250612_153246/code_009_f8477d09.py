"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: Create a Python program to simulate the design of a custom deck, incorporating features like size, material, and style options inspired by "The Fence Guys" services.
Generated: DETERMINISTIC_f8477d090add7fb0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional

class Material(Enum):
    """Enum representing different deck materials."""
    PRESSURE_TREATED = "Pressure Treated Wood"
    CEDAR = "Cedar"
    COMPOSITE = "Composite"
    PVC = "PVC"
    REDWOOD = "Redwood"

class Style(Enum):
    """Enum representing different deck styles."""
    TRADITIONAL = "Traditional"
    MODERN = "Modern"
    RUSTIC = "Rustic"
    TROPICAL = "Tropical"
    MEDITERRANEAN = "Mediterranean"

class Railing(Enum):
    """Enum representing different railing options."""
    NONE = "None"
    WOOD = "Wood"
    METAL = "Metal"
    GLASS = "Glass"
    CABLE = "Cable"

class DeckDesign:
    """Class representing a custom deck design."""
    
    def __init__(
        self,
        length: float,
        width: float,
        material: Material,
        style: Style,
        railing: Railing = Railing.NONE,
        features: Optional[List[str]] = None
    ):
        """
        Initialize a deck design with given parameters.
        
        Args:
            length: Length of the deck in feet.
            width: Width of the deck in feet.
            material: Material of the deck.
            style: Style of the deck.
            railing: Railing option (default: None).
            features: List of additional features (default: None).
        """
        self.length = length
        self.width = width
        self.material = material
        self.style = style
        self.railing = railing
        self.features = features if features else []
    
    @property
    def area(self) -> float:
        """Calculate the area of the deck in square feet."""
        return self.length * self.width
    
    def add_feature(self, feature: str) -> None:
        """Add a feature to the deck design."""
        self.features.append(feature)
    
    def remove_feature(self, feature: str) -> None:
        """Remove a feature from the deck design if it exists."""
        if feature in self.features:
            self.features.remove(feature)
    
    def to_dict(self) -> Dict:
        """Convert the deck design to a dictionary."""
        return {
            "length": self.length,
            "width": self.width,
            "area": self.area,
            "material": self.material.value,
            "style": self.style.value,
            "railing": self.railing.value,
            "features": self.features
        }
    
    def __str__(self) -> str:
        """Return a string representation of the deck design."""
        return json.dumps(self.to_dict(), indent=2)

class DeckDesigner:
    """Class to simulate a deck designer application."""
    
    def __init__(self):
        """Initialize the deck designer with empty designs."""
        self.designs: List[DeckDesign] = []
    
    def create_design(
        self,
        length: float,
        width: float,
        material: Material,
        style: Style,
        railing: Railing = Railing.NONE,
        features: Optional[List[str]] = None
    ) -> DeckDesign:
        """
        Create a new deck design and add it to the collection.
        
        Args:
            length: Length of the deck in feet.
            width: Width of the deck in feet.
            material: Material of the deck.
            style: Style of the deck.
            railing: Railing option (default: None).
            features: List of additional features (default: None).
            
        Returns:
            The created DeckDesign object.
        """
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        
        design = DeckDesign(length, width, material, style, railing, features)
        self.designs.append(design)
        return design
    
    def get_design(self, index: int) -> DeckDesign:
        """
        Get a deck design by index.
        
        Args:
            index: Index of the design to retrieve.
            
        Returns:
            The DeckDesign object at the specified index.
            
        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self.designs):
            raise IndexError("Design index out of range.")
        return self.designs[index]
    
    def list_designs(self) -> List[Dict]:
        """List all deck designs as dictionaries."""
        return [design.to_dict() for design in self.designs]
    
    def save_designs(self, filename: str) -> None:
        """
        Save all deck designs to a JSON file.
        
        Args:
            filename: Name of the file to save to.
            
        Raises:
            IOError: If there's an issue writing to the file.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.list_designs(), f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save designs: {e}")
    
    def load_designs(self, filename: str) -> None:
        """
        Load deck designs from a JSON file.
        
        Args:
            filename: Name of the file to load from.
            
        Raises:
            IOError: If there's an issue reading the file.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.designs.clear()
                for item in data:
                    design = DeckDesign(
                        length=item['length'],
                        width=item['width'],
                        material=Material(item['material']),
                        style=Style(item['style']),
                        railing=Railing(item['railing']),
                        features=item['features']
                    )
                    self.designs.append(design)
        except IOError as e:
            raise IOError(f"Failed to load designs: {e}")
        except (KeyError, ValueError) as e:
            raise ValueError(f"Invalid data in file: {e}")

def main():
    """Main function to demonstrate the deck designer."""
    designer = DeckDesigner()
    
    # Create some sample designs
    design1 = designer.create_design(
        length=20,
        width=15,
        material=Material.CEDAR,
        style=Style.TRADITIONAL,
        railing=Railing.WOOD,
        features=["Built-in seating", "Pergola"]
    )
    
    design2 = designer.create_design(
        length=25,
        width=12,
        material=Material.COMPOSITE,
        style=Style.MODERN,
        railing=Railing.GLASS,
        features=["Outdoor kitchen", "Fire pit"]
    )
    
    # Print all designs
    print("All Deck Designs:")
    for i, design in enumerate(designer.list_designs()):
        print(f"Design {i + 1}:")
        print(json.dumps(design, indent=2))
    
    # Save designs to a file
    try:
        designer.save_designs("deck_designs.json")
        print("\nDesigns saved to 'deck_designs.json'")
    except IOError as e:
        print(f"Error saving designs: {e}")

if __name__ == "__main__":
    main()
```
