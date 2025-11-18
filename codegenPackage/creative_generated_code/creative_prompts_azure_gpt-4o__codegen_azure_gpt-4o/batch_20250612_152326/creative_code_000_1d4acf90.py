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
import uuid
from datetime import datetime


class FestivalEvent:
    """
    Represents an individual event in the festival.
    """
    def __init__(self, event_name, event_date, location):
        self.event_id = str(uuid.uuid4())  # Generate a unique event ID
        self.event_name = event_name
        self.event_date = event_date
        self.location = location

    def __str__(self):
        return f"Event Name: {self.event_name}, Date: {self.event_date}, Location: {self.location}"


class Ticket:
    """
    Represents a ticket purchased for a festival event.
    """
    def __init__(self, event, purchaser_name, purchaser_email):
        self.ticket_id = str(uuid.uuid4())  # Generate a unique ticket ID
        self.event = event
        self.purchaser_name = purchaser_name
        self.purchaser_email = purchaser_email
        self.purchase_date = datetime.now()  # Record the time of ticket purchase

    def __str__(self):
        return f"Ticket ID: {self.ticket_id}, Event: {self.event.event_name}, Purchaser: {self.purchaser_name}, Email: {self.purchaser_email}, Purchase Date: {self.purchase_date}"


class TicketingSystem:
    """
    Manages festival events, ticket purchases, and RSVPs for the multi-day festival.
    """
    def __init__(self):
        self.events = {}  # Stores events by their IDs
        self.tickets = {}  # Stores tickets by their IDs

    def add_event(self, event_name, event_date, location):
        """
        Creates a new event and adds it to the system.
        """
        try:
            event_date = datetime.strptime(event_date, "%Y-%m-%d %H:%M")  # Parse event date
            event = FestivalEvent(event_name, event_date, location)
            self.events[event.event_id] = event
            print(f"Event added successfully: {event}")
        except ValueError:
            print("Error: Invalid date format. Please use 'YYYY-MM-DD HH:MM'.")
        except Exception as e:
            print(f"Error: Unable to add event. Details: {str(e)}")

    def purchase_ticket(self, event_id, purchaser_name, purchaser_email):
        """
        Purchases a ticket for a specific festival event.
        """
        try:
            if event_id not in self.events:
                raise ValueError("Event ID not found.")
            event = self.events[event_id]
            ticket = Ticket(event, purchaser_name, purchaser_email)
            self.tickets[ticket.ticket_id] = ticket
            print(f"Ticket purchased successfully: {ticket}")
        except ValueError as ve:
            print(f"Error: {str(ve)}")
        except Exception as e:
            print(f"Error: Unable to purchase ticket. Details: {str(e)}")

    def list_events(self):
        """
        Displays all available events in the system.
        """
        if not self.events:
            print("No events available.")
        else:
            print("Available Events:")
            for event in self.events.values():
                print(event)

    def list_tickets(self):
        """
        Displays all purchased tickets.
        """
        if not self.tickets:
            print("No tickets purchased.")
        else:
            print("Purchased Tickets:")
            for ticket in self.tickets.values():
                print(ticket)


# Example Usage
if __name__ == "__main__":
    system = TicketingSystem()

    # Adding events
    system.add_event("Celestia Music Night", "2023-12-01 18:00", "Central Park")
    system.add_event("Celestia Art Exhibition", "2023-12-02 10:00", "City Gallery")

    # Listing events
    system.list_events()

    # Purchasing tickets
    system.purchase_ticket("invalid_event_id", "John Doe", "john@example.com")  # Invalid event ID
    for event_id in system.events.keys():  # Purchase ticket for the first event
        system.purchase_ticket(event_id, "Jane Doe", "jane@example.com")
        break

    # Listing purchased tickets
    system.list_tickets()
```
