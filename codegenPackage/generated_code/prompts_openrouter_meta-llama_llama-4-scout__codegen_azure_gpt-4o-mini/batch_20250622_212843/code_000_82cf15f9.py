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
import json
import logging
from datetime import datetime
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ServiceTicket:
    """Class to represent a service ticket for garage door repairs."""
    
    def __init__(self, ticket_id: int, customer_name: str, address: str, issue_description: str):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.address = address
        self.issue_description = issue_description
        self.status = 'Open'
        self.created_at = datetime.now()
    
    def __repr__(self):
        return f"ServiceTicket(ticket_id={self.ticket_id}, customer_name='{self.customer_name}', status='{self.status}')"

class TicketManager:
    """Class to manage service tickets."""
    
    def __init__(self, storage_file: str):
        self.storage_file = storage_file
        self.tickets: List[ServiceTicket] = self.load_tickets()
    
    def load_tickets(self) -> List[ServiceTicket]:
        """Load tickets from a JSON file."""
        try:
            with open(self.storage_file, 'r') as file:
                tickets_data = json.load(file)
                return [ServiceTicket(**ticket) for ticket in tickets_data]
        except FileNotFoundError:
            logging.warning("Storage file not found. Starting with an empty ticket list.")
            return []
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON: {e}")
            return []
    
    def save_tickets(self):
        """Save tickets to a JSON file."""
        try:
            with open(self.storage_file, 'w') as file:
                json.dump([ticket.__dict__ for ticket in self.tickets], file, default=str)
        except IOError as e:
            logging.error(f"Error saving tickets to file: {e}")
    
    def create_ticket(self, customer_name: str, address: str, issue_description: str) -> ServiceTicket:
        """Create a new service ticket."""
        ticket_id = len(self.tickets) + 1
        new_ticket = ServiceTicket(ticket_id, customer_name, address, issue_description)
        self.tickets.append(new_ticket)
        self.save_tickets()
        logging.info(f"Created new ticket: {new_ticket}")
        return new_ticket
    
    def update_ticket_status(self, ticket_id: int, new_status: str) -> Optional[ServiceTicket]:
        """Update the status of an existing ticket."""
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                ticket.status = new_status
                self.save_tickets()
                logging.info(f"Updated ticket {ticket_id} status to '{new_status}'")
                return ticket
        logging.warning(f"Ticket ID {ticket_id} not found.")
        return None
    
    def get_open_tickets(self) -> List[ServiceTicket]:
        """Retrieve all open tickets."""
        open_tickets = [ticket for ticket in self.tickets if ticket.status == 'Open']
        logging.info(f"Retrieved {len(open_tickets)} open tickets.")
        return open_tickets

def main():
    """Main function to run the ticket management system."""
    ticket_manager = TicketManager('tickets.json')
    
    # Example usage
    ticket_manager.create_ticket("John Doe", "123 Main St, Madrid", "Garage door won't open")
    ticket_manager.create_ticket("Jane Smith", "456 Elm St, Madrid", "Remote not working")
    
    open_tickets = ticket_manager.get_open_tickets()
    for ticket in open_tickets:
        print(ticket)
    
    # Update a ticket status
    ticket_manager.update_ticket_status(1, "In Progress")

if __name__ == "__main__":
    main()
```
