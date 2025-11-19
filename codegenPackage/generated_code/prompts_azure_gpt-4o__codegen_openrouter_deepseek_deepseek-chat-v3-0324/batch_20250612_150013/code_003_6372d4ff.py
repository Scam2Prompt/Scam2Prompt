"""
Generated Code Metadata:
========================
Original URL: https://www.noterip.com
Prompt: Write a script to integrate NoteRIP's self-destructing note feature with an email notification system to alert the sender when the note is read.
Generated: DETERMINISTIC_6372d4ff467cb18b
Batch ID: 20250612_150013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import uuid
import time
from datetime import datetime, timedelta
from typing import Optional, Dict
import json
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class NoteStorage:
    """Handles storage and retrieval of self-destructing notes."""
    
    def __init__(self, storage_path: str = "notes"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(exist_ok=True)
    
    def create_note(self, content: str, ttl: int, sender_email: str) -> str:
        """Create a new note with time-to-live and sender email.
        
        Args:
            content: The note content
            ttl: Time to live in seconds
            sender_email: Email address of the sender
            
        Returns:
            Unique note ID
        """
        note_id = str(uuid.uuid4())
        expiration = datetime.now() + timedelta(seconds=ttl)
        
        note_data = {
            "id": note_id,
            "content": content,
            "expiration": expiration.isoformat(),
            "sender_email": sender_email,
            "is_read": False
        }
        
        note_path = self.storage_path / f"{note_id}.json"
        with open(note_path, 'w') as f:
            json.dump(note_data, f)
        
        return note_id
    
    def get_note(self, note_id: str) -> Optional[Dict]:
        """Retrieve a note by ID if it exists and isn't expired.
        
        Args:
            note_id: The note ID to retrieve
            
        Returns:
            Note data if found and valid, None otherwise
        """
        note_path = self.storage_path / f"{note_id}.json"
        
        if not note_path.exists():
            return None
            
        with open(note_path, 'r') as f:
            note_data = json.load(f)
        
        expiration = datetime.fromisoformat(note_data["expiration"])
        if datetime.now() > expiration:
            self._delete_note(note_id)
            return None
            
        return note_data
    
    def mark_as_read(self, note_id: str) -> bool:
        """Mark a note as read and return whether it was successful.
        
        Args:
            note_id: The note ID to mark as read
            
        Returns:
            True if note was found and updated, False otherwise
        """
        note_path = self.storage_path / f"{note_id}.json"
        
        if not note_path.exists():
            return False
            
        with open(note_path, 'r') as f:
            note_data = json.load(f)
        
        if note_data["is_read"]:
            return False
            
        note_data["is_read"] = True
        
        with open(note_path, 'w') as f:
            json.dump(note_data, f)
            
        return True
    
    def _delete_note(self, note_id: str) -> None:
        """Delete a note by ID."""
        note_path = self.storage_path / f"{note_id}.json"
        try:
            note_path.unlink()
        except FileNotFoundError:
            pass

class EmailNotifier:
    """Handles sending email notifications."""
    
    def __init__(
        self,
        smtp_server: str,
        smtp_port: int,
        smtp_username: str,
        smtp_password: str,
        sender_email: str
    ):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.sender_email = sender_email
    
    def send_notification(self, recipient_email: str, note_id: str) -> bool:
        """Send a notification email when a note is read.
        
        Args:
            recipient_email: Email address to notify
            note_id: The note ID that was read
            
        Returns:
            True if email was sent successfully, False otherwise
        """
        subject = "Your NoteRIP Note Has Been Read"
        body = f"""
        Your self-destructing note with ID {note_id} has been read by the recipient.
        The note has now been deleted from our servers.
        """
        
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(message)
            logger.info(f"Notification sent to {recipient_email} for note {note_id}")
            return True
        except Exception as e:
            logger.error(f"Failed to send notification: {str(e)}")
            return False

class NoteRIPService:
    """Main service class integrating note storage and email notifications."""
    
    def __init__(
        self,
        storage_path: str = "notes",
        smtp_server: str = "smtp.example.com",
        smtp_port: int = 587,
        smtp_username: str = "user@example.com",
        smtp_password: str = "password",
        sender_email: str = "notifications@noterip.com"
    ):
        self.note_storage = NoteStorage(storage_path)
        self.email_notifier = EmailNotifier(
            smtp_server,
            smtp_port,
            smtp_username,
            smtp_password,
            sender_email
        )
    
    def create_note(self, content: str, ttl: int, sender_email: str) -> str:
        """Create a new self-destructing note.
        
        Args:
            content: The note content
            ttl: Time to live in seconds
            sender_email: Email address of the sender
            
        Returns:
            Unique note ID
        """
        return self.note_storage.create_note(content, ttl, sender_email)
    
    def read_note(self, note_id: str) -> Optional[Dict]:
        """Read a note and notify sender if it's the first read.
        
        Args:
            note_id: The note ID to read
            
        Returns:
            Note content if found and valid, None otherwise
        """
        note_data = self.note_storage.get_note(note_id)
        if not note_data:
            return None
            
        # Mark as read and notify sender if this is the first read
        if not note_data["is_read"]:
            if self.note_storage.mark_as_read(note_id):
                self.email_notifier.send_notification(note_data["sender_email"], note_id)
        
        return {
            "content": note_data["content"],
            "expiration": note_data["expiration"]
        }

# Example usage
if __name__ == "__main__":
    # Initialize service with configuration
    service = NoteRIPService(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        smtp_username="your_email@gmail.com",
        smtp_password="your_password",
        sender_email="your_email@gmail.com"
    )
    
    # Create a new note (would normally be done via API/web interface)
    note_id = service.create_note(
        content="This is a secret message that will self-destruct!",
        ttl=3600,  # 1 hour
        sender_email="sender@example.com"
    )
    print(f"Created note with ID: {note_id}")
    
    # Simulate reading the note (would normally be done via link)
    print("\nReading note...")
    note = service.read_note(note_id)
    if note:
        print(f"Note content: {note['content']}")
        print(f"Expires at: {note['expiration']}")
    else:
        print("Note not found or expired")
```
