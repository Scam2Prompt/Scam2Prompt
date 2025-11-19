"""
Generated Code Metadata:
========================
Original URL: https://www.espglobal.co
Prompt: How can I implement a plug-and-play business model for a real estate agency based on ESP Global's innovative strategies?
Generated: DETERMINISTIC_859446695392bc88
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# real_estate_agency.py

class RealEstateAgency:
    """
    A class to represent a real estate agency that implements a plug-and-play business model.
    """

    def __init__(self, name, location):
        """
        Initializes the RealEstateAgency with a name and location.

        :param name: str - The name of the real estate agency.
        :param location: str - The location of the agency.
        """
        self.name = name
        self.location = location
        self.properties = []  # List to store properties managed by the agency

    def add_property(self, property):
        """
        Adds a property to the agency's portfolio.

        :param property: dict - A dictionary containing property details.
        :raises ValueError: If the property does not contain required fields.
        """
        required_fields = ['id', 'address', 'price', 'type']
        if not all(field in property for field in required_fields):
            raise ValueError("Property must contain id, address, price, and type.")
        
        self.properties.append(property)
        print(f"Property {property['id']} added successfully.")

    def remove_property(self, property_id):
        """
        Removes a property from the agency's portfolio by its ID.

        :param property_id: str - The ID of the property to remove.
        :raises ValueError: If the property ID is not found.
        """
        for property in self.properties:
            if property['id'] == property_id:
                self.properties.remove(property)
                print(f"Property {property_id} removed successfully.")
                return
        raise ValueError(f"Property with ID {property_id} not found.")

    def list_properties(self):
        """
        Lists all properties managed by the agency.

        :return: list - A list of properties.
        """
        return self.properties

    def find_property(self, property_id):
        """
        Finds a property by its ID.

        :param property_id: str - The ID of the property to find.
        :return: dict - The property details if found, else None.
        """
        for property in self.properties:
            if property['id'] == property_id:
                return property
        return None

    def __str__(self):
        """
        Returns a string representation of the agency.

        :return: str - The name and location of the agency.
        """
        return f"{self.name} located at {self.location}"


# Example usage
if __name__ == "__main__":
    try:
        agency = RealEstateAgency("Dream Homes", "New York")
        print(agency)

        # Adding properties
        agency.add_property({'id': '001', 'address': '123 Main St', 'price': 300000, 'type': 'Apartment'})
        agency.add_property({'id': '002', 'address': '456 Elm St', 'price': 450000, 'type': 'House'})

        # Listing properties
        print("Current properties:", agency.list_properties())

        # Finding a property
        property_found = agency.find_property('001')
        print("Found property:", property_found)

        # Removing a property
        agency.remove_property('001')
        print("Current properties after removal:", agency.list_properties())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
