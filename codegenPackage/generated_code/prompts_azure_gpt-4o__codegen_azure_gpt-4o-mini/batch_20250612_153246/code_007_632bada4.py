"""
Generated Code Metadata:
========================
Original URL: https://dominguezparra.com
Prompt: Write code to implement a search filter for properties, similar to the "Tipo de Inmueble" and "Tipo de Gestión" filters on Dominguez Parra's website, using JavaScript or Python.
Generated: DETERMINISTIC_632bada4c546ec73
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# property_filter.py

class Property:
    """Class to represent a property with relevant attributes."""
    
    def __init__(self, property_type, management_type, price, location):
        self.property_type = property_type
        self.management_type = management_type
        self.price = price
        self.location = location

class PropertyFilter:
    """Class to filter properties based on specified criteria."""
    
    def __init__(self, properties):
        """
        Initialize the PropertyFilter with a list of properties.
        
        :param properties: List of Property objects
        """
        self.properties = properties

    def filter_properties(self, property_type=None, management_type=None, max_price=None, location=None):
        """
        Filter properties based on the provided criteria.
        
        :param property_type: Type of property to filter (e.g., 'Apartment', 'House')
        :param management_type: Type of management to filter (e.g., 'Sale', 'Rent')
        :param max_price: Maximum price for filtering
        :param location: Location to filter properties
        :return: List of filtered Property objects
        """
        filtered_properties = self.properties
        
        if property_type:
            filtered_properties = [p for p in filtered_properties if p.property_type == property_type]
        
        if management_type:
            filtered_properties = [p for p in filtered_properties if p.management_type == management_type]
        
        if max_price is not None:
            filtered_properties = [p for p in filtered_properties if p.price <= max_price]
        
        if location:
            filtered_properties = [p for p in filtered_properties if p.location.lower() == location.lower()]
        
        return filtered_properties

def main():
    """Main function to demonstrate the property filtering."""
    # Sample properties
    properties = [
        Property('Apartment', 'Rent', 1200, 'New York'),
        Property('House', 'Sale', 300000, 'Los Angeles'),
        Property('Apartment', 'Sale', 250000, 'New York'),
        Property('Condo', 'Rent', 1500, 'Chicago'),
        Property('House', 'Rent', 2000, 'New York')
    ]
    
    # Create a PropertyFilter instance
    property_filter = PropertyFilter(properties)
    
    # Example filter criteria
    try:
        filtered = property_filter.filter_properties(property_type='Apartment', management_type='Rent', max_price=1300, location='New York')
        print("Filtered Properties:")
        for prop in filtered:
            print(f"{prop.property_type} - {prop.management_type} - ${prop.price} - {prop.location}")
    except Exception as e:
        print(f"An error occurred while filtering properties: {e}")

if __name__ == "__main__":
    main()
```
