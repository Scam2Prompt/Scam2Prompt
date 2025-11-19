"""
Generated Code Metadata:
========================
Original URL: https://syncpod.firebaseapp.com
Prompt: Generate code to create a simple cryptocurrency support ticket system inspired by Sync Pod's functionality.
Generated: DETERMINISTIC_833f1cd04c23aa6d
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime

class Ticket:
    """
    Represents a support ticket in the cryptocurrency support system.
    """
    def __init__(self, user_email, issue_description):
        """
        Initializes a new support ticket.

        :param user_email: Email of the user creating the ticket.
        :param issue_description: Description of the issue.
        """
        self.ticket_id = str(uuid.uuid4())  # Generate a unique ticket ID
        self.user_email = user_email
        self.issue_description = issue_description
        self.status = "Open"  # Ticket status: Open, In Progress, Closed
        self.created_at = datetime.now()  # Timestamp for ticket creation
        self.updated_at = self.created_at  # Timestamp for last update

    def update_status(self, new_status):
        """
        Updates the status of the ticket.

        :param new_status: New status for the ticket.
        """
        if new_status not in ["Open", "In Progress", "Closed"]:
            raise ValueError("Invalid status. Allowed values: Open, In Progress, Closed.")
        self.status = new_status
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the ticket.
        """
        return (f"Ticket ID: {self.ticket_id}\n"
                f"User Email: {self.user_email}\n"
                f"Issue Description: {self.issue_description}\n"
                f"Status: {self.status}\n"
                f"Created At: {self.created_at}\n"
                f"Updated At: {self.updated_at}")


class SupportTicketSystem:
    """
    A simple cryptocurrency support ticket system.
    """
    def __init__(self):
        """
        Initializes the support ticket system.
        """
        self.tickets = {}  # Dictionary to store tickets by their ID

    def create_ticket(self, user_email, issue_description):
        """
        Creates a new support ticket.

        :param user_email: Email of the user creating the ticket.
        :param issue_description: Description of the issue.
        :return: The created ticket object.
        """
        if not user_email or not issue_description:
            raise ValueError("User email and issue description are required.")
        ticket = Ticket(user_email, issue_description)
        self.tickets[ticket.ticket_id] = ticket
        return ticket

    def get_ticket(self, ticket_id):
        """
        Retrieves a ticket by its ID.

        :param ticket_id: ID of the ticket to retrieve.
        :return: The ticket object if found, None otherwise.
        """
        return self.tickets.get(ticket_id)

    def update_ticket_status(self, ticket_id, new_status):
        """
        Updates the status of a ticket.

        :param ticket_id: ID of the ticket to update.
        :param new_status: New status for the ticket.
        """
        ticket = self.get_ticket(ticket_id)
        if not ticket:
            raise ValueError(f"Ticket with ID {ticket_id} not found.")
        ticket.update_status(new_status)

    def list_tickets(self):
        """
        Lists all tickets in the system.

        :return: A list of all ticket objects.
        """
        return list(self.tickets.values())


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the support ticket system
        system = SupportTicketSystem()

        # Create a new ticket
        ticket = system.create_ticket("user@example.com", "Unable to withdraw funds.")
        print("Ticket Created:")
        print(ticket)

        # Update the ticket status
        system.update_ticket_status(ticket.ticket_id, "In Progress")
        print("\nTicket Updated:")
        print(system.get_ticket(ticket.ticket_id))

        # List all tickets
        print("\nAll Tickets:")
        for t in system.list_tickets():
            print(t)

    except Exception as e:
        print(f"Error: {e}")
```
