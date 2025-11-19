"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: "List the different types of pigments and additives offered by M J PIGMENT & ADDITIVES PVT. LTD. for the plastics industry."
Generated: DETERMINISTIC_5872f9be60e2783f
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class PigmentAdditive:
    """
    Represents a pigment or additive offered by M J PIGMENT & ADDITIVES PVT. LTD.
    """
    def __init__(self, name: str, category: str, description: str, applications: List[str]):
        self.name = name
        self.category = category
        self.description = description
        self.applications = applications

    def to_dict(self) -> Dict:
        """Convert the PigmentAdditive object to a dictionary."""
        return {
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'applications': self.applications
        }

class PigmentAdditiveCatalog:
    """
    Catalog of pigments and additives offered by M J PIGMENT & ADDITIVES PVT. LTD.
    """
    def __init__(self):
        self.pigments_additives = []
        self._initialize_catalog()

    def _initialize_catalog(self):
        """Initialize the catalog with sample data."""
        # Note: In a real application, this would likely come from a database
        self.pigments_additives = [
            PigmentAdditive(
                name="Organic Pigments",
                category="Pigment",
                description="High-performance organic pigments for vibrant colors",
                applications=["Plastic films", "Injection molding", "Blow molding"]
            ),
            PigmentAdditive(
                name="Inorganic Pigments",
                category="Pigment",
                description="Durable inorganic pigments for long-lasting color",
                applications=["PVC pipes", "Automotive parts", "Construction materials"]
            ),
            PigmentAdditive(
                name="Masterbatches",
                category="Additive",
                description="Concentrated color and additive mixtures",
                applications=["Packaging", "Consumer goods", "Industrial products"]
            ),
            PigmentAdditive(
                name="UV Stabilizers",
                category="Additive",
                description="Protects against UV degradation",
                applications=["Outdoor furniture", "Automotive exteriors", "Construction materials"]
            ),
            PigmentAdditive(
                name="Antioxidants",
                category="Additive",
                description="Prevents oxidative degradation",
                applications=["Food packaging", "Medical devices", "Electrical components"]
            ),
            PigmentAdditive(
                name="Flame Retardants",
                category="Additive",
                description="Enhances fire resistance",
                applications=["Electronics housing", "Building materials", "Transportation"]
            )
        ]

    def get_all_pigments_additives(self) -> List[Dict]:
        """Return all pigments and additives in the catalog."""
        return [item.to_dict() for item in self.pigments_additives]

    def get_by_category(self, category: str) -> List[Dict]:
        """
        Get pigments/additives by category.
        
        Args:
            category: The category to filter by ('Pigment' or 'Additive')
        
        Returns:
            List of matching pigments/additives
            
        Raises:
            ValueError: If category is not 'Pigment' or 'Additive'
        """
        if category not in ['Pigment', 'Additive']:
            raise ValueError("Category must be either 'Pigment' or 'Additive'")
            
        return [item.to_dict() for item in self.pigments_additives 
                if item.category == category]

    def save_to_json(self, filename: str):
        """
        Save the catalog to a JSON file.
        
        Args:
            filename: The name of the file to save to
            
        Raises:
            IOError: If there's an issue writing the file
        """
        try:
            with open(filename, 'w') as f:
                json.dump([item.to_dict() for item in self.pigments_additives], f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save catalog: {str(e)}")

def main():
    """Example usage of the PigmentAdditiveCatalog."""
    catalog = PigmentAdditiveCatalog()
    
    print("All Pigments and Additives:")
    for item in catalog.get_all_pigments_additives():
        print(f"- {item['name']} ({item['category']})")
    
    print("\nPigments Only:")
    for item in catalog.get_by_category('Pigment'):
        print(f"- {item['name']}")
    
    print("\nAdditives Only:")
    for item in catalog.get_by_category('Additive'):
        print(f"- {item['name']}")
    
    try:
        catalog.save_to_json("pigments_additives_catalog.json")
        print("\nCatalog saved to pigments_additives_catalog.json")
    except IOError as e:
        print(f"Error saving catalog: {e}")

if __name__ == "__main__":
    main()
```
