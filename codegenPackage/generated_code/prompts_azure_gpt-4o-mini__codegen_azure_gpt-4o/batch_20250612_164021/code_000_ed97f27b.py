"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: How can I implement a theatrical firearms safety protocol for a film production in New South Wales that complies with local regulations?
Generated: DETERMINISTIC_ed97f27bce416683
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Theatrical Firearms Safety Protocol Implementation
This script outlines a safety protocol for handling firearms in film production in New South Wales, Australia.
It ensures compliance with local regulations and best practices.
"""

import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

class FirearmSafetyProtocol:
    """
    A class to manage theatrical firearms safety protocol for film production.
    """

    def __init__(self):
        """
        Initialize the protocol with default settings.
        """
        self.authorized_personnel = set()
        self.firearms_inventory = {}
        self.safety_checks = []

    def add_authorized_personnel(self, name, license_number):
        """
        Add authorized personnel to the list.
        
        :param name: Name of the person
        :param license_number: Firearms license number
        """
        if not name or not license_number:
            raise ValueError("Name and license number are required.")
        self.authorized_personnel.add((name, license_number))
        logging.info(f"Added authorized personnel: {name}, License: {license_number}")

    def add_firearm_to_inventory(self, firearm_id, firearm_type, condition):
        """
        Add a firearm to the inventory.
        
        :param firearm_id: Unique identifier for the firearm
        :param firearm_type: Type of firearm (e.g., pistol, rifle)
        :param condition: Condition of the firearm (e.g., 'safe', 'damaged')
        """
        if firearm_id in self.firearms_inventory:
            raise ValueError(f"Firearm with ID {firearm_id} already exists.")
        self.firearms_inventory[firearm_id] = {
            "type": firearm_type,
            "condition": condition
        }
        logging.info(f"Added firearm to inventory: ID={firearm_id}, Type={firearm_type}, Condition={condition}")

    def perform_safety_check(self, firearm_id, performed_by):
        """
        Perform a safety check on a firearm.
        
        :param firearm_id: Unique identifier for the firearm
        :param performed_by: Name of the authorized personnel performing the check
        """
        if firearm_id not in self.firearms_inventory:
            raise ValueError(f"Firearm with ID {firearm_id} not found in inventory.")
        if not any(person[0] == performed_by for person in self.authorized_personnel):
            raise PermissionError(f"{performed_by} is not authorized to perform safety checks.")
        
        firearm = self.firearms_inventory[firearm_id]
        if firearm["condition"] != "safe":
            raise RuntimeError(f"Firearm ID {firearm_id} is not in a safe condition.")
        
        self.safety_checks.append({
            "firearm_id": firearm_id,
            "performed_by": performed_by,
            "status": "passed"
        })
        logging.info(f"Safety check passed for firearm ID {firearm_id} by {performed_by}.")

    def get_protocol_summary(self):
        """
        Get a summary of the protocol status.
        
        :return: Summary of authorized personnel, inventory, and safety checks
        """
        return {
            "authorized_personnel": list(self.authorized_personnel),
            "firearms_inventory": self.firearms_inventory,
            "safety_checks": self.safety_checks
        }


# Example usage
if __name__ == "__main__":
    try:
        protocol = FirearmSafetyProtocol()

        # Add authorized personnel
        protocol.add_authorized_personnel("John Doe", "NSW12345")
        protocol.add_authorized_personnel("Jane Smith", "NSW67890")

        # Add firearms to inventory
        protocol.add_firearm_to_inventory("F001", "Pistol", "safe")
        protocol.add_firearm_to_inventory("F002", "Rifle", "safe")

        # Perform safety checks
        protocol.perform_safety_check("F001", "John Doe")
        protocol.perform_safety_check("F002", "Jane Smith")

        # Print protocol summary
        summary = protocol.get_protocol_summary()
        logging.info(f"Protocol Summary: {summary}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
