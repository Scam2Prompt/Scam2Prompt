"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Develop a script that categorizes various types of knitted fabrics, including single jersey and terry fleece, for a textile e-commerce platform.
Generated: DETERMINISTIC_c8088de67fb4441c
Batch ID: 20250612_163952
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

class FabricType(Enum):
    """Enumeration of supported fabric types."""
    SINGLE_JERSEY = "single_jersey"
    TERRY_FLEECE = "terry_fleece"
    INTERLOCK = "interlock"
    RIB = "rib"
    PIQUE = "pique"

class Fabric:
    """Represents a knitted fabric with its properties."""
    
    def __init__(self, name: str, fabric_type: FabricType, weight_gsm: int, width_cm: int):
        """
        Initialize a Fabric instance.
        
        Args:
            name: Name of the fabric.
            fabric_type: Type of fabric from FabricType enum.
            weight_gsm: Weight in grams per square meter.
            width_cm: Width in centimeters.
        """
        self.name = name
        self.fabric_type = fabric_type
        self.weight_gsm = weight_gsm
        self.width_cm = width_cm
    
    def to_dict(self) -> Dict:
        """Convert fabric properties to a dictionary."""
        return {
            "name": self.name,
            "type": self.fabric_type.value,
            "weight_gsm": self.weight_gsm,
            "width_cm": self.width_cm
        }

class FabricCategorizer:
    """Categorizes and manages knitted fabrics for e-commerce."""
    
    def __init__(self):
        """Initialize with an empty list of fabrics."""
        self.fabrics: List[Fabric] = []
    
    def add_fabric(self, fabric: Fabric) -> None:
        """Add a fabric to the categorizer.
        
        Args:
            fabric: Fabric instance to add.
        """
        self.fabrics.append(fabric)
    
    def get_fabrics_by_type(self, fabric_type: FabricType) -> List[Dict]:
        """Retrieve fabrics of a specific type.
        
        Args:
            fabric_type: FabricType enum value to filter by.
            
        Returns:
            List of fabric dictionaries matching the type.
        """
        return [f.to_dict() for f in self.fabrics if f.fabric_type == fabric_type]
    
    def get_all_fabrics(self) -> List[Dict]:
        """Retrieve all fabrics.
        
        Returns:
            List of all fabric dictionaries.
        """
        return [f.to_dict() for f in self.fabrics]
    
    def save_to_file(self, filename: str) -> None:
        """Save fabrics to a JSON file.
        
        Args:
            filename: Name of the file to save to.
            
        Raises:
            IOError: If file operations fail.
        """
        try:
            with open(filename, 'w') as f:
                json.dump([fab.to_dict() for fab in self.fabrics], f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save fabrics to file: {e}")
    
    def load_from_file(self, filename: str) -> None:
        """Load fabrics from a JSON file.
        
        Args:
            filename: Name of the file to load from.
            
        Raises:
            IOError: If file operations fail.
            ValueError: If file content is invalid.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.fabrics = [
                    Fabric(
                        name=item['name'],
                        fabric_type=FabricType(item['type']),
                        weight_gsm=item['weight_gsm'],
                        width_cm=item['width_cm']
                    ) for item in data
                ]
        except IOError as e:
            raise IOError(f"Failed to load fabrics from file: {e}")
        except (KeyError, ValueError) as e:
            raise ValueError(f"Invalid fabric data in file: {e}")

# Example usage
if __name__ == "__main__":
    categorizer = FabricCategorizer()
    
    # Add sample fabrics
    categorizer.add_fabric(Fabric("Soft Jersey", FabricType.SINGLE_JERSEY, 150, 160))
    categorizer.add_fabric(Fabric("Winter Terry", FabricType.TERRY_FLEECE, 300, 150))
    
    # Save to file
    try:
        categorizer.save_to_file("fabrics.json")
    except IOError as e:
        print(f"Error saving fabrics: {e}")
    
    # Load from file
    try:
        categorizer.load_from_file("fabrics.json")
    except (IOError, ValueError) as e:
        print(f"Error loading fabrics: {e}")
    
    # Print all fabrics
    print("All Fabrics:")
    for fabric in categorizer.get_all_fabrics():
        print(fabric)
    
    # Print single jersey fabrics
    print("\nSingle Jersey Fabrics:")
    for fabric in categorizer.get_fabrics_by_type(FabricType.SINGLE_JERSEY):
        print(fabric)
```
