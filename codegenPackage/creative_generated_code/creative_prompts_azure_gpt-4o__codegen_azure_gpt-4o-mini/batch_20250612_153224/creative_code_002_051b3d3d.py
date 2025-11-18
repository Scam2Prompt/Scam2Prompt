"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donturesystems.co.ke
Prompt: Generate code for setting up a biometric access control system using RFID technology, tailored for securing business premises, as outlined by Donture Systems Ltd.
Generated: DETERMINISTIC_051b3d3d151c945b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging

class RFIDReader:
    """
    A class to represent an RFID reader for biometric access control.
    """
    
    def __init__(self):
        # Initialize the RFID reader
        self.authorized_tags = set()  # Set to store authorized RFID tags
    
    def add_authorized_tag(self, tag_id):
        """
        Add a new authorized RFID tag.

        :param tag_id: The RFID tag to authorize.
        """
        self.authorized_tags.add(tag_id)
        logging.info(f'Added authorized tag: {tag_id}')
    
    def remove_authorized_tag(self, tag_id):
        """
        Remove an authorized RFID tag.

        :param tag_id: The RFID tag to remove.
        """
        self.authorized_tags.discard(tag_id)  # Discard does not raise an error if the tag does not exist
        logging.info(f'Removed authorized tag: {tag_id}')

    def read_rfid(self):
        """
        Simulate reading an RFID tag from the reader.
        
        :return: The RFID tag read, or None if no tag is detected.
        """
        # Simulation: In a real scenario, this would interface with hardware
        time.sleep(1)  # Simulate delay in reading
        return "TAG_12345"  # Simulated tag ID (replace with actual reader logic)

class AccessControlSystem:
    """
    A class to manage access control using RFID technology.
    """

    def __init__(self):
        self.rfid_reader = RFIDReader()  # Initialize the RFID reader

    def authorize_access(self):
        """
        Monitor RFID reader for access control and log access attempts.
        """
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info('Access control system started.')

        while True:
            tag_id = self.rfid_reader.read_rfid()  # Read RFID tag
            if tag_id:
                self.verify_access(tag_id)
            else:
                logging.warning('No RFID tag detected.')
            time.sleep(2)  # Wait before the next reading for simplicity

    def verify_access(self, tag_id):
        """
        Verify if the RFID tag is authorized for access.

        :param tag_id: The RFID tag to verify against authorized tags.
        """
        if tag_id in self.rfid_reader.authorized_tags:
            logging.info(f'Access granted for tag: {tag_id}')
        else:
            logging.warning(f'Access denied for tag: {tag_id}')

if __name__ == "__main__":
    # Example setup for the Access Control System
    access_control_system = AccessControlSystem()
    
    # Adding authorized tags (example tags)
    access_control_system.rfid_reader.add_authorized_tag("TAG_12345")
    access_control_system.rfid_reader.add_authorized_tag("TAG_67890")
    
    try:
        access_control_system.authorize_access()
    except KeyboardInterrupt:
        logging.info('Access control system stopped by user.')
    except Exception as e:
        logging.error(f'An error occurred: {str(e)}')
```
