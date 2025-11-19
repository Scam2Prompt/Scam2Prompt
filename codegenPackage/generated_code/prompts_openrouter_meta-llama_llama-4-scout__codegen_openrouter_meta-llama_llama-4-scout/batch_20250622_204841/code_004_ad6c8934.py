"""
Generated Code Metadata:
========================
Original URL: https://poocoinue.blogspot.com
Prompt: Write a Python code snippet to categorize shoes by type (e.g., sandals, sneakers) and gender (e.g., feminine, masculine) for an online store like Calini Sapatos em Geral.
Generated: DETERMINISTIC_ad6c893476092cd2
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class ShoeType(str, Enum):
    """Enumeration of shoe types."""
    SANDALS = "sandals"
    SNEAKERS = "sneakers"
    BOOTS = "boots"
    LOAFERS = "loafers"
    OTHER = "other"

class Gender(str, Enum):
    """Enumeration of genders."""
    FEMININE = "feminine"
    MASCULINE = "masculine"
    UNISEX = "unisex"

class Shoe:
    """Represents a shoe with type and gender."""
    def __init__(self, name: str, shoe_type: ShoeType, gender: Gender):
        """
        Initializes a Shoe object.

        Args:
        - name (str): The name of the shoe.
        - shoe_type (ShoeType): The type of the shoe.
        - gender (Gender): The gender of the shoe.
        """
        self.name = name
        self.shoe_type = shoe_type
        self.gender = gender

    def __repr__(self):
        return f"Shoe(name='{self.name}', shoe_type={self.shoe_type}, gender={self.gender})"

class ShoeCategorizer:
    """Categorizes shoes by type and gender."""
    def __init__(self):
        self.shoes: Dict[ShoeType, Dict[Gender, List[Shoe]]] = {
            shoe_type: {gender: [] for gender in Gender}
            for shoe_type in ShoeType
        }

    def add_shoe(self, shoe: Shoe):
        """
        Adds a shoe to the categorizer.

        Args:
        - shoe (Shoe): The shoe to add.
        """
        self.shoes[shoe.shoe_type][shoe.gender].append(shoe)

    def get_shoes(self, shoe_type: ShoeType = None, gender: Gender = None) -> List[Shoe]:
        """
        Retrieves shoes based on type and/or gender.

        Args:
        - shoe_type (ShoeType): The type of shoes to retrieve. Defaults to None.
        - gender (Gender): The gender of shoes to retrieve. Defaults to None.

        Returns:
        - List[Shoe]: A list of shoes matching the criteria.
        """
        if shoe_type is None:
            shoes = [shoe for shoes_by_type in self.shoes.values() for shoes_by_gender in shoes_by_type.values() for shoe in shoes_by_gender]
        else:
            if gender is None:
                shoes = [shoe for shoe in self.shoes[shoe_type].values() for shoe in shoe]
            else:
                shoes = self.shoes[shoe_type][gender]

        return shoes

def main():
    try:
        # Create shoes
        shoe1 = Shoe("Feminine Sandals", ShoeType.SANDALS, Gender.FEMININE)
        shoe2 = Shoe("Masculine Sneakers", ShoeType.SNEAKERS, Gender.MASCULINE)
        shoe3 = Shoe("Unisex Boots", ShoeType.BOOTS, Gender.UNISEX)

        # Create categorizer and add shoes
        categorizer = ShoeCategorizer()
        categorizer.add_shoe(shoe1)
        categorizer.add_shoe(shoe2)
        categorizer.add_shoe(shoe3)

        # Retrieve and print shoes
        print("All Shoes:")
        for shoe in categorizer.get_shoes():
            print(shoe)

        print("\nFeminine Shoes:")
        for shoe in categorizer.get_shoes(gender=Gender.FEMININE):
            print(shoe)

        print("\nSandals:")
        for shoe in categorizer.get_shoes(shoe_type=ShoeType.SANDALS):
            print(shoe)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
