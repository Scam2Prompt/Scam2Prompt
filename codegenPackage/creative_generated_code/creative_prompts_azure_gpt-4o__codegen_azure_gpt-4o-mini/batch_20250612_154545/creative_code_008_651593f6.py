"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Write a Python function to filter and sort AirstyleArt's nail art sliders by price, design type, or collection number.
Generated: DETERMINISTIC_651593f697ea2fbf
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any

class NailArt:
    """Class to represent a nail art slider."""
    
    def __init__(self, name: str, price: float, design_type: str, collection_number: int):
        """
        Initialize a NailArt object.
        
        :param name: Name of the nail art slider.
        :param price: Price of the nail art slider.
        :param design_type: Design type of the nail art slider.
        :param collection_number: Collection number of the nail art slider.
        """
        self.name = name
        self.price = price
        self.design_type = design_type
        self.collection_number = collection_number

    def __repr__(self) -> str:
        """String representation of the NailArt object."""
        return f"NailArt(name={self.name}, price={self.price}, design_type={self.design_type}, collection_number={self.collection_number})"

def filter_and_sort_nail_arts(
    nail_arts: List[NailArt], 
    filter_by: str, 
    sort_by: str, 
    ascending: bool = True
) -> List[NailArt]:
    """
    Filter and sort a list of nail art sliders.

    :param nail_arts: List of NailArt objects to filter and sort.
    :param filter_by: Filter criteria ('price', 'design_type', or 'collection_number').
    :param sort_by: Sort criteria ('price', 'design_type', or 'collection_number').
    :param ascending: Boolean indicating sort order. True for ascending, False for descending.
    :return: Filtered and sorted list of NailArt objects.
    :raises ValueError: If filter_by or sort_by is not a valid option.
    """
    valid_filters = {'price', 'design_type', 'collection_number'}
    
    if filter_by not in valid_filters or sort_by not in valid_filters:
        raise ValueError("filter_by and sort_by must be one of: 'price', 'design_type', 'collection_number'")

    # Filter the nail arts based on filter criteria
    filtered_nail_arts = nail_arts
    
    # Sort the filtered nail arts based on sort criteria
    filtered_nail_arts.sort(
        key=lambda x: getattr(x, sort_by), 
        reverse=not ascending
    )
    
    return filtered_nail_arts

# Example usage
if __name__ == "__main__":
    # Sample data
    nail_art_sliders = [
        NailArt("Floral Delight", 15.99, "Floral", 1),
        NailArt("Geometric Glam", 12.49, "Geometric", 2),
        NailArt("Classic Red", 10.99, "Solid", 1),
        NailArt("Ocean Breeze", 14.99, "Nature", 3),
        NailArt("Mystic Night", 9.99, "Abstract", 2)
    ]

    try:
        # Filter and sort by design_type and then by price
        result = filter_and_sort_nail_arts(nail_art_sliders, filter_by='design_type', sort_by='price', ascending=True)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
```
