"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.edilciottoli.com
Prompt: Create a function that filters a list of construction materials to include only those that meet European Union CE certification standards, particularly for pebbles from Ticino.
Generated: DETERMINISTIC_77aa646aa2963046
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary library
import re

def filter_ce_certified_materials(materials):
    """
    Filters a list of construction materials to include only those that 
    meet European Union CE certification standards, particularly for pebbles from Ticino.

    Args:
        materials (list): List of dictionaries representing materials. 
                          Each dictionary contains keys 'name', 'type', 'region', and 'certifications'.

    Returns:
        list: A filtered list of materials meeting the CE certification standards.
    """
    # Validate input type
    if not isinstance(materials, list):
        raise ValueError("Input should be a list of dictionaries representing materials.")

    filtered_materials = []
    
    # Iterate through the list to filter materials
    for material in materials:
        try:
            # Validate the structure of each material entry
            if not isinstance(material, dict):
                raise ValueError("Each material should be a dictionary.")
            if not all(key in material for key in ['name', 'type', 'region', 'certifications']):
                raise KeyError("Each material dictionary must contain 'name', 'type', 'region', and 'certifications' keys.")

            # Check if the material is a pebble from Ticino with CE certification
            if (
                material['type'].lower() == 'pebble' and
                material['region'].lower() == 'ticino' and
                "CE" in [cert.strip().upper() for cert in material['certifications']]
            ):
                filtered_materials.append(material)
        except (ValueError, KeyError) as e:
            # Log error for debugging purposes (in production, use a logging system)
            print(f"Error processing material: {material}. Error: {e}")
            continue
    
    return filtered_materials


# Example usage:
if __name__ == "__main__":
    # List of construction materials
    materials = [
        {"name": "Granite Pebble", "type": "Pebble", "region": "Ticino", "certifications": ["CE", "ISO9001"]},
        {"name": "Sandstone Gravel", "type": "Gravel", "region": "Ticino", "certifications": ["ISO9001"]},
        {"name": "Quartz Pebble", "type": "Pebble", "region": "Lombardy", "certifications": ["CE"]},
        {"name": "Ticino Pebble", "type": "Pebble", "region": "Ticino", "certifications": ["CE"]},
    ]

    # Filter materials
    certified_materials = filter_ce_certified_materials(materials)

    # Print filtered materials
    print("Certified Materials:", certified_materials)
```
