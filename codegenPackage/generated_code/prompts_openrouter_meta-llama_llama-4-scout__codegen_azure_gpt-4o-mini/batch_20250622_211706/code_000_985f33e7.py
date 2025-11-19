"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: "What are the different types of knit fabrics used for sportswear and swimwear, and how do they differ in terms of material and application?"
Generated: DETERMINISTIC_985f33e7acaf107d
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Fabric:
    """
    A class to represent a type of fabric used in sportswear and swimwear.
    """

    def __init__(self, name, material, application):
        """
        Initializes a new Fabric instance.

        :param name: str - The name of the fabric
        :param material: str - The primary material used in the fabric
        :param application: str - The typical application of the fabric
        """
        self.name = name
        self.material = material
        self.application = application

    def __str__(self):
        """
        Returns a string representation of the Fabric instance.

        :return: str - A description of the fabric
        """
        return f"{self.name} (Material: {self.material}, Application: {self.application})"


class FabricCatalog:
    """
    A class to manage a catalog of fabrics.
    """

    def __init__(self):
        """
        Initializes a new FabricCatalog instance with an empty list of fabrics.
        """
        self.fabrics = []

    def add_fabric(self, fabric):
        """
        Adds a new fabric to the catalog.

        :param fabric: Fabric - The Fabric instance to add
        """
        if not isinstance(fabric, Fabric):
            raise ValueError("Only Fabric instances can be added.")
        self.fabrics.append(fabric)

    def list_fabrics(self):
        """
        Lists all fabrics in the catalog.

        :return: list - A list of string representations of all fabrics
        """
        return [str(fabric) for fabric in self.fabrics]


def main():
    """
    Main function to demonstrate the Fabric and FabricCatalog classes.
    """
    try:
        # Create a fabric catalog
        catalog = FabricCatalog()

        # Define different types of knit fabrics
        nylon_spandex = Fabric("Nylon-Spandex Blend", "Nylon and Spandex", "Sportswear and Swimwear")
        polyester = Fabric("Polyester", "Polyester", "Sportswear")
        lycra = Fabric("Lycra", "Lycra", "Swimwear")
        merino_wool = Fabric("Merino Wool", "Wool", "Sportswear")

        # Add fabrics to the catalog
        catalog.add_fabric(nylon_spandex)
        catalog.add_fabric(polyester)
        catalog.add_fabric(lycra)
        catalog.add_fabric(merino_wool)

        # List all fabrics in the catalog
        for fabric in catalog.list_fabrics():
            print(fabric)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
