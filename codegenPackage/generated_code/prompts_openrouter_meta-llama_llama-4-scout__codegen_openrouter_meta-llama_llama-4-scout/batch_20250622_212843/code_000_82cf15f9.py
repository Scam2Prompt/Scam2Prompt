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
# service_ticket_system.py

"""
Service Ticket System for Automatic Garage Door Repairs in Madrid.

This script manages service tickets for automatic garage door repairs in Madrid,
considering the Marcado CE directive 89/106/CEE for industrial and commercial doors.

Author: [Your Name]
Date: [Today's Date]
"""

import datetime
import logging
from enum import Enum
from typing import Dict, List

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DoorStatus(str, Enum):
    """Enum for door status."""
    FUNCTIONAL = "Functional"
    MALFUNCTIONING = "Malfunctioning"
    UNDER_REPAIR = "Under Repair"
    REPAIRED = "Repaired"

class ServiceTicket:
    """Represents a service ticket."""
    def __init__(self, ticket_id: int, customer_name: str, door_type: str, status: DoorStatus):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.door_type = door_type
        self.status = status
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def update_status(self, status: DoorStatus):
        """Updates the status of the service ticket."""
        self.status = status
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"Ticket ID: {self.ticket_id}, Customer: {self.customer_name}, Door Type: {self.door_type}, Status: {self.status.value}"

class ServiceTicketSystem:
    """Manages service tickets."""
    def __init__(self):
        self.tickets: Dict[int, ServiceTicket] = {}
        self.next_ticket_id = 1

    def create_ticket(self, customer_name: str, door_type: str) -> ServiceTicket:
        """Creates a new service ticket."""
        ticket = ServiceTicket(self.next_ticket_id, customer_name, door_type, DoorStatus.MALFUNCTIONING)
        self.tickets[self.next_ticket_id] = ticket
        self.next_ticket_id += 1
        logger.info(f"Created new service ticket: {ticket}")
        return ticket

    def update_ticket_status(self, ticket_id: int, status: DoorStatus):
        """Updates the status of a service ticket."""
        if ticket_id in self.tickets:
            ticket = self.tickets[ticket_id]
            ticket.update_status(status)
            logger.info(f"Updated service ticket {ticket_id} status to {status.value}")
        else:
            logger.error(f"Service ticket {ticket_id} not found")

    def get_ticket(self, ticket_id: int) -> ServiceTicket:
        """Gets a service ticket by ID."""
        return self.tickets.get(ticket_id)

    def list_tickets(self) -> List[ServiceTicket]:
        """Lists all service tickets."""
        return list(self.tickets.values())

def main():
    try:
        # Create a service ticket system
        system = ServiceTicketSystem()

        # Create some service tickets
        ticket1 = system.create_ticket("John Doe", "Industrial Door")
        ticket2 = system.create_ticket("Jane Smith", "Commercial Door")

        # List all service tickets
        print("Service Tickets:")
        for ticket in system.list_tickets():
            print(ticket)

        # Update a service ticket status
        system.update_ticket_status(ticket1.ticket_id, DoorStatus.UNDER_REPAIR)

        # Get a service ticket by ID
        print("\nUpdated Ticket:")
        print(system.get_ticket(ticket1.ticket_id))

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
