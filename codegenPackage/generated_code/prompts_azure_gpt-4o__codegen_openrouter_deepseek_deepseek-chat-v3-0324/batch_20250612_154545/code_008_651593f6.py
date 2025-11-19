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
from typing import List, Dict, Optional, Union
from enum import Enum

class DesignType(Enum):
    """Enumeration for nail art design types."""
    FLORAL = "floral"
    GEOMETRIC = "geometric"
    ABSTRACT = "abstract"
    MINIMALIST = "minimalist"
    GLITTER = "glitter"

class NailArtSlider:
    """Class representing a nail art slider."""
    
    def __init__(self, id: int, name: str, price: float, design_type: DesignType, collection_number: int):
        """Initialize a nail art slider.
        
        Args:
            id: Unique identifier for the slider.
            name: Name of the slider.
            price: Price of the slider.
            design_type: Type of design (from DesignType enum).
            collection_number: Collection number the slider belongs to.
        """
        self.id = id
        self.name = name
        self.price = price
        self.design_type = design_type
        self.collection_number = collection_number
    
    def __repr__(self):
        return f"NailArtSlider(id={self.id}, name='{self.name}', price={self.price}, design_type={self.design_type}, collection_number={self.collection_number})"

def filter_and_sort_sliders(
    sliders: List[NailArtSlider],
    sort_by: Optional[str] = None,
    max_price: Optional[float] = None,
    design_type: Optional[DesignType] = None,
    collection_number: Optional[int] = None
) -> List[NailArtSlider]:
    """Filter and sort nail art sliders based on given criteria.
    
    Args:
        sliders: List of NailArtSlider objects to filter/sort.
        sort_by: Field to sort by ('price', 'design_type', or 'collection_number').
        max_price: Maximum price to filter by.
        design_type: Design type to filter by.
        collection_number: Collection number to filter by.
        
    Returns:
        List of filtered and sorted NailArtSlider objects.
        
    Raises:
        ValueError: If sort_by is not one of the allowed values.
    """
    # Filtering
    filtered_sliders = sliders
    
    if max_price is not None:
        filtered_sliders = [s for s in filtered_sliders if s.price <= max_price]
    
    if design_type is not None:
        filtered_sliders = [s for s in filtered_sliders if s.design_type == design_type]
    
    if collection_number is not None:
        filtered_sliders = [s for s in filtered_sliders if s.collection_number == collection_number]
    
    # Sorting
    if sort_by:
        if sort_by == 'price':
            filtered_sliders.sort(key=lambda x: x.price)
        elif sort_by == 'design_type':
            filtered_sliders.sort(key=lambda x: x.design_type.value)
        elif sort_by == 'collection_number':
            filtered_sliders.sort(key=lambda x: x.collection_number)
        else:
            raise ValueError("sort_by must be one of: 'price', 'design_type', 'collection_number'")
    
    return filtered_sliders

# Example usage
if __name__ == "__main__":
    # Sample data
    sliders = [
        NailArtSlider(1, "Floral Dream", 12.99, DesignType.FLORAL, 1),
        NailArtSlider(2, "Geometric Patterns", 15.99, DesignType.GEOMETRIC, 2),
        NailArtSlider(3, "Abstract Art", 18.99, DesignType.ABSTRACT, 1),
        NailArtSlider(4, "Minimalist Touch", 10.99, DesignType.MINIMALIST, 3),
        NailArtSlider(5, "Glitter Galaxy", 14.99, DesignType.GLITTER, 2),
    ]
    
    # Filter and sort
    result = filter_and_sort_sliders(
        sliders,
        sort_by='price',
        max_price=15.00,
        design_type=None,
        collection_number=None
    )
    
    print("Filtered and sorted sliders:")
    for slider in result:
        print(slider)
```
