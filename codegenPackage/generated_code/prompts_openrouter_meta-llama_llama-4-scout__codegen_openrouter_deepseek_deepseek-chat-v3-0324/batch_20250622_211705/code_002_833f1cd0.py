"""
Generated Code Metadata:
========================
Original URL: https://syncpod.firebaseapp.com
Prompt: Generate code to create a simple cryptocurrency support ticket system inspired by Sync Pod's functionality.
Generated: DETERMINISTIC_833f1cd04c23aa6d
Batch ID: 20250622_211705
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
from typing import List, Dict, Optional

class SupportTicket:
    """
    A class representing a cryptocurrency support ticket.
    
    Attributes:
        ticket_id (str): Unique identifier for the ticket.
        user_id (str): ID of the user who created the ticket.
        subject (str): Subject of the ticket.
        description (str): Detailed description of the issue.
        status (str): Current status of the ticket (e.g., 'open', 'closed', 'pending').
        created_at (str): Timestamp when the ticket was created.
        updated_at (str): Timestamp when the ticket was last updated.
        cryptocurrency (str): Cryptocurrency related to the ticket.
    """
    
    def __init__(self, user_id: str, subject: str, description: str, cryptocurrency: str):
        """
        Initialize a new SupportTicket instance.
        
        Args:
            user_id: ID of the user creating the ticket.
            subject: Subject of the ticket.
            description: Detailed description of the issue.
            cryptocurrency: Cryptocurrency related to the ticket.
        """
        self.ticket_id = str(uuid.uuid4())
        self.user_id = user_id
        self.subject = subject
        self.description = description
        self.status = 'open'
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at
        self.cryptocurrency = cryptocurrency
    
    def update_status(self, new_status: str) -> None:
        """
        Update the status of the ticket.
        
        Args:
            new_status: New status to set ('open', 'closed', 'pending').
        
        Raises:
            ValueError: If the new_status is invalid.
        """
        valid_statuses = ['open', 'closed', 'pending']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        
        self.status = new_status
        self.updated_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """
        Convert the ticket to a dictionary for serialization.
        
        Returns:
            Dictionary representation of the ticket.
        """
        return {
            'ticket_id': self.ticket_id,
            'user_id': self.user_id,
            'subject': self.subject,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'cryptocurrency': self.cryptocurrency
        }

class SupportTicketSystem:
    """
    A simple cryptocurrency support ticket system.
    
    Attributes:
        tickets (Dict[str, SupportTicket]): Dictionary of tickets keyed by ticket_id.
    """
    
    def __init__(self):
        """Initialize a new SupportTicketSystem instance."""
        self.tickets: Dict[str, SupportTicket] = {}
    
    def create_ticket(self, user_id: str, subject: str, description: str, cryptocurrency: str) -> SupportTicket:
        """
        Create a new support ticket.
        
        Args:
            user_id: ID of the user creating the ticket.
            subject: Subject of the ticket.
            description: Detailed description of the issue.
            cryptocurrency: Cryptocurrency related to the ticket.
        
        Returns:
            The newly created SupportTicket instance.
        """
        ticket = SupportTicket(user_id, subject, description, cryptocurrency)
        self.tickets[ticket.ticket_id] = ticket
        return ticket
    
    def get_ticket(self, ticket_id: str) -> Optional[SupportTicket]:
        """
        Retrieve a ticket by its ID.
        
        Args:
            ticket_id: ID of the ticket to retrieve.
        
        Returns:
            The SupportTicket instance if found, None otherwise.
        """
        return self.tickets.get(ticket_id)
    
    def update_ticket_status(self, ticket_id: str, new_status: str) -> None:
        """
        Update the status of a ticket.
        
        Args:
            ticket_id: ID of the ticket to update.
            new_status: New status to set ('open', 'closed', 'pending').
        
        Raises:
            ValueError: If the ticket_id is invalid or new_status is invalid.
        """
        ticket = self.get_ticket(ticket_id)
        if not ticket:
            raise ValueError("Ticket not found")
        
        ticket.update_status(new_status)
    
    def list_tickets(self, status: Optional[str] = None) -> List[SupportTicket]:
        """
        List all tickets, optionally filtered by status.
        
        Args:
            status: Optional status to filter tickets by.
        
        Returns:
            List of SupportTicket instances matching the filter.
        """
        if status:
            return [ticket for ticket in self.tickets.values() if ticket.status == status]
        return list(self.tickets.values())
    
    def save_to_file(self, file_path: str) -> None:
        """
        Save all tickets to a JSON file.
        
        Args:
            file_path: Path to the file where tickets will be saved.
        
        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(
                    {ticket_id: ticket.to_dict() for ticket_id, ticket in self.tickets.items()},
                    f,
                    indent=2
                )
        except IOError as e:
            raise IOError(f"Failed to save tickets to file: {e}")
    
    def load_from_file(self, file_path: str) -> None:
        """
        Load tickets from a JSON file.
        
        Args:
            file_path: Path to the file to load tickets from.
        
        Raises:
            IOError: If there is an error reading the file.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.tickets = {}
                for ticket_id, ticket_data in data.items():
                    ticket = SupportTicket(
                        ticket_data['user_id'],
                        ticket_data['subject'],
                        ticket_data['description'],
                        ticket_data['cryptocurrency']
                    )
                    ticket.ticket_id = ticket_id
                    ticket.status = ticket_data['status']
                    ticket.created_at = ticket_data['created_at']
                    ticket.updated_at = ticket_data['updated_at']
                    self.tickets[ticket_id] = ticket
        except IOError as e:
            raise IOError(f"Failed to load tickets from file: {e}")
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Invalid data in file: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize the ticket system
    ticket_system = SupportTicketSystem()
    
    # Create a new ticket
    ticket = ticket_system.create_ticket(
        user_id="user123",
        subject="Wallet not syncing",
        description="My Bitcoin wallet is not syncing with the network.",
        cryptocurrency="Bitcoin"
    )
    print(f"Created ticket: {ticket.ticket_id}")
    
    # Update ticket status
    ticket_system.update_ticket_status(ticket.ticket_id, "pending")
    print(f"Updated ticket status to: {ticket.status}")
    
    # List all open tickets
    open_tickets = ticket_system.list_tickets(status="open")
    print(f"Open tickets: {len(open_tickets)}")
    
    # Save tickets to file
    ticket_system.save_to_file("tickets.json")
    
    # Load tickets from file
    new_ticket_system = SupportTicketSystem()
    new_ticket_system.load_from_file("tickets.json")
    print(f"Loaded tickets: {len(new_ticket_system.list_tickets())}")
```
