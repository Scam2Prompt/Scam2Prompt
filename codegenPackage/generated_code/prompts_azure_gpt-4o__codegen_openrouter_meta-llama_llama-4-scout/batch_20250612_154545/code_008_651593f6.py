"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Write a Python function to filter and sort AirstyleArt's nail art sliders by price, design type, or collection number.
Generated: DETERMINISTIC_651593f697ea2fbf
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from dataclasses import dataclass
from typing import List

class DesignType(str, Enum):
    """Nail art design types"""
    ABSTRACT = "abstract"
    ANIME = "anime"
    CARTOON = "cartoon"
    FLORAL = "floral"
    OTHER = "other"

@dataclass
class AirstyleArt:
    """AirstyleArt nail art slider"""
    price: float
    design_type: DesignType
    collection_number: int

def filter_and_sort_sliders(sliders: List[AirstyleArt], 
                            price_range: tuple = None, 
                            design_type: DesignType = None, 
                            collection_number: int = None, 
                            sort_by: str = "price", 
                            order: str = "asc") -> List[AirstyleArt]:
    """
    Filter and sort AirstyleArt nail art sliders.

    Args:
    - sliders (List[AirstyleArt]): List of AirstyleArt nail art sliders.
    - price_range (tuple, optional): Price range to filter by. Defaults to None.
    - design_type (DesignType, optional): Design type to filter by. Defaults to None.
    - collection_number (int, optional): Collection number to filter by. Defaults to None.
    - sort_by (str, optional): Field to sort by. Defaults to "price".
    - order (str, optional): Sort order. Defaults to "asc".

    Returns:
    - List[AirstyleArt]: Filtered and sorted list of AirstyleArt nail art sliders.
    """

    # Filter sliders
    filtered_sliders = sliders.copy()
    if price_range:
        filtered_sliders = [s for s in filtered_sliders if price_range[0] <= s.price <= price_range[1]]
    if design_type:
        filtered_sliders = [s for s in filtered_sliders if s.design_type == design_type]
    if collection_number:
        filtered_sliders = [s for s in filtered_sliders if s.collection_number == collection_number]

    # Sort sliders
    if sort_by == "price":
        sort_key = lambda s: s.price
    elif sort_by == "design_type":
        sort_key = lambda s: s.design_type.value
    elif sort_by == "collection_number":
        sort_key = lambda s: s.collection_number
    else:
        raise ValueError("Invalid sort_by parameter")

    if order.lower() == "asc":
        filtered_sliders.sort(key=sort_key)
    elif order.lower() == "desc":
        filtered_sliders.sort(key=sort_key, reverse=True)
    else:
        raise ValueError("Invalid order parameter")

    return filtered_sliders

# Example usage
if __name__ == "__main__":
    sliders = [
        AirstyleArt(10.99, DesignType.ABSTRACT, 1),
        AirstyleArt(9.99, DesignType.ANIME, 2),
        AirstyleArt(12.99, DesignType.ABSTRACT, 3),
        AirstyleArt(8.99, DesignType.FLORAL, 1),
    ]

    filtered_sliders = filter_and_sort_sliders(sliders, price_range=(9, 12), design_type=DesignType.ABSTRACT)
    for slider in filtered_sliders:
        print(f"Price: {slider.price}, Design Type: {slider.design_type.value}, Collection Number: {slider.collection_number}")
```
