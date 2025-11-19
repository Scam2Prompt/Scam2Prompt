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
from dataclasses import dataclass
from enum import Enum
from typing import List

class VillaType(Enum):
    """Villa type enumeration"""
    VILLA = "Villa"
    PLOT = "Plot"

class Amenity(Enum):
    """Amenity enumeration"""
    POOL = "Pool"
    GARDEN = "Garden"
    SEA_VIEW = "Sea View"
    FURNISHED = "Furnished"

@dataclass
class Address:
    """Address data class"""
    street: str
    city: str
    region: str
    country: str
    postal_code: str

@dataclass
class Price:
    """Price data class"""
    amount: float
    currency: str

@dataclass
class VillaListing:
    """Villa listing data class"""
    id: int
    type: VillaType
    title: str
    description: str
    address: Address
    price: Price
    amenities: List[Amenity]
    features: List[str]
    created_at: str
    updated_at: str

    def __post_init__(self):
        """Validate villa listing attributes"""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("Invalid villa ID")
        if not self.title or not self.description:
            raise ValueError("Title and description are required")
        if not self.address or not self.price:
            raise ValueError("Address and price are required")

class VillaListingService:
    """Villa listing service class"""
    def __init__(self):
        self.listings = []

    def add_listing(self, listing: VillaListing):
        """Add villa listing"""
        self.listings.append(listing)

    def get_listing(self, id: int):
        """Get villa listing by ID"""
        for listing in self.listings:
            if listing.id == id:
                return listing
        return None

    def update_listing(self, id: int, listing: VillaListing):
        """Update villa listing"""
        existing_listing = self.get_listing(id)
        if existing_listing:
            existing_listing.title = listing.title
            existing_listing.description = listing.description
            existing_listing.address = listing.address
            existing_listing.price = listing.price
            existing_listing.amenities = listing.amenities
            existing_listing.features = listing.features

    def delete_listing(self, id: int):
        """Delete villa listing"""
        self.listings = [listing for listing in self.listings if listing.id != id]

def main():
    # Example usage
    address = Address("Main Street", "Corfu", "Ionian Islands", "Greece", "49100")
    price = Price(1000000.0, "EUR")
    amenities = [Amenity.POOL, Amenity.GARDEN]
    features = ["Furnished", "Sea View"]

    villa_listing = VillaListing(
        id=1,
        type=VillaType.VILLA,
        title="Luxury Villa",
        description="Beautiful villa with pool and garden",
        address=address,
        price=price,
        amenities=amenities,
        features=features,
        created_at="2022-01-01",
        updated_at="2022-01-01"
    )

    service = VillaListingService()
    service.add_listing(villa_listing)

    print(service.get_listing(1).title)

if __name__ == "__main__":
    main()
```
