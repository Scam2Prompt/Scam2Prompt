"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Write a Python code to generate a catalog for a custom box packaging company like Box Creatived Semarang.
Generated: DETERMINISTIC_a1a9bbff45843c5f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# catalog_generator.py

class Box:
    def __init__(self, box_id, name, length, width, height, material, price):
        """
        Initialize a Box object.

        Args:
            box_id (int): Unique identifier for the box.
            name (str): Name of the box.
            length (float): Length of the box in cm.
            width (float): Width of the box in cm.
            height (float): Height of the box in cm.
            material (str): Material used to make the box.
            price (float): Price of the box in IDR.
        """
        self.box_id = box_id
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.material = material
        self.price = price

    def __str__(self):
        return f"Box {self.box_id}: {self.name}"


class Catalog:
    def __init__(self):
        """
        Initialize an empty catalog.
        """
        self.boxes = []

    def add_box(self, box):
        """
        Add a box to the catalog.

        Args:
            box (Box): Box object to add.
        """
        self.boxes.append(box)

    def remove_box(self, box_id):
        """
        Remove a box from the catalog by its ID.

        Args:
            box_id (int): ID of the box to remove.

        Raises:
            ValueError: If the box is not found in the catalog.
        """
        for box in self.boxes:
            if box.box_id == box_id:
                self.boxes.remove(box)
                return
        raise ValueError("Box not found in catalog")

    def generate_catalog(self):
        """
        Generate a string representation of the catalog.

        Returns:
            str: String representation of the catalog.
        """
        catalog_str = "Box Catalog:\n"
        for box in self.boxes:
            catalog_str += f"  - {box}\n"
            catalog_str += f"    Dimensions: {box.length} x {box.width} x {box.height} cm\n"
            catalog_str += f"    Material: {box.material}\n"
            catalog_str += f"    Price: {box.price} IDR\n\n"
        return catalog_str


def main():
    try:
        catalog = Catalog()

        # Create boxes
        box1 = Box(1, "Small Box", 10, 10, 5, "Corrugated Cardboard", 5000)
        box2 = Box(2, "Medium Box", 20, 15, 10, "Corrugated Cardboard", 10000)
        box3 = Box(3, "Large Box", 30, 20, 15, "Corrugated Cardboard", 15000)

        # Add boxes to catalog
        catalog.add_box(box1)
        catalog.add_box(box2)
        catalog.add_box(box3)

        # Generate and print catalog
        print(catalog.generate_catalog())

        # Remove a box from catalog
        catalog.remove_box(2)

        # Generate and print updated catalog
        print("\nUpdated Catalog:")
        print(catalog.generate_catalog())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
