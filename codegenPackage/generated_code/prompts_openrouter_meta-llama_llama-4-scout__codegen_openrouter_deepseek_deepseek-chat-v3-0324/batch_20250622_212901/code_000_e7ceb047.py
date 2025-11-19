"""
Generated Code Metadata:
========================
Original URL: https://fodyem.com
Prompt: Write a Python code snippet to create a travel itinerary for a trip to Senegal, including activities like "Plongée sous marine" and "Camping Ado", with estimated costs and durations.
Generated: DETERMINISTIC_e7ceb047b668f984
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class TravelItinerary:
    """
    A class to create and manage a travel itinerary for Senegal.
    """
    
    def __init__(self, trip_name, start_date, end_date):
        """
        Initialize the itinerary with trip details.
        
        Args:
            trip_name (str): Name of the trip
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
        """
        self.trip_name = trip_name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        self.activities = []
        self.total_cost = 0.0
        
    def add_activity(self, name, date, duration_hours, cost_usd, description=""):
        """
        Add an activity to the itinerary.
        
        Args:
            name (str): Name of the activity
            date (str): Date in YYYY-MM-DD format
            duration_hours (float): Duration in hours
            cost_usd (float): Cost in USD
            description (str, optional): Description of the activity
        """
        try:
            activity_date = datetime.strptime(date, "%Y-%m-%d").date()
            if activity_date < self.start_date or activity_date > self.end_date:
                raise ValueError("Activity date outside trip dates")
                
            activity = {
                "name": name,
                "date": date,
                "duration_hours": duration_hours,
                "cost_usd": cost_usd,
                "description": description
            }
            self.activities.append(activity)
            self.total_cost += cost_usd
        except ValueError as e:
            print(f"Error adding activity: {e}")
    
    def generate_itinerary(self):
        """
        Generate a formatted itinerary with all activities.
        
        Returns:
            dict: Complete itinerary details
        """
        return {
            "trip_name": self.trip_name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "total_days": (self.end_date - self.start_date).days + 1,
            "total_cost_usd": round(self.total_cost, 2),
            "activities": sorted(self.activities, key=lambda x: x["date"])
        }
    
    def save_to_file(self, filename):
        """
        Save the itinerary to a JSON file.
        
        Args:
            filename (str): Name of the output file
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.generate_itinerary(), f, indent=4)
            print(f"Itinerary saved to {filename}")
        except IOError as e:
            print(f"Error saving file: {e}")

# Example usage
if __name__ == "__main__":
    # Create itinerary
    senegal_trip = TravelItinerary(
        trip_name="Senegal Adventure",
        start_date="2023-11-15",
        end_date="2023-11-25"
    )
    
    # Add activities
    senegal_trip.add_activity(
        name="Plongée sous marine",
        date="2023-11-16",
        duration_hours=3.5,
        cost_usd=120.00,
        description="Scuba diving in the beautiful waters of Senegal"
    )
    
    senegal_trip.add_activity(
        name="Camping Ado",
        date="2023-11-18",
        duration_hours=24,
        cost_usd=75.50,
        description="Overnight camping experience in Ado"
    )
    
    senegal_trip.add_activity(
        name="Gorée Island Visit",
        date="2023-11-20",
        duration_hours=5,
        cost_usd=45.00,
        description="Historical tour of Gorée Island"
    )
    
    # Generate and save itinerary
    itinerary = senegal_trip.generate_itinerary()
    print(json.dumps(itinerary, indent=4))
    senegal_trip.save_to_file("senegal_itinerary.json")
```
