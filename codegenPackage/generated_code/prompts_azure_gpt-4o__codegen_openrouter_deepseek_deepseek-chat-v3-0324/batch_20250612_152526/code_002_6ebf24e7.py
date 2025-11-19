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
import csv
import json
import os
from datetime import datetime
from typing import List, Dict, Optional, Union

class PropertyListing:
    """Class to represent a property listing."""
    
    def __init__(self, property_id: str, title: str, description: str, 
                 property_type: str, price: float, location: str, 
                 bedrooms: int, bathrooms: int, area_sqft: int, 
                 status: str = "available", listed_date: Optional[str] = None):
        """
        Initialize a property listing.
        
        Args:
            property_id: Unique identifier for the property
            title: Title of the listing
            description: Detailed description
            property_type: Type of property (house, apartment, etc.)
            price: Listing price
            location: Property address/location
            bedrooms: Number of bedrooms
            bathrooms: Number of bathrooms
            area_sqft: Area in square feet
            status: Current status (available, sold, rented)
            listed_date: Date when listed (defaults to current date)
        """
        self.property_id = property_id
        self.title = title
        self.description = description
        self.property_type = property_type
        self.price = price
        self.location = location
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.area_sqft = area_sqft
        self.status = status
        self.listed_date = listed_date if listed_date else datetime.now().strftime("%Y-%m-%d")
    
    def to_dict(self) -> Dict[str, Union[str, int, float]]:
        """Convert property listing to dictionary."""
        return {
            "property_id": self.property_id,
            "title": self.title,
            "description": self.description,
            "property_type": self.property_type,
            "price": self.price,
            "location": self.location,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "area_sqft": self.area_sqft,
            "status": self.status,
            "listed_date": self.listed_date
        }

class PropertyManager:
    """Class to manage property listings."""
    
    def __init__(self, data_file: str = "property_listings.json"):
        """
        Initialize property manager.
        
        Args:
            data_file: Path to JSON file storing listings
        """
        self.data_file = data_file
        self.listings: List[PropertyListing] = []
        self._load_listings()
    
    def _load_listings(self) -> None:
        """Load listings from JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.listings = [PropertyListing(**item) for item in data]
        except Exception as e:
            print(f"Error loading listings: {e}")
            self.listings = []
    
    def _save_listings(self) -> None:
        """Save listings to JSON file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump([listing.to_dict() for listing in self.listings], f, indent=2)
        except Exception as e:
            print(f"Error saving listings: {e}")
    
    def add_listing(self, listing: PropertyListing) -> bool:
        """Add a new property listing."""
        if any(l.property_id == listing.property_id for l in self.listings):
            print(f"Property with ID {listing.property_id} already exists")
            return False
        
        self.listings.append(listing)
        self._save_listings()
        return True
    
    def update_listing(self, property_id: str, **kwargs) -> bool:
        """Update an existing property listing."""
        for listing in self.listings:
            if listing.property_id == property_id:
                for key, value in kwargs.items():
                    if hasattr(listing, key):
                        setattr(listing, key, value)
                self._save_listings()
                return True
        print(f"Property with ID {property_id} not found")
        return False
    
    def remove_listing(self, property_id: str) -> bool:
        """Remove a property listing."""
        for i, listing in enumerate(self.listings):
            if listing.property_id == property_id:
                del self.listings[i]
                self._save_listings()
                return True
        print(f"Property with ID {property_id} not found")
        return False
    
    def get_listing(self, property_id: str) -> Optional[PropertyListing]:
        """Get a property listing by ID."""
        for listing in self.listings:
            if listing.property_id == property_id:
                return listing
        return None
    
    def search_listings(self, **kwargs) -> List[PropertyListing]:
        """
        Search listings based on criteria.
        
        Args:
            kwargs: Search criteria (e.g., property_type="house", bedrooms=3)
        
        Returns:
            List of matching PropertyListing objects
        """
        results = []
        for listing in self.listings:
            match = True
            for key, value in kwargs.items():
                if hasattr(listing, key):
                    if getattr(listing, key) != value:
                        match = False
                        break
                else:
                    match = False
                    break
            if match:
                results.append(listing)
        return results
    
    def export_to_csv(self, filename: str) -> bool:
        """Export listings to CSV file."""
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = [
                    'property_id', 'title', 'description', 'property_type',
                    'price', 'location', 'bedrooms', 'bathrooms',
                    'area_sqft', 'status', 'listed_date'
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for listing in self.listings:
                    writer.writerow(listing.to_dict())
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False
    
    def import_from_csv(self, filename: str) -> bool:
        """Import listings from CSV file."""
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        listing = PropertyListing(
                            property_id=row['property_id'],
                            title=row['title'],
                            description=row['description'],
                            property_type=row['property_type'],
                            price=float(row['price']),
                            location=row['location'],
                            bedrooms=int(row['bedrooms']),
                            bathrooms=int(row['bathrooms']),
                            area_sqft=int(row['area_sqft']),
                            status=row.get('status', 'available'),
                            listed_date=row.get('listed_date')
                        )
                        self.add_listing(listing)
                    except Exception as e:
                        print(f"Error processing row {row}: {e}")
                        continue
            return True
        except Exception as e:
            print(f"Error importing from CSV: {e}")
            return False

def generate_property_id() -> str:
    """Generate a unique property ID."""
    return f"PROP-{datetime.now().strftime('%Y%m%d%H%M%S')}"

def main_menu(manager: PropertyManager) -> None:
    """Display main menu and handle user input."""
    while True:
        print("\nReal Estate Property Management System")
        print("1. Add New Property Listing")
        print("2. Update Property Listing")
        print("3. Remove Property Listing")
        print("4. View Property Listing")
        print("5. Search Listings")
        print("6. Export to CSV")
        print("7. Import from CSV")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            add_listing_menu(manager)
        elif choice == "2":
            update_listing_menu(manager)
        elif choice == "3":
            remove_listing_menu(manager)
        elif choice == "4":
            view_listing_menu(manager)
        elif choice == "5":
            search_listings_menu(manager)
        elif choice == "6":
            export_csv_menu(manager)
        elif choice == "7":
            import_csv_menu(manager)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def add_listing_menu(manager: PropertyManager) -> None:
    """Handle adding a new property listing."""
    print("\nAdd New Property Listing")
    property_id = generate_property_id()
    title = input("Title: ")
    description = input("Description: ")
    property_type = input("Property Type (house/apartment/land): ")
    price = float(input("Price: "))
    location = input("Location: ")
    bedrooms = int(input("Bedrooms: "))
    bathrooms = int(input("Bathrooms: "))
    area_sqft = int(input("Area (sqft): "))
    
    listing = PropertyListing(
        property_id=property_id,
        title=title,
        description=description,
        property_type=property_type,
        price=price,
