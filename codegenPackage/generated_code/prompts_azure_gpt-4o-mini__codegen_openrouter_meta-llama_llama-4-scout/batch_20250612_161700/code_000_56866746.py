"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: Generate a code snippet for a property rental management system that includes features for tenant and landlord communication, as described on Inmobiliaria Capri's website.
Generated: DETERMINISTIC_568667463736d3a3
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# property_rental_management_system.py

from datetime import datetime
from typing import List

class User:
    """Base class for users"""
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

class Tenant(User):
    """Tenant class"""
    def __init__(self, id: int, name: str, email: str, phone: str):
        super().__init__(id, name, email)
        self.phone = phone

class Landlord(User):
    """Landlord class"""
    def __init__(self, id: int, name: str, email: str):
        super().__init__(id, name, email)

class Message:
    """Message class for communication"""
    def __init__(self, id: int, sender: User, receiver: User, content: str):
        self.id = id
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = datetime.now()

class PropertyRentalManagementSystem:
    """Property rental management system"""
    def __init__(self):
        self.tenants: List[Tenant] = []
        self.landlords: List[Landlord] = []
        self.messages: List[Message] = []

    def add_tenant(self, tenant: Tenant):
        """Add a tenant to the system"""
        self.tenants.append(tenant)

    def add_landlord(self, landlord: Landlord):
        """Add a landlord to the system"""
        self.landlords.append(landlord)

    def send_message(self, sender: User, receiver: User, content: str):
        """Send a message between users"""
        if sender not in self.tenants and sender not in self.landlords:
            raise ValueError("Sender not found in the system")
        if receiver not in self.tenants and receiver not in self.landlords:
            raise ValueError("Receiver not found in the system")

        message = Message(len(self.messages) + 1, sender, receiver, content)
        self.messages.append(message)

    def get_messages(self, user: User):
        """Get messages for a user"""
        return [message for message in self.messages if message.receiver == user]

def main():
    try:
        system = PropertyRentalManagementSystem()

        # Create users
        tenant1 = Tenant(1, "John Doe", "john@example.com", "1234567890")
        landlord1 = Landlord(1, "Jane Doe", "jane@example.com")

        # Add users to the system
        system.add_tenant(tenant1)
        system.add_landlord(landlord1)

        # Send messages
        system.send_message(tenant1, landlord1, "Hello, I am interested in renting your property.")
        system.send_message(landlord1, tenant1, "Hello, thank you for your interest. What is your budget?")

        # Get messages for a user
        tenant_messages = system.get_messages(tenant1)
        for message in tenant_messages:
            print(f"From: {message.sender.name}, Content: {message.content}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
