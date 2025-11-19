"""
Generated Code Metadata:
========================
Original URL: https://shravrav1.co.il
Prompt: Write a code snippet to integrate Google Maps API with a plumbing service management system to optimize plumber routing and scheduling.
Generated: DETERMINISTIC_fc665f784ed74a06
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import googlemaps
from datetime import datetime
from typing import List, Dict

# Define constants
GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')

class Plumber:
    def __init__(self, id: int, name: str, latitude: float, longitude: float):
        """
        Initialize a Plumber object.

        Args:
        id (int): Unique identifier for the plumber.
        name (str): Name of the plumber.
        latitude (float): Latitude of the plumber's current location.
        longitude (float): Longitude of the plumber's current location.
        """
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

class ServiceRequest:
    def __init__(self, id: int, address: str, latitude: float, longitude: float):
        """
        Initialize a ServiceRequest object.

        Args:
        id (int): Unique identifier for the service request.
        address (str): Address of the service request.
        latitude (float): Latitude of the service request location.
        longitude (float): Longitude of the service request location.
        """
        self.id = id
        self.address = address
        self.latitude = latitude
        self.longitude = longitude

class PlumbingService:
    def __init__(self, plumbers: List[Plumber], service_requests: List[ServiceRequest]):
        """
        Initialize a PlumbingService object.

        Args:
        plumbers (List[Plumber]): List of Plumber objects.
        service_requests (List[ServiceRequest]): List of ServiceRequest objects.
        """
        self.plumbers = plumbers
        self.service_requests = service_requests
        self.gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

    def get_distance_matrix(self, origins: List[Dict[str, float]], destinations: List[Dict[str, float]]) -> Dict:
        """
        Get the distance matrix between plumbers and service requests.

        Args:
        origins (List[Dict[str, float]]): List of plumber locations.
        destinations (List[Dict[str, float]]): List of service request locations.

        Returns:
        Dict: Distance matrix.
        """
        try:
            distance_matrix = self.gmaps.distance_matrix(origins, destinations, mode='driving', traffic_model='pessimistic')
            return distance_matrix
        except googlemaps.exceptions.ApiError as e:
            print(f"Google Maps API error: {e}")
            return {}

    def optimize_plumber_routing(self) -> List[List[int]]:
        """
        Optimize plumber routing and scheduling.

        Returns:
        List[List[int]]: List of plumber-service request pairs.
        """
        # Initialize lists to store plumber and service request locations
        plumber_locations = [{'lat': plumber.latitude, 'lng': plumber.longitude} for plumber in self.plumbers]
        service_request_locations = [{'lat': request.latitude, 'lng': request.longitude} for request in self.service_requests]

        # Get distance matrix
        distance_matrix = self.get_distance_matrix(plumber_locations, service_request_locations)

        # Implement the Hungarian algorithm to find the optimal assignment
        # For simplicity, we will use a nearest neighbor approach
        assignments = []
        for plumber_index, plumber in enumerate(self.plumbers):
            min_distance = float('inf')
            assigned_request_index = -1
            for request_index, request in enumerate(self.service_requests):
                distance = distance_matrix['rows'][plumber_index]['elements'][request_index]['distance']['value']
                if distance < min_distance:
                    min_distance = distance
                    assigned_request_index = request_index
            assignments.append([plumber.id, self.service_requests[assigned_request_index].id])

        return assignments

def main():
    # Example usage
    plumbers = [
        Plumber(1, 'John Doe', 37.7749, -122.4194),
        Plumber(2, 'Jane Doe', 37.7859, -122.4364)
    ]

    service_requests = [
        ServiceRequest(1, '123 Main St', 37.7949, -122.4064),
        ServiceRequest(2, '456 Elm St', 37.8067, -122.4076)
    ]

    plumbing_service = PlumbingService(plumbers, service_requests)
    assignments = plumbing_service.optimize_plumber_routing()
    print(assignments)

if __name__ == "__main__":
    main()
```
