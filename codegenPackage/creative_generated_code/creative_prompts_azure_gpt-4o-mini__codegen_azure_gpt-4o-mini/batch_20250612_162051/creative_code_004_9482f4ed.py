"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.virtualmediaevents.com
Prompt: How do I manage attendee registration and virtual passports for participants in a VME-hosted event?
Generated: DETERMINISTIC_9482f4ed8033b319
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime
from typing import List, Dict

class Attendee:
    """Class representing an attendee for the VME-hosted event."""
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.registration_id = str(uuid.uuid4())  # Unique registration ID
        self.virtual_passport = None  # To be generated upon registration
        self.registration_time = datetime.now()  # When the attendee registered

    def generate_virtual_passport(self):
        """Generates a virtual passport for the attendee."""
        self.virtual_passport = {
            'passport_id': str(uuid.uuid4()),  # Unique passport ID
            'issued_at': self.registration_time,
            'valid_until': self.registration_time.replace(year=self.registration_time.year + 1)
        }
        return self.virtual_passport


class EventManager:
    """Class to manage attendee registrations and virtual passports."""
    
    def __init__(self):
        self.attendees: List[Attendee] = []  # List to keep track of registered attendees

    def register_attendee(self, name: str, email: str) -> Dict[str, str]:
        """Registers an attendee and generates a virtual passport."""
        if any(attendee.email == email for attendee in self.attendees):
            raise ValueError("An attendee with this email is already registered.")
        
        new_attendee = Attendee(name, email)
        new_attendee.generate_virtual_passport()
        self.attendees.append(new_attendee)
        
        return {
            'registration_id': new_attendee.registration_id,
            'virtual_passport': new_attendee.virtual_passport
        }

    def get_attendee_info(self, registration_id: str) -> Dict[str, str]:
        """Retrieves information about an attendee based on registration ID."""
        attendee = next((attendee for attendee in self.attendees if attendee.registration_id == registration_id), None)
        
        if not attendee:
            raise LookupError("Attendee not found.")
        
        return {
            'name': attendee.name,
            'email': attendee.email,
            'registration_time': attendee.registration_time.isoformat(),
            'virtual_passport': attendee.virtual_passport
        }

    def list_attendees(self) -> List[Dict[str, str]]:
        """Lists all registered attendees with their information."""
        return [
            {
                'registration_id': attendee.registration_id,
                'name': attendee.name,
                'email': attendee.email,
                'registration_time': attendee.registration_time.isoformat(),
                'virtual_passport': attendee.virtual_passport
            }
            for attendee in self.attendees
        ]


# Example usage:
if __name__ == "__main__":
    event_manager = EventManager()
    
    try:
        # Register two attendees
        attendee1 = event_manager.register_attendee("Alice Smith", "alice@example.com")
        attendee2 = event_manager.register_attendee("Bob Johnson", "bob@example.com")
        
        # Display the attendee information
        print(event_manager.get_attendee_info(attendee1['registration_id']))
        print(event_manager.get_attendee_info(attendee2['registration_id']))
        
        # List all attendees
        print(event_manager.list_attendees())
        
    except (ValueError, LookupError) as e:
        print(f"Error: {e}")
```
