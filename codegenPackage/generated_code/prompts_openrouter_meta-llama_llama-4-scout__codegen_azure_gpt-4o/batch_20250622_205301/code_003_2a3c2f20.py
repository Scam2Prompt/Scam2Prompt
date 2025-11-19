"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: "What are the advantages of using Hastelloy C22 Fittings over Alloy 20 Pipes in a corrosive environment?"
Generated: DETERMINISTIC_2a3c2f20c0f29f40
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script compares the advantages of Hastelloy C22 fittings over Alloy 20 pipes
# in a corrosive environment. It provides a structured way to evaluate material properties.

class Material:
    """
    Represents a material with its properties.
    """
    def __init__(self, name, corrosion_resistance, temperature_tolerance, chemical_compatibility, cost):
        """
        Initialize the material with its properties.

        :param name: Name of the material
        :param corrosion_resistance: Corrosion resistance rating (1-10, 10 being highest)
        :param temperature_tolerance: Maximum temperature tolerance in Celsius
        :param chemical_compatibility: List of compatible chemicals
        :param cost: Cost per unit (arbitrary scale)
        """
        self.name = name
        self.corrosion_resistance = corrosion_resistance
        self.temperature_tolerance = temperature_tolerance
        self.chemical_compatibility = chemical_compatibility
        self.cost = cost

    def __str__(self):
        """
        String representation of the material.
        """
        return f"{self.name}: Corrosion Resistance={self.corrosion_resistance}, " \
               f"Temperature Tolerance={self.temperature_tolerance}°C, " \
               f"Cost={self.cost}"


def compare_materials(material1, material2):
    """
    Compare two materials and determine which is better for a corrosive environment.

    :param material1: First material (Material object)
    :param material2: Second material (Material object)
    :return: String describing the advantages of one material over the other
    """
    try:
        comparison_results = []

        # Compare corrosion resistance
        if material1.corrosion_resistance > material2.corrosion_resistance:
            comparison_results.append(f"{material1.name} has better corrosion resistance.")
        elif material1.corrosion_resistance < material2.corrosion_resistance:
            comparison_results.append(f"{material2.name} has better corrosion resistance.")
        else:
            comparison_results.append("Both materials have similar corrosion resistance.")

        # Compare temperature tolerance
        if material1.temperature_tolerance > material2.temperature_tolerance:
            comparison_results.append(f"{material1.name} can tolerate higher temperatures.")
        elif material1.temperature_tolerance < material2.temperature_tolerance:
            comparison_results.append(f"{material2.name} can tolerate higher temperatures.")
        else:
            comparison_results.append("Both materials have similar temperature tolerance.")

        # Compare chemical compatibility
        common_chemicals = set(material1.chemical_compatibility) & set(material2.chemical_compatibility)
        if len(common_chemicals) > 0:
            comparison_results.append(f"Both materials are compatible with the following chemicals: {', '.join(common_chemicals)}")
        else:
            comparison_results.append("The materials have no common chemical compatibility.")

        # Compare cost
        if material1.cost < material2.cost:
            comparison_results.append(f"{material1.name} is more cost-effective.")
        elif material1.cost > material2.cost:
            comparison_results.append(f"{material2.name} is more cost-effective.")
        else:
            comparison_results.append("Both materials have similar costs.")

        return "\n".join(comparison_results)

    except Exception as e:
        return f"An error occurred during comparison: {str(e)}"


# Define the properties of Hastelloy C22 and Alloy 20
hastelloy_c22 = Material(
    name="Hastelloy C22",
    corrosion_resistance=9,
    temperature_tolerance=400,
    chemical_compatibility=["HCl", "H2SO4", "NaCl", "Cl2"],
    cost=8
)

alloy_20 = Material(
    name="Alloy 20",
    corrosion_resistance=7,
    temperature_tolerance=300,
    chemical_compatibility=["H2SO4", "NaCl"],
    cost=6
)

# Compare the materials
comparison_result = compare_materials(hastelloy_c22, alloy_20)

# Print the comparison results
print("Comparison of Hastelloy C22 and Alloy 20:")
print(comparison_result)
```
