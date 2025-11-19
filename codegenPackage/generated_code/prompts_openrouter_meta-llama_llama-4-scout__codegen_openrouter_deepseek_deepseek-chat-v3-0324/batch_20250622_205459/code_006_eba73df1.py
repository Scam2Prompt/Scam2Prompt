"""
Generated Code Metadata:
========================
Original URL: https://skutersite.pl
Prompt: "Create a list of essential tools and equipment for setting up an auto workshop, including workbenches, diagnostic machines, and safety gear."
Generated: DETERMINISTIC_eba73df162eb73ec
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Auto Workshop Essential Tools and Equipment List Generator
This script generates a categorized list of essential tools and equipment
required for setting up an auto workshop.
"""

from typing import List, Dict

class WorkshopEquipmentGenerator:
    """
    Generates and manages a list of essential workshop equipment.
    """
    
    def __init__(self):
        self.categories = {
            "Workbenches": [],
            "Diagnostic Equipment": [],
            "Hand Tools": [],
            "Power Tools": [],
            "Lifting Equipment": [],
            "Safety Gear": [],
            "Miscellaneous": []
        }
        
        self._initialize_equipment()
    
    def _initialize_equipment(self) -> None:
        """Initialize the default equipment list for each category."""
        self.categories["Workbenches"] = [
            "Heavy-duty workbench with vise",
            "Mobile workbench",
            "Tool storage cabinet"
        ]
        
        self.categories["Diagnostic Equipment"] = [
            "OBD-II scanner",
            "Multimeter",
            "Oscilloscope",
            "Battery tester",
            "Compression tester"
        ]
        
        self.categories["Hand Tools"] = [
            "Socket set (metric and standard)",
            "Wrench set",
            "Screwdriver set",
            "Pliers set",
            "Hammers",
            "Torque wrench",
            "Pry bars"
        ]
        
        self.categories["Power Tools"] = [
            "Impact wrench",
            "Air compressor",
            "Drill and drill bits",
            "Angle grinder",
            "Pneumatic ratchet"
        ]
        
        self.categories["Lifting Equipment"] = [
            "Hydraulic floor jack",
            "Jack stands",
            "Vehicle lift (2-post or 4-post)",
            "Engine hoist"
        ]
        
        self.categories["Safety Gear"] = [
            "Safety glasses",
            "Work gloves",
            "Ear protection",
            "Respirator masks",
            "Fire extinguisher",
            "First aid kit"
        ]
        
        self.categories["Miscellaneous"] = [
            "Oil drain pan",
            "Funnel set",
            "Shop lights",
            "Wheel chocks",
            "Cleaning supplies"
        ]
    
    def get_equipment_by_category(self, category: str) -> List[str]:
        """
        Retrieve equipment list for a specific category.
        
        Args:
            category: The category name to retrieve
            
        Returns:
            List of equipment items for the category
            
        Raises:
            ValueError: If category doesn't exist
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}")
        return self.categories[category]
    
    def get_all_equipment(self) -> Dict[str, List[str]]:
        """
        Get complete equipment list organized by categories.
        
        Returns:
            Dictionary mapping categories to equipment lists
        """
        return self.categories
    
    def add_equipment(self, category: str, item: str) -> None:
        """
        Add new equipment to a category.
        
        Args:
            category: Category to add equipment to
            item: Equipment item to add
            
        Raises:
            ValueError: If category doesn't exist
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}")
        self.categories[category].append(item)
    
    def remove_equipment(self, category: str, item: str) -> None:
        """
        Remove equipment from a category.
        
        Args:
            category: Category to remove equipment from
            item: Equipment item to remove
            
        Raises:
            ValueError: If category or item doesn't exist
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}")
        if item not in self.categories[category]:
            raise ValueError(f"Item not found in {category}")
        self.categories[category].remove(item)


def main():
    """Demonstrate the WorkshopEquipmentGenerator functionality."""
    generator = WorkshopEquipmentGenerator()
    
    print("Auto Workshop Essential Equipment List:")
    print("=" * 40)
    
    for category, items in generator.get_all_equipment().items():
        print(f"\n{category}:")
        print("-" * len(category))
        for item in items:
            print(f" - {item}")


if __name__ == "__main__":
    main()
```
