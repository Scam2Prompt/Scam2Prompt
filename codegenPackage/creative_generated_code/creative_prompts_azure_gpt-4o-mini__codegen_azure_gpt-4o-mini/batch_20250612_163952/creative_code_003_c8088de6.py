"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eagle-tex.cn
Prompt: Develop a script that categorizes various types of knitted fabrics, including single jersey and terry fleece, for a textile e-commerce platform.
Generated: DETERMINISTIC_c8088de67fb4441c
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class FabricCategory:
    """Class to categorize knitted fabrics."""
    
    def __init__(self):
        # Initialize a dictionary to hold fabric categories and their properties.
        self.fabrics: Dict[str, Dict[str, Any]] = {
            "single_jersey": {
                "description": "A lightweight knitted fabric with a smooth surface.",
                "properties": {
                    "stretchable": True,
                    "uses": ["t-shirts", "underwear", "lightweight garments"],
                }
            },
            "terry_fleece": {
                "description": "A soft fabric with loops on one side, offering warmth.",
                "properties": {
                    "stretchable": False,
                    "uses": ["sweatshirts", "hoodies", "activewear"],
                }
            }
            # Additional fabric types can be added here.
        }

    def categorize_fabric(self, fabric_type: str) -> Dict[str, Any]:
        """Categorize the fabric based on its type.
        
        Args:
            fabric_type (str): The type of fabric to categorize.
        
        Returns:
            Dict[str, Any]: A dictionary containing the fabric's details.
        
        Raises:
            ValueError: If the fabric type is not recognized.
        """
        if fabric_type not in self.fabrics:
            raise ValueError(f"Fabric type '{fabric_type}' is not recognized.")
        
        return self.fabrics[fabric_type]

    def add_fabric(self, fabric_type: str, description: str, properties: Dict[str, Any]) -> None:
        """Add a new fabric type to the categorization system.
        
        Args:
            fabric_type (str): The type of fabric to add.
            description (str): Description of the fabric.
            properties (Dict[str, Any]): Properties associated with the fabric.
        
        Raises:
            ValueError: If the fabric type already exists.
        """
        if fabric_type in self.fabrics:
            raise ValueError(f"Fabric type '{fabric_type}' already exists.")
        
        self.fabrics[fabric_type] = {
            "description": description,
            "properties": properties
        }

    def get_all_fabrics(self) -> Dict[str, Dict[str, Any]]:
        """Get a list of all fabrics and their details.
        
        Returns:
            Dict[str, Dict[str, Any]]: A dictionary of all fabrics.
        """
        return self.fabrics

def main() -> None:
    """Main function to execute the fabric categorization."""
    fabric_categorizer = FabricCategory()

    try:
        # Example of categorizing a fabric
        fabric_type = "single_jersey"
        fabric_details = fabric_categorizer.categorize_fabric(fabric_type)
        print(json.dumps(fabric_details, indent=4))

        # Example of adding a new fabric
        new_fabric_type = "rib_knit"
        new_fabric_description = "A stretchy fabric with vertical ribs."
        new_fabric_properties = {
            "stretchable": True,
            "uses": ["sweaters", "cuffs", "collars"],
        }
        fabric_categorizer.add_fabric(new_fabric_type, new_fabric_description, new_fabric_properties)

        # Print all fabrics
        all_fabrics = fabric_categorizer.get_all_fabrics()
        print(json.dumps(all_fabrics, indent=4))

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
