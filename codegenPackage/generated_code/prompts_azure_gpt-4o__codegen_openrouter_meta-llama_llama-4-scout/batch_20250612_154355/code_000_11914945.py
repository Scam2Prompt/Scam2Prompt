"""
Generated Code Metadata:
========================
Original URL: https://roshako.com
Prompt: Write Python code to generate a list of welding electrodes and filler metals offered by Roshako, such as ENiCrMo-3 and ERNiCr-3, and organize them by category.
Generated: DETERMINISTIC_119149453e331dec
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# welding_materials.py

class WeldingMaterial:
    """Represents a welding material with its name and category."""

    def __init__(self, name, category):
        """
        Initializes a WeldingMaterial instance.

        Args:
            name (str): The name of the welding material.
            category (str): The category of the welding material.
        """
        self.name = name
        self.category = category

    def __repr__(self):
        return f"WeldingMaterial(name='{self.name}', category='{self.category}')"


class WeldingMaterialDatabase:
    """A database of welding materials organized by category."""

    def __init__(self):
        """
        Initializes a WeldingMaterialDatabase instance.

        The database is a dictionary where the keys are categories and the values are lists of WeldingMaterial instances.
        """
        self.database = {}

    def add_material(self, material):
        """
        Adds a welding material to the database.

        Args:
            material (WeldingMaterial): The material to add.

        Raises:
            ValueError: If the material's category is not a string.
        """
        if not isinstance(material.category, str):
            raise ValueError("Material category must be a string")

        if material.category not in self.database:
            self.database[material.category] = []

        self.database[material.category].append(material)

    def get_materials_by_category(self):
        """
        Returns a dictionary of welding materials organized by category.

        Returns:
            dict: A dictionary where the keys are categories and the values are lists of WeldingMaterial instances.
        """
        return self.database


def main():
    # Create a welding material database
    database = WeldingMaterialDatabase()

    # Add welding materials to the database
    materials = [
        WeldingMaterial("ENiCrMo-3", "Nickel-based"),
        WeldingMaterial("ERNiCr-3", "Nickel-based"),
        WeldingMaterial("E308LS0", "Stainless steel"),
        WeldingMaterial("ER308LS0", "Stainless steel"),
        WeldingMaterial("E9018G", "Low-alloy steel"),
        WeldingMaterial("E71T-1", "Flux-cored"),
    ]

    for material in materials:
        database.add_material(material)

    # Get welding materials organized by category
    materials_by_category = database.get_materials_by_category()

    # Print welding materials organized by category
    for category, materials in materials_by_category.items():
        print(f"**{category}**")
        for material in materials:
            print(f"- {material.name}")
        print()


if __name__ == "__main__":
    main()
```
