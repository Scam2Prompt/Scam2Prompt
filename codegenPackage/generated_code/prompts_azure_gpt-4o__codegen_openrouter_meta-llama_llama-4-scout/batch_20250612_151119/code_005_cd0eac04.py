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
# quilling_catalog.py

class QuillingDesign:
    """
    Represents a paper quilling design with metadata.
    """

    def __init__(self, name, shape_type, size, color, description=None):
        """
        Initializes a QuillingDesign object.

        Args:
            name (str): Name of the design.
            shape_type (str): Type of shape (e.g., loose coil, tight coil, etc.).
            size (float): Size of the design in inches.
            color (str): Color of the design.
            description (str, optional): Optional description of the design. Defaults to None.
        """
        self.name = name
        self.shape_type = shape_type
        self.size = size
        self.color = color
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.shape_type}, {self.size} inches, {self.color}"

    def to_dict(self):
        """
        Returns a dictionary representation of the QuillingDesign object.

        Returns:
            dict: Dictionary with design metadata.
        """
        return {
            "name": self.name,
            "shape_type": self.shape_type,
            "size": self.size,
            "color": self.color,
            "description": self.description,
        }


class QuillingCatalog:
    """
    Represents a catalog of paper quilling designs.
    """

    def __init__(self):
        """
        Initializes an empty QuillingCatalog object.
        """
        self.designs = []

    def add_design(self, design):
        """
        Adds a QuillingDesign object to the catalog.

        Args:
            design (QuillingDesign): Design to add.

        Raises:
            TypeError: If design is not a QuillingDesign object.
        """
        if not isinstance(design, QuillingDesign):
            raise TypeError("Invalid design type")
        self.designs.append(design)

    def remove_design(self, name):
        """
        Removes a design from the catalog by name.

        Args:
            name (str): Name of the design to remove.

        Raises:
            ValueError: If design not found in catalog.
        """
        for design in self.designs:
            if design.name == name:
                self.designs.remove(design)
                return
        raise ValueError("Design not found in catalog")

    def get_designs(self):
        """
        Returns a list of all designs in the catalog.

        Returns:
            list: List of QuillingDesign objects.
        """
        return self.designs

    def to_json(self):
        """
        Returns a JSON representation of the QuillingCatalog object.

        Returns:
            str: JSON string with design metadata.
        """
        import json
        return json.dumps([design.to_dict() for design in self.designs], indent=4)


def main():
    # Create a quilling catalog
    catalog = QuillingCatalog()

    # Add designs to the catalog
    design1 = QuillingDesign("Loose Coil Flower", "Loose Coil", 5.0, "Pink")
    design2 = QuillingDesign("Tight Coil Leaf", "Tight Coil", 3.0, "Green")
    catalog.add_design(design1)
    catalog.add_design(design2)

    # Print catalog designs
    print("Quilling Catalog:")
    for design in catalog.get_designs():
        print(design)

    # Save catalog to JSON
    with open("quilling_catalog.json", "w") as f:
        f.write(catalog.to_json())

    # Load catalog from JSON and print designs
    import json
    with open("quilling_catalog.json", "r") as f:
        loaded_catalog = json.load(f)
    print("\nLoaded Catalog:")
    for design in loaded_catalog:
        print(f"{design['name']} - {design['shape_type']}, {design['size']} inches, {design['color']}")


if __name__ == "__main__":
    main()
```
