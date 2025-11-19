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
from typing import List, Dict, Optional
from enum import Enum, auto

class Gender(Enum):
    """Enum representing gender categories for shoes."""
    FEMININE = auto()
    MASCULINE = auto()
    UNISEX = auto()

class ShoeType(Enum):
    """Enum representing different types of shoes."""
    SANDALS = auto()
    SNEAKERS = auto()
    BOOTS = auto()
    HEELS = auto()
    LOAFERS = auto()
    FLATS = auto()
    OXFORD = auto()
    OTHER = auto()

class Shoe:
    """Class representing a shoe product."""
    def __init__(
        self,
        id: str,
        name: str,
        shoe_type: ShoeType,
        gender: Gender,
        price: float,
        description: Optional[str] = None
    ):
        self.id = id
        self.name = name
        self.shoe_type = shoe_type
        self.gender = gender
        self.price = price
        self.description = description

    def __repr__(self):
        return f"Shoe(id={self.id}, name={self.name}, type={self.shoe_type.name}, gender={self.gender.name}, price={self.price})"

class ShoeInventory:
    """Class to manage and categorize shoe inventory."""
    def __init__(self):
        self.inventory: List[Shoe] = []
    
    def add_shoe(self, shoe: Shoe) -> None:
        """Add a shoe to the inventory."""
        if not isinstance(shoe, Shoe):
            raise ValueError("Only Shoe objects can be added to inventory")
        self.inventory.append(shoe)
    
    def get_shoes_by_type(self, shoe_type: ShoeType) -> List[Shoe]:
        """Return all shoes of a specific type."""
        return [shoe for shoe in self.inventory if shoe.shoe_type == shoe_type]
    
    def get_shoes_by_gender(self, gender: Gender) -> List[Shoe]:
        """Return all shoes for a specific gender."""
        return [shoe for shoe in self.inventory if shoe.gender == gender]
    
    def get_shoes_by_type_and_gender(self, shoe_type: ShoeType, gender: Gender) -> List[Shoe]:
        """Return shoes filtered by both type and gender."""
        return [
            shoe for shoe in self.inventory 
            if shoe.shoe_type == shoe_type and shoe.gender == gender
        ]
    
    def get_inventory_summary(self) -> Dict[str, Dict[str, int]]:
        """Return summary statistics of the inventory."""
        summary = {
            'by_type': {t.name: 0 for t in ShoeType},
            'by_gender': {g.name: 0 for g in Gender}
        }
        
        for shoe in self.inventory:
            summary['by_type'][shoe.shoe_type.name] += 1
            summary['by_gender'][shoe.gender.name] += 1
            
        return summary

# Example usage
if __name__ == "__main__":
    inventory = ShoeInventory()
    
    # Add sample shoes
    inventory.add_shoe(Shoe("001", "Summer Sandals", ShoeType.SANDALS, Gender.FEMININE, 49.99))
    inventory.add_shoe(Shoe("002", "Classic Sneakers", ShoeType.SNEAKERS, Gender.UNISEX, 79.99))
    inventory.add_shoe(Shoe("003", "Leather Boots", ShoeType.BOOTS, Gender.MASCULINE, 129.99))
    inventory.add_shoe(Shoe("004", "High Heels", ShoeType.HEELS, Gender.FEMININE, 89.99))
    
    # Get some filtered results
    feminine_shoes = inventory.get_shoes_by_gender(Gender.FEMININE)
    sandals = inventory.get_shoes_by_type(ShoeType.SANDALS)
    masculine_boots = inventory.get_shoes_by_type_and_gender(ShoeType.BOOTS, Gender.MASCULINE)
    
    # Get summary
    summary = inventory.get_inventory_summary()
```
