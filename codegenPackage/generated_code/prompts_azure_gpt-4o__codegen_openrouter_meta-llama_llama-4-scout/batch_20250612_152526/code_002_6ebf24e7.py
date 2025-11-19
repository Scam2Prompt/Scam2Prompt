"""
Generated Code Metadata:
========================
Original URL: https://kigaliinstitute.rw
Prompt: Create a script for real estate brokerage that automates property listing management, inspired by Kigali Institute's real estate brokerage curriculum.
Generated: DETERMINISTIC_6ebf24e73ed19146
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# property_listing_management.py

class Property:
    def __init__(self, listing_id, title, description, price, location, agent):
        """
        Initialize a Property object.

        Args:
            listing_id (int): Unique identifier for the property listing.
            title (str): Brief title of the property.
            description (str): Detailed description of the property.
            price (float): Price of the property.
            location (str): Location of the property.
            agent (str): Agent responsible for the property listing.
        """
        self.listing_id = listing_id
        self.title = title
        self.description = description
        self.price = price
        self.location = location
        self.agent = agent

    def __str__(self):
        return f"Listing ID: {self.listing_id}\nTitle: {self.title}\nDescription: {self.description}\nPrice: {self.price}\nLocation: {self.location}\nAgent: {self.agent}"


class PropertyListingManagement:
    def __init__(self):
        """
        Initialize a PropertyListingManagement object.
        """
        self.properties = {}

    def add_property(self, property):
        """
        Add a property to the listing management system.

        Args:
            property (Property): Property object to be added.

        Raises:
            ValueError: If a property with the same listing ID already exists.
        """
        if property.listing_id in self.properties:
            raise ValueError("Property with the same listing ID already exists.")
        self.properties[property.listing_id] = property

    def remove_property(self, listing_id):
        """
        Remove a property from the listing management system.

        Args:
            listing_id (int): Listing ID of the property to be removed.

        Raises:
            KeyError: If the property with the given listing ID does not exist.
        """
        if listing_id not in self.properties:
            raise KeyError("Property with the given listing ID does not exist.")
        del self.properties[listing_id]

    def update_property(self, listing_id, **kwargs):
        """
        Update a property in the listing management system.

        Args:
            listing_id (int): Listing ID of the property to be updated.
            **kwargs: Updated property attributes.

        Raises:
            KeyError: If the property with the given listing ID does not exist.
        """
        if listing_id not in self.properties:
            raise KeyError("Property with the given listing ID does not exist.")
        for key, value in kwargs.items():
            setattr(self.properties[listing_id], key, value)

    def get_property(self, listing_id):
        """
        Get a property from the listing management system.

        Args:
            listing_id (int): Listing ID of the property to be retrieved.

        Returns:
            Property: Property object with the given listing ID.

        Raises:
            KeyError: If the property with the given listing ID does not exist.
        """
        if listing_id not in self.properties:
            raise KeyError("Property with the given listing ID does not exist.")
        return self.properties[listing_id]

    def list_properties(self):
        """
        List all properties in the listing management system.

        Returns:
            list: List of Property objects.
        """
        return list(self.properties.values())


def main():
    try:
        # Create a PropertyListingManagement object
        plm = PropertyListingManagement()

        # Create Property objects
        property1 = Property(1, "Apartment for Sale", "3 bedroom apartment in Kigali.", 200000, "Kigali", "Agent John")
        property2 = Property(2, "House for Rent", "4 bedroom house in Gisenyi.", 500000, "Gisenyi", "Agent Jane")

        # Add properties to the listing management system
        plm.add_property(property1)
        plm.add_property(property2)

        # List all properties
        print("All Properties:")
        for property in plm.list_properties():
            print(property)
            print("--------------------")

        # Update a property
        plm.update_property(1, price=250000)

        # Get a property
        print("\nUpdated Property:")
        print(plm.get_property(1))

        # Remove a property
        plm.remove_property(2)

        # List all properties after removal
        print("\nAll Properties after Removal:")
        for property in plm.list_properties():
            print(property)
            print("--------------------")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
