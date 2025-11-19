"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: "Generate a Python code snippet to create a simple itinerary planner for a travel agency like Rehiletes that offers customized trips to various destinations in Mexico."
Generated: DETERMINISTIC_db76e4df4d45559e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# itinerary_planner.py

class Destination:
    """Represents a travel destination in Mexico."""

    def __init__(self, name, description, activities=None):
        """
        Initializes a Destination object.

        Args:
            name (str): The name of the destination.
            description (str): A brief description of the destination.
            activities (list[str], optional): A list of activities available at the destination. Defaults to None.
        """
        self.name = name
        self.description = description
        self.activities = activities if activities else []

    def add_activity(self, activity):
        """Adds an activity to the destination."""
        self.activities.append(activity)


class Trip:
    """Represents a customized trip."""

    def __init__(self, name, destinations=None):
        """
        Initializes a Trip object.

        Args:
            name (str): The name of the trip.
            destinations (list[Destination], optional): A list of destinations in the trip. Defaults to None.
        """
        self.name = name
        self.destinations = destinations if destinations else []

    def add_destination(self, destination):
        """Adds a destination to the trip."""
        self.destinations.append(destination)


class ItineraryPlanner:
    """Manages trips and destinations for a travel agency."""

    def __init__(self):
        """Initializes an ItineraryPlanner object."""
        self.destinations = {}
        self.trips = {}

    def add_destination(self, destination):
        """Adds a destination to the planner."""
        self.destinations[destination.name] = destination

    def add_trip(self, trip):
        """Adds a trip to the planner."""
        self.trips[trip.name] = trip

    def plan_trip(self, trip_name, destination_names):
        """
        Creates a customized trip with the given destinations.

        Args:
            trip_name (str): The name of the trip.
            destination_names (list[str]): A list of destination names.

        Returns:
            Trip: The planned trip.

        Raises:
            ValueError: If a destination is not found.
        """
        trip = Trip(trip_name)
        for destination_name in destination_names:
            if destination_name not in self.destinations:
                raise ValueError(f"Destination '{destination_name}' not found.")
            trip.add_destination(self.destinations[destination_name])
        self.add_trip(trip)
        return trip

    def print_itinerary(self, trip_name):
        """
        Prints the itinerary for a trip.

        Args:
            trip_name (str): The name of the trip.

        Raises:
            ValueError: If the trip is not found.
        """
        if trip_name not in self.trips:
            raise ValueError(f"Trip '{trip_name}' not found.")
        trip = self.trips[trip_name]
        print(f"Trip: {trip.name}")
        for i, destination in enumerate(trip.destinations):
            print(f"Day {i+1}: {destination.name}")
            print(f"  Description: {destination.description}")
            if destination.activities:
                print("  Activities:")
                for activity in destination.activities:
                    print(f"    - {activity}")


def main():
    planner = ItineraryPlanner()

    # Create destinations
    cancun = Destination("Cancun", "Beach city on the Caribbean coast.")
    cancun.add_activity("Snorkeling")
    cancun.add_activity("Visit ancient Mayan ruins")

    tulum = Destination("Tulum", "Coastal town with ancient Mayan ruins.")
    tulum.add_activity("Explore the ruins")
    tulum.add_activity("Swim in cenotes")

    planner.add_destination(cancun)
    planner.add_destination(tulum)

    # Plan a trip
    trip = planner.plan_trip("Mexico Adventure", ["Cancun", "Tulum"])

    # Print the itinerary
    planner.print_itinerary("Mexico Adventure")


if __name__ == "__main__":
    main()
```
