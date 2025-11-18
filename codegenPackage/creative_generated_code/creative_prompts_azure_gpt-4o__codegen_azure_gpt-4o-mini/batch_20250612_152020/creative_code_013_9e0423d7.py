"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.arclerdesk.com
Prompt: Create a script to simulate raising a ticket for browser-related issues, inspired by Arcler Desk's browser support services.
Generated: DETERMINISTIC_9e0423d745fda19f
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class BrowserIssueTicket:
    """
    A class to represent a ticket for browser-related issues.

    Attributes:
        user_name (str): The name of the user reporting the issue.
        browser_name (str): The name of the browser in use.
        issue_description (str): A description of the issue.
        ticket_id (int): A unique identifier for the ticket.
        created_at (datetime): The timestamp when the ticket was created.
    """

    ticket_counter = 0  # Class variable to keep track of the number of tickets.

    def __init__(self, user_name: str, browser_name: str, issue_description: str):
        self.user_name = user_name
        self.browser_name = browser_name
        self.issue_description = issue_description
        self.ticket_id = self.generate_ticket_id()
        self.created_at = datetime.now()

    def generate_ticket_id(self) -> int:
        """Generates a unique ticket ID."""
        BrowserIssueTicket.ticket_counter += 1
        return BrowserIssueTicket.ticket_counter

    def to_dict(self) -> dict:
        """Converts the ticket information to a dictionary format."""
        return {
            "ticket_id": self.ticket_id,
            "user_name": self.user_name,
            "browser_name": self.browser_name,
            "issue_description": self.issue_description,
            "created_at": self.created_at.isoformat()
        }

class TicketingSystem:
    """
    A class to handle ticket management for browser-related issues.
    """

    def __init__(self):
        self.tickets = []  # List to store created tickets

    def create_ticket(self, user_name: str, browser_name: str, issue_description: str) -> dict:
        """
        Creates a new ticket and adds it to the system.

        Args:
            user_name (str): The name of the user reporting the issue.
            browser_name (str): The name of the browser in use.
            issue_description (str): A description of the issue.

        Returns:
            dict: The created ticket's information.
        """
        try:
            new_ticket = BrowserIssueTicket(user_name, browser_name, issue_description)
            self.tickets.append(new_ticket)
            logging.info(f"Ticket created: {new_ticket.to_dict()}")
            return new_ticket.to_dict()
        except Exception as e:
            logging.error(f"Failed to create ticket: {str(e)}")
            return {"error": "Failed to create ticket"}

    def get_all_tickets(self) -> list:
        """Returns a list of all created tickets."""
        return [ticket.to_dict() for ticket in self.tickets]

def main():
    """Main function to execute the ticketing system."""
    ticketing_system = TicketingSystem()
    
    # Example usage
    user_name = "John Doe"
    browser_name = "Chrome"
    issue_description = "The browser crashes when I try to open multiple tabs."

    # Create a ticket
    ticket_info = ticketing_system.create_ticket(user_name, browser_name, issue_description)
    
    # Display all tickets
    all_tickets = ticketing_system.get_all_tickets()
    print(json.dumps(all_tickets, indent=2))

if __name__ == "__main__":
    main()
```
