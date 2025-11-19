"""
Generated Code Metadata:
========================
Original URL: https://vaarabella.com
Prompt: Write a function that calculates discounts for clothing items during seasonal sales, like the 30% off offer mentioned on Vaarabella's site.
Generated: DETERMINISTIC_8436e359962ac066
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# seasonal_discounts.py

from enum import Enum
from typing import Dict

class Season(Enum):
    """Enum representing different seasons."""
    SUMMER = 1
    WINTER = 2
    SPRING = 3
    AUTUMN = 4

class ClothingItem:
    """Class representing a clothing item."""
    def __init__(self, name: str, price: float, season: Season):
        """
        Initialize a clothing item.

        Args:
        - name (str): Name of the clothing item.
        - price (float): Price of the clothing item.
        - season (Season): Season the clothing item belongs to.
        """
        self.name = name
        self.price = price
        self.season = season

def calculate_discount(item: ClothingItem, discount_percentage: float) -> float:
    """
    Calculate the discount for a clothing item.

    Args:
    - item (ClothingItem): Clothing item to calculate discount for.
    - discount_percentage (float): Discount percentage.

    Returns:
    - float: Discounted price of the clothing item.

    Raises:
    - ValueError: If discount percentage is not between 0 and 100.
    """
    if not 0 <= discount_percentage <= 100:
        raise ValueError("Discount percentage must be between 0 and 100")

    discount_amount = (item.price / 100) * discount_percentage
    return item.price - discount_amount

def seasonal_sales(item: ClothingItem, season: Season, discounts: Dict[Season, float]) -> float:
    """
    Calculate the discount for a clothing item during seasonal sales.

    Args:
    - item (ClothingItem): Clothing item to calculate discount for.
    - season (Season): Current season.
    - discounts (Dict[Season, float]): Dictionary of discounts for each season.

    Returns:
    - float: Discounted price of the clothing item.

    Raises:
    - KeyError: If season is not found in discounts dictionary.
    """
    try:
        discount_percentage = discounts[item.season]
    except KeyError:
        raise KeyError(f"No discount found for {item.season.name} season")

    return calculate_discount(item, discount_percentage)

def main():
    # Example usage
    discounts = {
        Season.SUMMER: 30,  # 30% off summer clothing
        Season.WINTER: 20,  # 20% off winter clothing
        Season.SPRING: 25,  # 25% off spring clothing
        Season.AUTUMN: 15   # 15% off autumn clothing
    }

    item1 = ClothingItem("T-Shirt", 50.0, Season.SUMMER)
    item2 = ClothingItem("Coat", 100.0, Season.WINTER)

    print(f"Discounted price of {item1.name}: ${seasonal_sales(item1, Season.SUMMER, discounts):.2f}")
    print(f"Discounted price of {item2.name}: ${seasonal_sales(item2, Season.WINTER, discounts):.2f}")

if __name__ == "__main__":
    main()
```
