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
from typing import List, Dict, Any

def filter_properties(properties: List[Dict[str, Any]], min_kvadratura: float = 0, max_kvadratura: float = float('inf'), 
                      min_cijena: float = 0, max_cijena: float = float('inf')) -> List[Dict[str, Any]]:
    """
    Filters a list of real estate properties based on specified criteria.

    Parameters:
    - properties (List[Dict[str, Any]]): A list of properties, where each property is represented as a dictionary.
    - min_kvadratura (float): Minimum square meters of the property.
    - max_kvadratura (float): Maximum square meters of the property.
    - min_cijena (float): Minimum price of the property.
    - max_cijena (float): Maximum price of the property.

    Returns:
    - List[Dict[str, Any]]: A list of properties that match the criteria.
    
    Raises:
    - ValueError: If min_kvadratura or max_kvadratura is negative.
    - ValueError: If min_cijena or max_cijena is negative.
    """

    # Validate input parameters
    if min_kvadratura < 0 or max_kvadratura < 0:
        raise ValueError("Kvadratura values must be non-negative.")
    if min_cijena < 0 or max_cijena < 0:
        raise ValueError("Cijena values must be non-negative.")
    
    if min_kvadratura > max_kvadratura:
        raise ValueError("Minimum kvadratura cannot be greater than maximum kvadratura.")
    if min_cijena > max_cijena:
        raise ValueError("Minimum cijena cannot be greater than maximum cijena.")
    
    filtered_properties = []
    
    # Filter properties based on given criteria
    for property in properties:
        try:
            kvadratura = property.get("Kvadratura", 0)
            cijena = property.get("Cijena", 0)

            # Check if the property meets the criteria
            if (min_kvadratura <= kvadratura <= max_kvadratura) and (min_cijena <= cijena <= max_cijena):
                filtered_properties.append(property)
        except Exception as e:
            print(f"Error processing property {property}: {e}")
    
    return filtered_properties

# Example usage:
if __name__ == "__main__":
    # Sample data
    properties_list = [
        {"Kvadratura": 50, "Cijena": 80000},
        {"Kvadratura": 70, "Cijena": 120000},
        {"Kvadratura": 30, "Cijena": 50000},
        {"Kvadratura": 100, "Cijena": 200000},
    ]
    
    # Filter properties with specific criteria
    try:
        result = filter_properties(properties_list, min_kvadratura=30, max_kvadratura=75, min_cijena=50000, max_cijena=100000)
        print("Filtered Properties:", result)
    except ValueError as ve:
        print(f"ValueError: {ve}")
```
