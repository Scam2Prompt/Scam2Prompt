"""
Generated Code Metadata:
========================
Original URL: https://etherofficial.com
Prompt: "Design a summer clothing collection using recycled polyester and eco-friendly fabrics, with a focus on sustainable fashion practices."
Generated: DETERMINISTIC_cf708fa3d4179fb1
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# summer_clothing_collection.py

class ClothingItem:
    """Represents a clothing item in the summer collection."""

    def __init__(self, name, fabric, color, size):
        """
        Initializes a ClothingItem.

        Args:
            name (str): The name of the clothing item.
            fabric (str): The fabric used for the clothing item.
            color (str): The color of the clothing item.
            size (str): The size of the clothing item.
        """
        self.name = name
        self.fabric = fabric
        self.color = color
        self.size = size

    def __str__(self):
        return f"{self.name} - {self.fabric}, {self.color}, {self.size}"


class SummerCollection:
    """Represents a summer clothing collection."""

    def __init__(self):
        """Initializes an empty summer collection."""
        self.items = []

    def add_item(self, item):
        """
        Adds a clothing item to the collection.

        Args:
            item (ClothingItem): The item to add.

        Raises:
            ValueError: If the item is not made from recycled polyester or eco-friendly fabrics.
        """
        if item.fabric.lower() not in ["recycled polyester", "eco-friendly fabrics"]:
            raise ValueError("Item must be made from recycled polyester or eco-friendly fabrics")
        self.items.append(item)

    def remove_item(self, item_name):
        """
        Removes a clothing item from the collection.

        Args:
            item_name (str): The name of the item to remove.

        Raises:
            ValueError: If the item is not found in the collection.
        """
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return
        raise ValueError("Item not found in collection")

    def __str__(self):
        collection_str = "Summer Clothing Collection:\n"
        for item in self.items:
            collection_str += f"- {item}\n"
        return collection_str


def main():
    try:
        collection = SummerCollection()

        # Add items to the collection
        collection.add_item(ClothingItem("T-Shirt", "Recycled Polyester", "Blue", "Medium"))
        collection.add_item(ClothingItem("Shorts", "Eco-friendly Fabrics", "Green", "Large"))
        collection.add_item(ClothingItem("Dress", "Recycled Polyester", "Yellow", "Small"))

        # Print the collection
        print(collection)

        # Remove an item from the collection
        collection.remove_item("Shorts")

        # Print the updated collection
        print("\nUpdated Collection:")
        print(collection)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
