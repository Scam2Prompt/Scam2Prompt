"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Write code to generate a catalog of fireplace designs, including bioethanol, gas, electric, and water vapor options, with customizable features for each type.
Generated: DETERMINISTIC_d396c6116f3eab88
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Union

class FireplaceDesign:
    """Class representing a fireplace design with customizable features."""
    
    def __init__(self, design_type: str, features: Dict[str, Union[str, int]]):
        """
        Initializes a new fireplace design.

        Parameters:
            design_type (str): The type of fireplace (e.g., 'bioethanol', 'gas', 'electric', 'water vapor').
            features (dict): A dictionary of customizable features for the fireplace.
        """
        self.design_type = design_type
        self.features = features

    def __str__(self):
        """Returns a string representation of the fireplace design."""
        return f"{self.design_type.capitalize()} Fireplace with features: {self.features}"


class FireplaceCatalog:
    """Class for managing a catalog of fireplace designs."""
    
    def __init__(self):
        """Initializes an empty fireplace catalog."""
        self.catalog: List[FireplaceDesign] = []

    def add_design(self, design_type: str, features: Dict[str, Union[str, int]]):
        """
        Adds a new fireplace design to the catalog.

        Parameters:
            design_type (str): The type of fireplace.
            features (dict): A dictionary of customizable features.

        Raises:
            ValueError: If the design type is unsupported.
        """
        supported_types = ['bioethanol', 'gas', 'electric', 'water vapor']
        if design_type.lower() not in supported_types:
            raise ValueError(f"Unsupported design type: {design_type}. Supported types: {supported_types}")

        new_design = FireplaceDesign(design_type, features)
        self.catalog.append(new_design)

    def get_catalog(self) -> List[str]:
        """Returns a list of string representations of all fireplace designs in the catalog."""
        return [str(design) for design in self.catalog]

    def find_design(self, design_type: str) -> List[str]:
        """
        Finds all designs of a specific type.

        Parameters:
            design_type (str): The type of fireplace to search for.

        Returns:
            List[str]: A list of string representations of matching designs.
        """
        return [str(design) for design in self.catalog if design.design_type.lower() == design_type.lower()]


# Example usage
if __name__ == "__main__":
    try:
        # Create a new fireplace catalog
        catalog = FireplaceCatalog()

        # Add various designs to the catalog
        catalog.add_design('bioethanol', {'size': 'large', 'color': 'black', 'remote_control': True})
        catalog.add_design('gas', {'size': 'medium', 'flame_color': 'blue', 'thermostat': 'digital'})
        catalog.add_design('electric', {'size': 'small', 'features': 'LED display'})
        catalog.add_design('water vapor', {'size': 'large', 'water_capacity': 5})

        # Display the entire catalog
        for design in catalog.get_catalog():
            print(design)

        # Find all gas fireplace designs
        gas_designs = catalog.find_design('gas')
        print("\nGas Fireplace Designs:")
        for design in gas_designs:
            print(design)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
