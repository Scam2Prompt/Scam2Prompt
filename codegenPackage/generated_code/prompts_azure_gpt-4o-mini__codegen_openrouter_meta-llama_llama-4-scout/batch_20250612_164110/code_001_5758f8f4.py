"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: Generate a Python script that evaluates the mechanical properties of eucalyptus and pine wood, highlighting their advantages for construction projects.
Generated: DETERMINISTIC_5758f8f4c1af5ea8
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wood_properties_evaluator.py

class WoodProperties:
    def __init__(self, name, density, compressive_strength, tensile_strength, flexural_strength):
        """
        Initialize wood properties.

        Args:
            name (str): Wood type name.
            density (float): Density in kg/m^3.
            compressive_strength (float): Compressive strength in MPa.
            tensile_strength (float): Tensile strength in MPa.
            flexural_strength (float): Flexural strength in MPa.
        """
        self.name = name
        self.density = density
        self.compressive_strength = compressive_strength
        self.tensile_strength = tensile_strength
        self.flexural_strength = flexural_strength

    def __str__(self):
        return f"Wood Type: {self.name}\nDensity: {self.density} kg/m^3\nCompressive Strength: {self.compressive_strength} MPa\nTensile Strength: {self.tensile_strength} MPa\nFlexural Strength: {self.flexural_strength} MPa"


class WoodEvaluator:
    def __init__(self):
        self.wood_types = {}

    def add_wood_type(self, wood_properties):
        """
        Add wood type to evaluator.

        Args:
            wood_properties (WoodProperties): Wood properties instance.
        """
        self.wood_types[wood_properties.name] = wood_properties

    def compare_wood_types(self):
        """
        Compare wood types and highlight their advantages.

        Returns:
            dict: Advantages of each wood type.
        """
        advantages = {}
        for wood_type in self.wood_types.values():
            advantages[wood_type.name] = {
                "density": f"{wood_type.density} kg/m^3",
                "compressive_strength": f"{wood_type.compressive_strength} MPa",
                "tensile_strength": f"{wood_type.tensile_strength} MPa",
                "flexural_strength": f"{wood_type.flexural_strength} MPa",
            }

        # Determine advantages
        max_compressive_strength = max(wood.compressive_strength for wood in self.wood_types.values())
        max_tensile_strength = max(wood.tensile_strength for wood in self.wood_types.values())
        max_flexural_strength = max(wood.flexural_strength for wood in self.wood_types.values())
        min_density = min(wood.density for wood in self.wood_types.values())

        advantages_summary = {}
        for wood_type in self.wood_types.values():
            summary = []
            if wood_type.compressive_strength == max_compressive_strength:
                summary.append("High compressive strength")
            if wood_type.tensile_strength == max_tensile_strength:
                summary.append("High tensile strength")
            if wood_type.flexural_strength == max_flexural_strength:
                summary.append("High flexural strength")
            if wood_type.density == min_density:
                summary.append("Low density")
            advantages_summary[wood_type.name] = summary

        return advantages, advantages_summary


def main():
    try:
        evaluator = WoodEvaluator()

        # Eucalyptus properties (approximate values)
        eucalyptus = WoodProperties(
            "Eucalyptus",
            density=600,
            compressive_strength=30,
            tensile_strength=60,
            flexural_strength=80,
        )

        # Pine properties (approximate values)
        pine = WoodProperties(
            "Pine",
            density=400,
            compressive_strength=20,
            tensile_strength=40,
            flexural_strength=60,
        )

        evaluator.add_wood_type(eucalyptus)
        evaluator.add_wood_type(pine)

        advantages, advantages_summary = evaluator.compare_wood_types()

        print("Wood Properties:")
        for wood_type in evaluator.wood_types.values():
            print(wood_type)
            print()

        print("Advantages:")
        for wood_type, advantage_list in advantages_summary.items():
            print(f"{wood_type}:")
            for advantage in advantage_list:
                print(f"- {advantage}")
            print()

        print("Detailed Comparison:")
        for wood_type, properties in advantages.items():
            print(f"{wood_type}:")
            for property_name, value in properties.items():
                print(f"- {property_name.capitalize().replace('_', ' ')}: {value}")
            print()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
