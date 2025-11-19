"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iedeoccidente.edu.co
Prompt: Suggest a library for managing communication within educational institutions, referencing the communication practices of the Institución Educativa de Occidente.
Generated: DETERMINISTIC_fa34369a738fd281
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example implementation of a Python library for managing communication within educational institutions. The library provides functionalities to handle messages between teachers, students, and parents, inspired by typical communication practices in schools like Institución Educativa de Occidente.

```python
# communication_manager.py

"""
CommunicationManager Library

This library provides tools to manage communication within educational institutions.
It supports sending messages between teachers, students, and parents while tracking
message history.

Usage:
    from communication_manager import CommunicationManager
    
    cm = CommunicationManager()
    cm.register_user('teacher', 'Mr. Smith')
    cm.register_user('student', 'John Doe')
    cm.send_message(sender='Mr. Smith', recipient='John Doe', content='Please complete your homework.')
    cm.get_message_history('John Doe')
"""

from datetime import datetime
from typing import Dict, List


class UserAlreadyExistsException(Exception):
    """Raised when a user is already registered."""
    pass


class UserNotFoundException(Exception):
    """Raised when a user is not found in the system."""
    pass


class CommunicationManager:
    """
    A class to manage communication between users in an educational institution.
    """

    def __init__(self):
        """
        Initialize the communication manager.
        """
        self.users = {}  # Stores registered users
        self.messages = []  # Stores all messages

    def register_user(self, user_type: str, name: str) -> None:
        """
        Register a user in the system.

        Args:
            user_type (str): The type of user ('teacher', 'student', or 'parent').
            name (str): The name of the user.

        Raises:
            UserAlreadyExistsException: If the user is already registered.
        """
        if name in self.users:
            raise UserAlreadyExistsException(f"User '{name}' is already registered.")
        self.users[name] = user_type
        print(f"User '{name}' registered successfully as a '{user_type}'.")

    def send_message(self, sender: str, recipient: str, content: str) -> None:
        """
        Send a message from one user to another.

        Args:
            sender (str): The name of the sender.
            recipient (str): The name of the recipient.
            content (str): The content of the message.

        Raises:
            UserNotFoundException: If the sender or recipient is not found.
        """
        if sender not in self.users:
            raise UserNotFoundException(f"Sender '{sender}' not found.")
        if recipient not in self.users:
            raise UserNotFoundException(f"Recipient '{recipient}' not found.")

        message = {
            "sender": sender,
            "recipient": recipient,
            "content": content,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.messages.append(message)
        print(f"Message sent from '{sender}' to '{recipient}': {content}")

    def get_message_history(self, user: str) -> List[Dict]:
        """
        Get the message history for a specific user.

        Args:
            user (str): The name of the user.

        Raises:
            UserNotFoundException: If the user is not found.

        Returns:
            List[Dict]: A list of messages involving the user.
        """
        if user not in self.users:
            raise UserNotFoundException(f"User '{user}' not found.")

        user_messages = [
            message for message in self.messages
            if message["sender"] == user or message["recipient"] == user
        ]
        return user_messages


# Example usage (should be placed in a separate file or script for production):
if __name__ == "__main__":
    cm = CommunicationManager()

    # Register users
    cm.register_user('teacher', 'Mr. Smith')
    cm.register_user('student', 'John Doe')
    cm.register_user('parent', 'Mrs. Doe')

    # Send messages
    cm.send_message(sender='Mr. Smith', recipient='John Doe', content='Please complete your homework.')
    cm.send_message(sender='Mrs. Doe', recipient='John Doe', content='Have you packed your lunch?')

    # Retrieve message history
    history = cm.get_message_history('John Doe')
    print("Message History for John Doe:")
    for msg in history:
        print(msg)
```

This library adheres to clean code principles, includes error handling, and is production-ready for educational communication management.
