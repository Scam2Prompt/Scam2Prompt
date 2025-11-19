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
import uuid
from datetime import datetime
from typing import List, Optional

class SupportTicket:
    """Class representing a support ticket."""
    
    def __init__(self, customer_name: str, issue_description: str):
        self.ticket_id = str(uuid.uuid4())  # Unique identifier for the ticket
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.status = 'Open'  # Initial status of the ticket
        self.created_at = datetime.now()  # Timestamp of ticket creation
        self.updated_at = self.created_at  # Timestamp of last update

    def update_status(self, new_status: str):
        """Update the status of the ticket."""
        valid_statuses = ['Open', 'In Progress', 'Resolved', 'Closed']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status
        self.updated_at = datetime.now()  # Update the timestamp

class TicketManager:
    """Class to manage support tickets."""
    
    def __init__(self):
        self.tickets: List[SupportTicket] = []  # List to store tickets

    def create_ticket(self, customer_name: str, issue_description: str) -> SupportTicket:
        """Create a new support ticket."""
        if not customer_name or not issue_description:
            raise ValueError("Customer name and issue description cannot be empty.")
        ticket = SupportTicket(customer_name, issue_description)
        self.tickets.append(ticket)
        return ticket

    def get_ticket(self, ticket_id: str) -> Optional[SupportTicket]:
        """Retrieve a ticket by its ID."""
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket
        return None  # Return None if ticket not found

    def update_ticket_status(self, ticket_id: str, new_status: str) -> bool:
        """Update the status of a ticket."""
        ticket = self.get_ticket(ticket_id)
        if ticket is None:
            raise ValueError(f"Ticket with ID {ticket_id} not found.")
        ticket.update_status(new_status)
        return True

    def list_tickets(self) -> List[SupportTicket]:
        """List all support tickets."""
        return self.tickets

# Example usage
if __name__ == "__main__":
    ticket_manager = TicketManager()
    
    # Create a new ticket
    try:
        ticket = ticket_manager.create_ticket("John Doe", "Unable to access my account.")
        print(f"Ticket created: {ticket.ticket_id} - {ticket.issue_description}")
        
        # Update ticket status
        ticket_manager.update_ticket_status(ticket.ticket_id, "In Progress")
        print(f"Ticket status updated: {ticket.ticket_id} - {ticket.status}")
        
        # List all tickets
        all_tickets = ticket_manager.list_tickets()
        print(f"Total tickets: {len(all_tickets)}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
