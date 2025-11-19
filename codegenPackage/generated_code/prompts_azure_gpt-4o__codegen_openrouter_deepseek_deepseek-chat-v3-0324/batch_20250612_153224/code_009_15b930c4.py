"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Provide code to filter Yanmar spare parts (e.g., filters, pistons, alternators) based on compatibility with specific mini excavator models like ViO12, ViO17, ViO25, ViO35, and SV100.
Generated: DETERMINISTIC_15b930c48cc95c86
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class YanmarSparePart:
    """
    Represents a Yanmar spare part with its compatibility information.
    """
    def __init__(self, part_id: str, name: str, description: str, compatible_models: list):
        """
        Initialize a Yanmar spare part.
        
        Args:
            part_id (str): Unique identifier for the part
            name (str): Name of the part (e.g., "Oil Filter")
            description (str): Description of the part
            compatible_models (list): List of compatible excavator models
        """
        self.part_id = part_id
        self.name = name
        self.description = description
        self.compatible_models = compatible_models

    def is_compatible(self, model: str) -> bool:
        """
        Check if this part is compatible with the specified model.
        
        Args:
            model (str): Excavator model to check compatibility with
            
        Returns:
            bool: True if compatible, False otherwise
        """
        return model in self.compatible_models


class YanmarPartsCatalog:
    """
    Catalog of Yanmar spare parts with filtering capabilities.
    """
    def __init__(self):
        """Initialize an empty parts catalog."""
        self.parts = []

    def add_part(self, part: YanmarSparePart) -> None:
        """
        Add a part to the catalog.
        
        Args:
            part (YanmarSparePart): Part to add to the catalog
        """
        if not isinstance(part, YanmarSparePart):
            raise ValueError("Only YanmarSparePart objects can be added to the catalog")
        self.parts.append(part)

    def filter_by_model(self, model: str) -> list:
        """
        Filter parts by compatible excavator model.
        
        Args:
            model (str): Model to filter by (e.g., "ViO12")
            
        Returns:
            list: List of compatible YanmarSparePart objects
            
        Raises:
            ValueError: If model is empty or None
        """
        if not model:
            raise ValueError("Model cannot be empty or None")
            
        return [part for part in self.parts if part.is_compatible(model)]

    def filter_by_name(self, name: str) -> list:
        """
        Filter parts by name (case-insensitive partial match).
        
        Args:
            name (str): Name to search for
            
        Returns:
            list: List of matching YanmarSparePart objects
            
        Raises:
            ValueError: If name is empty or None
        """
        if not name:
            raise ValueError("Name cannot be empty or None")
            
        name_lower = name.lower()
        return [part for part in self.parts if name_lower in part.name.lower()]


# Example usage
if __name__ == "__main__":
    # Create a catalog
    catalog = YanmarPartsCatalog()
    
    # Add some sample parts
    catalog.add_part(YanmarSparePart(
        "F1234",
        "Oil Filter",
        "High-performance oil filter for mini excavators",
        ["ViO12", "ViO17", "ViO25"]
    ))
    
    catalog.add_part(YanmarSparePart(
        "P5678",
        "Piston Kit",
        "Complete piston kit for SV100 models",
        ["SV100"]
    ))
    
    catalog.add_part(YanmarSparePart(
        "A9012",
        "Alternator",
        "Heavy-duty alternator for ViO35",
        ["ViO35"]
    ))
    
    # Filter parts by model
    compatible_parts = catalog.filter_by_model("ViO17")
    print(f"Parts compatible with ViO17: {[p.name for p in compatible_parts]}")
    
    # Filter parts by name
    filter_parts = catalog.filter_by_name("filter")
    print(f"Parts containing 'filter': {[p.name for p in filter_parts]}")
```
