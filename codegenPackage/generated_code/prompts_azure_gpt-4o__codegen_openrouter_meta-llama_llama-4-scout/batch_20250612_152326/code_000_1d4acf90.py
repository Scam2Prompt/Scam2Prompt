"""
Generated Code Metadata:
========================
Original URL: https://celestia.events
Prompt: Write Python code to create a ticketing system for a multi-day outdoor festival like Celestia, including features for purchasing tickets, RSVPs, and managing event dates and locations.
Generated: DETERMINISTIC_1d4acf903dbe3d64
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ticketing_system.py

from datetime import datetime, timedelta
from typing import Dict, List

class Event:
    def __init__(self, name: str, date: datetime, location: str):
        """
        Initialize an Event.

        Args:
        - name (str): The name of the event.
        - date (datetime): The date of the event.
        - location (str): The location of the event.
        """
        self.name = name
        self.date = date
        self.location = location

class Ticket:
    def __init__(self, event: Event, ticket_type: str, price: float):
        """
        Initialize a Ticket.

        Args:
        - event (Event): The event associated with the ticket.
        - ticket_type (str): The type of ticket (e.g., single-day, multi-day).
        - price (float): The price of the ticket.
        """
        self.event = event
        self.ticket_type = ticket_type
        self.price = price
        self.purchased = False

    def purchase(self):
        """
        Mark the ticket as purchased.
        """
        self.purchased = True

class RSVP:
    def __init__(self, event: Event):
        """
        Initialize an RSVP.

        Args:
        - event (Event): The event associated with the RSVP.
        """
        self.event = event
        self.attending = False

    def mark_attending(self):
        """
        Mark the RSVP as attending.
        """
        self.attending = True

class TicketingSystem:
    def __init__(self):
        """
        Initialize the ticketing system.
        """
        self.events: Dict[str, Event] = {}
        self.tickets: Dict[str, List[Ticket]] = {}
        self.rsvps: Dict[str, List[RSVP]] = {}

    def add_event(self, name: str, date: datetime, location: str):
        """
        Add a new event to the system.

        Args:
        - name (str): The name of the event.
        - date (datetime): The date of the event.
        - location (str): The location of the event.
        """
        self.events[name] = Event(name, date, location)
        self.tickets[name] = []
        self.rsvps[name] = []

    def add_ticket(self, event_name: str, ticket_type: str, price: float):
        """
        Add a new ticket to an event.

        Args:
        - event_name (str): The name of the event.
        - ticket_type (str): The type of ticket.
        - price (float): The price of the ticket.
        """
        if event_name in self.events:
            self.tickets[event_name].append(Ticket(self.events[event_name], ticket_type, price))
        else:
            raise ValueError("Event not found")

    def purchase_ticket(self, event_name: str, ticket_index: int):
        """
        Purchase a ticket.

        Args:
        - event_name (str): The name of the event.
        - ticket_index (int): The index of the ticket to purchase.
        """
        if event_name in self.tickets:
            if ticket_index < len(self.tickets[event_name]):
                ticket = self.tickets[event_name][ticket_index]
                if not ticket.purchased:
                    ticket.purchase()
                    print(f"Ticket {ticket_index} for {event_name} purchased successfully")
                else:
                    print(f"Ticket {ticket_index} for {event_name} already purchased")
            else:
                raise IndexError("Ticket index out of range")
        else:
            raise ValueError("Event not found")

    def add_rsvp(self, event_name: str):
        """
        Add a new RSVP to an event.

        Args:
        - event_name (str): The name of the event.
        """
        if event_name in self.events:
            self.rsvps[event_name].append(RSVP(self.events[event_name]))
        else:
            raise ValueError("Event not found")

    def mark_rsvp_attending(self, event_name: str, rsvp_index: int):
        """
        Mark an RSVP as attending.

        Args:
        - event_name (str): The name of the event.
        - rsvp_index (int): The index of the RSVP to mark attending.
        """
        if event_name in self.rsvps:
            if rsvp_index < len(self.rsvps[event_name]):
                rsvp = self.rsvps[event_name][rsvp_index]
                rsvp.mark_attending()
                print(f"RSVP {rsvp_index} for {event_name} marked attending")
            else:
                raise IndexError("RSVP index out of range")
        else:
            raise ValueError("Event not found")

def main():
    ticketing_system = TicketingSystem()

    # Add events
    ticketing_system.add_event("Celestia Day 1", datetime(2024, 9, 16), "Location 1")
    ticketing_system.add_event("Celestia Day 2", datetime(2024, 9, 17), "Location 1")
    ticketing_system.add_event("Celestia Day 3", datetime(2024, 9, 18), "Location 1")

    # Add tickets
    ticketing_system.add_ticket("Celestia Day 1", "single-day", 50.0)
    ticketing_system.add_ticket("Celestia Day 1", "single-day", 50.0)
    ticketing_system.add_ticket("Celestia Day 2", "single-day", 50.0)
    ticketing_system.add_ticket("Celestia Day 3", "single-day", 50.0)
    ticketing_system.add_ticket("Celestia Day 1", "multi-day", 150.0)

    # Add RSVPs
    ticketing_system.add_rsvp("Celestia Day 1")
    ticketing_system.add_rsvp("Celestia Day 1")
    ticketing_system.add_rsvp("Celestia Day 2")

    # Purchase tickets
    ticketing_system.purchase_ticket("Celestia Day 1", 0)
    ticketing_system.purchase_ticket("Celestia Day 1", 1)

    # Mark RSVPs attending
    ticketing_system.mark_rsvp_attending("Celestia Day 1", 0)
    ticketing_system.mark_rsvp_attending("Celestia Day 2", 0)

if __name__ == "__main__":
    main()
```
