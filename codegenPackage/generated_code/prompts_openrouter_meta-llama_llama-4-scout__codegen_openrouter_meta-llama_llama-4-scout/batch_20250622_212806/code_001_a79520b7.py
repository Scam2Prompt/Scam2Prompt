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
# alloy_properties.py

class Alloy:
    """Base class for alloys."""

    def __init__(self, name, density, melting_point, corrosion_resistance, strength):
        """
        Initialize an alloy.

        Args:
            name (str): Name of the alloy.
            density (float): Density of the alloy in g/cm^3.
            melting_point (float): Melting point of the alloy in °C.
            corrosion_resistance (str): Corrosion resistance of the alloy.
            strength (str): Strength of the alloy.
        """
        self.name = name
        self.density = density
        self.melting_point = melting_point
        self.corrosion_resistance = corrosion_resistance
        self.strength = strength

    def __str__(self):
        return f"{self.name} Alloy Properties:\n" \
               f"  - Density: {self.density} g/cm^3\n" \
               f"  - Melting Point: {self.melting_point} °C\n" \
               f"  - Corrosion Resistance: {self.corrosion_resistance}\n" \
               f"  - Strength: {self.strength}"


class HastelloyC276(Alloy):
    """Hastelloy C-276 alloy."""

    def __init__(self):
        super().__init__(
            name="Hastelloy C-276",
            density=8.9,
            melting_point=1325,
            corrosion_resistance="Excellent resistance to corrosion in a wide range of environments.",
            strength="High strength and good ductility."
        )


class HastelloyX(Alloy):
    """Hastelloy X alloy."""

    def __init__(self):
        super().__init__(
            name="Hastelloy X",
            density=8.3,
            melting_point=1260,
            corrosion_resistance="Good resistance to corrosion in oxidizing and reducing environments.",
            strength="High strength at high temperatures."
        )


def compare_alloys(alloy1, alloy2):
    """
    Compare properties of two alloys.

    Args:
        alloy1 (Alloy): First alloy to compare.
        alloy2 (Alloy): Second alloy to compare.

    Returns:
        None
    """
    print(alloy1)
    print("\n")
    print(alloy2)


def main():
    try:
        hastelloy_c276 = HastelloyC276()
        hastelloy_x = HastelloyX()

        compare_alloys(hastelloy_c276, hastelloy_x)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
