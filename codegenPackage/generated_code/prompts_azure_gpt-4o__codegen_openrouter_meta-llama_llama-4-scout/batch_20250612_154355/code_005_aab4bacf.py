"""
Generated Code Metadata:
========================
Original URL: https://roshako.com
Prompt: Write a program to categorize and display the welding electrodes and filler metals offered by Roshako, such as Alloy 625 and Hastelloy C-276, along with their technical specifications.
Generated: DETERMINISTIC_aab4bacf61b5b71d
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# welding_electrodes.py

class WeldingElectrode:
    """Represents a welding electrode with its technical specifications."""

    def __init__(self, name, alloy, tensile_strength, elongation, density):
        """
        Initializes a WeldingElectrode object.

        Args:
            name (str): Name of the welding electrode.
            alloy (str): Alloy type of the welding electrode.
            tensile_strength (float): Tensile strength of the welding electrode in MPa.
            elongation (float): Elongation of the welding electrode in %.
            density (float): Density of the welding electrode in g/cm^3.
        """
        self.name = name
        self.alloy = alloy
        self.tensile_strength = tensile_strength
        self.elongation = elongation
        self.density = density

    def __str__(self):
        return f"{self.name} ({self.alloy}) - Technical Specifications:\n" \
               f"Tensile Strength: {self.tensile_strength} MPa\n" \
               f"Elongation: {self.elongation}%\n" \
               f"Density: {self.density} g/cm^3"


class FillerMetal:
    """Represents a filler metal with its technical specifications."""

    def __init__(self, name, alloy, melting_range, corrosion_resistance):
        """
        Initializes a FillerMetal object.

        Args:
            name (str): Name of the filler metal.
            alloy (str): Alloy type of the filler metal.
            melting_range (str): Melting range of the filler metal in °C.
            corrosion_resistance (str): Corrosion resistance of the filler metal.
        """
        self.name = name
        self.alloy = alloy
        self.melting_range = melting_range
        self.corrosion_resistance = corrosion_resistance

    def __str__(self):
        return f"{self.name} ({self.alloy}) - Technical Specifications:\n" \
               f"Melting Range: {self.melting_range} °C\n" \
               f"Corrosion Resistance: {self.corrosion_resistance}"


class RoshakoProducts:
    """Represents the welding electrodes and filler metals offered by Roshako."""

    def __init__(self):
        self.electrodes = []
        self.filler_metals = []

    def add_electrode(self, electrode):
        """Adds a welding electrode to the catalog."""
        self.electrodes.append(electrode)

    def add_filler_metal(self, filler_metal):
        """Adds a filler metal to the catalog."""
        self.filler_metals.append(filler_metal)

    def display_products(self):
        """Displays all welding electrodes and filler metals in the catalog."""
        print("Welding Electrodes:")
        for electrode in self.electrodes:
            print(electrode)
            print("--------------------")

        print("\nFiller Metals:")
        for filler_metal in self.filler_metals:
            print(filler_metal)
            print("--------------------")


def main():
    try:
        roshako_products = RoshakoProducts()

        # Add welding electrodes
        alloy_625_electrode = WeldingElectrode(
            "Alloy 625 Electrode",
            "Inconel 625",
            900,
            30,
            8.9
        )
        hastelloy_c276_electrode = WeldingElectrode(
            "Hastelloy C-276 Electrode",
            "Hastelloy C-276",
            1000,
            25,
            8.9
        )
        roshako_products.add_electrode(alloy_625_electrode)
        roshako_products.add_electrode(hastelloy_c276_electrode)

        # Add filler metals
        alloy_625_filler_metal = FillerMetal(
            "Alloy 625 Filler Metal",
            "Inconel 625",
            "1300-1350",
            "Highly resistant to corrosion"
        )
        hastelloy_c276_filler_metal = FillerMetal(
            "Hastelloy C-276 Filler Metal",
            "Hastelloy C-276",
            "1300-1350",
            "Highly resistant to corrosion"
        )
        roshako_products.add_filler_metal(alloy_625_filler_metal)
        roshako_products.add_filler_metal(hastelloy_c276_filler_metal)

        # Display products
        roshako_products.display_products()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
