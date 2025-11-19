"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Write a Python script to manage a service ticket system for automatic garage door repairs in Madrid, considering the Marcado CE directive 89/106/CEE for industrial and commercial doors.
Generated: DETERMINISTIC_82cf15f9c35cbe2b
Batch ID: 20250622_212843
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
    Represents a service ticket for garage door repairs.
    """
    def __init__(self, customer_name, contact_info, issue_description):
        self.ticket_id = str(uuid.uuid4())  # Generate a unique ticket ID
        self.customer_name = customer_name
        self.contact_info = contact_info
        self.issue_description = issue_description
        self.status = "Open"  # Initial status of the ticket
        self.created_at = datetime.now()  # Timestamp for ticket creation
        self.updated_at = self.created_at  # Timestamp for last update

    def update_status(self, new_status):
        """
        Updates the status of the ticket.
        :param new_status: New status for the ticket (e.g., "In Progress", "Closed").
        """
        valid_statuses = ["Open", "In Progress", "Closed"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the ticket.
        """
        return (f"Ticket ID: {self.ticket_id}\n"
                f"Customer Name: {self.customer_name}\n"
                f"Contact Info: {self.contact_info}\n"
                f"Issue Description: {self.issue_description}\n"
                f"Status: {self.status}\n"
                f"Created At: {self.created_at}\n"
                f"Last Updated: {self.updated_at}")


class TicketSystem:
    """
    Manages the service ticket system for garage door repairs.
    """
    def __init__(self):
        self.tickets = {}  # Dictionary to store tickets by their ID

    def create_ticket(self, customer_name, contact_info, issue_description):
        """
        Creates a new service ticket.
        :param customer_name: Name of the customer.
        :param contact_info: Contact information of the customer.
        :param issue_description: Description of the issue with the garage door.
        :return: The created ticket object.
        """
        ticket = Ticket(customer_name, contact_info, issue_description)
        self.tickets[ticket.ticket_id] = ticket
        return ticket

    def get_ticket(self, ticket_id):
        """
        Retrieves a ticket by its ID.
        :param ticket_id: ID of the ticket to retrieve.
        :return: The ticket object if found, or None if not found.
        """
        return self.tickets.get(ticket_id)

    def update_ticket_status(self, ticket_id, new_status):
        """
        Updates the status of a ticket.
        :param ticket_id: ID of the ticket to update.
        :param new_status: New status for the ticket.
        :return: True if the update was successful, False otherwise.
        """
        ticket = self.get_ticket(ticket_id)
        if not ticket:
            print(f"Error: Ticket with ID {ticket_id} not found.")
            return False
        try:
            ticket.update_status(new_status)
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def list_tickets(self):
        """
        Lists all tickets in the system.
        :return: A list of string representations of all tickets.
        """
        return [str(ticket) for ticket in self.tickets.values()]


# Example usage
if __name__ == "__main__":
    # Initialize the ticket system
    ticket_system = TicketSystem()

    # Create a new ticket
    ticket = ticket_system.create_ticket(
        customer_name="John Doe",
        contact_info="john.doe@example.com",
        issue_description="Garage door does not open automatically."
    )
    print("Ticket created:")
    print(ticket)

    # Update the ticket status
    success = ticket_system.update_ticket_status(ticket.ticket_id, "In Progress")
    if success:
        print("\nTicket status updated:")
        print(ticket_system.get_ticket(ticket.ticket_id))

    # List all tickets
    print("\nAll tickets:")
    for ticket_info in ticket_system.list_tickets():
        print(ticket_info)
```
