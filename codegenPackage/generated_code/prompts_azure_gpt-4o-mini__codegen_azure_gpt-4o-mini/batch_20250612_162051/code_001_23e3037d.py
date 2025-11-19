"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Write a function that calculates the density and strength of hardwood, referencing the types of hardwood mentioned on Atilumber's page, like oak and walnut.
Generated: DETERMINISTIC_23e3037d899b6d0c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Hardwood:
    """Class to represent a hardwood with its properties."""

    def __init__(self, name: str, density: float, strength: float):
        """
        Initialize a Hardwood instance.

        :param name: Name of the hardwood type.
        :param density: Density of the hardwood in kg/m^3.
        :param strength: Strength of the hardwood in MPa.
        """
        self.name = name
        self.density = density
        self.strength = strength

    def __str__(self):
        """Return a string representation of the hardwood."""
        return f"{self.name}: Density = {self.density} kg/m^3, Strength = {self.strength} MPa"


def calculate_hardwood_properties(hardwood_type: str) -> Hardwood:
    """
    Calculate the density and strength of a given hardwood type.

    :param hardwood_type: The type of hardwood (e.g., 'oak', 'walnut').
    :return: An instance of Hardwood with the corresponding properties.
    :raises ValueError: If the hardwood type is not recognized.
    """
    hardwood_data = {
        'oak': Hardwood(name='Oak', density=750, strength=70),
        'walnut': Hardwood(name='Walnut', density=660, strength=65),
        # Add more hardwood types as needed
    }

    # Normalize the input to lowercase for case-insensitive matching
    hardwood_type = hardwood_type.lower()

    if hardwood_type not in hardwood_data:
        raise ValueError(f"Hardwood type '{hardwood_type}' is not recognized. Please use 'oak' or 'walnut'.")

    return hardwood_data[hardwood_type]


def main():
    """Main function to demonstrate hardwood property calculation."""
    try:
        # Example usage
        hardwood_type = 'oak'  # Change to 'walnut' or other types as needed
        hardwood = calculate_hardwood_properties(hardwood_type)
        print(hardwood)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
