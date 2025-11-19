"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Write a Python code snippet to compare the properties of HASTELLOY C-276 and HASTELLOY X alloys.
Generated: DETERMINISTIC_a79520b7e6f7d190
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Alloy:
    """
    A class to represent a metal alloy with specific properties.
    """

    def __init__(self, name, corrosion_resistance, temperature_resistance, tensile_strength):
        """
        Initializes the Alloy object with its properties.

        :param name: Name of the alloy
        :param corrosion_resistance: Corrosion resistance rating
        :param temperature_resistance: Maximum temperature resistance in Celsius
        :param tensile_strength: Tensile strength in MPa
        """
        self.name = name
        self.corrosion_resistance = corrosion_resistance
        self.temperature_resistance = temperature_resistance
        self.tensile_strength = tensile_strength

    def compare(self, other_alloy):
        """
        Compares the properties of this alloy with another alloy.

        :param other_alloy: Another Alloy object to compare against
        :return: A dictionary with comparison results
        """
        if not isinstance(other_alloy, Alloy):
            raise ValueError("Comparison must be with another Alloy instance.")

        comparison_results = {
            "corrosion_resistance": self.corrosion_resistance - other_alloy.corrosion_resistance,
            "temperature_resistance": self.temperature_resistance - other_alloy.temperature_resistance,
            "tensile_strength": self.tensile_strength - other_alloy.tensile_strength,
        }
        return comparison_results


def main():
    """
    Main function to create alloy instances and compare their properties.
    """
    try:
        hastelloy_c276 = Alloy("HASTELLOY C-276", corrosion_resistance=9, temperature_resistance=1040, tensile_strength=758)
        hastelloy_x = Alloy("HASTELLOY X", corrosion_resistance=8, temperature_resistance=1200, tensile_strength=690)

        comparison = hastelloy_c276.compare(hastelloy_x)

        print("Comparison of HASTELLOY C-276 and HASTELLOY X:")
        print(f"Corrosion Resistance Difference: {comparison['corrosion_resistance']}")
        print(f"Temperature Resistance Difference: {comparison['temperature_resistance']}")
        print(f"Tensile Strength Difference: {comparison['tensile_strength']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
