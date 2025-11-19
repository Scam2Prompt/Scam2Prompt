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
import datetime
from typing import List, Dict, Optional

class Event:
    """Class representing an event in the festival."""
    
    def __init__(self, name: str, date: datetime.date, location: str):
        self.name = name
        self.date = date
        self.location = location

    def __str__(self):
        return f"{self.name} on {self.date} at {self.location}"


class Ticket:
    """Class representing a ticket for an event."""
    
    def __init__(self, event: Event, ticket_type: str, price: float):
        self.event = event
        self.ticket_type = ticket_type
        self.price = price
        self.purchased = False

    def purchase(self):
        """Mark the ticket as purchased."""
        if not self.purchased:
            self.purchased = True
        else:
            raise ValueError("Ticket has already been purchased.")

    def __str__(self):
        return f"{self.ticket_type} ticket for {self.event}"


class Festival:
    """Class representing the festival with events and ticket management."""
    
    def __init__(self, name: str):
        self.name = name
        self.events: List[Event] = []
        self.tickets: List[Ticket] = []

    def add_event(self, event: Event):
        """Add an event to the festival."""
        self.events.append(event)

    def create_ticket(self, event: Event, ticket_type: str, price: float):
        """Create a ticket for a specific event."""
        ticket = Ticket(event, ticket_type, price)
        self.tickets.append(ticket)
        return ticket

    def purchase_ticket(self, ticket: Ticket):
        """Purchase a ticket if available."""
        try:
            ticket.purchase()
            print(f"Successfully purchased {ticket}.")
        except ValueError as e:
            print(f"Error purchasing ticket: {e}")

    def list_events(self) -> List[str]:
        """List all events in the festival."""
        return [str(event) for event in self.events]

    def list_tickets(self) -> List[str]:
        """List all tickets available for purchase."""
        return [str(ticket) for ticket in self.tickets if not ticket.purchased]


# Example usage
if __name__ == "__main__":
    # Create a festival
    celestia_festival = Festival("Celestia Festival")

    # Add events to the festival
    event1 = Event("Opening Ceremony", datetime.date(2023, 8, 1), "Main Stage")
    event2 = Event("Music Night", datetime.date(2023, 8, 2), "Main Stage")
    celestia_festival.add_event(event1)
    celestia_festival.add_event(event2)

    # Create tickets for the events
    ticket1 = celestia_festival.create_ticket(event1, "VIP", 150.0)
    ticket2 = celestia_festival.create_ticket(event2, "General Admission", 75.0)

    # List events and tickets
    print("Events:")
    print("\n".join(celestia_festival.list_events()))
    
    print("\nAvailable Tickets:")
    print("\n".join(celestia_festival.list_tickets()))

    # Purchase a ticket
    celestia_festival.purchase_ticket(ticket1)

    # Attempt to purchase the same ticket again
    celestia_festival.purchase_ticket(ticket1)

    # List available tickets after purchase
    print("\nAvailable Tickets after purchase:")
    print("\n".join(celestia_festival.list_tickets()))
```
