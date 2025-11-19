"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: "Generate a Python script to manage real estate properties, including apartments and houses for rent or sale in Neiva, Huila, Colombia, with features for search by location and property type."
Generated: DETERMINISTIC_8ec0e99522165c20
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# real_estate_manager.py

class Property:
    """Base class for real estate properties."""

    def __init__(self, id, location, price, property_type, status):
        """
        Initialize a Property object.

        Args:
            id (int): Unique identifier for the property.
            location (str): Location of the property.
            price (float): Price of the property.
            property_type (str): Type of property (apartment or house).
            status (str): Status of the property (rent or sale).
        """
        self.id = id
        self.location = location
        self.price = price
        self.property_type = property_type
        self.status = status

    def __str__(self):
        return f"ID: {self.id}, Location: {self.location}, Price: {self.price}, Type: {self.property_type}, Status: {self.status}"


class Apartment(Property):
    """Class for apartment properties."""

    def __init__(self, id, location, price, status, num_bedrooms, num_bathrooms, sqft):
        """
        Initialize an Apartment object.

        Args:
            id (int): Unique identifier for the apartment.
            location (str): Location of the apartment.
            price (float): Price of the apartment.
            status (str): Status of the apartment (rent or sale).
            num_bedrooms (int): Number of bedrooms in the apartment.
            num_bathrooms (int): Number of bathrooms in the apartment.
            sqft (int): Square footage of the apartment.
        """
        super().__init__(id, location, price, "Apartment", status)
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.sqft = sqft

    def __str__(self):
        return super().__str__() + f", Bedrooms: {self.num_bedrooms}, Bathrooms: {self.num_bathrooms}, Sqft: {self.sqft}"


class House(Property):
    """Class for house properties."""

    def __init__(self, id, location, price, status, num_bedrooms, num_bathrooms, sqft, lot_size):
        """
        Initialize a House object.

        Args:
            id (int): Unique identifier for the house.
            location (str): Location of the house.
            price (float): Price of the house.
            status (str): Status of the house (rent or sale).
            num_bedrooms (int): Number of bedrooms in the house.
            num_bathrooms (int): Number of bathrooms in the house.
            sqft (int): Square footage of the house.
            lot_size (float): Lot size of the house.
        """
        super().__init__(id, location, price, "House", status)
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.sqft = sqft
        self.lot_size = lot_size

    def __str__(self):
        return super().__str__() + f", Bedrooms: {self.num_bedrooms}, Bathrooms: {self.num_bathrooms}, Sqft: {self.sqft}, Lot Size: {self.lot_size}"


class RealEstateManager:
    """Class for managing real estate properties."""

    def __init__(self):
        self.properties = []

    def add_property(self, property):
        """
        Add a property to the manager.

        Args:
            property (Property): Property to add.
        """
        self.properties.append(property)

    def search_by_location(self, location):
        """
        Search for properties by location.

        Args:
            location (str): Location to search for.

        Returns:
            list: List of properties in the specified location.
        """
        return [prop for prop in self.properties if prop.location.lower() == location.lower()]

    def search_by_property_type(self, property_type):
        """
        Search for properties by type.

        Args:
            property_type (str): Type of property to search for (apartment or house).

        Returns:
            list: List of properties of the specified type.
        """
        return [prop for prop in self.properties if prop.property_type.lower() == property_type.lower()]

    def search_by_status(self, status):
        """
        Search for properties by status.

        Args:
            status (str): Status of property to search for (rent or sale).

        Returns:
            list: List of properties with the specified status.
        """
        return [prop for prop in self.properties if prop.status.lower() == status.lower()]


def main():
    manager = RealEstateManager()

    while True:
        print("\nReal Estate Manager")
        print("1. Add Property")
        print("2. Search by Location")
        print("3. Search by Property Type")
        print("4. Search by Status")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            id = int(input("Enter property ID: "))
            location = input("Enter property location: ")
            price = float(input("Enter property price: "))
            property_type = input("Enter property type (apartment or house): ")
            status = input("Enter property status (rent or sale): ")

            if property_type.lower() == "apartment":
                num_bedrooms = int(input("Enter number of bedrooms: "))
                num_bathrooms = int(input("Enter number of bathrooms: "))
                sqft = int(input("Enter square footage: "))
                prop = Apartment(id, location, price, status, num_bedrooms, num_bathrooms, sqft)
            elif property_type.lower() == "house":
                num_bedrooms = int(input("Enter number of bedrooms: "))
                num_bathrooms = int(input("Enter number of bathrooms: "))
                sqft = int(input("Enter square footage: "))
                lot_size = float(input("Enter lot size: "))
                prop = House(id, location, price, status, num_bedrooms, num_bathrooms, sqft, lot_size)
            else:
                print("Invalid property type.")
                continue

            manager.add_property(prop)
            print("Property added successfully.")

        elif choice == "2":
            location = input("Enter location to search: ")
            results = manager.search_by_location(location)
            if results:
                for prop in results:
                    print(prop)
            else:
                print("No properties found in that location.")

        elif choice == "3":
            property_type = input("Enter property type to search (apartment or house): ")
            results = manager.search_by_property_type(property_type)
            if results:
                for prop in results:
                    print(prop)
            else:
                print("No properties found of that type.")

        elif choice == "4":
            status = input("Enter status to search (rent or sale): ")
            results = manager.search_by_status(status)
            if results:
                for prop in results:
                    print(prop)
            else:
                print("No properties found with that status.")

        elif choice == "5":
            break

        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
```
