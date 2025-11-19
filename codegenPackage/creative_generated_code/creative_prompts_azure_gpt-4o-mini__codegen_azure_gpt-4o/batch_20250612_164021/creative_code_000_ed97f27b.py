"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poweredproductions.com.au
Prompt: How can I implement a theatrical firearms safety protocol for a film production in New South Wales that complies with local regulations?
Generated: DETERMINISTIC_ed97f27bce416683
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Theatrical Firearms Safety Protocol Implementation
This script handles firearms safety for film productions in New South Wales (NSW) according to local regulations.
It includes functionality for managing firearms, tracking licenses, and ensuring compliance with NSW safety standards.

Note: This code assumes the NSW regulations may include checking valid licenses, logging firearm usage, and ensuring proper handling.
"""

import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='firearms_safety.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class LicenseValidationError(Exception):
    """Custom exception for invalid license cases."""
    pass

class FirearmSafetyProtocol:
    """
    A class to manage theatrical firearms safety compliance in NSW.
    """

    def __init__(self):
        # Dictionary to store firearm details
        # {'firearm_id': {'name': 'Gun Model', 'licensed_to': 'License Holder'}}
        self.firearms = {}

        # List to store valid licenses
        self.valid_licenses = set()

    def add_license(self, license_number):
        """
        Add a valid license to the list of licenses.
        
        Args:
            license_number (str): The license number to add.
        """
        if not license_number:
            raise ValueError("License number cannot be empty.")

        self.valid_licenses.add(license_number)
        logging.info(f"License {license_number} added to valid licenses.")

    def register_firearm(self, firearm_id, firearm_name, license_number):
        """
        Register a firearm under a specific license.
        
        Args:
            firearm_id (str): Unique identifier for the firearm.
            firearm_name (str): Name of the firearm.
            license_number (str): License number of the handler.

        Raises:
            LicenseValidationError: If the license is not valid.
        """
        if license_number not in self.valid_licenses:
            logging.error(f"Attempt to register firearm {firearm_id} with invalid license {license_number}.")
            raise LicenseValidationError(f"License {license_number} is not valid.")

        self.firearms[firearm_id] = {
            'name': firearm_name,
            'licensed_to': license_number
        }
        logging.info(f"Firearm {firearm_id} ({firearm_name}) registered to license {license_number}.")

    def log_firearm_usage(self, firearm_id, user, action):
        """
        Log the usage of a firearm.
        
        Args:
            firearm_id (str): Unique identifier for the firearm.
            user (str): Name of the person using the firearm.
            action (str): Description of the action (e.g., "fired", "cleaned").

        Raises:
            KeyError: If the firearm is not registered.
        """
        if firearm_id not in self.firearms:
            logging.error(f"Attempt to log usage for unregistered firearm {firearm_id}.")
            raise KeyError(f"Firearm {firearm_id} is not registered in the system.")

        firearm = self.firearms[firearm_id]
        log_entry = f"Firearm '{firearm['name']}' (ID: {firearm_id}) used by {user}: {action}"
        logging.info(log_entry)
        print(log_entry)  # Optional: Print log entry to console

    def validate_protocol(self):
        """
        Validate the protocol to ensure compliance with NSW regulations.
        This is a placeholder function that can include compliance checks.
        """
        # Example compliance check: Ensure all firearms are registered with valid licenses
        for firearm_id, firearm_details in self.firearms.items():
            if firearm_details['licensed_to'] not in self.valid_licenses:
                logging.warning(f"Firearm {firearm_id} is registered with invalid license {firearm_details['licensed_to']}.")
                print(f"Warning: Firearm {firearm_id} has invalid license!")
        logging.info("Compliance validation completed.")

# Example usage of the protocol system
if __name__ == "__main__":
    try:
        protocol = FirearmSafetyProtocol()
        
        # Add valid licenses
        protocol.add_license("NSW12345")
        protocol.add_license("NSW67890")

        # Register firearms
        protocol.register_firearm("F001", "Prop Gun Model A", "NSW12345")
        protocol.register_firearm("F002", "Prop Gun Model B", "NSW67890")

        # Log firearm usage
        protocol.log_firearm_usage("F001", "John Doe", "rehearsal firing")
        protocol.log_firearm_usage("F002", "Jane Smith", "cleaning")

        # Validate protocol compliance
        protocol.validate_protocol()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"Error: {e}")
```
