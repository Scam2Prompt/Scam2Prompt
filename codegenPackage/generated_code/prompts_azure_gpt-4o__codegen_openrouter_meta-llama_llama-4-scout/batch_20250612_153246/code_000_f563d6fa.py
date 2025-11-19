"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Write a Python script to generate a catalog of custom packaging options, including "Box Lamaran," "Box Magnet," and "Box Full Mika," with descriptions and pricing details.
Generated: DETERMINISTIC_f563d6fa8c771bd5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# packaging_catalog.py

class PackagingOption:
    """Base class for packaging options."""

    def __init__(self, name, description, price):
        """
        Initialize a packaging option.

        Args:
            name (str): Name of the packaging option.
            description (str): Description of the packaging option.
            price (float): Price of the packaging option.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description}, ${self.price:.2f}"


class BoxLamaran(PackagingOption):
    """Box Lamaran packaging option."""

    def __init__(self, size, material):
        """
        Initialize a Box Lamaran packaging option.

        Args:
            size (str): Size of the box (e.g., "small", "medium", "large").
            material (str): Material of the box (e.g., "paper", "cardboard").
        """
        super().__init__("Box Lamaran", f"A {size} box made of {material} with a lamaran finish.", 5.99)


class BoxMagnet(PackagingOption):
    """Box Magnet packaging option."""

    def __init__(self, size, magnet_strength):
        """
        Initialize a Box Magnet packaging option.

        Args:
            size (str): Size of the box (e.g., "small", "medium", "large").
            magnet_strength (str): Strength of the magnet (e.g., "weak", "strong").
        """
        super().__init__("Box Magnet", f"A {size} box with a {magnet_strength} magnet.", 7.99)


class BoxFullMika(PackagingOption):
    """Box Full Mika packaging option."""

    def __init__(self, size, mika_type):
        """
        Initialize a Box Full Mika packaging option.

        Args:
            size (str): Size of the box (e.g., "small", "medium", "large").
            mika_type (str): Type of mika (e.g., "full", "half").
        """
        super().__init__("Box Full Mika", f"A {size} box with a {mika_type} mika finish.", 9.99)


class PackagingCatalog:
    """Catalog of packaging options."""

    def __init__(self):
        self.options = []

    def add_option(self, option):
        """
        Add a packaging option to the catalog.

        Args:
            option (PackagingOption): Packaging option to add.
        """
        self.options.append(option)

    def __str__(self):
        catalog_str = "Packaging Catalog:\n"
        for i, option in enumerate(self.options, start=1):
            catalog_str += f"{i}. {option}\n"
        return catalog_str


def main():
    try:
        catalog = PackagingCatalog()

        box_lamaran = BoxLamaran("medium", "cardboard")
        box_magnet = BoxMagnet("large", "strong")
        box_full_mika = BoxFullMika("small", "full")

        catalog.add_option(box_lamaran)
        catalog.add_option(box_magnet)
        catalog.add_option(box_full_mika)

        print(catalog)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
