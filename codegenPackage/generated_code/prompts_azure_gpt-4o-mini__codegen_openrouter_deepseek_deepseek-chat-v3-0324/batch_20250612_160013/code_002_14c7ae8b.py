"""
Generated Code Metadata:
========================
Original URL: https://piscorealestate.com
Prompt: Create a function that filters real estate properties based on specific criteria such as "Kvadratura" and "Cijena" for listings in Montenegro.
Generated: DETERMINISTIC_14c7ae8bf0c09b84
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional

def filter_properties(
    properties: List[Dict[str, any]],
    min_kvadratura: Optional[float] = None,
    max_kvadratura: Optional[float] = None,
    min_cijena: Optional[float] = None,
    max_cijena: Optional[float] = None
) -> List[Dict[str, any]]:
    """
    Filters a list of real estate properties based on specified criteria for Kvadratura and Cijena.

    Args:
        properties: List of property dictionaries to filter.
        min_kvadratura: Minimum Kvadratura (square meters) to include.
        max_kvadratura: Maximum Kvadratura (square meters) to include.
        min_cijena: Minimum Cijena (price) to include.
        max_cijena: Maximum Cijena (price) to include.

    Returns:
        List of filtered property dictionaries that meet all specified criteria.
    """
    filtered_properties = []
    
    for prop in properties:
        # Check if property has required fields
        if 'Kvadratura' not in prop or 'Cijena' not in prop:
            continue
        
        try:
            kvadratura = float(prop['Kvadratura'])
            cijena = float(prop['Cijena'])
        except (ValueError, TypeError):
            continue  # Skip properties with invalid numeric values
        
        # Apply filters
        kvadratura_ok = (
            (min_kvadratura is None or kvadratura >= min_kvadratura) and
            (max_kvadratura is None or kvadratura <= max_kvadratura)
        )
        
        cijena_ok = (
            (min_cijena is None or cijena >= min_cijena) and
            (max_cijena is None or cijena <= max_cijena)
        )
        
        if kvadratura_ok and cijena_ok:
            filtered_properties.append(prop)
    
    return filtered_properties
```
