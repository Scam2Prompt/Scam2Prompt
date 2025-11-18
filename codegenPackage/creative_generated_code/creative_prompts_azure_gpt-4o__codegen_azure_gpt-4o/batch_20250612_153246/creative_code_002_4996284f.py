"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refrigeratortransport.com
Prompt: Generate code for calculating delivery schedules and optimizing routes for a fleet of chiller vans equipped with GPS tracking, as mentioned on RefrigeratorTransport.com.
Generated: DETERMINISTIC_4996284f3b02e248
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import heapq
import math
from datetime import datetime, timedelta

class GPSLocation:
    """
    Represents a GPS location with latitude and longitude.
    """
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def distance_to(self, other_location):
        """
        Calculates the Haversine distance between two GPS locations.
        :param other_location: GPSLocation object
        :return: Distance in kilometers
        """
        R = 6371  # Radius of the Earth in km
        lat1, lon1, lat2, lon2 = map(math.radians, [self.latitude, self.longitude, other_location.latitude, other_location.longitude])

        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c


class Delivery:
    """
    Represents a delivery with a destination location and delivery deadline.
    """
    def __init__(self, delivery_id, destination, deadline):
        self.delivery_id = delivery_id
        self.destination = destination  # GPSLocation object
        self.deadline = deadline  # datetime object


class ChillerVan:
    """
    Represents a chiller van in the fleet.
    """
    def __init__(self, van_id, current_location):
        self.van_id = van_id
        self.current_location = current_location  # GPSLocation object
        self.route = []  # List of Delivery objects
        self.total_distance = 0  # Total travel distance in km

    def add_delivery(self, delivery, distance_to_delivery):
        """
        Adds a delivery to the van's route and updates the total distance.
        :param delivery: Delivery object
        :param distance_to_delivery: Distance in km to the delivery location
        """
        self.route.append(delivery)
        self.total_distance += distance_to_delivery


def optimize_routes(vans, deliveries):
    """
    Optimizes delivery routes for a fleet of chiller vans.
    :param vans: List of ChillerVan objects
    :param deliveries: List of Delivery objects
    :return: None (routes assigned directly to van objects)
    """
    # Create a priority queue for vans based on their total distance (min-heap)
    van_queue = [(van.total_distance, van) for van in vans]
    heapq.heapify(van_queue)

    for delivery in deliveries:
        # Find the nearest van to the delivery location
        _, nearest_van = min(van_queue, key=lambda x: x[1].current_location.distance_to(delivery.destination))
        distance_to_delivery = nearest_van.current_location.distance_to(delivery.destination)

        # Assign delivery to the nearest van
        nearest_van.add_delivery(delivery, distance_to_delivery)

        # Update the van's location to the delivery destination
        nearest_van.current_location = delivery.destination

        # Rebuild the priority queue to account for updated distances
        van_queue = [(van.total_distance, van) for van in vans]
        heapq.heapify(van_queue)


def generate_delivery_schedule(vans):
    """
    Generates a delivery schedule for each van.
    :param vans: List of ChillerVan objects
    :return: Schedule dictionary mapping van IDs to delivery routes and times
    """
    schedule = {}

    for van in vans:
        van_schedule = []
        current_time = datetime.now()

        for delivery in van.route:
            distance = van.current_location.distance_to(delivery.destination)
            travel_time = timedelta(hours=distance / 60)  # Assume an average speed of 60 km/h
            arrival_time = current_time + travel_time

            # Update current time to include travel time
            current_time = arrival_time

            van_schedule.append({
                'delivery_id': delivery.delivery_id,
                'arrival_time': arrival_time.strftime('%Y-%m-%d %H:%M:%S'),
                'deadline': delivery.deadline.strftime('%Y-%m-%d %H:%M:%S')
            })

        schedule[van.van_id] = van_schedule

    return schedule


# Example usage:
if __name__ == '__main__':
    # Initialize fleet of chiller vans
    vans = [
        ChillerVan('van_1', GPSLocation(40.7128, -74.0060)),  # New York City
        ChillerVan('van_2', GPSLocation(34.0522, -118.2437)),  # Los Angeles
        ChillerVan('van_3', GPSLocation(41.8781, -87.6298))   # Chicago
    ]

    # Initialize delivery requests
    deliveries = [
        Delivery('delivery_1', GPSLocation(40.730610, -73.935242), datetime(2023, 10, 10, 14, 0)),  # NYC
        Delivery('delivery_2', GPSLocation(34.147785, -118.144516), datetime(2023, 10, 11, 9, 0)),  # Pasadena, CA
        Delivery('delivery_3', GPSLocation(41.850033, -87.650052), datetime(2023, 10, 10, 12, 0))   # Chicago
    ]

    # Optimize routes
    optimize_routes(vans, deliveries)

    # Generate schedule
    delivery_schedule = generate_delivery_schedule(vans)

    # Output the schedule
    for van_id, schedule in delivery_schedule.items():
        print(f"Van {van_id} Schedule:")
        for entry in schedule:
            print(f"  Delivery ID: {entry['delivery_id']}, Arrival Time: {entry['arrival_time']}, Deadline: {entry['deadline']}")
```
