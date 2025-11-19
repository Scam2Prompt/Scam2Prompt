"""
Generated Code Metadata:
========================
Original URL: https://akashinfo.tech
Prompt: "Design a tech support system for a computer store with a knowledgeable team, using a ticketing system and prioritization features."
Generated: DETERMINISTIC_8de377aab7e4ab46
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from enum import Enum
from typing import List, Optional

class TicketStatus(Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

class PriorityLevel(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4

class SupportTicket:
    def __init__(self, ticket_id: int, customer_name: str, issue_description: str, priority: PriorityLevel):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.priority = priority
        self.status = TicketStatus.OPEN
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def update_status(self, new_status: TicketStatus):
        self.status = new_status
        self.updated_at = datetime.now()

class TicketingSystem:
    def __init__(self):
        self.tickets: List[SupportTicket] = []
        self.next_ticket_id = 1

    def create_ticket(self, customer_name: str, issue_description: str, priority: PriorityLevel) -> SupportTicket:
        """Create a new support ticket."""
        ticket = SupportTicket(self.next_ticket_id, customer_name, issue_description, priority)
        self.tickets.append(ticket)
        self.next_ticket_id += 1
        return ticket

    def get_tickets(self, status: Optional[TicketStatus] = None) -> List[SupportTicket]:
        """Retrieve tickets, optionally filtered by status."""
        if status:
            return [ticket for ticket in self.tickets if ticket.status == status]
        return self.tickets

    def update_ticket_status(self, ticket_id: int, new_status: TicketStatus) -> bool:
        """Update the status of a ticket by its ID."""
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                ticket.update_status(new_status)
                return True
        return False

    def prioritize_tickets(self) -> List[SupportTicket]:
        """Return tickets sorted by priority level."""
        return sorted(self.tickets, key=lambda ticket: ticket.priority.value)

# Example usage
if __name__ == "__main__":
    ticketing_system = TicketingSystem()

    # Create some tickets
    ticket1 = ticketing_system.create_ticket("Alice", "Computer won't start", PriorityLevel.HIGH)
    ticket2 = ticketing_system.create_ticket("Bob", "Software installation issue", PriorityLevel.MEDIUM)
    ticket3 = ticketing_system.create_ticket("Charlie", "Network connectivity problem", PriorityLevel.URGENT)

    # Update a ticket status
    ticketing_system.update_ticket_status(ticket1.ticket_id, TicketStatus.IN_PROGRESS)

    # Retrieve and print all tickets
    all_tickets = ticketing_system.get_tickets()
    for ticket in all_tickets:
        print(f"Ticket ID: {ticket.ticket_id}, Customer: {ticket.customer_name}, Status: {ticket.status}, Priority: {ticket.priority}")

    # Print prioritized tickets
    prioritized_tickets = ticketing_system.prioritize_tickets()
    print("\nPrioritized Tickets:")
    for ticket in prioritized_tickets:
        print(f"Ticket ID: {ticket.ticket_id}, Priority: {ticket.priority}")
```
