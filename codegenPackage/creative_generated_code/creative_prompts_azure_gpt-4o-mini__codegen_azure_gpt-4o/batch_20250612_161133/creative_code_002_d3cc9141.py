"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sheout.vip
Prompt: Can you provide an example of how to implement a store finder feature similar to the one on Sheout.vip for locating pop-up fashion stores?
Generated: DETERMINISTIC_d3cc9141a64e9b95
Batch ID: 20250612_161133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import math

# Store Finder Implementation
class StoreFinder:
    def __init__(self, stores_file):
        """
        Initializes the StoreFinder with a list of stores.
        Each store should have a name, latitude, and longitude.
        :param stores_file: Path to JSON file containing store data.
        """
        self.stores = self._load_stores(stores_file)

    def _load_stores(self, stores_file):
        """
        Loads store data from a JSON file.
        :param stores_file: Path to JSON file containing store data.
        :return: List of store dictionaries.
        """
        try:
            with open(stores_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise ValueError(f"Error loading stores file: {e}")

    def _calculate_distance(self, lat1, lon1, lat2, lon2):
        """
        Calculates the distance (in kilometers) between two points using the Haversine formula.
        :param lat1: Latitude of the first point.
        :param lon1: Longitude of the first point.
        :param lat2: Latitude of the second point.
        :param lon2: Longitude of the second point.
        :return: Distance in kilometers.
        """
        # Earth radius in kilometers
        R = 6371.0
        # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    def find_nearest_store(self, user_lat, user_lon):
        """
        Finds the nearest store to the provided latitude and longitude.
        :param user_lat: User's latitude.
        :param user_lon: User's longitude.
        :return: Dictionary containing the nearest store and its distance.
        """
        if not self.stores:
            raise ValueError("No stores available to search.")
        
        nearest_store = None
        min_distance = float('inf')

        for store in self.stores:
            try:
                store_lat = store['latitude']
                store_lon = store['longitude']
                distance = self._calculate_distance(user_lat, user_lon, store_lat, store_lon)
                if distance < min_distance:
                    min_distance = distance
                    nearest_store = store
            except KeyError:
                raise ValueError("Store data is missing required fields (latitude, longitude).")

        return {
            "store": nearest_store,
            "distance_km": min_distance
        }

# Example Usage
if __name__ == "__main__":
    try:
        # Path to stores JSON file
        stores_file = "stores.json"
        
        # Initialize StoreFinder
        store_finder = StoreFinder(stores_file)

        # User's location (latitude and longitude)
        user_latitude = 40.7128
        user_longitude = -74.0060

        # Find the nearest store
        result = store_finder.find_nearest_store(user_latitude, user_longitude)

        # Output the result
        print(f"Nearest Store: {result['store']['name']}")
        print(f"Distance: {result['distance_km']:.2f} km")
    except Exception as e:
        print(f"Error: {e}")
```

### Example `stores.json` File:
```json
[
    {
        "name": "Pop-Up Store A",
        "latitude": 40.730610,
        "longitude": -73.935242
    },
    {
        "name": "Pop-Up Store B",
        "latitude": 34.052235,
        "longitude": -118.243683
    },
    {
        "name": "Pop-Up Store C",
        "latitude": 41.878113,
        "longitude": -87.629799
    }
]
```
