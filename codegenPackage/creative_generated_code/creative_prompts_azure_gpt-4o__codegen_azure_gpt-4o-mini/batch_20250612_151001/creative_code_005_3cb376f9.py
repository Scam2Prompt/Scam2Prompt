"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mastermeatsqa.com
Prompt: Provide a code example for implementing continuous support features in an architectural project management tool, inspired by Études Architectural Solutions.
Generated: DETERMINISTIC_3cb376f921a891c7
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SupportTicket:
    """
    Represents a support ticket in the architectural project management tool.
    """
    
    def __init__(self, ticket_id: int, project_name: str, issue_description: str, created_at: datetime):
        self.ticket_id = ticket_id
        self.project_name = project_name
        self.issue_description = issue_description
        self.created_at = created_at
        self.is_resolved = False

    def resolve(self):
        """Mark the ticket as resolved."""
        self.is_resolved = True
        logging.info(f"Ticket {self.ticket_id} resolved.")


class SupportManager:
    """
    Manages support tickets and their lifecycle.
    """
    
    def __init__(self):
        self.tickets: List[SupportTicket] = []
        self.ticket_counter = 1

    def create_ticket(self, project_name: str, issue_description: str) -> SupportTicket:
        """
        Create a new support ticket.
        :param project_name: The name of the project related to the ticket.
        :param issue_description: A description of the issue.
        :return: The created SupportTicket instance.
        """
        new_ticket = SupportTicket(self.ticket_counter, project_name, issue_description, datetime.now())
        self.tickets.append(new_ticket)
        self.ticket_counter += 1
        logging.info(f"Created ticket {new_ticket.ticket_id} for project '{project_name}'.")
        return new_ticket

    def resolve_ticket(self, ticket_id: int) -> Optional[SupportTicket]:
        """
        Resolve an existing support ticket.
        :param ticket_id: The ID of the ticket to resolve.
        :return: The resolved SupportTicket instance or None if not found.
        """
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                ticket.resolve()
                return ticket
        logging.warning(f"Ticket {ticket_id} not found for resolution.")
        return None

    def get_open_tickets(self) -> List[Dict]:
        """
        Get a list of open tickets.
        :return: A list of dictionaries representing open tickets.
        """
        open_tickets = [ticket.__dict__ for ticket in self.tickets if not ticket.is_resolved]
        logging.info(f"Retrieved {len(open_tickets)} open tickets.")
        return open_tickets


# Example usage of the SupportManager class
if __name__ == "__main__":
    try:
        support_manager = SupportManager()

        # Creating tickets
        ticket1 = support_manager.create_ticket("Project Alpha", "Issue with the design document.")
        ticket2 = support_manager.create_ticket("Project Beta", "Error in the project estimation.")

        # Resolving a ticket
        support_manager.resolve_ticket(ticket1.ticket_id)

        # Fetching open tickets
        open_tickets = support_manager.get_open_tickets()
        logging.info(f"Open tickets: {open_tickets}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
