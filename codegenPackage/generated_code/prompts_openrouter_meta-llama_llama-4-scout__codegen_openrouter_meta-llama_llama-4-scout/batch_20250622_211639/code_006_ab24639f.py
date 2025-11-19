"""
Generated Code Metadata:
========================
Original URL: https://sushiswapweacc.blogspot.com
Prompt: Provide a list of different types of sand used in construction, including their advantages and disadvantages.
Generated: DETERMINISTIC_ab24639f91036091
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sand_types.py

class SandType:
    """Represents a type of sand used in construction."""

    def __init__(self, name, advantages, disadvantages):
        """
        Initializes a SandType object.

        Args:
            name (str): The name of the sand type.
            advantages (list[str]): A list of advantages of the sand type.
            disadvantages (list[str]): A list of disadvantages of the sand type.
        """
        self.name = name
        self.advantages = advantages
        self.disadvantages = disadvantages

    def __str__(self):
        """Returns a string representation of the SandType object."""
        return f"{self.name}\nAdvantages: {', '.join(self.advantages)}\nDisadvantages: {', '.join(self.disadvantages)}"


class SandTypeRepository:
    """Provides a repository of different types of sand used in construction."""

    def __init__(self):
        """Initializes a SandTypeRepository object."""
        self.sand_types = []

    def add_sand_type(self, sand_type):
        """
        Adds a sand type to the repository.

        Args:
            sand_type (SandType): The sand type to add.
        """
        self.sand_types.append(sand_type)

    def get_sand_types(self):
        """
        Returns a list of all sand types in the repository.

        Returns:
            list[SandType]: A list of SandType objects.
        """
        return self.sand_types


def main():
    try:
        # Create a repository of sand types
        repository = SandTypeRepository()

        # Add different types of sand to the repository
        river_sand = SandType(
            "River Sand",
            ["Well-graded", "Good for construction", "High strength"],
            ["Expensive", "May contain impurities"]
        )
        repository.add_sand_type(river_sand)

        manufactured_sand = SandType(
            "Manufactured Sand",
            ["Cost-effective", "Consistent quality", "Environmentally friendly"],
            ["May not be suitable for high-strength applications"]
        )
        repository.add_sand_type(manufactured_sand)

        sea_sand = SandType(
            "Sea Sand",
            ["Abundant", "Low cost"],
            ["High salt content may cause corrosion", "May contain impurities"]
        )
        repository.add_sand_type(sea_sand)

        pit_sand = SandType(
            "Pit Sand",
            ["Good for construction", "Low cost"],
            ["May contain impurities", "May not be well-graded"]
        )
        repository.add_sand_type(pit_sand)

        # Print all sand types
        for i, sand_type in enumerate(repository.get_sand_types()):
            print(f"Sand Type {i+1}:")
            print(sand_type)
            print("------------------------")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
