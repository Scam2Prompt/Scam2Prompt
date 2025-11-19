"""
Generated Code Metadata:
========================
Original URL: https://ibcaj.org
Prompt: "Generate an event schedule for a cultural festival like Saraswati Puja, including puja, guest reception, worship, and cultural programs."
Generated: DETERMINISTIC_896ada2152cd3921
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Event:
    """
    Represents a single event in the schedule.
    """
    def __init__(self, name, start_time, end_time, description):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}): {self.description}"


class FestivalSchedule:
    """
    Represents the schedule for a cultural festival.
    """
    def __init__(self, festival_name, date):
        self.festival_name = festival_name
        self.date = date
        self.events = []

    def add_event(self, name, start_time, end_time, description):
        """
        Adds an event to the schedule.
        """
        if not isinstance(start_time, datetime.time) or not isinstance(end_time, datetime.time):
            raise ValueError("start_time and end_time must be instances of datetime.time.")
        if start_time >= end_time:
            raise ValueError("start_time must be earlier than end_time.")
        
        event = Event(name, start_time, end_time, description)
        self.events.append(event)

    def display_schedule(self):
        """
        Displays the full schedule for the festival.
        """
        print(f"Schedule for {self.festival_name} on {self.date.strftime('%B %d, %Y')}")
        print("-" * 40)
        for event in self.events:
            print(event)
        print("-" * 40)


# Main function to create and display the festival schedule
def main():
    try:
        # Define the festival details
        festival_name = "Saraswati Puja Cultural Festival"
        festival_date = datetime.date(2023, 10, 15)

        # Create the schedule
        schedule = FestivalSchedule(festival_name, festival_date)

        # Add events to the schedule
        schedule.add_event(
            name="Puja Preparation",
            start_time=datetime.time(8, 0),
            end_time=datetime.time(9, 0),
            description="Preparation for the Saraswati Puja ceremony."
        )
        schedule.add_event(
            name="Guest Reception",
            start_time=datetime.time(9, 0),
            end_time=datetime.time(10, 0),
            description="Welcoming guests and dignitaries."
        )
        schedule.add_event(
            name="Saraswati Puja",
            start_time=datetime.time(10, 0),
            end_time=datetime.time(11, 30),
            description="Worship ceremony dedicated to Goddess Saraswati."
        )
        schedule.add_event(
            name="Lunch and Social Gathering",
            start_time=datetime.time(12, 0),
            end_time=datetime.time(2, 0),
            description="Lunch and informal social interactions."
        )
        schedule.add_event(
            name="Cultural Programs",
            start_time=datetime.time(3, 0),
            end_time=datetime.time(6, 0),
            description="Dance, music, and other cultural performances."
        )

        # Display the schedule
        schedule.display_schedule()

    except Exception as e:
        print(f"An error occurred: {e}")


# Run the main function
if __name__ == "__main__":
    main()
```
