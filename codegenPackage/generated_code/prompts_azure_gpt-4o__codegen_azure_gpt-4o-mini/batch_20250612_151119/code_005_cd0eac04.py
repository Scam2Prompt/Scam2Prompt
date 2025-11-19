"""
Generated Code Metadata:
========================
Original URL: https://quilling.xii.jp
Prompt: Write code to generate a catalog of paper quilling designs, including metadata like shape type, size, and color, for organizing workshop materials as described on ペーパークイリング カントリーフレンズ.
Generated: DETERMINISTIC_cd0eac046b1ac6b2
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class QuillingDesign:
    """
    A class to represent a paper quilling design.

    Attributes:
        shape_type (str): The type of shape (e.g., flower, animal).
        size (str): The size of the design (e.g., small, medium, large).
        color (str): The primary color of the design.
        description (str): A brief description of the design.
    """

    def __init__(self, shape_type: str, size: str, color: str, description: str):
        self.shape_type = shape_type
        self.size = size
        self.color = color
        self.description = description

    def to_dict(self) -> Dict[str, Any]:
        """Convert the QuillingDesign instance to a dictionary."""
        return {
            "shape_type": self.shape_type,
            "size": self.size,
            "color": self.color,
            "description": self.description
        }

class QuillingCatalog:
    """
    A class to manage a catalog of paper quilling designs.

    Attributes:
        designs (List[QuillingDesign]): A list of quilling designs in the catalog.
    """

    def __init__(self):
        self.designs: List[QuillingDesign] = []

    def add_design(self, design: QuillingDesign) -> None:
        """Add a new design to the catalog."""
        self.designs.append(design)

    def remove_design(self, shape_type: str) -> bool:
        """Remove a design from the catalog by shape type.

        Args:
            shape_type (str): The shape type of the design to remove.

        Returns:
            bool: True if the design was removed, False if not found.
        """
        for design in self.designs:
            if design.shape_type == shape_type:
                self.designs.remove(design)
                return True
        return False

    def save_to_file(self, filename: str) -> None:
        """Save the catalog to a JSON file.

        Args:
            filename (str): The name of the file to save the catalog to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([design.to_dict() for design in self.designs], file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the catalog from a JSON file.

        Args:
            filename (str): The name of the file to load the catalog from.
        """
        try:
            with open(filename, 'r') as file:
                designs_data = json.load(file)
                self.designs = [QuillingDesign(**data) for data in designs_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    catalog = QuillingCatalog()
    
    # Adding designs to the catalog
    catalog.add_design(QuillingDesign("Flower", "Medium", "Red", "A beautiful red flower design."))
    catalog.add_design(QuillingDesign("Animal", "Small", "Blue", "A cute blue bird design."))
    
    # Saving the catalog to a file
    catalog.save_to_file("quilling_catalog.json")
    
    # Loading the catalog from a file
    catalog.load_from_file("quilling_catalog.json")
    
    # Removing a design
    if catalog.remove_design("Flower"):
        print("Design removed successfully.")
    else:
        print("Design not found.")
```
