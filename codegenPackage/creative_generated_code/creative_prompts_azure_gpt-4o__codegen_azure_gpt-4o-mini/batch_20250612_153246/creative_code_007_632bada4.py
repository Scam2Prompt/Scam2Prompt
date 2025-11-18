"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dominguezparra.com
Prompt: Write code to implement a search filter for properties, similar to the "Tipo de Inmueble" and "Tipo de Gestión" filters on Dominguez Parra's website, using JavaScript or Python.
Generated: DETERMINISTIC_632bada4c546ec73
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# PropertySearchFilter.py

class Property:
    """Class to represent a real estate property."""
    def __init__(self, property_type, management_type, price):
        self.property_type = property_type
        self.management_type = management_type
        self.price = price

class PropertySearchFilter:
    """Class to filter properties based on type and management type."""
    
    def __init__(self, properties):
        """Initialize with a list of properties."""
        if not isinstance(properties, list):
            raise ValueError("Properties should be a list of Property instances.")
        self.properties = properties

    def filter(self, property_type=None, management_type=None):
        """Filter properties based on property type and management type."""
        if property_type is not None and not isinstance(property_type, str):
            raise ValueError("Property type must be a string.")
        if management_type is not None and not isinstance(management_type, str):
            raise ValueError("Management type must be a string.")

        filtered_properties = self.properties
        
        if property_type:
            filtered_properties = [prop for prop in filtered_properties if prop.property_type == property_type]
        
        if management_type:
            filtered_properties = [prop for prop in filtered_properties if prop.management_type == management_type]
        
        return filtered_properties

# Example usage
if __name__ == "__main__":
    # Sample properties
    properties = [
        Property("Apartment", "Sale", 250000),
        Property("House", "Rent", 1500),
        Property("Apartment", "Rent", 1200),
        Property("Commercial", "Sale", 500000),
    ]
    
    search_filter = PropertySearchFilter(properties)
    
    # Filter properties by type and management
    try:
        filtered = search_filter.filter(property_type="Apartment", management_type="Rent")
        for prop in filtered:
            print(f"{prop.property_type} - {prop.management_type} - ${prop.price}")
    except ValueError as e:
        print(f"Error: {e}")
```
