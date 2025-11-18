"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atilumber.com
Prompt: Write a function to calculate the density of hardwood species such as oak, maple, and walnut, based on the descriptions provided by Askar Trading International.
Generated: DETERMINISTIC_f6b7904613feb84b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HardwoodDensityCalculator:
    """
    A class to calculate the density of various hardwood species.
    """

    DENSITY_MAP = {
        "oak": 0.75,    # Density in g/cm^3
        "maple": 0.70,  # Density in g/cm^3
        "walnut": 0.65  # Density in g/cm^3
    }

    @staticmethod
    def calculate_density(species: str) -> float:
        """
        Calculate the density of the given hardwood species.

        Args:
            species (str): The name of the hardwood species.

        Returns:
            float: The density of the hardwood in g/cm^3.

        Raises:
            ValueError: If the species is not recognized.
        """
        species = species.lower()  # Normalize species name to lowercase

        if species not in HardwoodDensityCalculator.DENSITY_MAP:
            raise ValueError(f"Species '{species}' is not recognized. Valid options are: {', '.join(HardwoodDensityCalculator.DENSITY_MAP.keys())}.")

        return HardwoodDensityCalculator.DENSITY_MAP[species]

# Example usage:
if __name__ == "__main__":
    try:
        species_input = "oak"  # Change this input to test different species
        density = HardwoodDensityCalculator.calculate_density(species_input)
        print(f"The density of {species_input.capitalize()} is {density} g/cm^3.")
    except ValueError as e:
        print(e)
```
