"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invictacobrancas.com.br
Prompt: Describe how to set up a discadora eletrônica system to optimize call handling for debt recovery operations.
Generated: DETERMINISTIC_f637ef6004b661ea
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import logging
from typing import List, Dict, Any

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DialerSystem:
    def __init__(self, contacts: List[Dict[str, Any]]):
        """
        Initializes the DialerSystem with a list of contacts.

        :param contacts: A list of dictionaries containing contact information.
        """
        self.contacts = contacts
        self.calls_in_progress = []
    
    def dial_contact(self, contact: Dict[str, Any]) -> None:
        """
        Simulates dialing a single contact.

        :param contact: A dictionary containing contact information.
        """
        try:
            logging.info(f"Dialing {contact['name']} at {contact['phone_number']}...")
            # Simulate call duration
            call_duration = random.randint(1, 5)  # Random call duration between 1 to 5 seconds
            time.sleep(call_duration)
            logging.info(f"Call with {contact['name']} completed.")
            self.calls_in_progress.remove(contact)
        except Exception as e:
            logging.error(f"Error while dialing {contact['name']}: {e}")

    def optimize_call_handling(self) -> None:
        """
        Optimizes the call handling process by managing multiple calls.
        """
        try:
            for contact in self.contacts:
                # Start call if less than 3 calls are in progress
                if len(self.calls_in_progress) < 3:
                    self.calls_in_progress.append(contact)
                    self.dial_contact(contact)
                else:
                    logging.info("Maximum calls in progress. Waiting...")
                    time.sleep(2)  # Wait before checking again
        except Exception as e:
            logging.error(f"Error in call handling: {e}")

# Example usage
if __name__ == '__main__':
    # Sample contacts for testing
    contacts_list = [
        {"name": "Alice", "phone_number": "123-456-7890"},
        {"name": "Bob", "phone_number": "234-567-8901"},
        {"name": "Charlie", "phone_number": "345-678-9012"},
        {"name": "Diana", "phone_number": "456-789-0123"},
        {"name": "Evan", "phone_number": "567-890-1234"}
    ]

    # Create and run the dialer system
    dialer = DialerSystem(contacts=contacts_list)
    dialer.optimize_call_handling()
```
