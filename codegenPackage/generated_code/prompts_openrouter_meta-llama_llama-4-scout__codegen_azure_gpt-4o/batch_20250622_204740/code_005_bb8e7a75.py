"""
Generated Code Metadata:
========================
Original URL: https://tramsipublicidad.com
Prompt: Develop a code example for a smart transit system that utilizes eco-friendly options and provides valuable data for enhancing passenger satisfaction.
Generated: DETERMINISTIC_bb8e7a75301b80e2
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class TransitSystem:
    """
    A smart transit system that utilizes eco-friendly options and provides valuable data
    for enhancing passenger satisfaction.
    """

    def __init__(self):
        # Initialize transit system with eco-friendly options and passenger data
        self.routes = []
        self.passenger_feedback = []
        self.eco_friendly_options = ["Electric Bus", "Bike Sharing", "Walking Routes"]

    def add_route(self, route_name, stops, eco_option):
        """
        Add a new route to the transit system.

        :param route_name: Name of the route
        :param stops: List of stops on the route
        :param eco_option: Eco-friendly option for the route
        """
        if eco_option not in self.eco_friendly_options:
            raise ValueError(f"Invalid eco-friendly option. Choose from: {self.eco_friendly_options}")
        
        route = {
            "route_name": route_name,
            "stops": stops,
            "eco_option": eco_option,
            "created_at": datetime.datetime.now().isoformat()
        }
        self.routes.append(route)

    def collect_feedback(self, route_name, passenger_name, rating, comments):
        """
        Collect feedback from passengers.

        :param route_name: Name of the route
        :param passenger_name: Name of the passenger
        :param rating: Rating given by the passenger (1-5)
        :param comments: Additional comments from the passenger
        """
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        
        feedback = {
            "route_name": route_name,
            "passenger_name": passenger_name,
            "rating": rating,
            "comments": comments,
            "submitted_at": datetime.datetime.now().isoformat()
        }
        self.passenger_feedback.append(feedback)

    def get_route_data(self):
        """
        Retrieve all route data.

        :return: List of routes
        """
        return self.routes

    def get_feedback_summary(self):
        """
        Generate a summary of passenger feedback.

        :return: Summary of feedback including average rating per route
        """
        summary = {}
        for feedback in self.passenger_feedback:
            route_name = feedback["route_name"]
            if route_name not in summary:
                summary[route_name] = {"total_ratings": 0, "rating_sum": 0, "feedback_count": 0}
            
            summary[route_name]["total_ratings"] += 1
            summary[route_name]["rating_sum"] += feedback["rating"]
            summary[route_name]["feedback_count"] += 1
        
        for route_name, data in summary.items():
            data["average_rating"] = round(data["rating_sum"] / data["total_ratings"], 2)
        
        return summary

    def save_data_to_file(self, filename):
        """
        Save transit system data to a JSON file.

        :param filename: Name of the file to save data
        """
        try:
            data = {
                "routes": self.routes,
                "passenger_feedback": self.passenger_feedback
            }
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving data to file: {e}")

    def load_data_from_file(self, filename):
        """
        Load transit system data from a JSON file.

        :param filename: Name of the file to load data
        """
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.routes = data.get("routes", [])
                self.passenger_feedback = data.get("passenger_feedback", [])
        except Exception as e:
            print(f"Error loading data from file: {e}")


# Example usage
if __name__ == "__main__":
    transit_system = TransitSystem()

    # Add routes
    transit_system.add_route("Route A", ["Stop 1", "Stop 2", "Stop 3"], "Electric Bus")
    transit_system.add_route("Route B", ["Stop 4", "Stop 5", "Stop 6"], "Bike Sharing")

    # Collect feedback
    transit_system.collect_feedback("Route A", "Alice", 5, "Great service!")
    transit_system.collect_feedback("Route A", "Bob", 4, "Comfortable ride.")
    transit_system.collect_feedback("Route B", "Charlie", 3, "Bike quality could be better.")

    # Get route data
    print("Routes:", transit_system.get_route_data())

    # Get feedback summary
    print("Feedback Summary:", transit_system.get_feedback_summary())

    # Save data to file
    transit_system.save_data_to_file("transit_data.json")

    # Load data from file
    transit_system.load_data_from_file("transit_data.json")
    print("Loaded Routes:", transit_system.get_route_data())
    print("Loaded Feedback Summary:", transit_system.get_feedback_summary())
```
