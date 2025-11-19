"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Write a program to manage a "For Sale" section for tractor pulling equipment, similar to the listings for puller tires and mini chassis on jobbo.com.au.
Generated: DETERMINISTIC_f58cd4b323daa9ad
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# equipment_listing.py

from enum import Enum
from typing import List, Dict

class EquipmentType(str, Enum):
    """Types of tractor pulling equipment"""
    PULLER_TIRE = "puller_tire"
    MINI_CHASSIS = "mini_chassis"
    OTHER = "other"

class EquipmentListing:
    """Represents a listing for tractor pulling equipment"""

    def __init__(self, 
                 listing_id: int, 
                 equipment_type: EquipmentType, 
                 title: str, 
                 description: str, 
                 price: float, 
                 location: str, 
                 contact_info: str):
        """
        Initializes an EquipmentListing object.

        Args:
        - listing_id (int): Unique identifier for the listing
        - equipment_type (EquipmentType): Type of equipment being listed
        - title (str): Title of the listing
        - description (str): Description of the equipment
        - price (float): Price of the equipment
        - location (str): Location of the equipment
        - contact_info (str): Contact information for the seller
        """
        self.listing_id = listing_id
        self.equipment_type = equipment_type
        self.title = title
        self.description = description
        self.price = price
        self.location = location
        self.contact_info = contact_info

    def __str__(self):
        return f"Listing {self.listing_id}: {self.title} - {self.equipment_type.value}"

class EquipmentListingManager:
    """Manages a collection of equipment listings"""

    def __init__(self):
        self.listings: Dict[int, EquipmentListing] = {}

    def add_listing(self, listing: EquipmentListing):
        """
        Adds a new listing to the collection.

        Args:
        - listing (EquipmentListing): The listing to add
        """
        if listing.listing_id in self.listings:
            raise ValueError("Listing ID already exists")
        self.listings[listing.listing_id] = listing

    def remove_listing(self, listing_id: int):
        """
        Removes a listing from the collection.

        Args:
        - listing_id (int): The ID of the listing to remove
        """
        if listing_id not in self.listings:
            raise ValueError("Listing ID does not exist")
        del self.listings[listing_id]

    def get_listing(self, listing_id: int) -> EquipmentListing:
        """
        Retrieves a listing by its ID.

        Args:
        - listing_id (int): The ID of the listing to retrieve

        Returns:
        - EquipmentListing: The listing with the specified ID, or None if not found
        """
        return self.listings.get(listing_id)

    def list_all(self) -> List[EquipmentListing]:
        """
        Retrieves a list of all listings.

        Returns:
        - List[EquipmentListing]: A list of all equipment listings
        """
        return list(self.listings.values())

def main():
    # Create an equipment listing manager
    manager = EquipmentListingManager()

    try:
        # Create some sample listings
        listing1 = EquipmentListing(
            listing_id=1,
            equipment_type=EquipmentType.PULLER_TIRE,
            title="Puller Tire for Sale",
            description="Good condition puller tire for sale",
            price=100.0,
            location="Location 1",
            contact_info="Contact 1"
        )

        listing2 = EquipmentListing(
            listing_id=2,
            equipment_type=EquipmentType.MINI_CHASSIS,
            title="Mini Chassis for Sale",
            description="Good condition mini chassis for sale",
            price=500.0,
            location="Location 2",
            contact_info="Contact 2"
        )

        # Add listings to the manager
        manager.add_listing(listing1)
        manager.add_listing(listing2)

        # Print all listings
        print("All Listings:")
        for listing in manager.list_all():
            print(listing)
            print(f"  Type: {listing.equipment_type.value}")
            print(f"  Price: ${listing.price:.2f}")
            print(f"  Location: {listing.location}")
            print(f"  Contact: {listing.contact_info}")
            print()

        # Retrieve a listing by ID
        retrieved_listing = manager.get_listing(1)
        if retrieved_listing:
            print("Retrieved Listing:")
            print(retrieved_listing)
        else:
            print("Listing not found")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
