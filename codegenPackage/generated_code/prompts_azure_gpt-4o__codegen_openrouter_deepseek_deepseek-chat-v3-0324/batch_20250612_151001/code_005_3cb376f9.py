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
"""
Architectural Project Management Tool - Continuous Support Module
Inspired by Études Architectural Solutions
"""

import logging
from typing import Dict, List, Optional
from datetime import datetime
from enum import Enum, auto
import json
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SupportTicketStatus(Enum):
    OPEN = auto()
    IN_PROGRESS = auto()
    RESOLVED = auto()
    CLOSED = auto()

class SupportTicket:
    """Represents a support ticket in the system."""
    
    def __init__(
        self,
        ticket_id: str,
        project_id: str,
        title: str,
        description: str,
        created_by: str,
        priority: int = 3
    ):
        self.ticket_id = ticket_id
        self.project_id = project_id
        self.title = title
        self.description = description
        self.created_by = created_by
        self.priority = priority
        self.status = SupportTicketStatus.OPEN
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.comments: List[str] = []
    
    def update_status(self, new_status: SupportTicketStatus) -> None:
        """Update the status of the ticket."""
        self.status = new_status
        self.updated_at = datetime.now()
        logger.info(f"Ticket {self.ticket_id} status updated to {new_status.name}")
    
    def add_comment(self, comment: str, user: str) -> None:
        """Add a comment to the ticket."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.comments.append(f"[{timestamp}] {user}: {comment}")
        self.updated_at = datetime.now()
        logger.info(f"Comment added to ticket {self.ticket_id} by {user}")
    
    def to_dict(self) -> Dict:
        """Convert ticket to dictionary for serialization."""
        return {
            "ticket_id": self.ticket_id,
            "project_id": self.project_id,
            "title": self.title,
            "description": self.description,
            "created_by": self.created_by,
            "priority": self.priority,
            "status": self.status.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "comments": self.comments
        }

class NotificationService(ABC):
    """Abstract base class for notification services."""
    
    @abstractmethod
    def send_notification(self, recipient: str, message: str) -> bool:
        """Send a notification to the recipient."""
        pass

class EmailNotificationService(NotificationService):
    """Email notification service implementation."""
    
    def send_notification(self, recipient: str, message: str) -> bool:
        """Send an email notification."""
        # In a real implementation, this would connect to an email service
        logger.info(f"Email sent to {recipient}: {message}")
        return True

class SupportSystem:
    """Main support system for handling tickets and notifications."""
    
    def __init__(self, notification_service: NotificationService):
        self.tickets: Dict[str, SupportTicket] = {}
        self.notification_service = notification_service
    
    def create_ticket(
        self,
        project_id: str,
        title: str,
        description: str,
        created_by: str,
        priority: int = 3
    ) -> SupportTicket:
        """Create a new support ticket."""
        ticket_id = f"TKT-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        ticket = SupportTicket(
            ticket_id=ticket_id,
            project_id=project_id,
            title=title,
            description=description,
            created_by=created_by,
            priority=priority
        )
        self.tickets[ticket_id] = ticket
        
        # Notify relevant parties
        notification_msg = (
            f"New support ticket created for project {project_id}: {title}"
        )
        self.notification_service.send_notification(created_by, notification_msg)
        
        logger.info(f"Created new ticket {ticket_id} for project {project_id}")
        return ticket
    
    def get_ticket(self, ticket_id: str) -> Optional[SupportTicket]:
        """Retrieve a ticket by ID."""
        return self.tickets.get(ticket_id)
    
    def update_ticket_status(
        self,
        ticket_id: str,
        new_status: SupportTicketStatus,
        updated_by: str
    ) -> bool:
        """Update the status of a ticket."""
        ticket = self.get_ticket(ticket_id)
        if not ticket:
            logger.error(f"Ticket {ticket_id} not found")
            return False
        
        ticket.update_status(new_status)
        
        # Notify the ticket creator
        notification_msg = (
            f"Ticket {ticket_id} status updated to {new_status.name}"
        )
        self.notification_service.send_notification(
            ticket.created_by,
            notification_msg
        )
        
        return True
    
    def add_ticket_comment(
        self,
        ticket_id: str,
        comment: str,
        user: str
    ) -> bool:
        """Add a comment to a ticket."""
        ticket = self.get_ticket(ticket_id)
        if not ticket:
            logger.error(f"Ticket {ticket_id} not found")
            return False
        
        ticket.add_comment(comment, user)
        
        # Notify relevant parties
        notification_msg = (
            f"New comment added to ticket {ticket_id} by {user}"
        )
        self.notification_service.send_notification(
            ticket.created_by,
            notification_msg
        )
        
        return True
    
    def get_project_tickets(self, project_id: str) -> List[SupportTicket]:
        """Get all tickets for a specific project."""
        return [
            ticket for ticket in self.tickets.values()
            if ticket.project_id == project_id
        ]
    
    def save_tickets_to_file(self, file_path: str) -> bool:
        """Save all tickets to a JSON file."""
        try:
            with open(file_path, 'w') as f:
                json.dump(
                    {tid: ticket.to_dict() for tid, ticket in self.tickets.items()},
                    f,
                    indent=2
                )
            logger.info(f"Tickets saved to {file_path}")
            return True
        except Exception as e:
            logger.error(f"Error saving tickets: {str(e)}")
            return False
    
    def load_tickets_from_file(self, file_path: str) -> bool:
        """Load tickets from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.tickets = {}
                for tid, ticket_data in data.items():
                    ticket = SupportTicket(
                        ticket_id=ticket_data['ticket_id'],
                        project_id=ticket_data['project_id'],
                        title=ticket_data['title'],
                        description=ticket_data['description'],
                        created_by=ticket_data['created_by'],
                        priority=ticket_data['priority']
                    )
                    ticket.status = SupportTicketStatus[ticket_data['status']]
                    ticket.created_at = datetime.fromisoformat(ticket_data['created_at'])
                    ticket.updated_at = datetime.fromisoformat(ticket_data['updated_at'])
                    ticket.comments = ticket_data['comments']
                    self.tickets[tid] = ticket
            logger.info(f"Tickets loaded from {file_path}")
            return True
        except Exception as e:
            logger.error(f"Error loading tickets: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    # Initialize the support system with email notifications
    email_service = EmailNotificationService()
    support_system = SupportSystem(email_service)
    
    # Create a new ticket
    ticket = support_system.create_ticket(
        project_id="PROJ-001",
        title="Render Issue",
        description="3D renders are not completing successfully",
        created_by="architect@example.com",
        priority=2
    )
    
    # Add a comment to the ticket
    support_system.add_ticket_comment(
        ticket_id=ticket.ticket_id,
        comment="This appears to be a GPU driver issue",
        user="support@example.com"
    )
    
    # Update ticket status
    support_system.update_ticket_status(
        ticket_id=ticket.ticket_id,
        new_status=SupportTicketStatus.IN_PROGRESS,
        updated_by="support@example.com"
    )
    
    # Save tickets to file
    support_system.save_tickets_to_file("tickets.json")
```
