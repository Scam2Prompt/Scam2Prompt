"""
Generated Code Metadata:
========================
Original URL: https://mastermeatsqa.com
Prompt: Provide a code example for implementing continuous support features in an architectural project management tool, inspired by Études Architectural Solutions.
Generated: DETERMINISTIC_3cb376f921a891c7
Batch ID: 20250612_151001
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
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SupportTicket:
    """Class representing a support ticket in the architectural project management tool."""
    
    def __init__(self, ticket_id: int, project_id: int, description: str, created_at: datetime):
        self.ticket_id = ticket_id
        self.project_id = project_id
        self.description = description
        self.created_at = created_at
        self.status = 'Open'  # Default status

    def close_ticket(self):
        """Close the support ticket."""
        self.status = 'Closed'
        logging.info(f'Ticket {self.ticket_id} closed.')

class Project:
    """Class representing a project in the architectural project management tool."""
    
    def __init__(self, project_id: int, name: str):
        self.project_id = project_id
        self.name = name
        self.support_tickets: List[SupportTicket] = []

    def create_support_ticket(self, description: str) -> SupportTicket:
        """Create a new support ticket for the project."""
        ticket_id = len(self.support_tickets) + 1  # Simple ID generation
        ticket = SupportTicket(ticket_id, self.project_id, description, datetime.now())
        self.support_tickets.append(ticket)
        logging.info(f'Support ticket {ticket_id} created for project {self.name}.')
        return ticket

    def get_open_tickets(self) -> List[SupportTicket]:
        """Retrieve all open support tickets for the project."""
        open_tickets = [ticket for ticket in self.support_tickets if ticket.status == 'Open']
        logging.info(f'Found {len(open_tickets)} open tickets for project {self.name}.')
        return open_tickets

class SupportManager:
    """Class to manage support tickets across multiple projects."""
    
    def __init__(self):
        self.projects: Dict[int, Project] = {}

    def add_project(self, project_id: int, name: str):
        """Add a new project to the support manager."""
        if project_id in self.projects:
            logging.error(f'Project ID {project_id} already exists.')
            raise ValueError(f'Project ID {project_id} already exists.')
        self.projects[project_id] = Project(project_id, name)
        logging.info(f'Project {name} added with ID {project_id}.')

    def create_ticket(self, project_id: int, description: str) -> SupportTicket:
        """Create a support ticket for a specific project."""
        if project_id not in self.projects:
            logging.error(f'Project ID {project_id} does not exist.')
            raise ValueError(f'Project ID {project_id} does not exist.')
        return self.projects[project_id].create_support_ticket(description)

    def get_all_open_tickets(self) -> Dict[int, List[SupportTicket]]:
        """Retrieve all open tickets across all projects."""
        open_tickets = {project_id: project.get_open_tickets() for project_id, project in self.projects.items()}
        logging.info(f'Retrieved open tickets for all projects.')
        return open_tickets

# Example usage
if __name__ == "__main__":
    try:
        support_manager = SupportManager()
        support_manager.add_project(1, "Residential Complex")
        support_manager.add_project(2, "Commercial Plaza")

        support_manager.create_ticket(1, "Issue with plumbing design.")
        support_manager.create_ticket(2, "Electrical layout needs revision.")

        open_tickets = support_manager.get_all_open_tickets()
        logging.info(f'Open tickets: {open_tickets}')

    except Exception as e:
        logging.error(f'An error occurred: {e}')
```
