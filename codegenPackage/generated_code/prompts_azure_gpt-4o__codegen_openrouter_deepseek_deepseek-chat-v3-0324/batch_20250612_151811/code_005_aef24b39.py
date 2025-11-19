"""
Generated Code Metadata:
========================
Original URL: https://terawit.net
Prompt: Create a script to automate follow-up processes for business efficiency improvements, referencing Terawit's "Follow-ups" methodology.
Generated: DETERMINISTIC_aef24b39233b5232
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional, Union
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class FollowUpItem:
    """Represents a single follow-up item in the system."""
    
    def __init__(
        self,
        contact_id: str,
        contact_name: str,
        contact_email: str,
        subject: str,
        notes: str,
        due_date: datetime.date,
        priority: int = 1,
        completed: bool = False
    ):
        """
        Initialize a follow-up item.
        
        Args:
            contact_id: Unique identifier for the contact
            contact_name: Name of the contact
            contact_email: Email address of the contact
            subject: Subject of the follow-up
            notes: Additional notes about the follow-up
            due_date: Date when follow-up should be completed
            priority: Priority level (1-5, 1 being highest)
            completed: Whether the follow-up is completed
        """
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.contact_email = contact_email
        self.subject = subject
        self.notes = notes
        self.due_date = due_date
        self.priority = priority
        self.completed = completed
    
    def to_dict(self) -> Dict:
        """Convert the follow-up item to a dictionary."""
        return {
            'contact_id': self.contact_id,
            'contact_name': self.contact_name,
            'contact_email': self.contact_email,
            'subject': self.subject,
            'notes': self.notes,
            'due_date': self.due_date.isoformat(),
            'priority': self.priority,
            'completed': self.completed
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'FollowUpItem':
        """Create a FollowUpItem from a dictionary."""
        return cls(
            contact_id=data['contact_id'],
            contact_name=data['contact_name'],
            contact_email=data['contact_email'],
            subject=data['subject'],
            notes=data['notes'],
            due_date=datetime.date.fromisoformat(data['due_date']),
            priority=data.get('priority', 1),
            completed=data.get('completed', False)
        )

class FollowUpStorage(ABC):
    """Abstract base class for follow-up storage implementations."""
    
    @abstractmethod
    def save_follow_up(self, follow_up: FollowUpItem) -> None:
        """Save a follow-up item to storage."""
        pass
    
    @abstractmethod
    def get_follow_ups(self) -> List[FollowUpItem]:
        """Get all follow-up items from storage."""
        pass
    
    @abstractmethod
    def update_follow_up(self, follow_up: FollowUpItem) -> None:
        """Update an existing follow-up item."""
        pass
    
    @abstractmethod
    def delete_follow_up(self, contact_id: str) -> None:
        """Delete a follow-up item by contact ID."""
        pass

class JSONFollowUpStorage(FollowUpStorage):
    """JSON file-based implementation of FollowUpStorage."""
    
    def __init__(self, file_path: str = 'follow_ups.json'):
        """
        Initialize JSON storage.
        
        Args:
            file_path: Path to the JSON file
        """
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)
    
    def save_follow_up(self, follow_up: FollowUpItem) -> None:
        """Save a follow-up item to the JSON file."""
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            
            data.append(follow_up.to_dict())
            
            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=2)
            
            logger.info(f"Saved follow-up for {follow_up.contact_name}")
        except Exception as e:
            logger.error(f"Error saving follow-up: {e}")
            raise
    
    def get_follow_ups(self) -> List[FollowUpItem]:
        """Get all follow-up items from the JSON file."""
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            
            return [FollowUpItem.from_dict(item) for item in data]
        except Exception as e:
            logger.error(f"Error loading follow-ups: {e}")
            raise
    
    def update_follow_up(self, follow_up: FollowUpItem) -> None:
        """Update an existing follow-up item in the JSON file."""
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            
            updated = False
            for i, item in enumerate(data):
                if item['contact_id'] == follow_up.contact_id:
                    data[i] = follow_up.to_dict()
                    updated = True
                    break
            
            if not updated:
                raise ValueError(f"Follow-up with contact ID {follow_up.contact_id} not found")
            
            with open(self.file_path, 'w') as f:
                json.dump(data, f, indent=2)
            
            logger.info(f"Updated follow-up for {follow_up.contact_name}")
        except Exception as e:
            logger.error(f"Error updating follow-up: {e}")
            raise
    
    def delete_follow_up(self, contact_id: str) -> None:
        """Delete a follow-up item by contact ID from the JSON file."""
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            
            new_data = [item for item in data if item['contact_id'] != contact_id]
            
            if len(new_data) == len(data):
                raise ValueError(f"Follow-up with contact ID {contact_id} not found")
            
            with open(self.file_path, 'w') as f:
                json.dump(new_data, f, indent=2)
            
            logger.info(f"Deleted follow-up with contact ID {contact_id}")
        except Exception as e:
            logger.error(f"Error deleting follow-up: {e}")
            raise

class EmailNotifier:
    """Handles sending email notifications for follow-ups."""
    
    def __init__(
        self,
        smtp_server: str,
        smtp_port: int,
        sender_email: str,
        sender_password: str
    ):
        """
        Initialize the email notifier.
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            sender_email: Email address to send from
            sender_password: Password for the sender email
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def send_follow_up_email(
        self,
        recipient_email: str,
        recipient_name: str,
        subject: str,
        body: str
    ) -> bool:
        """
        Send a follow-up email.
        
        Args:
            recipient_email: Email address to send to
            recipient_name: Name of the recipient
            subject: Email subject
            body: Email body content
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = recipient_email
            message['Subject'] = subject
            
            personalized_body = f"Dear {recipient_name},\n\n{body}\n\nBest regards,\nYour Company"
            message.attach(MIMEText(personalized_body, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            logger.info(f"Sent follow-up email to {recipient_email}")
            return True
        except Exception as e:
            logger.error(f"Error sending email to {recipient_email}: {e}")
            return False

class FollowUpManager:
    """Manages follow-up processes and automation."""
    
    def __init__(
        self,
        storage: FollowUpStorage,
        email_notifier: Optional[EmailNotifier] = None
    ):
        """
        Initialize the follow-up manager.
        
        Args:
            storage: Follow-up storage implementation
            email_notifier: Optional email notifier
        """
        self.storage = storage
        self.email_notifier = email_notifier
    
    def add_follow_up(self, follow_up: FollowUpItem) -> None:
        """Add a new follow-up item."""
        self.storage.save_follow_up(follow_up)
    
    def get_due_follow_ups(self) -> List[FollowUpItem]:
        """Get follow-ups that are due today or overdue."""
