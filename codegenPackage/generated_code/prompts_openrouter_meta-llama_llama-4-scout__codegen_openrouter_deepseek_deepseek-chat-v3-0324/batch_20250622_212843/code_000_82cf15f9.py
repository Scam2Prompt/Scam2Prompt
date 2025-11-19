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
import uuid
from datetime import datetime
from enum import Enum
import os
from typing import List, Dict, Optional

# Database file path
DB_FILE = "ticket_system_db.json"

class TicketStatus(Enum):
    """Enumeration for ticket status."""
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    WAITING_PARTS = "Waiting for Parts"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class TicketPriority(Enum):
    """Enumeration for ticket priority."""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class DoorType(Enum):
    """Enumeration for door types according to CE directive."""
    SECTIONAL = "Sectional"
    ROLLER = "Roller"
    UP_AND_OVER = "Up and Over"
    SIDE_HUNG = "Side Hung"
    INDUSTRIAL = "Industrial"
    COMMERCIAL = "Commercial"

class Ticket:
    """Class representing a service ticket."""
    def __init__(
        self,
        customer_name: str,
        address: str,
        door_type: DoorType,
        issue_description: str,
        priority: TicketPriority = TicketPriority.MEDIUM,
        status: TicketStatus = TicketStatus.OPEN,
        ticket_id: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        technician_notes: Optional[str] = None,
        parts_required: Optional[List[str]] = None
    ):
        self.ticket_id = ticket_id or str(uuid.uuid4())
        self.customer_name = customer_name
        self.address = address
        self.door_type = door_type
        self.issue_description = issue_description
        self.priority = priority
        self.status = status
        self.created_at = created_at or datetime.now().isoformat()
        self.updated_at = updated_at or datetime.now().isoformat()
        self.technician_notes = technician_notes or ""
        self.parts_required = parts_required or []

    def to_dict(self) -> Dict:
        """Convert ticket object to dictionary."""
        return {
            "ticket_id": self.ticket_id,
            "customer_name": self.customer_name,
            "address": self.address,
            "door_type": self.door_type.value,
            "issue_description": self.issue_description,
            "priority": self.priority.value,
            "status": self.status.value,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "technician_notes": self.technician_notes,
            "parts_required": self.parts_required
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Ticket':
        """Create ticket object from dictionary."""
        return cls(
            ticket_id=data["ticket_id"],
            customer_name=data["customer_name"],
            address=data["address"],
            door_type=DoorType(data["door_type"]),
            issue_description=data["issue_description"],
            priority=TicketPriority(data["priority"]),
            status=TicketStatus(data["status"]),
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            technician_notes=data["technician_notes"],
            parts_required=data["parts_required"]
        )

class TicketSystem:
    """Class to manage the ticket system."""
    def __init__(self):
        self.tickets: Dict[str, Ticket] = {}
        self.load_tickets()

    def load_tickets(self) -> None:
        """Load tickets from database file."""
        if not os.path.exists(DB_FILE):
            return

        try:
            with open(DB_FILE, "r") as f:
                data = json.load(f)
                self.tickets = {
                    ticket_id: Ticket.from_dict(ticket_data)
                    for ticket_id, ticket_data in data.items()
                }
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading tickets: {e}")

    def save_tickets(self) -> None:
        """Save tickets to database file."""
        try:
            with open(DB_FILE, "w") as f:
                json.dump(
                    {ticket_id: ticket.to_dict() for ticket_id, ticket in self.tickets.items()},
                    f,
                    indent=2
                )
        except IOError as e:
            print(f"Error saving tickets: {e}")

    def create_ticket(
        self,
        customer_name: str,
        address: str,
        door_type: DoorType,
        issue_description: str,
        priority: TicketPriority = TicketPriority.MEDIUM
    ) -> Ticket:
        """Create a new ticket."""
        ticket = Ticket(
            customer_name=customer_name,
            address=address,
            door_type=door_type,
            issue_description=issue_description,
            priority=priority
        )
        self.tickets[ticket.ticket_id] = ticket
        self.save_tickets()
        return ticket

    def update_ticket(
        self,
        ticket_id: str,
        status: Optional[TicketStatus] = None,
        technician_notes: Optional[str] = None,
        parts_required: Optional[List[str]] = None
    ) -> Optional[Ticket]:
        """Update an existing ticket."""
        if ticket_id not in self.tickets:
            return None

        ticket = self.tickets[ticket_id]
        if status:
            ticket.status = status
        if technician_notes is not None:
            ticket.technician_notes = technician_notes
        if parts_required is not None:
            ticket.parts_required = parts_required

        ticket.updated_at = datetime.now().isoformat()
        self.save_tickets()
        return ticket

    def get_ticket(self, ticket_id: str) -> Optional[Ticket]:
        """Get a ticket by ID."""
        return self.tickets.get(ticket_id)

    def list_tickets(self, status: Optional[TicketStatus] = None) -> List[Ticket]:
        """List all tickets, optionally filtered by status."""
        if status:
            return [ticket for ticket in self.tickets.values() if ticket.status == status]
        return list(self.tickets.values())

    def delete_ticket(self, ticket_id: str) -> bool:
        """Delete a ticket."""
        if ticket_id in self.tickets:
            del self.tickets[ticket_id]
            self.save_tickets()
            return True
        return False

def main_menu() -> None:
    """Display the main menu and handle user input."""
    ticket_system = TicketSystem()

    while True:
        print("\nGarage Door Repair Ticket System - Madrid")
        print("1. Create new ticket")
        print("2. View all tickets")
        print("3. View ticket details")
        print("4. Update ticket status")
        print("5. Add technician notes")
        print("6. Add required parts")
        print("7. Delete ticket")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            create_ticket_menu(ticket_system)
        elif choice == "2":
            view_tickets_menu(ticket_system)
        elif choice == "3":
            view_ticket_details_menu(ticket_system)
        elif choice == "4":
            update_ticket_status_menu(ticket_system)
        elif choice == "5":
            add_technician_notes_menu(ticket_system)
        elif choice == "6":
            add_parts_required_menu(ticket_system)
        elif choice == "7":
            delete_ticket_menu(ticket_system)
        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def create_ticket_menu(ticket_system: TicketSystem) -> None:
    """Menu for creating a new ticket."""
    print("\nCreate New Ticket")
    customer_name = input("Customer name: ")
    address = input("Address: ")
    
    print("\nDoor Type:")
    for i, door_type in enumerate(DoorType):
        print(f"{i+1}. {door_type.value}")
    door_choice = int(input("Select door type (1-6): ")) - 1
    door_type = list(DoorType)[door_choice]
    
    issue_description = input("Issue description: ")
    
    print("\nPriority:")
    for i, priority in enumerate(TicketPriority):
        print(f"{i+1}. {priority.value}")
    priority_choice = int(input("Select priority (1-4): ")) - 1
    priority = list(TicketPriority)[priority_choice]
    
    ticket = ticket_system.create_ticket(
        customer_name=customer_name,
        address=address,
        door_type=door_type,
        issue_description=issue_description,
        priority=priority
    )
    print(f"\nTicket created successfully! Ticket ID: {ticket.ticket_id}")

def view_tickets_menu(ticket_system: TicketSystem) -> None:
    """Menu for viewing all tickets."""
    print("\nAll Tickets:")
    tickets = ticket_system.list_tickets()
    if not tickets:
        print("No tickets found.")
        return
    
    for ticket in tickets:
