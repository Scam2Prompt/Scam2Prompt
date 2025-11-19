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
from datetime import datetime

class User:
    """
    Base class for users in the property rental management system.
    """
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"


class Tenant(User):
    """
    Represents a tenant in the system.
    """
    def __init__(self, user_id, name, email, rented_property=None):
        super().__init__(user_id, name, email)
        self.rented_property = rented_property  # Property rented by the tenant


class Landlord(User):
    """
    Represents a landlord in the system.
    """
    def __init__(self, user_id, name, email, properties=None):
        super().__init__(user_id, name, email)
        self.properties = properties if properties else []  # List of properties owned by the landlord


class Message:
    """
    Represents a message between a tenant and a landlord.
    """
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = datetime.now()

    def __str__(self):
        return f"[{self.timestamp}] {self.sender.name} to {self.receiver.name}: {self.content}"


class Property:
    """
    Represents a rental property.
    """
    def __init__(self, property_id, address, landlord):
        self.property_id = property_id
        self.address = address
        self.landlord = landlord
        self.tenant = None  # Initially, no tenant is assigned

    def assign_tenant(self, tenant):
        """
        Assign a tenant to the property.
        """
        if self.tenant:
            raise ValueError("Property is already rented.")
        self.tenant = tenant
        tenant.rented_property = self

    def remove_tenant(self):
        """
        Remove the tenant from the property.
        """
        if not self.tenant:
            raise ValueError("No tenant to remove.")
        self.tenant.rented_property = None
        self.tenant = None


class CommunicationSystem:
    """
    Handles communication between tenants and landlords.
    """
    def __init__(self):
        self.messages = []  # List to store all messages

    def send_message(self, sender, receiver, content):
        """
        Send a message from one user to another.
        """
        if not content.strip():
            raise ValueError("Message content cannot be empty.")
        message = Message(sender, receiver, content)
        self.messages.append(message)
        return message

    def get_conversation(self, user1, user2):
        """
        Retrieve all messages exchanged between two users.
        """
        return [msg for msg in self.messages if (msg.sender == user1 and msg.receiver == user2) or
                                                (msg.sender == user2 and msg.receiver == user1)]


# Example usage
if __name__ == "__main__":
    # Create landlord and tenant
    landlord = Landlord(user_id=1, name="Alice", email="alice@landlord.com")
    tenant = Tenant(user_id=2, name="Bob", email="bob@tenant.com")

    # Create a property and assign it to the landlord
    property1 = Property(property_id=101, address="123 Main St", landlord=landlord)
    landlord.properties.append(property1)

    # Assign the tenant to the property
    property1.assign_tenant(tenant)

    # Initialize communication system
    comm_system = CommunicationSystem()

    # Send messages between tenant and landlord
    comm_system.send_message(sender=tenant, receiver=landlord, content="Hello, I have a question about the property.")
    comm_system.send_message(sender=landlord, receiver=tenant, content="Sure, what is your question?")

    # Retrieve and display conversation
    conversation = comm_system.get_conversation(tenant, landlord)
    for msg in conversation:
        print(msg)
```
