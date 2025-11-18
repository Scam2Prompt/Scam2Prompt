"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Suggest a library or tool to optimize route planning for cleaning teams traveling to multiple locations in the San Fernando Valley, CA area. Include considerations for minimizing travel time.
Generated: DETERMINISTIC_0b4c5550184c3be2
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://maps.googleapis.com/maps/api/directions/json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from typing import List, Dict, Tuple

class RouteOptimizer:
    """A class to optimize route planning for cleaning teams using the Google Maps API."""
    
    def __init__(self, api_key: str):
        """Initialize the RouteOptimizer with the Google Maps API key."""
        self.api_key = api_key

    def optimize_route(self, locations: List[str]) -> Dict[str, any]:
        """
        Optimize the route for multiple locations.

        Args:
            locations (List[str]): A list of addresses/locations to visit.

        Returns:
            Dict[str, any]: A dictionary containing the optimized route and travel time.
        """
        # Check for at least two locations
        if len(locations) < 2:
            raise ValueError("At least two locations are required to optimize a route.")

        # Build the API request URL
        url = "https://maps.googleapis.com/maps/api/directions/json"
        params = {
            "origin": locations[0],
            "destination": locations[0],  # Return to the starting point
            "waypoints": "|".join(locations[1:]),  # Intermediate stops
            "optimizeWaypoints": "true",
            "key": self.api_key
        }

        # Make a request to the Google Maps Directions API
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
        except requests.RequestException as e:
            raise RuntimeError(f"API request failed: {e}")

        # Parse the JSON response
        data = response.json()

        # Check for valid routes
        if data['status'] != 'OK':
            raise RuntimeError(f"Error from API: {data['status']}")

        # Extract optimized route and travel time
        optimized_route = data['routes'][0]
        travel_time = optimized_route['legs'][0]['duration']['text']
        waypoints_order = optimized_route['waypoint_order']

        # Gather the optimized locations based on the waypoint order
        optimized_locations = [locations[0]] + [locations[i + 1] for i in waypoints_order]

        return {
            "optimized_route": optimized_locations,
            "travel_time": travel_time
        }

# Example usage:
if __name__ == "__main__":
    # Replace with your actual Google Maps API key
    GOOGLE_MAPS_API_KEY = "YOUR_API_KEY"

    # Initialize the route optimizer
    optimizer = RouteOptimizer(api_key=GOOGLE_MAPS_API_KEY)

    # List of locations (addresses) to visit
    locations_to_visit = [
        "123 Main St, San Fernando Valley, CA",
        "456 Oak St, San Fernando Valley, CA",
        "789 Pine St, San Fernando Valley, CA"
    ]

    try:
        result = optimizer.optimize_route(locations_to_visit)
        print("Optimized Route:", result["optimized_route"])
        print("Estimated Travel Time:", result["travel_time"])
    except Exception as e:
        print("An error occurred:", e)
```
