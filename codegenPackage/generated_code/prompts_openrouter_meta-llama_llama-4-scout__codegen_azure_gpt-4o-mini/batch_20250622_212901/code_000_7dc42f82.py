"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: What are the different types of materials used for large-format printing, and how do they compare in terms of durability and application?
Generated: DETERMINISTIC_7dc42f82d0fd51c3
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Material:
    """
    A class to represent a printing material.
    """

    def __init__(self, name, durability, application):
        """
        Initializes a new Material instance.

        :param name: str - The name of the material
        :param durability: str - The durability level of the material
        :param application: str - The common applications of the material
        """
        self.name = name
        self.durability = durability
        self.application = application

    def __str__(self):
        """
        Returns a string representation of the Material instance.

        :return: str - A formatted string with material details
        """
        return f"Material: {self.name}, Durability: {self.durability}, Application: {self.application}"


class MaterialComparison:
    """
    A class to compare different printing materials.
    """

    def __init__(self):
        """
        Initializes a new MaterialComparison instance with an empty list of materials.
        """
        self.materials = []

    def add_material(self, material):
        """
        Adds a new material to the comparison list.

        :param material: Material - An instance of the Material class
        """
        if not isinstance(material, Material):
            raise ValueError("Only instances of Material can be added.")
        self.materials.append(material)

    def compare_materials(self):
        """
        Compares the materials based on their durability and application.

        :return: list - A list of strings representing each material's details
        """
        if not self.materials:
            raise ValueError("No materials to compare.")
        return [str(material) for material in self.materials]


def main():
    """
    Main function to demonstrate the material comparison.
    """
    try:
        # Create instances of different materials
        vinyl = Material("Vinyl", "High", "Banners, Signage")
        canvas = Material("Canvas", "Medium", "Art Prints, Wall Decor")
        paper = Material("Paper", "Low", "Posters, Flyers")

        # Initialize the material comparison
        comparison = MaterialComparison()

        # Add materials to the comparison
        comparison.add_material(vinyl)
        comparison.add_material(canvas)
        comparison.add_material(paper)

        # Compare materials and print the results
        results = comparison.compare_materials()
        for result in results:
            print(result)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
