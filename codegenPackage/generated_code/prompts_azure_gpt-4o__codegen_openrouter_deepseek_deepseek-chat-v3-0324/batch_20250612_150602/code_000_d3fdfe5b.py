"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Write Python code to generate a list of FSC-certified materials for a cleaning product inventory system, referencing PDC Brush's focus on sustainability.
Generated: DETERMINISTIC_d3fdfe5bb7272f44
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from enum import Enum

class FSCCertification(Enum):
    """Enum representing FSC certification types."""
    FSC_PURE = "FSC 100%"
    FSC_MIXED = "FSC Mix"
    FSC_RECYCLED = "FSC Recycled"
    NON_FSC = "Non-FSC"

class Material:
    """Class representing a material with FSC certification details."""
    
    def __init__(self, name: str, certification: FSCCertification, description: str, supplier: str = "PDC Brush"):
        """
        Initialize a material with its properties.
        
        Args:
            name: Name of the material
            certification: FSC certification type
            description: Description of the material
            supplier: Supplier name (defaults to PDC Brush)
        """
        self.name = name
        self.certification = certification
        self.description = description
        self.supplier = supplier
    
    def to_dict(self) -> Dict:
        """Convert material to dictionary for serialization."""
        return {
            "name": self.name,
            "certification": self.certification.value,
            "description": self.description,
            "supplier": self.supplier
        }

class InventoryManager:
    """Class to manage FSC-certified materials inventory."""
    
    def __init__(self):
        """Initialize with empty materials list."""
        self.materials: List[Material] = []
    
    def add_material(self, material: Material) -> None:
        """Add a material to the inventory."""
        self.materials.append(material)
    
    def get_materials_by_certification(self, certification: FSCCertification) -> List[Material]:
        """
        Get materials filtered by FSC certification.
        
        Args:
            certification: FSC certification type to filter by
            
        Returns:
            List of materials with matching certification
        """
        return [m for m in self.materials if m.certification == certification]
    
    def save_to_json(self, filename: str) -> bool:
        """
        Save materials inventory to JSON file.
        
        Args:
            filename: Name of the file to save to
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(filename, 'w') as f:
                json.dump([m.to_dict() for m in self.materials], f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving to JSON: {e}")
            return False
    
    def load_from_json(self, filename: str) -> bool:
        """
        Load materials inventory from JSON file.
        
        Args:
            filename: Name of the file to load from
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.materials = [
                    Material(
                        name=item['name'],
                        certification=FSCCertification(item['certification']),
                        description=item['description'],
                        supplier=item.get('supplier', 'PDC Brush')
                    ) for item in data
                ]
            return True
        except Exception as e:
            print(f"Error loading from JSON: {e}")
            return False

def generate_sample_materials() -> InventoryManager:
    """Generate sample FSC-certified materials for PDC Brush."""
    inventory = InventoryManager()
    
    inventory.add_material(Material(
        name="Bamboo Handle",
        certification=FSCCertification.FSC_PURE,
        description="Sustainable bamboo handle for brushes"
    ))
    
    inventory.add_material(Material(
        name="Recycled Plastic Bristles",
        certification=FSCCertification.FSC_RECYCLED,
        description="Bristles made from 100% recycled plastic"
    ))
    
    inventory.add_material(Material(
        name="Mixed Wood Base",
        certification=FSCCertification.FSC_MIXED,
        description="Wood base made from FSC-certified mixed sources"
    ))
    
    inventory.add_material(Material(
        name="Natural Fiber Bristles",
        certification=FSCCertification.FSC_PURE,
        description="Bristles made from sustainably harvested natural fibers"
    ))
    
    return inventory

if __name__ == "__main__":
    # Example usage
    inventory = generate_sample_materials()
    
    # Save to file
    inventory.save_to_json("fsc_materials.json")
    
    # Load from file
    new_inventory = InventoryManager()
    if new_inventory.load_from_json("fsc_materials.json"):
        print("Loaded materials:")
        for material in new_inventory.materials:
            print(f"- {material.name} ({material.certification.value})")
```
