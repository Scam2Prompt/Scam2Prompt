"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sheout.vip
Prompt: Write code to create a search functionality for finding pop-up stores near a user’s location, referencing the store categories (e.g., beauty, fashion museums, women's clothing) listed on Sheout.vip.
Generated: DETERMINISTIC_7cb493195cc24ccb
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from typing import List, Dict, Tuple, Optional

# Define data model for a pop-up store
class PopUpStore:
    def __init__(self, name: str, category: str, latitude: float, longitude: float):
        """
        Initialize a PopUpStore object.
        :param name: Name of the store.
        :param category: Category of the store (e.g., beauty, fashion museums, women's clothing).
        :param latitude: Latitude of the store's location.
        :param longitude: Longitude of the store's location.
        """
        self.name = name
        self.category = category
        self.latitude = latitude
        self.longitude = longitude

# Function to calculate distance between two geographic points using the Haversine formula
def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great-circle distance between two points on the Earth's surface.
    :param lat1: Latitude of the first point.
    :param lon1: Longitude of the first point.
    :param lat2: Latitude of the second point.
    :param lon2: Longitude of the second point.
    :return: Distance in kilometers.
    """
    R = 6371  # Earth radius in kilometers
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# Search functionality
def search_pop_up_stores(stores: List[PopUpStore], user_location: Tuple[float, float], max_distance: float, category_filter: Optional[str] = None) -> List[Dict]:
    """
    Search for pop-up stores near the user's location within a specified distance and optional category filter.
    :param stores: List of PopUpStore objects.
    :param user_location: Tuple containing the user's latitude and longitude.
    :param max_distance: Maximum distance in kilometers to search for stores.
    :param category_filter: Optional category filter (e.g., 'beauty', 'fashion museums', etc.).
    :return: List of dictionaries containing store information.
    """
    user_lat, user_lon = user_location
    results = []

    for store in stores:
        try:
            # Calculate distance between user and store
            distance = calculate_distance(user_lat, user_lon, store.latitude, store.longitude)

            # Check if the store is within the specified distance and matches the category filter
            if distance <= max_distance and (category_filter is None or store.category.lower() == category_filter.lower()):
                results.append({
                    "name": store.name,
                    "category": store.category,
                    "latitude": store.latitude,
                    "longitude": store.longitude,
                    "distance_km": round(distance, 2)
                })
        except Exception as e:
            # Log or handle errors gracefully
            print(f"Error calculating distance for store '{store.name}': {e}")
    
    return results

# Example usage
if __name__ == "__main__":
    # Sample list of pop-up stores
    stores = [
        PopUpStore("Beauty Bliss", "Beauty", 40.712776, -74.005974),
        PopUpStore("Fashion Corner", "Fashion Museums", 34.052235, -118.243683),
        PopUpStore("Women's World", "Women's Clothing", 41.878113, -87.629799),
        PopUpStore("Artistic Fashion", "Fashion Museums", 29.760427, -95.369803)
    ]

    # User's current location
    user_location = (37.774929, -122.419416)  # San Francisco, CA

    # Search for stores within 3000 km, filtered by "Fashion Museums" category
    search_results = search_pop_up_stores(stores, user_location, max_distance=3000, category_filter="Fashion Museums")

    # Print the results
    print("Search Results:")
    for result in search_results:
        print(result)
```
