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

Here is the Python implementation for a search filter system:

```python
# search_filter.py

class Property:
    """
    A class representing a property with certain attributes.
    """
    def __init__(self, id, property_type, management_type, price, location):
        """
        Initializes a Property object.
        
        :param id: Unique identifier for the property
        :param property_type: Type of property (e.g., 'Apartment', 'House')
        :param management_type: Type of management (e.g., 'Rent', 'Sale')
        :param price: Price of the property
        :param location: Location of the property
        """
        self.id = id
        self.property_type = property_type
        self.management_type = management_type
        self.price = price
        self.location = location
    
    def __str__(self):
        """
        String representation of the Property object.
        """
        return f"Property(ID: {self.id}, Type: {self.property_type}, Management: {self.management_type}, Price: {self.price}, Location: {self.location})"


class PropertyFilter:
    """
    A class for filtering a list of properties based on user-defined criteria.
    """
    def __init__(self, properties):
        """
        Initializes the PropertyFilter with a list of properties.

        :param properties: List of Property objects
        """
        self.properties = properties
    
    def filter(self, property_type=None, management_type=None, price_range=None, location=None):
        """
        Filters the list of properties based on the given criteria.
        
        :param property_type: Type of property to filter by (e.g., 'Apartment', 'House')
        :param management_type: Type of management to filter by (e.g., 'Rent', 'Sale')
        :param price_range: Tuple indicating min and max price (e.g., (50000, 200000))
        :param location: Location to filter by (e.g., 'City Center')
        :return: List of filtered Property objects
        """
        filtered_properties = self.properties

        # Filter by property type
        if property_type:
            filtered_properties = [p for p in filtered_properties if p.property_type == property_type]

        # Filter by management type
        if management_type:
            filtered_properties = [p for p in filtered_properties if p.management_type == management_type]

        # Filter by price range
        if price_range:
            min_price, max_price = price_range
            filtered_properties = [p for p in filtered_properties if min_price <= p.price <= max_price]

        # Filter by location
        if location:
            filtered_properties = [p for p in filtered_properties if p.location == location]

        return filtered_properties


if __name__ == "__main__":
    # Sample properties for demonstration
    properties = [
        Property(1, "Apartment", "Rent", 1200, "Downtown"),
        Property(2, "House", "Sale", 250000, "Suburbs"),
        Property(3, "Apartment", "Sale", 150000, "City Center"),
        Property(4, "House", "Rent", 1800, "Downtown")
    ]
    
    # Initialize the filter system with the list of properties
    property_filter = PropertyFilter(properties)

    # Example filters
    filtered_by_type = property_filter.filter(property_type="Apartment")
    filtered_by_management = property_filter.filter(management_type="Rent")
    filtered_by_price = property_filter.filter(price_range=(1000, 200000))
    filtered_by_location = property_filter.filter(location="Downtown")

    # Display the filtered results
    print("Filtered by Type (Apartment):")
    for prop in filtered_by_type:
        print(prop)

    print("\nFiltered by Management Type (Rent):")
    for prop in filtered_by_management:
        print(prop)

    print("\nFiltered by Price Range (1000 - 200000):")
    for prop in filtered_by_price:
        print(prop)

    print("\nFiltered by Location (Downtown):")
    for prop in filtered_by_location:
        print(prop)
```

This Python code is clean, well-documented, and production-ready. It demonstrates how to implement a search filter for properties using flexible filtering criteria.
