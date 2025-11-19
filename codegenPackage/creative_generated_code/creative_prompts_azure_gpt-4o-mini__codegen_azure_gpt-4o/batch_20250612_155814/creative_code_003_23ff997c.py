"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beenzonsol.net
Prompt: Develop a code snippet that implements a search feature for real estate listings in Las Vegas, using the selling strategies and market insights from AndySellsVegas.com.
Generated: DETERMINISTIC_23ff997c39aacf6e
Batch ID: 20250612_155814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class RealEstateListing:
    """
    Class representing a Real Estate Listing with attributes for property details.
    """
    def __init__(self, property_id, name, price, bedrooms, bathrooms, sqft, location, selling_strategy):
        self.property_id = property_id
        self.name = name
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.sqft = sqft
        self.location = location
        self.selling_strategy = selling_strategy

    def to_dict(self):
        """
        Convert the object to a dictionary for easier JSON serialization.
        """
        return {
            "property_id": self.property_id,
            "name": self.name,
            "price": self.price,
            "bedrooms": self.bedrooms,
            "bathrooms": self.bathrooms,
            "sqft": self.sqft,
            "location": self.location,
            "selling_strategy": self.selling_strategy,
        }


class RealEstateSearch:
    """
    Class to search real estate listings based on filters and strategies.
    """
    def __init__(self, listings):
        self.listings = listings

    def search_listings(self, max_price=None, min_bedrooms=None, location=None, strategy=None):
        """
        Search listings based on filters: max_price, min_bedrooms, location, and selling_strategy.
        """
        try:
            results = self.listings
            # Filter by maximum price
            if max_price is not None:
                results = [listing for listing in results if listing.price <= max_price]

            # Filter by minimum bedrooms
            if min_bedrooms is not None:
                results = [listing for listing in results if listing.bedrooms >= min_bedrooms]

            # Filter by location
            if location is not None:
                results = [listing for listing in results if location.lower() in listing.location.lower()]

            # Filter by selling strategy
            if strategy is not None:
                results = [listing for listing in results if strategy.lower() in listing.selling_strategy.lower()]

            return results

        except Exception as e:
            # Log and handle unexpected errors
            print(f"An error occurred while searching listings: {e}")
            return []


# Sample data for Real Estate Listings
listings_data = [
    RealEstateListing(1, "Luxury Villa", 750000, 5, 4, 3500, "Las Vegas", "Aggressive Pricing"),
    RealEstateListing(2, "Cozy Condo", 300000, 2, 2, 1200, "Las Vegas", "Targeted Marketing"),
    RealEstateListing(3, "Family Home", 450000, 3, 3, 2500, "Henderson", "Local Networking"),
    RealEstateListing(4, "Modern Apartment", 200000, 1, 1, 800, "Las Vegas", "Online Campaigns"),
]

# Initialize search system with sample data
search_engine = RealEstateSearch(listings_data)

# Example usage of search_listings
try:
    criteria = {
        "max_price": 500000,
        "min_bedrooms": 2,
        "location": "Las Vegas",
        "strategy": "targeted marketing"
    }
    filtered_listings = search_engine.search_listings(
        max_price=criteria["max_price"],
        min_bedrooms=criteria["min_bedrooms"],
        location=criteria["location"],
        strategy=criteria["strategy"]
    )

    # Display results in JSON format
    print(json.dumps([listing.to_dict() for listing in filtered_listings], indent=4))

except Exception as err:
    print(f"An error occurred: {err}")
```
