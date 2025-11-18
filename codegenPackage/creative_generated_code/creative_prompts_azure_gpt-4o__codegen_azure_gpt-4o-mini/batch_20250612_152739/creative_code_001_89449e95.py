"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gradkosarke.org
Prompt: Recommend a library for managing memberships and event registrations for a sports organization like "Grad košarke."
Generated: DETERMINISTIC_89449e95d161881b
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Membership and Event Registration Management for a Sports Organization
"""

# Import necessary libraries
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SportsOrganization:
    """Class to manage memberships and event registrations for a sports organization."""
    
    def __init__(self):
        """Initialize the organization with empty lists for members and events."""
        self.members = []
        self.events = []

    def add_member(self, member_name):
        """Add a new member to the organization.
        
        Args:
            member_name (str): The name of the member to add.
        """
        if not member_name:
            logging.error("Member name cannot be empty.")
            return
        
        self.members.append({
            'name': member_name,
            'joined_date': datetime.now().isoformat()
        })
        logging.info(f"Added member: {member_name}")

    def remove_member(self, member_name):
        """Remove a member from the organization by name.
        
        Args:
            member_name (str): The name of the member to remove.
        """
        member_found = next((member for member in self.members if member['name'] == member_name), None)
        if member_found:
            self.members.remove(member_found)
            logging.info(f"Removed member: {member_name}")
        else:
            logging.warning(f"Member '{member_name}' not found.")

    def create_event(self, event_name, event_date):
        """Create a new event for the organization.
        
        Args:
            event_name (str): The name of the event.
            event_date (str): The date of the event in YYYY-MM-DD format.
        """
        try:
            event_date = datetime.strptime(event_date, '%Y-%m-%d')
            self.events.append({
                'name': event_name,
                'event_date': event_date.isoformat(),
                'registrations': []
            })
            logging.info(f"Created event: {event_name} on {event_date.date()}")
        except ValueError as e:
            logging.error(f"Invalid date format for event '{event_name}': {e}")

    def register_member_for_event(self, member_name, event_name):
        """Register a member for a specific event.
        
        Args:
            member_name (str): The name of the member to register.
            event_name (str): The name of the event for registration.
        """
        event_found = next((event for event in self.events if event['name'] == event_name), None)
        member_found = next((member for member in self.members if member['name'] == member_name), None)
        
        if not event_found:
            logging.warning(f"Event '{event_name}' not found.")
            return
        if not member_found:
            logging.warning(f"Member '{member_name}' not found.")
            return
        
        if member_name not in event_found['registrations']:
            event_found['registrations'].append(member_name)
            logging.info(f"{member_name} registered for event: {event_name}")
        else:
            logging.warning(f"{member_name} is already registered for event: {event_name}")

    def get_members(self):
        """Return a list of all members."""
        return self.members

    def get_events(self):
        """Return a list of all events."""
        return self.events
    
    def save_to_file(self, file_name):
        """Save members and events to a JSON file.
        
        Args:
            file_name (str): The name of the file to save data.
        """
        try:
            with open(file_name, 'w') as file:
                json.dump({'members': self.members, 'events': self.events}, file, indent=4)
            logging.info(f"Data saved to {file_name}")
        except IOError as e:
            logging.error(f"Error saving to file {file_name}: {e}")

# Example usage
if __name__ == "__main__":
    org = SportsOrganization()
    org.add_member("John Doe")
    org.create_event("Summer Basketball Tournament", "2023-08-15")
    org.register_member_for_event("John Doe", "Summer Basketball Tournament")
    org.save_to_file("sports_organization_data.json")
```
