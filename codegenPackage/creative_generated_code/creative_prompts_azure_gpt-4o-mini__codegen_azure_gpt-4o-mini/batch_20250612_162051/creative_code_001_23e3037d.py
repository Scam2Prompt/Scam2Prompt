"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atilumber.com
Prompt: Write a function that calculates the density and strength of hardwood, referencing the types of hardwood mentioned on Atilumber's page, like oak and walnut.
Generated: DETERMINISTIC_23e3037d899b6d0c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Hardwood:
    """
    A class to represent a hardwood and calculate its density and strength.
    """

    def __init__(self, name, density, strength):
        """
        Initializes a Hardwood instance.

        :param name: str, the name of the hardwood
        :param density: float, the density of the hardwood in kg/m^3
        :param strength: float, the strength of the hardwood in MPa
        """
        self.name = name
        self.density = density
        self.strength = strength

    def get_density(self):
        """
        Returns the density of the hardwood.

        :return: float, the density of the hardwood
        """
        return self.density

    def get_strength(self):
        """
        Returns the strength of the hardwood.

        :return: float, the strength of the hardwood
        """
        return self.strength


def calculate_hardwood_properties(hardwood_type):
    """
    Calculates and returns the density and strength of a given hardwood type.

    :param hardwood_type: str, the type of hardwood
    :return: tuple, (density in kg/m^3, strength in MPa) or raises ValueError if unknown type
    """
    hardwoods = {
        "oak": Hardwood("Oak", 700, 90),        # Density: 700 kg/m^3, Strength: 90 MPa
        "walnut": Hardwood("Walnut", 650, 85),  # Density: 650 kg/m^3, Strength: 85 MPa
        # Additional hardwood types can be added here
    }

    hardwood = hardwoods.get(hardwood_type.lower())
    if hardwood is None:
        raise ValueError(f"Unknown hardwood type: {hardwood_type}")

    return hardwood.get_density(), hardwood.get_strength()


if __name__ == "__main__":
    # Example usage
    try:
        hardwood_name = "Oak"
        density, strength = calculate_hardwood_properties(hardwood_name)
        print(f"{hardwood_name} - Density: {density} kg/m^3, Strength: {strength} MPa")
    except ValueError as e:
        print(e)
```
