"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Generate a list of nickel-based superalloys and their applications in the aerospace industry.
Generated: DETERMINISTIC_cce0a07af06031f2
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

class NickelSuperalloy:
    """
    Represents a nickel-based superalloy with its properties and aerospace applications.
    """
    
    def __init__(self, name, composition, temperature_resistance, applications):
        """
        Initialize a nickel superalloy instance.
        
        Args:
            name (str): Name of the superalloy
            composition (str): Primary chemical composition
            temperature_resistance (str): Temperature resistance range
            applications (list): List of aerospace applications
        """
        self.name = name
        self.composition = composition
        self.temperature_resistance = temperature_resistance
        self.applications = applications
    
    def __str__(self):
        """String representation of the superalloy."""
        apps = ", ".join(self.applications)
        return (f"{self.name} (Composition: {self.composition}, "
                f"Temp Resistance: {self.temperature_resistance}, "
                f"Applications: {apps})")

def get_aerospace_superalloys():
    """
    Returns a list of nickel-based superalloys used in aerospace industry.
    
    Returns:
        list[NickelSuperalloy]: List of superalloy instances
    """
    return [
        NickelSuperalloy(
            "Inconel 718",
            "Ni-Cr-Fe with Nb and Mo",
            "Up to 700°C (1292°F)",
            [
                "Jet engine components",
                "Rocket motor cases",
                "Aircraft structural parts"
            ]
        ),
        NickelSuperalloy(
            "Hastelloy X",
            "Ni-Cr-Fe-Mo with Co and W",
            "Up to 1200°C (2192°F)",
            [
                "Combustion chambers",
                "Afterburner components",
                "Turbine exhaust systems"
            ]
        ),
        NickelSuperalloy(
            "Waspaloy",
            "Ni-Cr-Co with Mo and Ti",
            "Up to 815°C (1500°F)",
            [
                "Turbine blades",
                "Discs and shafts",
                "High-temperature fasteners"
            ]
        ),
        NickelSuperalloy(
            "Rene 41",
            "Ni-Cr-Co-Mo with Ti and Al",
            "Up to 980°C (1800°F)",
            [
                "Turbine engine parts",
                "Afterburner liners",
                "Exhaust components"
            ]
        ),
        NickelSuperalloy(
            "Inconel 625",
            "Ni-Cr with Mo and Nb",
            "Up to 980°C (1800°F)",
            [
                "Ducting systems",
                "Exhaust systems",
                "Heat exchanger tubing"
            ]
        ),
        NickelSuperalloy(
            "Udimet 720",
            "Ni-Cr-Co with Ti and Al",
            "Up to 750°C (1382°F)",
            [
                "Turbine discs",
                "Compressor components",
                "High-pressure turbine blades"
            ]
        )
    ]

def display_superalloys():
    """Display all nickel-based superalloys and their aerospace applications."""
    try:
        superalloys = get_aerospace_superalloys()
        print("Nickel-Based Superalloys in Aerospace Industry:")
        print("=" * 50)
        for alloy in superalloys:
            print(alloy)
            print("-" * 50)
    except Exception as e:
        print(f"Error displaying superalloys: {str(e)}")

if __name__ == "__main__":
    display_superalloys()
```
