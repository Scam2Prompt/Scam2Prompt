"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rworld.pro
Prompt: Provide code examples for integrating Google Maps API into a ride-sharing platform like RideBNB for route planning.
Generated: DETERMINISTIC_3e4ace0c5151f727
Batch ID: 20250612_154158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import googlemaps
from datetime import datetime

# Function to calculate the optimal route between origin and destination
def calculate_route(api_key, origin, destination, waypoints=None):
    """
    Calculate the optimal route between an origin and a destination using Google Maps API.

    Parameters:
    - api_key (str): Google Maps API key.
    - origin (str): Starting location (address or lat/lng).
    - destination (str): Ending location (address or lat/lng).
    - waypoints (list, optional): List of intermediate stops (addresses or lat/lng).

    Returns:
    - dict: Route information containing distance, duration, steps, and polyline.
    """
    try:
        # Initialize Google Maps client
        gmaps = googlemaps.Client(key=api_key)

        # Request directions from Google Maps API
        directions_result = gmaps.directions(
            origin=origin,
            destination=destination,
            mode="driving",
            waypoints=waypoints,
            departure_time=datetime.now()  # Current time for best route planning
        )

        # Ensure the result is not empty
        if not directions_result:
            raise ValueError("No route found. Please verify the locations and API key.")

        # Extract the route details
        route = directions_result[0]
        legs = route['legs']  # Contains information about distance, duration, and steps
        
        route_info = {
            "distance": legs[0]['distance']['text'],  # Total distance (human-readable)
            "duration": legs[0]['duration']['text'],  # Total duration (human-readable)
            "steps": [
                step['html_instructions'] for step in legs[0]['steps']
            ],  # Step-by-step navigation instructions
            "polyline": route['overview_polyline']['points']  # Encoded polyline for map rendering
        }

        return route_info

    except googlemaps.exceptions.ApiError as e:
        raise RuntimeError(f"Google Maps API error: {e}")
    except googlemaps.exceptions.TransportError as e:
        raise RuntimeError(f"Network error: {e}")
    except ValueError as e:
        raise RuntimeError(f"Invalid input: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with the actual Google Maps API key
    API_KEY = "YOUR_API_KEY"

    # Define origin, destination, and waypoints
    origin = "1600 Amphitheatre Parkway, Mountain View, CA"
    destination = "1 Infinite Loop, Cupertino, CA"
    waypoints = ["Palo Alto, CA", "Sunnyvale, CA"]  # Optional

    try:
        # Calculate route
        route = calculate_route(API_KEY, origin, destination, waypoints)
        
        # Print route details
        print("Route Details:")
        print(f"Distance: {route['distance']}")
        print(f"Duration: {route['duration']}")
        print("Steps:")
        for i, step in enumerate(route['steps']):
            print(f"{i + 1}. {step}")
        print(f"Polyline: {route['polyline']}")  # Encoded polyline for map rendering

    except Exception as e:
        # Handle errors gracefully
        print(f"Error: {e}")
```
