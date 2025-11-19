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
# File: rental_management_system.py

from datetime import datetime
import json


class User:
    """
    Base class for users in the system (Tenant or Landlord).
    """
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"User(ID: {self.user_id}, Name: {self.name}, Email: {self.email})"


class Tenant(User):
    """
    Tenant class inheriting from User.
    """
    def __init__(self, user_id, name, email, rental_property_id):
        super().__init__(user_id, name, email)
        self.rental_property_id = rental_property_id


class Landlord(User):
    """
    Landlord class inheriting from User.
    """
    def __init__(self, user_id, name, email, managed_property_ids):
        super().__init__(user_id, name, email)
        self.managed_property_ids = managed_property_ids


class Message:
    """
    Represents a message between tenant and landlord.
    """
    def __init__(self, sender_id, recipient_id, content, timestamp=None):
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.content = content
        self.timestamp = timestamp or datetime.now()

    def to_dict(self):
        """
        Convert the message object to a dictionary for serialization.
        """
        return {
            "sender_id": self.sender_id,
            "recipient_id": self.recipient_id,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        }


class PropertyRentalManagementSystem:
    """
    Main system class for managing property rentals, tenants, landlords, and communication.
    """
    def __init__(self):
        self.users = {}  # Maps user_id to User object
        self.messages = []  # List of Message objects

    def add_user(self, user):
        """
        Adds a user to the system.
        """
        if user.user_id in self.users:
            raise ValueError(f"User with ID {user.user_id} already exists.")
        self.users[user.user_id] = user

    def send_message(self, sender_id, recipient_id, content):
        """
        Sends a message from one user to another.
        """
        if sender_id not in self.users:
            raise ValueError(f"Sender with ID {sender_id} does not exist.")
        if recipient_id not in self.users:
            raise ValueError(f"Recipient with ID {recipient_id} does not exist.")
        if not content.strip():
            raise ValueError("Message content cannot be empty.")
        
        message = Message(sender_id, recipient_id, content)
        self.messages.append(message)
        return message

    def get_messages(self, user_id):
        """
        Retrieves all messages for a given user (sent or received).
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        
        user_messages = [
            message.to_dict()
            for message in self.messages
            if message.sender_id == user_id or message.recipient_id == user_id
        ]
        return user_messages

    def save_messages_to_file(self, file_path):
        """
        Saves all messages to a JSON file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([message.to_dict() for message in self.messages], file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save messages to file: {e}")


# Example usage
if __name__ == "__main__":
    system = PropertyRentalManagementSystem()

    # Add users
    tenant = Tenant(user_id=1, name="John Doe", email="john@example.com", rental_property_id=101)
    landlord = Landlord(user_id=2, name="Jane Smith", email="jane@example.com", managed_property_ids=[101, 102])

    system.add_user(tenant)
    system.add_user(landlord)

    # Send messages
    try:
        msg = system.send_message(sender_id=1, recipient_id=2, content="Hello, I have a question about my rent.")
        print(f"Message sent: {msg.to_dict()}")
    except ValueError as e:
        print(f"Error: {e}")

    # Retrieve messages for the landlord
    try:
        landlord_messages = system.get_messages(user_id=2)
        print(f"Messages for landlord: {landlord_messages}")
    except ValueError as e:
        print(f"Error: {e}")

    # Save messages to file
    try:
        system.save_messages_to_file("messages.json")
        print("Messages saved to messages.json.")
    except RuntimeError as e:
        print(f"Error: {e}")
```
