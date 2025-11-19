"""
Generated Code Metadata:
========================
Original URL: https://nodoitalia.com
Prompt: Write a Python script to generate a catalog of outdoor furniture collections, including details like product names, materials (e.g., Olyna), and categories (e.g., chairs, poufs, rugs), based on the structure described on the Nodo Italia website.
Generated: DETERMINISTIC_4090b2e9de8825c6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# outdoor_furniture_catalog.py

class OutdoorFurniture:
    def __init__(self, name, material, category):
        """
        Initialize an OutdoorFurniture object.

        Args:
            name (str): Product name.
            material (str): Material used (e.g., Olyna).
            category (str): Category of furniture (e.g., chairs, poufs, rugs).
        """
        self.name = name
        self.material = material
        self.category = category

    def __repr__(self):
        return f"{self.name} ({self.material}, {self.category})"


class FurnitureCatalog:
    def __init__(self):
        """
        Initialize an empty furniture catalog.
        """
        self.collections = []

    def add_collection(self, name, material, category):
        """
        Add a new outdoor furniture collection to the catalog.

        Args:
            name (str): Product name.
            material (str): Material used (e.g., Olyna).
            category (str): Category of furniture (e.g., chairs, poufs, rugs).
        """
        new_furniture = OutdoorFurniture(name, material, category)
        self.collections.append(new_furniture)

    def get_collections(self):
        """
        Retrieve all outdoor furniture collections in the catalog.

        Returns:
            list[OutdoorFurniture]: List of OutdoorFurniture objects.
        """
        return self.collections

    def get_collections_by_category(self, category):
        """
        Retrieve outdoor furniture collections by category.

        Args:
            category (str): Category of furniture (e.g., chairs, poufs, rugs).

        Returns:
            list[OutdoorFurniture]: List of OutdoorFurniture objects in the specified category.
        """
        return [f for f in self.collections if f.category.lower() == category.lower()]


def main():
    try:
        # Create a new furniture catalog
        catalog = FurnitureCatalog()

        # Add some outdoor furniture collections
        catalog.add_collection("Garden Chair", "Olyna", "Chairs")
        catalog.add_collection("Outdoor Pouf", "Polyester", "Poufs")
        catalog.add_collection("Patio Rug", "Polypropylene", "Rugs")
        catalog.add_collection("Lounge Chair", "Olyna", "Chairs")

        # Retrieve and print all collections
        print("All Collections:")
        for collection in catalog.get_collections():
            print(collection)

        # Retrieve and print collections by category
        print("\nCollections by Category:")
        print("Chairs:")
        for chair in catalog.get_collections_by_category("Chairs"):
            print(chair)
        print("Poufs:")
        for pouf in catalog.get_collections_by_category("Poufs"):
            print(pouf)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
