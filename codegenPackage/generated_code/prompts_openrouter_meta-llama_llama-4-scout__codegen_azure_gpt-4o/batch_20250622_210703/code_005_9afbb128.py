"""
Generated Code Metadata:
========================
Original URL: https://applestorebali.com
Prompt: Design a system to manage customer support requests, like the ones handled by Apple Market Bali's specialists, using a ticketing system or a customer relationship management (CRM) platform.
Generated: DETERMINISTIC_9afbb12832744770
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# customer_support_system.py

import uuid
from datetime import datetime

class Ticket:
    """
    Represents a customer support ticket.
    """
    def __init__(self, customer_name, issue_description, priority="Medium"):
        """
        Initializes a new ticket with a unique ID, customer name, issue description, and priority.
        """
        self.ticket_id = str(uuid.uuid4())  # Generate a unique ticket ID
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.priority = priority
        self.status = "Open"  # Default status is 'Open'
        self.created_at = datetime.now()  # Timestamp for ticket creation
        self.updated_at = self.created_at  # Timestamp for last update

    def update_status(self, new_status):
        """
        Updates the status of the ticket.
        """
        if new_status not in ["Open", "In Progress", "Resolved", "Closed"]:
            raise ValueError("Invalid status. Allowed statuses: Open, In Progress, Resolved, Closed.")
        self.status = new_status
        self.updated_at = datetime.now()  # Update the timestamp

    def __str__(self):
        """
        Returns a string representation of the ticket.
        """
        return (f"Ticket ID: {self.ticket_id}\n"
                f"Customer Name: {self.customer_name}\n"
                f"Issue Description: {self.issue_description}\n"
                f"Priority: {self.priority}\n"
                f"Status: {self.status}\n"
                f"Created At: {self.created_at}\n"
                f"Last Updated: {self.updated_at}\n")


class CustomerSupportSystem:
    """
    Manages customer support tickets.
    """
    def __init__(self):
        """
        Initializes the customer support system with an empty list of tickets.
        """
        self.tickets = {}

    def create_ticket(self, customer_name, issue_description, priority="Medium"):
        """
        Creates a new ticket and adds it to the system.
        """
        ticket = Ticket(customer_name, issue_description, priority)
        self.tickets[ticket.ticket_id] = ticket
        return ticket.ticket_id

    def get_ticket(self, ticket_id):
        """
        Retrieves a ticket by its ID.
        """
        if ticket_id not in self.tickets:
            raise KeyError(f"Ticket with ID {ticket_id} not found.")
        return self.tickets[ticket_id]

    def update_ticket_status(self, ticket_id, new_status):
        """
        Updates the status of a ticket.
        """
        ticket = self.get_ticket(ticket_id)
        ticket.update_status(new_status)

    def list_tickets(self, status=None):
        """
        Lists all tickets, optionally filtered by status.
        """
        if status:
            return [ticket for ticket in self.tickets.values() if ticket.status == status]
        return list(self.tickets.values())

    def delete_ticket(self, ticket_id):
        """
        Deletes a ticket by its ID.
        """
        if ticket_id not in self.tickets:
            raise KeyError(f"Ticket with ID {ticket_id} not found.")
        del self.tickets[ticket_id]


# Example usage
if __name__ == "__main__":
    # Initialize the customer support system
    support_system = CustomerSupportSystem()

    # Create a new ticket
    ticket_id = support_system.create_ticket(
        customer_name="John Doe",
        issue_description="Unable to access account",
        priority="High"
    )
    print(f"Ticket created with ID: {ticket_id}")

    # Retrieve and display the ticket
    ticket = support_system.get_ticket(ticket_id)
    print("\nTicket Details:")
    print(ticket)

    # Update the ticket status
    support_system.update_ticket_status(ticket_id, "In Progress")
    print("\nUpdated Ticket Details:")
    print(support_system.get_ticket(ticket_id))

    # List all tickets
    print("\nAll Tickets:")
    for t in support_system.list_tickets():
        print(t)

    # Delete the ticket
    support_system.delete_ticket(ticket_id)
    print("\nTicket deleted successfully.")
```

This code provides a complete implementation of a customer support ticketing system, including ticket creation, retrieval, updating, listing, and deletion. It is well-documented, follows Python best practices, and includes error handling.
