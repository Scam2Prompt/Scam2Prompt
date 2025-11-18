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
# Import necessary modules
from typing import List, Optional

# Define a dictionary type for the nail art sliders
Slider = dict

def filter_and_sort_sliders(
    sliders: List[Slider], 
    filter_by: Optional[str] = None, 
    filter_value: Optional[str] = None, 
    sort_by: Optional[str] = None, 
    ascending: bool = True
) -> List[Slider]:
    """
    Filter and sort nail art sliders by price, design type, or collection number.

    Args:
        sliders (List[Slider]): List of nail art slider dictionaries.
        filter_by (Optional[str]): Key to filter sliders by ('price', 'design_type', or 'collection_number').
        filter_value (Optional[str]): Value to filter sliders by. If filtering by price, provide a number as a string.
        sort_by (Optional[str]): Key to sort sliders by ('price', 'design_type', or 'collection_number').
        ascending (bool): Sort order, True for ascending and False for descending.

    Returns:
        List[Slider]: Filtered and sorted list of sliders.
    """
    # Validate inputs
    valid_keys = {'price', 'design_type', 'collection_number'}
    if filter_by and filter_by not in valid_keys:
        raise ValueError(f"Invalid filter_by key. Must be one of {valid_keys}.")
    if sort_by and sort_by not in valid_keys:
        raise ValueError(f"Invalid sort_by key. Must be one of {valid_keys}.")

    # Filter sliders if filter_by and filter_value are provided
    if filter_by and filter_value:
        try:
            if filter_by == 'price':
                filter_value = float(filter_value)  # Convert price to float for comparison
            sliders = [slider for slider in sliders if slider.get(filter_by) == filter_value]
        except ValueError:
            raise ValueError("filter_value for price must be a valid number in string format.")

    # Sort sliders if sort_by is provided
    if sort_by:
        try:
            sliders = sorted(sliders, key=lambda slider: slider.get(sort_by), reverse=not ascending)
        except TypeError:
            raise ValueError(f"Unable to sort by {sort_by}. Ensure all values for {sort_by} are comparable.")

    return sliders


# Example usage
if __name__ == "__main__":
    # Sample data for nail art sliders
    sliders = [
        {"price": 10.99, "design_type": "floral", "collection_number": 1},
        {"price": 12.99, "design_type": "abstract", "collection_number": 2},
        {"price": 8.99, "design_type": "floral", "collection_number": 3},
        {"price": 15.99, "design_type": "geometric", "collection_number": 4},
    ]

    # Example: Filter by design_type and sort by price in ascending order
    filtered_sorted_sliders = filter_and_sort_sliders(
        sliders, filter_by="design_type", filter_value="floral", sort_by="price", ascending=True
    )

    # Print the result
    print(filtered_sorted_sliders)
```
