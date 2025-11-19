"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: Create a Python script to compare the mechanical properties of treated eucalyptus wood versus untreated native woods, as discussed on Trattar Madeiras' website.
Generated: DETERMINISTIC_516095e6529a8da3
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wood_comparator.py

class WoodProperties:
    """Represents the mechanical properties of a wood type."""

    def __init__(self, name, density, compressive_strength, tensile_strength, flexural_strength):
        """
        Initializes a WoodProperties instance.

        Args:
            name (str): The name of the wood type.
            density (float): The density of the wood in kg/m³.
            compressive_strength (float): The compressive strength of the wood in MPa.
            tensile_strength (float): The tensile strength of the wood in MPa.
            flexural_strength (float): The flexural strength of the wood in MPa.
        """
        self.name = name
        self.density = density
        self.compressive_strength = compressive_strength
        self.tensile_strength = tensile_strength
        self.flexural_strength = flexural_strength


class WoodComparator:
    """Compares the mechanical properties of different wood types."""

    def __init__(self):
        self.wood_properties = {}

    def add_wood_properties(self, wood_properties):
        """
        Adds the mechanical properties of a wood type.

        Args:
            wood_properties (WoodProperties): The mechanical properties of the wood type.
        """
        self.wood_properties[wood_properties.name] = wood_properties

    def compare_properties(self, property_name):
        """
        Compares the specified mechanical property of all wood types.

        Args:
            property_name (str): The name of the property to compare (density, compressive_strength, tensile_strength, flexural_strength).

        Returns:
            dict: A dictionary with the wood type names as keys and their corresponding property values as values.

        Raises:
            ValueError: If the specified property name is not valid.
        """
        valid_properties = ["density", "compressive_strength", "tensile_strength", "flexural_strength"]
        if property_name not in valid_properties:
            raise ValueError("Invalid property name")

        return {name: getattr(properties, property_name) for name, properties in self.wood_properties.items()}

    def print_comparison(self, property_name):
        """
        Prints a comparison of the specified mechanical property of all wood types.

        Args:
            property_name (str): The name of the property to compare.
        """
        try:
            comparison = self.compare_properties(property_name)
            print(f"Comparison of {property_name}:")
            for wood, value in comparison.items():
                print(f"{wood}: {value}")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    comparator = WoodComparator()

    # Treated eucalyptus wood properties (example values)
    treated_eucalyptus = WoodProperties(
        "Treated Eucalyptus",
        density=600,
        compressive_strength=30,
        tensile_strength=50,
        flexural_strength=40,
    )

    # Untreated native wood properties (example values)
    untreated_native_wood1 = WoodProperties(
        "Untreated Native Wood 1",
        density=500,
        compressive_strength=25,
        tensile_strength=40,
        flexural_strength=35,
    )

    untreated_native_wood2 = WoodProperties(
        "Untreated Native Wood 2",
        density=550,
        compressive_strength=28,
        tensile_strength=45,
        flexural_strength=38,
    )

    comparator.add_wood_properties(treated_eucalyptus)
    comparator.add_wood_properties(untreated_native_wood1)
    comparator.add_wood_properties(untreated_native_wood2)

    comparator.print_comparison("density")
    comparator.print_comparison("compressive_strength")
    comparator.print_comparison("tensile_strength")
    comparator.print_comparison("flexural_strength")


if __name__ == "__main__":
    main()
```
