"""
Generated Code Metadata:
========================
Original URL: https://corfucoastalcollection.com
Prompt: Design a data structure to represent a villa or plot listing on the Corfu Coastal Collection website, including its attributes and relationships.
Generated: DETERMINISTIC_6f8e05787ccbf843
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Villa:
    """
    Represents a villa listing on the Corfu Coastal Collection website.

    Attributes:
        id (int): Unique identifier for the villa.
        name (str): Name of the villa.
        location (str): Location of the villa.
        price_per_night (float): Price per night for renting the villa.
        amenities (list): List of amenities available in the villa.
        owner (Owner): Owner of the villa.
    """

    def __init__(self, id: int, name: str, location: str, price_per_night: float, amenities: list, owner: 'Owner'):
        self.id = id
        self.name = name
        self.location = location
        self.price_per_night = price_per_night
        self.amenities = amenities
        self.owner = owner

    def __str__(self):
        return f"Villa(id={self.id}, name='{self.name}', location='{self.location}', price_per_night={self.price_per_night}, amenities={self.amenities})"


class Owner:
    """
    Represents the owner of a villa.

    Attributes:
        id (int): Unique identifier for the owner.
        name (str): Name of the owner.
        contact_info (str): Contact information for the owner.
    """

    def __init__(self, id: int, name: str, contact_info: str):
        self.id = id
        self.name = name
        self.contact_info = contact_info

    def __str__(self):
        return f"Owner(id={self.id}, name='{self.name}', contact_info='{self.contact_info}')"


class VillaListing:
    """
    Manages a collection of villa listings.

    Attributes:
        villas (list): List of villas available for rent.
    """

    def __init__(self):
        self.villas = []

    def add_villa(self, villa: Villa):
        """
        Adds a villa to the listing.

        Args:
            villa (Villa): The villa to be added.

        Raises:
            ValueError: If the villa already exists in the listing.
        """
        if any(existing_villa.id == villa.id for existing_villa in self.villas):
            raise ValueError(f"Villa with id {villa.id} already exists.")
        self.villas.append(villa)

    def remove_villa(self, villa_id: int):
        """
        Removes a villa from the listing by its ID.

        Args:
            villa_id (int): The ID of the villa to be removed.

        Raises:
            ValueError: If the villa with the given ID does not exist.
        """
        villa_to_remove = next((villa for villa in self.villas if villa.id == villa_id), None)
        if villa_to_remove is None:
            raise ValueError(f"Villa with id {villa_id} does not exist.")
        self.villas.remove(villa_to_remove)

    def find_villa_by_id(self, villa_id: int) -> Villa:
        """
        Finds a villa by its ID.

        Args:
            villa_id (int): The ID of the villa to find.

        Returns:
            Villa: The villa with the given ID.

        Raises:
            ValueError: If the villa with the given ID does not exist.
        """
        villa = next((villa for villa in self.villas if villa.id == villa_id), None)
        if villa is None:
            raise ValueError(f"Villa with id {villa_id} does not exist.")
        return villa

    def list_villas(self):
        """
        Lists all villas in the collection.

        Returns:
            list: A list of all villas.
        """
        return self.villas


# Example usage
if __name__ == "__main__":
    try:
        owner1 = Owner(id=1, name="John Doe", contact_info="john@example.com")
        villa1 = Villa(id=101, name="Seaside Retreat", location="Corfu", price_per_night=250.0, amenities=["Pool", "WiFi"], owner=owner1)

        listing = VillaListing()
        listing.add_villa(villa1)

        print("Current Villa Listings:")
        for villa in listing.list_villas():
            print(villa)

    except ValueError as e:
        print(f"Error: {e}")
```
