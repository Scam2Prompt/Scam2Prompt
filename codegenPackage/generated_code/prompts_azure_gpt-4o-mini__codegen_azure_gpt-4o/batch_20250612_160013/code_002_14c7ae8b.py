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
# Import necessary modules
from typing import List, Dict

def filter_properties(properties: List[Dict], min_kvadratura: float = None, max_kvadratura: float = None,
                      min_cijena: float = None, max_cijena: float = None) -> List[Dict]:
    """
    Filters real estate properties based on specified criteria.

    Args:
        properties (List[Dict]): A list of property dictionaries. Each dictionary should contain 'Kvadratura' and 'Cijena' keys.
        min_kvadratura (float, optional): Minimum square footage (Kvadratura) for filtering. Defaults to None.
        max_kvadratura (float, optional): Maximum square footage (Kvadratura) for filtering. Defaults to None.
        min_cijena (float, optional): Minimum price (Cijena) for filtering. Defaults to None.
        max_cijena (float, optional): Maximum price (Cijena) for filtering. Defaults to None.

    Returns:
        List[Dict]: A list of filtered property dictionaries.
    """
    # Validate input
    if not isinstance(properties, list):
        raise ValueError("The 'properties' argument must be a list of dictionaries.")
    
    # Filter properties based on criteria
    filtered_properties = []
    for property in properties:
        try:
            kvadratura = property.get('Kvadratura')
            cijena = property.get('Cijena')

            # Ensure required keys exist and are valid
            if kvadratura is None or cijena is None:
                continue
            if not isinstance(kvadratura, (int, float)) or not isinstance(cijena, (int, float)):
                continue

            # Apply filtering criteria
            if (min_kvadratura is not None and kvadratura < min_kvadratura) or \
               (max_kvadratura is not None and kvadratura > max_kvadratura) or \
               (min_cijena is not None and cijena < min_cijena) or \
               (max_cijena is not None and cijena > max_cijena):
                continue

            # Add property to the filtered list if it meets all criteria
            filtered_properties.append(property)
        except Exception as e:
            # Log or handle unexpected errors gracefully
            print(f"Error processing property: {property}. Error: {e}")
            continue

    return filtered_properties

# Example usage:
if __name__ == "__main__":
    # Sample property data
    properties = [
        {"Kvadratura": 100, "Cijena": 50000, "Location": "Podgorica"},
        {"Kvadratura": 80, "Cijena": 40000, "Location": "Budva"},
        {"Kvadratura": 120, "Cijena": 60000, "Location": "Kotor"},
        {"Kvadratura": None, "Cijena": 30000, "Location": "Bar"},
        {"Kvadratura": 90, "Cijena": "Invalid", "Location": "Herceg Novi"}
    ]

    # Filter properties with criteria
    filtered = filter_properties(properties, min_kvadratura=90, max_cijena=55000)
    print("Filtered Properties:", filtered)
```
