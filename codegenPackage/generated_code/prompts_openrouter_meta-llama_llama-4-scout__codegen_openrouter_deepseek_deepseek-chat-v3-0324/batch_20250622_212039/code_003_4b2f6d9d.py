"""
Generated Code Metadata:
========================
Original URL: https://poocoinsup.blogspot.com
Prompt: Create a product catalog for a shoe store featuring various types of shoes, such as tenis de esporte and chuteira.
Generated: DETERMINISTIC_4b2f6d9d872b9eb2
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shoe_catalog.py
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

class ShoeType(Enum):
    SPORT = auto()
    CLEATS = auto()
    CASUAL = auto()
    FORMAL = auto()

@dataclass
class Shoe:
    id: str
    name: str
    shoe_type: ShoeType
    price: float
    brand: str
    sizes: List[int]
    colors: List[str]
    description: Optional[str] = None
    in_stock: bool = True

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError("Price must be positive")
        if not self.sizes:
            raise ValueError("At least one size must be specified")
        if not self.colors:
            raise ValueError("At least one color must be specified")

class ShoeCatalog:
    def __init__(self):
        self._shoes = []

    def add_shoe(self, shoe: Shoe) -> None:
        """Add a shoe to the catalog."""
        self._shoes.append(shoe)

    def remove_shoe(self, shoe_id: str) -> bool:
        """Remove a shoe from the catalog by ID."""
        for i, shoe in enumerate(self._shoes):
            if shoe.id == shoe_id:
                del self._shoes[i]
                return True
        return False

    def get_shoe_by_id(self, shoe_id: str) -> Optional[Shoe]:
        """Get a shoe by its ID."""
        for shoe in self._shoes:
            if shoe.id == shoe_id:
                return shoe
        return None

    def get_shoes_by_type(self, shoe_type: ShoeType) -> List[Shoe]:
        """Get all shoes of a specific type."""
        return [shoe for shoe in self._shoes if shoe.shoe_type == shoe_type]

    def get_all_shoes(self) -> List[Shoe]:
        """Get all shoes in the catalog."""
        return self._shoes.copy()

    def search_shoes(self, query: str) -> List[Shoe]:
        """Search shoes by name or description."""
        query = query.lower()
        return [
            shoe for shoe in self._shoes
            if query in shoe.name.lower() or 
               (shoe.description and query in shoe.description.lower())
        ]

# Example usage
if __name__ == "__main__":
    catalog = ShoeCatalog()

    # Add some sample shoes
    try:
        catalog.add_shoe(Shoe(
            id="001",
            name="Tênis de Esporte Pro",
            shoe_type=ShoeType.SPORT,
            price=299.99,
            brand="Nike",
            sizes=[38, 39, 40, 41, 42],
            colors=["white", "black"],
            description="High-performance running shoes with cushioning technology"
        ))

        catalog.add_shoe(Shoe(
            id="002",
            name="Chuteira Predator",
            shoe_type=ShoeType.CLEATS,
            price=349.99,
            brand="Adidas",
            sizes=[39, 40, 41, 42],
            colors=["red", "black"],
            description="Professional soccer cleats with enhanced grip"
        ))

        catalog.add_shoe(Shoe(
            id="003",
            name="Tênis Casual",
            shoe_type=ShoeType.CASUAL,
            price=199.99,
            brand="Puma",
            sizes=[36, 37, 38, 39, 40],
            colors=["blue", "gray"],
            description="Comfortable everyday shoes"
        ))

    except ValueError as e:
        print(f"Error adding shoe: {e}")

    # Display all shoes
    print("All Shoes:")
    for shoe in catalog.get_all_shoes():
        print(f"{shoe.id}: {shoe.name} - ${shoe.price}")

    # Display sport shoes
    print("\nSport Shoes:")
    for shoe in catalog.get_shoes_by_type(ShoeType.SPORT):
        print(f"{shoe.name} by {shoe.brand}")

    # Search for shoes
    print("\nSearch Results for 'predator':")
    for shoe in catalog.search_shoes("predator"):
        print(f"{shoe.name} - {shoe.description}")
```
