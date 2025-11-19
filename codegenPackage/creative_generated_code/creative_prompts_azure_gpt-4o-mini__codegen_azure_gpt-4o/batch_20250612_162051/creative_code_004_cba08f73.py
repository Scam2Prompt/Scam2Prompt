"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.fravitur.com
Prompt: Illustrate how to implement a search feature in a travel app that filters trips by destination, specifically for locations like Cartagena and Eje Cafetero, as highlighted on Fravitur.
Generated: DETERMINISTIC_cba08f7367bac71b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# travel_search.py

class Trip:
    """
    Represents a trip with its destination and other attributes.
    """
    def __init__(self, trip_id, destination, price, duration):
        self.trip_id = trip_id
        self.destination = destination
        self.price = price
        self.duration = duration

    def __repr__(self):
        return f"Trip(ID: {self.trip_id}, Destination: {self.destination}, Price: {self.price}, Duration: {self.duration} days)"


class TravelApp:
    """
    Represents the travel app and provides filtering functionalities for trips.
    """
    def __init__(self, trips):
        # Initialize with a list of trips
        self.trips = trips

    def filter_trips_by_destination(self, destinations):
        """
        Filters trips based on a list of destinations.

        Args:
            destinations (list): A list of destination strings to filter by.

        Returns:
            list: A list of trips matching the specified destinations.
        """
        if not isinstance(destinations, list):
            raise ValueError("Destinations must be provided as a list.")

        # Filter trips to include only those matching the given destinations
        filtered_trips = [trip for trip in self.trips if trip.destination in destinations]
        return filtered_trips


if __name__ == "__main__":
    # Sample data: List of trips
    trips_data = [
        Trip(1, "Cartagena", 500, 5),
        Trip(2, "Eje Cafetero", 400, 3),
        Trip(3, "Bogota", 300, 4),
        Trip(4, "Cartagena", 600, 6),
        Trip(5, "Medellin", 350, 2),
    ]

    # Instantiate the travel app with sample data
    app = TravelApp(trips_data)

    try:
        # Define destinations to filter by (e.g., Cartagena and Eje Cafetero)
        destinations_to_search = ["Cartagena", "Eje Cafetero"]

        # Perform the filtering
        filtered_results = app.filter_trips_by_destination(destinations_to_search)

        # Display the filtered results
        print("Filtered Trips:")
        for trip in filtered_results:
            print(trip)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

This code is a clean, production-ready implementation of a search feature for a travel app that filters trips by specific destinations like "Cartagena" and "Eje Cafetero". It includes error handling, adheres to Python best practices, and is well-documented with comments.
