"""
Generated Code Metadata:
========================
Original URL: https://kidanah.sa
Prompt: Generate a sample itinerary for a Hajj or Umrah trip using Python, considering factors like travel dates, accommodation, and transportation.
Generated: DETERMINISTIC_e51b16fdca3467c7
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Itinerary:
    """
    A class to represent a Hajj or Umrah trip itinerary.
    """

    def __init__(self, name, start_date, end_date, accommodation, transportation):
        """
        Initialize the itinerary with basic details.

        :param name: Name of the traveler
        :param start_date: Start date of the trip (YYYY-MM-DD)
        :param end_date: End date of the trip (YYYY-MM-DD)
        :param accommodation: Accommodation details (e.g., hotel name)
        :param transportation: Transportation details (e.g., flight, bus)
        """
        self.name = name
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.accommodation = accommodation
        self.transportation = transportation
        self.activities = []

    def _validate_date(self, date_str):
        """
        Validate and parse the date string.

        :param date_str: Date in string format (YYYY-MM-DD)
        :return: Parsed datetime.date object
        :raises ValueError: If the date format is invalid
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD")

    def add_activity(self, date, description):
        """
        Add an activity to the itinerary.

        :param date: Date of the activity (YYYY-MM-DD)
        :param description: Description of the activity
        :raises ValueError: If the activity date is outside the trip dates
        """
        activity_date = self._validate_date(date)
        if not (self.start_date <= activity_date <= self.end_date):
            raise ValueError(f"Activity date {activity_date} is outside the trip dates.")
        self.activities.append({"date": activity_date, "description": description})

    def generate_itinerary(self):
        """
        Generate the full itinerary as a formatted string.

        :return: Formatted itinerary string
        """
        itinerary = f"--- Itinerary for {self.name} ---\n"
        itinerary += f"Trip Dates: {self.start_date} to {self.end_date}\n"
        itinerary += f"Accommodation: {self.accommodation}\n"
        itinerary += f"Transportation: {self.transportation}\n"
        itinerary += "\nActivities:\n"
        if not self.activities:
            itinerary += "No activities planned.\n"
        else:
            for activity in sorted(self.activities, key=lambda x: x["date"]):
                itinerary += f"{activity['date']}: {activity['description']}\n"
        return itinerary


# Example usage
if __name__ == "__main__":
    try:
        # Create an itinerary
        hajj_itinerary = Itinerary(
            name="John Doe",
            start_date="2024-06-01",
            end_date="2024-06-15",
            accommodation="Hilton Makkah Convention Hotel",
            transportation="Round-trip flight with Saudi Airlines"
        )

        # Add activities
        hajj_itinerary.add_activity("2024-06-02", "Arrival in Makkah and check-in to hotel")
        hajj_itinerary.add_activity("2024-06-03", "Perform Umrah rituals")
        hajj_itinerary.add_activity("2024-06-08", "Travel to Mina for Hajj")
        hajj_itinerary.add_activity("2024-06-09", "Day of Arafah")
        hajj_itinerary.add_activity("2024-06-10", "Eid al-Adha and stoning of the Jamarat")
        hajj_itinerary.add_activity("2024-06-14", "Return to Makkah and farewell Tawaf")

        # Generate and print the itinerary
        print(hajj_itinerary.generate_itinerary())

    except Exception as e:
        print(f"Error: {e}")
```
