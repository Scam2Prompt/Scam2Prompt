"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberconnectit.com
Prompt: Provide code to set up a ticketing system for IT support for an established business, as described in CyberConnect's IT services.
Generated: DETERMINISTIC_3f8545fc86100ee1
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Ticketing System for IT Support
Author: CyberConnect IT Services Developer

Description:
This script sets up a simple ticketing system for IT support requests. 
It allows users to create, view, update, and close tickets. 
The system stores ticket information in memory for simplicity. For production, replace with a database.
"""

import uuid
from datetime import datetime

class Ticket:
    """
    Represents a single IT support ticket.
    """
    def __init__(self, title, description, priority, reporter):
        self.id = str(uuid.uuid4())  # Unique identifier for the ticket
        self.title = title           # Ticket title
        self.description = description  # Detailed description of the issue
        self.priority = priority     # Priority ('Low', 'Medium', 'High')
        self.reporter = reporter     # Name of the person reporting the issue
        self.status = 'Open'         # Ticket status ('Open', 'In Progress', 'Closed')
        self.created_at = datetime.now()  # Time when the ticket was created

    def update_status(self, new_status):
        """
        Updates the status of the ticket.
        :param new_status: New status ('Open', 'In Progress', 'Closed')
        """
        valid_statuses = ['Open', 'In Progress', 'Closed']
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are {valid_statuses}.")

    def __str__(self):
        """
        Returns a string representation of the ticket.
        """
        return (f"Ticket ID: {self.id}\nTitle: {self.title}\nDescription: {self.description}\n"
                f"Priority: {self.priority}\nReporter: {self.reporter}\nStatus: {self.status}\n"
                f"Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n")


class TicketingSystem:
    """
    Manages IT support tickets.
    """
    def __init__(self):
        self.tickets = {}  # Dictionary to store tickets with ticket ID as key

    def create_ticket(self, title, description, priority, reporter):
        """
        Creates a new ticket.
        :param title: Title of the ticket
        :param description: Detailed description of the issue
        :param priority: Priority of the ticket ('Low', 'Medium', 'High')
        :param reporter: Name of the person reporting the issue
        :return: The created Ticket object
        """
        if priority not in ['Low', 'Medium', 'High']:
            raise ValueError("Invalid priority. Priority must be 'Low', 'Medium', or 'High'.")
        
        ticket = Ticket(title, description, priority, reporter)
        self.tickets[ticket.id] = ticket
        return ticket

    def view_ticket(self, ticket_id):
        """
        Retrieves a ticket by its ID.
        :param ticket_id: ID of the ticket
        :return: Ticket object or None if not found
        """
        return self.tickets.get(ticket_id, None)

    def update_ticket_status(self, ticket_id, new_status):
        """
        Updates the status of a ticket.
        :param ticket_id: ID of the ticket
        :param new_status: New status ('Open', 'In Progress', 'Closed')
        """
        ticket = self.view_ticket(ticket_id)
        if ticket:
            ticket.update_status(new_status)
        else:
            raise KeyError(f"No ticket found with ID: {ticket_id}")

    def close_ticket(self, ticket_id):
        """
        Closes a ticket by setting its status to 'Closed'.
        :param ticket_id: ID of the ticket
        """
        self.update_ticket_status(ticket_id, 'Closed')

    def list_tickets(self):
        """
        Lists all tickets in the system.
        :return: List of Ticket objects
        """
        return list(self.tickets.values())


# Example usage:
if __name__ == "__main__":
    try:
        system = TicketingSystem()

        # Create tickets
        ticket1 = system.create_ticket("Printer Issue", "The office printer is not working.", "High", "Alice")
        ticket2 = system.create_ticket("Network Problem", "Wi-Fi is intermittently disconnecting.", "Medium", "Bob")

        print("Created Tickets:")
        print(ticket1)
        print(ticket2)

        # View a ticket
        print("\nViewing Ticket:")
        print(system.view_ticket(ticket1.id))

        # Update ticket status
        system.update_ticket_status(ticket1.id, "In Progress")

        print("\nUpdated Ticket Status:")
        print(system.view_ticket(ticket1.id))

        # List all tickets
        print("\nAll Tickets:")
        for ticket in system.list_tickets():
            print(ticket)

        # Close a ticket
        system.close_ticket(ticket1.id)

        print("\nClosed Ticket:")
        print(system.view_ticket(ticket1.id))

    except Exception as e:
        print(f"An error occurred: {e}")
```
