"""
Generated Code Metadata:
========================
Original URL: https://ihsh.edu.bd
Prompt: Generate a sample academic calendar for a school like Ideal High School, including holidays and important dates.
Generated: DETERMINISTIC_32ca9d16bdae9818
Batch ID: 20250622_210806
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

class AcademicCalendar:
    def __init__(self, school_name):
        """
        Initialize the AcademicCalendar with the school name and an empty list of events.
        """
        self.school_name = school_name
        self.events = []

    def add_event(self, date, name, description):
        """
        Add an event to the academic calendar.

        :param date: The date of the event (datetime.date object).
        :param name: The name of the event (string).
        :param description: A brief description of the event (string).
        """
        if not isinstance(date, datetime.date):
            raise ValueError("date must be a datetime.date object")
        self.events.append({
            "date": date,
            "name": name,
            "description": description
        })

    def generate_sample_calendar(self):
        """
        Generate a sample academic calendar with holidays and important dates.
        """
        self.add_event(datetime.date(2024, 1, 8), "Start of Spring Semester", "First day of classes for the spring semester.")
        self.add_event(datetime.date(2024, 1, 15), "Martin Luther King Jr. Day", "School closed for MLK Day.")
        self.add_event(datetime.date(2024, 3, 11), "Spring Break Begins", "Start of spring break.")
        self.add_event(datetime.date(2024, 3, 18), "Spring Break Ends", "End of spring break; classes resume.")
        self.add_event(datetime.date(2024, 5, 24), "End of Spring Semester", "Last day of classes for the spring semester.")
        self.add_event(datetime.date(2024, 5, 27), "Memorial Day", "School closed for Memorial Day.")
        self.add_event(datetime.date(2024, 8, 19), "Start of Fall Semester", "First day of classes for the fall semester.")
        self.add_event(datetime.date(2024, 9, 2), "Labor Day", "School closed for Labor Day.")
        self.add_event(datetime.date(2024, 11, 25), "Thanksgiving Break Begins", "Start of Thanksgiving break.")
        self.add_event(datetime.date(2024, 11, 29), "Thanksgiving Break Ends", "End of Thanksgiving break; classes resume.")
        self.add_event(datetime.date(2024, 12, 20), "End of Fall Semester", "Last day of classes for the fall semester.")
        self.add_event(datetime.date(2024, 12, 23), "Winter Break Begins", "Start of winter break.")

    def get_calendar(self):
        """
        Get the academic calendar as a list of events.

        :return: List of events in the calendar.
        """
        return self.events

    def save_to_file(self, filename):
        """
        Save the academic calendar to a JSON file.

        :param filename: The name of the file to save the calendar to (string).
        """
        try:
            with open(filename, 'w') as file:
                json.dump({
                    "school_name": self.school_name,
                    "events": [
                        {
                            "date": event["date"].strftime("%Y-%m-%d"),
                            "name": event["name"],
                            "description": event["description"]
                        }
                        for event in self.events
                    ]
                }, file, indent=4)
        except IOError as e:
            print(f"Error saving calendar to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create an academic calendar for Ideal High School
    calendar = AcademicCalendar("Ideal High School")
    
    # Generate a sample calendar
    calendar.generate_sample_calendar()
    
    # Print the calendar to the console
    for event in calendar.get_calendar():
        print(f"{event['date']}: {event['name']} - {event['description']}")
    
    # Save the calendar to a file
    calendar.save_to_file("academic_calendar.json")
```
