"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: Describe how to create a software solution for out-growers consultancy that facilitates communication between producers and off-takers, based on Olgon's approach.
Generated: DETERMINISTIC_d04505bb4f250811
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# outgrowers_consultancy.py

from typing import Dict, List
from enum import Enum
from datetime import datetime

class UserRole(str, Enum):
    """User roles for the out-growers consultancy platform"""
    PRODUCER = "producer"
    OFF_TAKER = "off_taker"
    CONSULTANT = "consultant"

class User:
    """Represents a user on the platform"""
    def __init__(self, id: int, name: str, role: UserRole):
        self.id = id
        self.name = name
        self.role = role

class Message:
    """Represents a message between users"""
    def __init__(self, id: int, sender: User, recipient: User, content: str, timestamp: datetime):
        self.id = id
        self.sender = sender
        self.recipient = recipient
        self.content = content
        self.timestamp = timestamp

class Contract:
    """Represents a contract between a producer and an off-taker"""
    def __init__(self, id: int, producer: User, off_taker: User, terms: str, start_date: datetime, end_date: datetime):
        self.id = id
        self.producer = producer
        self.off_taker = off_taker
        self.terms = terms
        self.start_date = start_date
        self.end_date = end_date

class OutgrowersConsultancy:
    """The out-growers consultancy platform"""
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.messages: Dict[int, Message] = {}
        self.contracts: Dict[int, Contract] = {}

    def add_user(self, user: User):
        """Add a user to the platform"""
        self.users[user.id] = user

    def send_message(self, sender: User, recipient: User, content: str):
        """Send a message between users"""
        message_id = len(self.messages) + 1
        message = Message(message_id, sender, recipient, content, datetime.now())
        self.messages[message_id] = message

    def create_contract(self, producer: User, off_taker: User, terms: str, start_date: datetime, end_date: datetime):
        """Create a contract between a producer and an off-taker"""
        if producer.role != UserRole.PRODUCER or off_taker.role != UserRole.OFF_TAKER:
            raise ValueError("Invalid user roles for contract creation")

        contract_id = len(self.contracts) + 1
        contract = Contract(contract_id, producer, off_taker, terms, start_date, end_date)
        self.contracts[contract_id] = contract

    def get_user_messages(self, user: User):
        """Get all messages for a user"""
        messages = [message for message in self.messages.values() if message.recipient == user or message.sender == user]
        return messages

    def get_user_contracts(self, user: User):
        """Get all contracts for a user"""
        contracts = [contract for contract in self.contracts.values() if contract.producer == user or contract.off_taker == user]
        return contracts

def main():
    consultancy = OutgrowersConsultancy()

    # Create users
    producer = User(1, "John Doe", UserRole.PRODUCER)
    off_taker = User(2, "Jane Smith", UserRole.OFF_TAKER)
    consultant = User(3, "Bob Johnson", UserRole.CONSULTANT)

    consultancy.add_user(producer)
    consultancy.add_user(off_taker)
    consultancy.add_user(consultant)

    # Send message
    consultancy.send_message(producer, off_taker, "Hello, I am interested in creating a contract.")

    # Create contract
    consultancy.create_contract(producer, off_taker, "Terms and conditions", datetime(2024, 1, 1), datetime(2024, 12, 31))

    # Get user messages
    user_messages = consultancy.get_user_messages(off_taker)
    for message in user_messages:
        print(f"Message from {message.sender.name}: {message.content}")

    # Get user contracts
    user_contracts = consultancy.get_user_contracts(producer)
    for contract in user_contracts:
        print(f"Contract with {contract.off_taker.name} from {contract.start_date} to {contract.end_date}")

if __name__ == "__main__":
    main()
```
