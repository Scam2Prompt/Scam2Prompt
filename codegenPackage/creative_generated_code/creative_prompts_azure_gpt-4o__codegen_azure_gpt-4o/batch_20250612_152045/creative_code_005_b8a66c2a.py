"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vircomem.ro
Prompt: Write code to generate a catalog of industrial brushes with customizable features, including EU-standardized dimensions and client-specific models, as detailed on the VIRCOMEM website.
Generated: DETERMINISTIC_b8a66c2a9b29be2e
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class BrushCatalog:
    """
    A class to generate a catalog of industrial brushes with customizable features.
    Includes EU-standardized dimensions and client-specific models.
    """

    def __init__(self):
        # Initialize the catalog with an empty list to store brush models
        self.catalog = []

    def add_standard_brush(self, name, dimensions):
        """
        Adds a brush with EU-standardized dimensions to the catalog.
        
        :param name: str - Name of the brush model
        :param dimensions: dict - Dictionary containing standardized dimensions (e.g., length, width, diameter)
        """
        if not self._validate_dimensions(dimensions):
            raise ValueError("Invalid dimensions. Dimensions must contain positive numeric values.")
        brush = {
            "name": name,
            "type": "standard",
            "dimensions": dimensions
        }
        self.catalog.append(brush)

    def add_client_specific_brush(self, name, client_requirements):
        """
        Adds a client-specific brush model to the catalog.
        
        :param name: str - Name of the brush model
        :param client_requirements: dict - Dictionary containing client-specific requirements (e.g., material, design)
        """
        if not client_requirements or not isinstance(client_requirements, dict):
            raise ValueError("Client requirements must be a valid dictionary.")
        brush = {
            "name": name,
            "type": "client-specific",
            "client_requirements": client_requirements
        }
        self.catalog.append(brush)

    def _validate_dimensions(self, dimensions):
        """
        Private method to validate brush dimensions.
        
        :param dimensions: dict - Dictionary containing dimensions
        :return: bool - True if valid, False otherwise
        """
        return all(isinstance(value, (int, float)) and value > 0 for value in dimensions.values())

    def export_catalog(self, file_path="brush_catalog.json"):
        """
        Exports the brush catalog to a JSON file.
        
        :param file_path: str - Path to the exported JSON file
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.catalog, file, indent=4)
            print(f"Catalog successfully exported to {file_path}")
        except IOError as e:
            print(f"Error exporting the catalog: {e}")

    def display_catalog(self):
        """
        Prints the catalog to the console in a readable format.
        """
        print(json.dumps(self.catalog, indent=4))


# Example usage
if __name__ == "__main__":
    # Create an instance of the BrushCatalog class
    catalog = BrushCatalog()

    # Add brushes with standardized dimensions
    try:
        catalog.add_standard_brush("EU Brush Model 1", {"length": 100, "width": 50, "diameter": 25})
        catalog.add_standard_brush("EU Brush Model 2", {"length": 120, "width": 60, "diameter": 30})
    except ValueError as e:
        print(f"Error adding standard brush: {e}")

    # Add client-specific brushes
    try:
        catalog.add_client_specific_brush("Custom Brush A", {"material": "nylon", "design": "spiral"})
        catalog.add_client_specific_brush("Custom Brush B", {"material": "steel", "design": "cylindrical"})
    except ValueError as e:
        print(f"Error adding client-specific brush: {e}")

    # Export the catalog to a JSON file
    catalog.export_catalog()

    # Display the catalog in the console
    catalog.display_catalog()
```
