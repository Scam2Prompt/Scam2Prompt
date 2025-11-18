"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quilling.xii.jp
Prompt: Write code to generate a catalog of paper quilling designs, including metadata like shape type, size, and color, for organizing workshop materials as described on ペーパークイリング カントリーフレンズ.
Generated: DETERMINISTIC_cd0eac046b1ac6b2
Batch ID: 20250612_151119
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

class QuillingDesign:
    """
    A class to represent a paper quilling design with its metadata.
    """

    def __init__(self, name: str, shape_type: str, size: str, color: str):
        """
        Initializes a new instance of QuillingDesign.

        Parameters:
        name (str): The name of the design.
        shape_type (str): The type of shape (e.g., flower, animal).
        size (str): The size of the design (e.g., small, medium, large).
        color (str): The primary color used in the design.
        """
        self.name = name
        self.shape_type = shape_type
        self.size = size
        self.color = color

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the QuillingDesign instance to a dictionary.

        Returns:
        dict: A dictionary representation of the quilling design.
        """
        return {
            "name": self.name,
            "shape_type": self.shape_type,
            "size": self.size,
            "color": self.color
        }

class QuillingCatalog:
    """
    A class to manage a catalog of paper quilling designs.
    """

    def __init__(self):
        """
        Initializes an empty catalog for storing quilling designs.
        """
        self.designs: List[QuillingDesign] = []

    def add_design(self, design: QuillingDesign):
        """
        Adds a quilling design to the catalog.

        Parameters:
        design (QuillingDesign): The quilling design to add.
        """
        self.designs.append(design)

    def remove_design(self, name: str):
        """
        Removes a quilling design from the catalog by name.

        Parameters:
        name (str): The name of the design to remove.

        Raises:
        ValueError: If design with the given name does not exist.
        """
        for design in self.designs:
            if design.name == name:
                self.designs.remove(design)
                return
        raise ValueError(f"Design with name '{name}' not found in catalog.")

    def export_catalog(self, file_path: str):
        """
        Exports the catalog to a JSON file.

        Parameters:
        file_path (str): The path where the JSON file will be saved.

        Raises:
        IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump([design.to_dict() for design in self.designs], file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    def load_catalog(self, file_path: str):
        """
        Loads the catalog from a JSON file.

        Parameters:
        file_path (str): The path from which the JSON file will be read.

        Raises:
        IOError: If there is an issue reading the file.
        ValueError: If the file does not contain valid JSON.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                designs = json.load(file)
                for design in designs:
                    self.add_design(QuillingDesign(design['name'], design['shape_type'], design['size'], design['color']))
        except IOError as e:
            print(f"An error occurred while reading the file: {e}")
        except ValueError as e:
            print(f"Invalid JSON format: {e}")

# Example usage:
if __name__ == "__main__":
    # Create a catalog instance
    catalog = QuillingCatalog()
    
    # Add some designs to the catalog
    catalog.add_design(QuillingDesign("Flower", "Flower", "Medium", "Red"))
    catalog.add_design(QuillingDesign("Butterfly", "Animal", "Small", "Blue"))
    
    # Export the catalog to a JSON file
    catalog.export_catalog("quilling_catalog.json")
    
    # Load the catalog from the JSON file
    new_catalog = QuillingCatalog()
    new_catalog.load_catalog("quilling_catalog.json")
```
