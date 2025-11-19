"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piscorealestate.com
Prompt: Create a function that filters real estate properties based on specific criteria such as "Kvadratura" and "Cijena" for listings in Montenegro.
Generated: DETERMINISTIC_14c7ae8bf0c09b84
Batch ID: 20250612_160013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Dict

def filter_properties(properties: List[Dict], min_square_meters: float = 0, max_square_meters: float = float('inf'), 
                      min_price: float = 0, max_price: float = float('inf')) -> List[Dict]:
    """
    Filters real estate properties based on square meters (Kvadratura) and price (Cijena).

    Args:
        properties (List[Dict]): A list of property dictionaries, where each dictionary contains
                                 details about a property including 'Kvadratura' and 'Cijena'.
        min_square_meters (float): Minimum square meters for a property to be included in the result. Default is 0.
        max_square_meters (float): Maximum square meters for a property to be included in the result. Default is infinity.
        min_price (float): Minimum price for a property to be included in the result. Default is 0.
        max_price (float): Maximum price for a property to be included in the result. Default is infinity.

    Returns:
        List[Dict]: A list of filtered property dictionaries that match the given criteria.
    """
    # Validate inputs
    if min_square_meters < 0 or min_price < 0:
        raise ValueError("Minimum square meters and price cannot be negative.")
    if max_square_meters <= 0 or max_price <= 0:
        raise ValueError("Maximum square meters and price must be positive.")

    # Filter properties based on criteria
    filtered_properties = []
    for property in properties:
        try:
            # Ensure required keys exist and are numeric
            kvadratura = float(property.get('Kvadratura', 0))
            cijena = float(property.get('Cijena', 0))
            
            # Apply filtering criteria
            if (min_square_meters <= kvadratura <= max_square_meters and
                min_price <= cijena <= max_price):
                filtered_properties.append(property)
        except (ValueError, TypeError):
            # Skip properties with invalid data
            continue

    return filtered_properties

# Example usage (for testing purposes):
# properties_list = [
#     {"Kvadratura": 45, "Cijena": 75000, "Location": "Podgorica"},
#     {"Kvadratura": 60, "Cijena": 120000, "Location": "Budva"},
#     {"Kvadratura": 30, "Cijena": 50000, "Location": "Podgorica"},
#     {"Kvadratura": 80, "Cijena": 200000, "Location": "Kotor"}
# ]
# filtered = filter_properties(properties_list, min_square_meters=40, max_square_meters=70, min_price=60000, max_price=150000)
# print(filtered)
```
