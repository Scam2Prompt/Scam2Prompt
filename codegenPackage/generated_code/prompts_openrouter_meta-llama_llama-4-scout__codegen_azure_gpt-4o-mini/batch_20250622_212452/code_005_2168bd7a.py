"""
Generated Code Metadata:
========================
Original URL: https://aydinspirate.com
Prompt: "Create a catalog of decorative items, including cojines, telas para muebles, and laja de piedra natural, that could be used to enhance the aesthetic of a living room, inspired by AyD Inspirate's collections."
Generated: DETERMINISTIC_2168bd7ab7755d45
Batch ID: 20250622_212452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict

class DecorativeItem:
    """
    A class to represent a decorative item.

    Attributes:
        name (str): The name of the decorative item.
        category (str): The category of the decorative item.
        description (str): A brief description of the decorative item.
        price (float): The price of the decorative item.
    """

    def __init__(self, name: str, category: str, description: str, price: float):
        """
        Initializes a new DecorativeItem instance.

        Args:
            name (str): The name of the decorative item.
            category (str): The category of the decorative item.
            description (str): A brief description of the decorative item.
            price (float): The price of the decorative item.
        """
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def __str__(self):
        """Returns a string representation of the decorative item."""
        return f"{self.name} ({self.category}): {self.description} - ${self.price:.2f}"


class Catalog:
    """
    A class to represent a catalog of decorative items.

    Attributes:
        items (List[DecorativeItem]): A list of decorative items in the catalog.
    """

    def __init__(self):
        """Initializes an empty catalog."""
        self.items: List[DecorativeItem] = []

    def add_item(self, item: DecorativeItem):
        """
        Adds a decorative item to the catalog.

        Args:
            item (DecorativeItem): The decorative item to add.
        """
        if not isinstance(item, DecorativeItem):
            raise ValueError("Item must be an instance of DecorativeItem.")
        self.items.append(item)

    def get_items(self) -> List[Dict[str, str]]:
        """
        Returns a list of all items in the catalog.

        Returns:
            List[Dict[str, str]]: A list of dictionaries representing the decorative items.
        """
        return [self._item_to_dict(item) for item in self.items]

    @staticmethod
    def _item_to_dict(item: DecorativeItem) -> Dict[str, str]:
        """
        Converts a DecorativeItem to a dictionary.

        Args:
            item (DecorativeItem): The decorative item to convert.

        Returns:
            Dict[str, str]: A dictionary representation of the decorative item.
        """
        return {
            "name": item.name,
            "category": item.category,
            "description": item.description,
            "price": f"${item.price:.2f}"
        }


# Example usage
if __name__ == "__main__":
    # Create a catalog instance
    catalog = Catalog()

    # Define some decorative items
    items = [
        DecorativeItem("Cojín Floral", "Cojines", "Cojín con diseño floral vibrante.", 25.99),
        DecorativeItem("Tela de Algodón", "Telas para Muebles", "Tela de algodón suave y duradera.", 15.50),
        DecorativeItem("Laja de Piedra Natural", "Piedra Decorativa", "Laja de piedra natural para un toque rústico.", 45.00)
    ]

    # Add items to the catalog
    for item in items:
        catalog.add_item(item)

    # Retrieve and print all items in the catalog
    for item in catalog.get_items():
        print(item)
```
