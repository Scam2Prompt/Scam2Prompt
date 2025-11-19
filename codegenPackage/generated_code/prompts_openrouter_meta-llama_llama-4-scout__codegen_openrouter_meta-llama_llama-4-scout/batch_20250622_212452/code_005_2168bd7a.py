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
# catalog.py

class DecorativeItem:
    """Base class for decorative items."""

    def __init__(self, name, description, price):
        """
        Initialize a decorative item.

        Args:
            name (str): Name of the item.
            description (str): Description of the item.
            price (float): Price of the item.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description}, ${self.price:.2f}"


class Cojine(DecorativeItem):
    """Class for cojines (throw pillows)."""

    def __init__(self, name, description, price, material, size):
        """
        Initialize a cojine.

        Args:
            name (str): Name of the cojine.
            description (str): Description of the cojine.
            price (float): Price of the cojine.
            material (str): Material of the cojine.
            size (str): Size of the cojine.
        """
        super().__init__(name, description, price)
        self.material = material
        self.size = size

    def __str__(self):
        return super().__str__() + f", Material: {self.material}, Size: {self.size}"


class TelaParaMuebles(DecorativeItem):
    """Class for telas para muebles (furniture fabrics)."""

    def __init__(self, name, description, price, material, width):
        """
        Initialize a tela para muebles.

        Args:
            name (str): Name of the tela.
            description (str): Description of the tela.
            price (float): Price of the tela.
            material (str): Material of the tela.
            width (float): Width of the tela in meters.
        """
        super().__init__(name, description, price)
        self.material = material
        self.width = width

    def __str__(self):
        return super().__str__() + f", Material: {self.material}, Width: {self.width} m"


class LajaDePiedraNatural(DecorativeItem):
    """Class for laja de piedra natural (natural stone slabs)."""

    def __init__(self, name, description, price, thickness, size):
        """
        Initialize a laja de piedra natural.

        Args:
            name (str): Name of the laja.
            description (str): Description of the laja.
            price (float): Price of the laja.
            thickness (float): Thickness of the laja in cm.
            size (str): Size of the laja.
        """
        super().__init__(name, description, price)
        self.thickness = thickness
        self.size = size

    def __str__(self):
        return super().__str__() + f", Thickness: {self.thickness} cm, Size: {self.size}"


class Catalog:
    """Class for a catalog of decorative items."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """
        Add an item to the catalog.

        Args:
            item (DecorativeItem): Item to add.
        """
        self.items.append(item)

    def __str__(self):
        catalog_str = "Catalog of Decorative Items:\n"
        for i, item in enumerate(self.items, start=1):
            catalog_str += f"{i}. {item}\n"
        return catalog_str


def main():
    try:
        catalog = Catalog()

        # Create cojines
        cojine1 = Cojine("Cojine Moderno", "Modern throw pillow", 20.99, "Velvet", "40x40 cm")
        cojine2 = Cojine("Cojine Rustico", "Rustic throw pillow", 15.99, "Cotton", "30x30 cm")

        # Create telas para muebles
        tela1 = TelaParaMuebles("Tela de Lino", "Linen fabric", 9.99, "Linen", 1.5)
        tela2 = TelaParaMuebles("Tela de Algodon", "Cotton fabric", 7.99, "Cotton", 2.0)

        # Create laja de piedra natural
        laja1 = LajaDePiedraNatural("Laja de Mármol", "Marble slab", 99.99, 2.0, "30x60 cm")
        laja2 = LajaDePiedraNatural("Laja de Granito", "Granite slab", 149.99, 3.0, "40x80 cm")

        # Add items to catalog
        catalog.add_item(cojine1)
        catalog.add_item(cojine2)
        catalog.add_item(tela1)
        catalog.add_item(tela2)
        catalog.add_item(laja1)
        catalog.add_item(laja2)

        # Print catalog
        print(catalog)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
