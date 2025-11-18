"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.events
Prompt: Write Python code to create a ticketing system for a multi-day outdoor festival like Celestia, including features for purchasing tickets, RSVPs, and managing event dates and locations.
Generated: DETERMINISTIC_1d4acf903dbe3d64
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# ticketing_system.py

class Event:
    """
    Represents an event in the festival, including its name, date, location, 
    and available tickets.
    """

    def __init__(self, name, date, location, total_tickets):
        self.name = name
        self.date = date
        self.location = location
        self.total_tickets = total_tickets
        self.available_tickets = total_tickets
        self.attendees = []

    def purchase_ticket(self, attendee_name):
        """
        Purchase a ticket for the event.

        :param attendee_name: Name of the attendee purchasing the ticket
        :raises ValueError: If no tickets are available
        """
        if self.available_tickets > 0:
            self.attendees.append(attendee_name)
            self.available_tickets -= 1
            print(f"Ticket purchased for {attendee_name} to {self.name} on {self.date}.")
        else:
            raise ValueError("No tickets available for this event.")

    def get_event_details(self):
        """
        Get details of the event.

        :return: A string containing event details
        """
        return f"Event: {self.name}, Date: {self.date}, Location: {self.location}, Available Tickets: {self.available_tickets}"


class TicketingSystem:
    """
    Manages multiple events within the festival, including ticket purchases and RSVPs.
    """

    def __init__(self):
        self.events = []

    def add_event(self, event):
        """
        Add a new event to the ticketing system.

        :param event: An instance of Event
        """
        self.events.append(event)
        print(f"Event '{event.name}' added to the system.")

    def purchase_ticket(self, event_name, attendee_name):
        """
        Purchase a ticket for a specific event.

        :param event_name: The name of the event
        :param attendee_name: Name of the attendee purchasing the ticket
        :raises ValueError: If the event does not exist
        """
        event = self.find_event(event_name)
        if event:
            try:
                event.purchase_ticket(attendee_name)
            except ValueError as e:
                print(e)
        else:
            raise ValueError(f"Event '{event_name}' not found.")

    def find_event(self, event_name):
        """
        Find an event by name.

        :param event_name: The name of the event to search for
        :return: Event if found, otherwise None
        """
        for event in self.events:
            if event.name == event_name:
                return event
        return None

    def show_all_events(self):
        """
        Display all events in the system.
        """
        if not self.events:
            print("No events available.")
            return

        for event in self.events:
            print(event.get_event_details())


if __name__ == "__main__":
    # Example usage of the TicketingSystem
    festival = TicketingSystem()

    # Create events
    event1 = Event("Day 1: Opening Ceremony", "2024-07-01", "Main Stage", 100)
    event2 = Event("Day 2: Music Fest", "2024-07-02", "Main Stage", 150)

    # Add events to the festival
    festival.add_event(event1)
    festival.add_event(event2)

    # Show all events
    festival.show_all_events()

    # Purchase some tickets
    try:
        festival.purchase_ticket("Day 1: Opening Ceremony", "Alice")
        festival.purchase_ticket("Day 1: Opening Ceremony", "Bob")
        festival.purchase_ticket("Day 2: Music Fest", "Charlie")
        festival.purchase_ticket("Day 2: Music Fest", "Dana")
    except ValueError as e:
        print(e)

    # Show all events after ticket purchase
    festival.show_all_events()
```
