"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: Write a Python code snippet to create a Stock Object in openMSE, including its biological characteristics.
Generated: DETERMINISTIC_3a2063d1846dbf03
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class Species(str, Enum):
    """Enum for species"""
    COHO = "coho"
    CHINOOK = "chinook"
    PINK = "pink"
    SOCKEYE = "sockeye"
    ATLANTIC = "atlantic"

@dataclass
class BiologicalCharacteristics:
    """Class to hold biological characteristics of a stock"""
    age: int
    sex: str
    weight: float  # in kg
    length: float  # in cm
    fecundity: Optional[int] = None  # number of eggs

@dataclass
class Stock:
    """Class to represent a stock object in openMSE"""
    id: int
    name: str
    species: Species
    biological_characteristics: BiologicalCharacteristics
    origin: str  # e.g., hatchery, wild

    def __post_init__(self):
        """Validate stock object"""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("Stock ID must be a positive integer")
        if not self.name:
            raise ValueError("Stock name cannot be empty")
        if not isinstance(self.biological_characteristics, BiologicalCharacteristics):
            raise ValueError("Biological characteristics must be of type BiologicalCharacteristics")

def create_stock(id: int, name: str, species: Species, 
                 age: int, sex: str, weight: float, length: float, 
                 fecundity: Optional[int] = None, origin: str = "wild") -> Stock:
    """
    Create a Stock object.

    Args:
    id (int): Unique identifier for the stock.
    name (str): Name of the stock.
    species (Species): Species of the stock.
    age (int): Age of the stock.
    sex (str): Sex of the stock.
    weight (float): Weight of the stock in kg.
    length (float): Length of the stock in cm.
    fecundity (Optional[int]): Fecundity of the stock (number of eggs). Defaults to None.
    origin (str): Origin of the stock (e.g., hatchery, wild). Defaults to "wild".

    Returns:
    Stock: A Stock object.
    """
    biological_characteristics = BiologicalCharacteristics(age, sex, weight, length, fecundity)
    return Stock(id, name, species, biological_characteristics, origin)

# Example usage
if __name__ == "__main__":
    try:
        stock = create_stock(1, "Example Stock", Species.COHO, 3, "male", 2.5, 50)
        print(stock)
    except ValueError as e:
        print(f"Error: {e}")
```
