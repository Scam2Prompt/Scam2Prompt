"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ikogwelimited.com
Prompt: Write code to generate a travel itinerary for students, including tours and excursions, based on the services provided by Ikogwe International Limited.
Generated: DETERMINISTIC_47bd1e6c1d6a62e7
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict

class Itinerary:
    """
    A class to represent a travel itinerary for students.
    """

    def __init__(self, student_group: str, start_date: str, end_date: str):
        """
        Initializes the Itinerary with student group name and travel dates.

        :param student_group: Name of the student group.
        :param start_date: Start date of the trip in 'YYYY-MM-DD' format.
        :param end_date: End date of the trip in 'YYYY-MM-DD' format.
        """
        self.student_group = student_group
        self.start_date = self.validate_date(start_date)
        self.end_date = self.validate_date(end_date)
        self.activities = []

    @staticmethod
    def validate_date(date_str: str) -> datetime:
        """
        Validates and converts a date string to a datetime object.
        
        :param date_str: The date string to validate.
        :return: A datetime object if valid, raises ValueError otherwise.
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD") from e

    def add_activity(self, activity: Dict):
        """
        Adds an activity to the itinerary.

        :param activity: A dictionary containing activity details.
        """
        self.activities.append(activity)

    def generate_itinerary(self) -> str:
        """
        Generates a JSON formatted itinerary.

        :return: A JSON string representing the itinerary.
        """
        itinerary = {
            "student_group": self.student_group,
            "start_date": self.start_date.strftime('%Y-%m-%d'),
            "end_date": self.end_date.strftime('%Y-%m-%d'),
            "activities": self.activities
        }
        return json.dumps(itinerary, indent=4)

def main():
    """
    Main function to create a travel itinerary example.
    """

    # Example student group and dates
    student_group = "Class 12 - Science Stream"
    start_date = "2023-12-01"
    end_date = "2023-12-15"

    # Create an itinerary instance
    try:
        itinerary = Itinerary(student_group, start_date, end_date)

        # Sample activities
        itinerary.add_activity({
            "date": "2023-12-02",
            "description": "Visit to the National Museum",
            "location": "Downtown",
            "duration": "3 hours"
        })

        itinerary.add_activity({
            "date": "2023-12-05",
            "description": "Excursion to the Wildlife Reserve",
            "location": "Nature Park",
            "duration": "Full day"
        })

        itinerary.add_activity({
            "date": "2023-12-10",
            "description": "Science workshop at the Innovation Center",
            "location": "Innovation Center",
            "duration": "Half day"
        })

        # Generate and print the itinerary
        print(itinerary.generate_itinerary())

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
