"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Write a program to monitor and control access to premises using gate automation systems, incorporating features described by Donture Systems Ltd.
Generated: DETERMINISTIC_ee955af266579431
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gate_automation_system.py

"""
Gate Automation System for monitoring and controlling access to premises.

This program simulates a gate automation system with user authentication,
access level management, and gate status monitoring.

Author: [Your Name]
Date: [Today's Date]
"""

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class User:
    """Represents a user with a unique ID and access level."""

    def __init__(self, user_id, access_level):
        """
        Initializes a User object.

        Args:
            user_id (str): Unique user ID.
            access_level (str): Access level (e.g., 'admin', 'employee', 'visitor').
        """
        self.user_id = user_id
        self.access_level = access_level

class Gate:
    """Represents a gate with a unique ID and status."""

    def __init__(self, gate_id):
        """
        Initializes a Gate object.

        Args:
            gate_id (str): Unique gate ID.
        """
        self.gate_id = gate_id
        self.status = 'closed'  # Initial gate status

    def open_gate(self):
        """Opens the gate."""
        self.status = 'open'
        logging.info(f"Gate {self.gate_id} opened.")

    def close_gate(self):
        """Closes the gate."""
        self.status = 'closed'
        logging.info(f"Gate {self.gate_id} closed.")

class AccessControlSystem:
    """Manages user access and gate automation."""

    def __init__(self):
        """Initializes the access control system."""
        self.users = {}  # User database
        self.gates = {}  # Gate database

    def add_user(self, user_id, access_level):
        """
        Adds a user to the system.

        Args:
            user_id (str): Unique user ID.
            access_level (str): Access level.
        """
        self.users[user_id] = User(user_id, access_level)
        logging.info(f"User {user_id} added with access level {access_level}.")

    def add_gate(self, gate_id):
        """
        Adds a gate to the system.

        Args:
            gate_id (str): Unique gate ID.
        """
        self.gates[gate_id] = Gate(gate_id)
        logging.info(f"Gate {gate_id} added.")

    def authenticate_user(self, user_id):
        """
        Authenticates a user.

        Args:
            user_id (str): Unique user ID.

        Returns:
            bool: True if the user exists, False otherwise.
        """
        return user_id in self.users

    def grant_access(self, user_id, gate_id):
        """
        Grants access to a gate for a user.

        Args:
            user_id (str): Unique user ID.
            gate_id (str): Unique gate ID.

        Returns:
            bool: True if access is granted, False otherwise.
        """
        if self.authenticate_user(user_id) and gate_id in self.gates:
            user = self.users[user_id]
            gate = self.gates[gate_id]
            if user.access_level == 'admin' or user.access_level == 'employee':
                gate.open_gate()
                return True
        logging.warning(f"Access denied for user {user_id} to gate {gate_id}.")
        return False

    def revoke_access(self, gate_id):
        """
        Revokes access to a gate.

        Args:
            gate_id (str): Unique gate ID.
        """
        if gate_id in self.gates:
            gate = self.gates[gate_id]
            gate.close_gate()

def main():
    # Create an access control system
    acs = AccessControlSystem()

    # Add users
    acs.add_user('admin123', 'admin')
    acs.add_user('emp456', 'employee')
    acs.add_user('vis789', 'visitor')

    # Add gates
    acs.add_gate('gate1')
    acs.add_gate('gate2')

    # Grant access
    acs.grant_access('admin123', 'gate1')
    acs.grant_access('emp456', 'gate1')
    acs.grant_access('vis789', 'gate1')  # Should be denied

    # Revoke access
    acs.revoke_access('gate1')

if __name__ == '__main__':
    main()
```
