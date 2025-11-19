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
import json
import os
from typing import List, Dict, Optional, Union

class Property:
    """Base class for all property types."""
    def __init__(
        self,
        property_id: str,
        title: str,
        description: str,
        location: str,
        price: float,
        area: float,
        bedrooms: int,
        bathrooms: int,
        transaction_type: str,
        property_type: str
    ):
        self.property_id = property_id
        self.title = title
        self.description = description
        self.location = location
        self.price = price
        self.area = area
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.transaction_type = transaction_type  # "rent" or "sale"
        self.property_type = property_type  # "apartment" or "house"

    def to_dict(self) -> Dict:
        """Convert property details to dictionary."""
        return {
            "property_id": self.property_id,
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "price": self.price,
            "area": self.area,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "transaction_type": self.transaction_type,
            "property_type": self.property_type
        }

class Apartment(Property):
    """Class representing an apartment property."""
    def __init__(
        self,
        property_id: str,
        title: str,
        description: str,
        location: str,
        price: float,
        area: float,
        bedrooms: int,
        bathrooms: int,
        transaction_type: str,
        floor: int
    ):
        super().__init__(
            property_id, title, description, location, price,
            area, bedrooms, bathrooms, transaction_type, "apartment"
        )
        self.floor = floor

    def to_dict(self) -> Dict:
        """Convert apartment details to dictionary."""
        property_dict = super().to_dict()
        property_dict["floor"] = self.floor
        return property_dict

class House(Property):
    """Class representing a house property."""
    def __init__(
        self,
        property_id: str,
        title: str,
        description: str,
        location: str,
        price: float,
        area: float,
        bedrooms: int,
        bathrooms: int,
        transaction_type: str,
        has_garden: bool,
        has_pool: bool
    ):
        super().__init__(
            property_id, title, description, location, price,
            area, bedrooms, bathrooms, transaction_type, "house"
        )
        self.has_garden = has_garden
        self.has_pool = has_pool

    def to_dict(self) -> Dict:
        """Convert house details to dictionary."""
        property_dict = super().to_dict()
        property_dict["has_garden"] = self.has_garden
        property_dict["has_pool"] = self.has_pool
        return property_dict

class PropertyManager:
    """Manages property operations including CRUD and search."""
    def __init__(self, data_file: str = "properties.json"):
        self.data_file = data_file
        self.properties: List[Property] = []
        self._load_properties()

    def _load_properties(self) -> None:
        """Load properties from JSON file."""
        if not os.path.exists(self.data_file):
            self._save_properties()
            return

        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                for item in data:
                    if item["property_type"] == "apartment":
                        self.properties.append(
                            Apartment(
                                item["property_id"],
                                item["title"],
                                item["description"],
                                item["location"],
                                item["price"],
                                item["area"],
                                item["bedrooms"],
                                item["bathrooms"],
                                item["transaction_type"],
                                item["floor"]
                            )
                        )
                    elif item["property_type"] == "house":
                        self.properties.append(
                            House(
                                item["property_id"],
                                item["title"],
                                item["description"],
                                item["location"],
                                item["price"],
                                item["area"],
                                item["bedrooms"],
                                item["bathrooms"],
                                item["transaction_type"],
                                item["has_garden"],
                                item["has_pool"]
                            )
                        )
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error loading properties: {e}")
            self.properties = []

    def _save_properties(self) -> None:
        """Save properties to JSON file."""
        try:
            with open(self.data_file, "w", encoding="utf-8") as file:
                json.dump(
                    [prop.to_dict() for prop in self.properties],
                    file,
                    indent=4,
                    ensure_ascii=False
                )
        except IOError as e:
            print(f"Error saving properties: {e}")

    def add_property(self, property: Property) -> bool:
        """Add a new property."""
        if any(p.property_id == property.property_id for p in self.properties):
            print(f"Property with ID {property.property_id} already exists.")
            return False
        self.properties.append(property)
        self._save_properties()
        return True

    def update_property(self, property_id: str, updated_property: Property) -> bool:
        """Update an existing property."""
        for i, prop in enumerate(self.properties):
            if prop.property_id == property_id:
                self.properties[i] = updated_property
                self._save_properties()
                return True
        print(f"Property with ID {property_id} not found.")
        return False

    def delete_property(self, property_id: str) -> bool:
        """Delete a property."""
        for i, prop in enumerate(self.properties):
            if prop.property_id == property_id:
                del self.properties[i]
                self._save_properties()
                return True
        print(f"Property with ID {property_id} not found.")
        return False

    def get_property(self, property_id: str) -> Optional[Property]:
        """Get a property by ID."""
        for prop in self.properties:
            if prop.property_id == property_id:
                return prop
        return None

    def search_properties(
        self,
        location: Optional[str] = None,
        property_type: Optional[str] = None,
        transaction_type: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        min_bedrooms: Optional[int] = None,
        max_bedrooms: Optional[int] = None
    ) -> List[Property]:
        """Search properties based on criteria."""
        results = self.properties

        if location:
            results = [p for p in results if location.lower() in p.location.lower()]
        if property_type:
            results = [p for p in results if p.property_type == property_type.lower()]
        if transaction_type:
            results = [p for p in results if p.transaction_type == transaction_type.lower()]
        if min_price is not None:
            results = [p for p in results if p.price >= min_price]
        if max_price is not None:
            results = [p for p in results if p.price <= max_price]
        if min_bedrooms is not None:
            results = [p for p in results if p.bedrooms >= min_bedrooms]
        if max_bedrooms is not None:
            results = [p for p in results if p.bedrooms <= max_bedrooms]

        return results

def main():
    """Main function to demonstrate property management."""
    manager = PropertyManager()

    # Example usage
    apartment = Apartment(
        property_id="apt001",
        title="Modern Apartment in Downtown Neiva",
        description="Beautiful modern apartment with great views.",
        location="Neiva, Huila",
        price=1200000,
        area=85,
        bedrooms=2,
        bathrooms=1,
        transaction_type="rent",
        floor=5
    )

    house = House(
        property_id="house001",
        title="Spacious House in North Neiva",
        description="Large family house with garden.",
        location="Neiva, Huila",
        price=350000000,
        area=200,
        bedrooms=4,
        bathrooms=3,
        transaction_type="sale",
        has_garden=True,
        has_pool=False
    )

    # Add properties
    manager.add_property(apartment)
    manager.add_property(house)

    # Search properties
    print("\nSearch results for apartments for rent in Neiva:")
    results = manager.search_properties(
        location="Neiva",
        property_type="apartment",
        transaction_type="rent"
    )
    for prop in results:
        print(f"{prop.title} - {prop.price}")

    print("\nSearch results for houses for sale with at least 3 bedrooms:")
    results = manager.search_properties(
        property_type="house",
        transaction_type="sale",
        min_bedrooms=3
    )
    for prop in results:
        print(f"{prop.title} - {prop.price}")

if __name__ == "__main__":
    main()
```
