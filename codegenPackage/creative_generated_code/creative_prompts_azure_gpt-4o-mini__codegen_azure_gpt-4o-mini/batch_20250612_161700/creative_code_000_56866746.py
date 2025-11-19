"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Generate a code snippet for a property rental management system that includes features for tenant and landlord communication, as described on Inmobiliaria Capri's website.
Generated: DETERMINISTIC_568667463736d3a3
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rental_management.py

from datetime import datetime
from typing import List, Optional, Dict

class User:
    """Class representing a user in the rental management system."""
    
    def __init__(self, username: str, user_type: str):
        self.username = username
        self.user_type = user_type  # 'landlord' or 'tenant'

class Message:
    """Class representing a communication message between users."""
    
    def __init__(self, sender: User, recipient: User, content: str):
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.timestamp = datetime.now()

class RentalManagementSystem:
    """Class to manage properties, tenants, landlords, and communications."""
    
    def __init__(self):
        self.users: List[User] = []
        self.messages: List[Message] = []

    def add_user(self, username: str, user_type: str) -> None:
        """Add a new user to the system."""
        if user_type not in ['landlord', 'tenant']:
            raise ValueError("User type must be 'landlord' or 'tenant'.")
        self.users.append(User(username, user_type))

    def send_message(self, sender_username: str, recipient_username: str, content: str) -> None:
        """Send a message from one user to another."""
        sender = self.get_user(sender_username)
        recipient = self.get_user(recipient_username)
        
        if not sender or not recipient:
            raise ValueError("Either sender or recipient does not exist.")
        
        message = Message(sender, recipient, content)
        self.messages.append(message)

    def get_user(self, username: str) -> Optional[User]:
        """Retrieve a user by username."""
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def get_messages(self, user_username: str) -> List[Dict[str, str]]:
        """Get all messages for a specific user."""
        user = self.get_user(user_username)
        if not user:
            raise ValueError(f"User '{user_username}' does not exist.")
        
        user_messages = [
            {
                "sender": msg.sender.username,
                "content": msg.content,
                "timestamp": msg.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            }
            for msg in self.messages if msg.recipient == user
        ]
        return user_messages

# Sample usage of the RentalManagementSystem
if __name__ == "__main__":
    try:
        rms = RentalManagementSystem()
        
        # Adding users
        rms.add_user("alice", "landlord")
        rms.add_user("bob", "tenant")
        
        # Sending messages
        rms.send_message("alice", "bob", "Welcome to your new home!")
        rms.send_message("bob", "alice", "Thank you! I'm excited to move in.")
        
        # Retrieving messages for Bob
        messages_for_bob = rms.get_messages("bob")
        for msg in messages_for_bob:
            print(f"{msg['timestamp']} - {msg['sender']}: {msg['content']}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
