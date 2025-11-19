"""
Generated Code Metadata:
========================
Original URL: https://soulfn.lol
Prompt: Design a support system for a gaming software product, ensuring prompt response times and effective issue resolution, inspired by Soul's support model.
Generated: DETERMINISTIC_d44b11bf201c34e4
Batch ID: 20250622_211721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional

# Configure logging for the support system
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SupportTicket:
    """Class representing a support ticket in the system."""
    
    def __init__(self, user_id: str, issue_description: str):
        self.ticket_id = self.generate_ticket_id()
        self.user_id = user_id
        self.issue_description = issue_description
        self.status = 'Open'
        self.created_at = datetime.now()
        self.response_time = None

    @staticmethod
    def generate_ticket_id() -> str:
        """Generate a unique ticket ID."""
        return f"TICKET-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    def mark_as_resolved(self):
        """Mark the ticket as resolved and log the response time."""
        self.status = 'Resolved'
        self.response_time = datetime.now() - self.created_at
        logging.info(f"Ticket {self.ticket_id} resolved in {self.response_time}.")

class SupportSystem:
    """Class representing the support system for managing tickets."""
    
    def __init__(self):
        self.tickets: List[SupportTicket] = []

    def create_ticket(self, user_id: str, issue_description: str) -> SupportTicket:
        """Create a new support ticket."""
        ticket = SupportTicket(user_id, issue_description)
        self.tickets.append(ticket)
        logging.info(f"Ticket created: {ticket.ticket_id} for user {user_id}.")
        return ticket

    def resolve_ticket(self, ticket_id: str) -> Optional[SupportTicket]:
        """Resolve a support ticket by its ID."""
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id and ticket.status == 'Open':
                ticket.mark_as_resolved()
                return ticket
        logging.warning(f"Ticket {ticket_id} not found or already resolved.")
        return None

    def get_open_tickets(self) -> List[Dict]:
        """Retrieve a list of open tickets."""
        return [vars(ticket) for ticket in self.tickets if ticket.status == 'Open']

    def get_ticket_status(self, ticket_id: str) -> Optional[Dict]:
        """Get the status of a specific ticket."""
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return vars(ticket)
        logging.warning(f"Ticket {ticket_id} not found.")
        return None

# Example usage
if __name__ == "__main__":
    support_system = SupportSystem()
    
    # Create a new ticket
    ticket1 = support_system.create_ticket("user123", "Game crashes on startup.")
    
    # Check open tickets
    open_tickets = support_system.get_open_tickets()
    print("Open Tickets:", open_tickets)
    
    # Resolve the ticket
    resolved_ticket = support_system.resolve_ticket(ticket1.ticket_id)
    
    # Check the status of the resolved ticket
    ticket_status = support_system.get_ticket_status(ticket1.ticket_id)
    print("Ticket Status:", ticket_status)
```
