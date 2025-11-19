"""
Generated Code Metadata:
========================
Original URL: https://alphamor.com
Prompt: Design a system for automating the maintenance and servicing of home security and alarm systems in a property management company.
Generated: DETERMINISTIC_1f8db90d35c744de
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging
from typing import List, Dict, Optional

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AlarmSystem:
    """Class representing an alarm system in a property."""
    
    def __init__(self, system_id: str, location: str):
        self.system_id = system_id
        self.location = location
        self.last_serviced: Optional[datetime.date] = None
        self.service_interval_days = 180  # Default service interval

    def schedule_service(self):
        """Schedule the next service date based on the last serviced date."""
        if self.last_serviced:
            next_service_date = self.last_serviced + datetime.timedelta(days=self.service_interval_days)
            logging.info(f"Next service for system {self.system_id} at {self.location} is scheduled for {next_service_date}.")
            return next_service_date
        else:
            logging.warning(f"Service date not set for system {self.system_id}.")
            return None

    def record_service(self):
        """Record the service date for the alarm system."""
        self.last_serviced = datetime.date.today()
        logging.info(f"Service recorded for system {self.system_id} at {self.location} on {self.last_serviced}.")

class PropertyManager:
    """Class to manage multiple alarm systems in a property management company."""
    
    def __init__(self):
        self.alarm_systems: List[AlarmSystem] = []

    def add_alarm_system(self, system_id: str, location: str):
        """Add a new alarm system to the management system."""
        new_system = AlarmSystem(system_id, location)
        self.alarm_systems.append(new_system)
        logging.info(f"Added alarm system {system_id} at {location}.")

    def service_all_systems(self):
        """Service all alarm systems and schedule the next service."""
        for system in self.alarm_systems:
            system.record_service()
            system.schedule_service()

    def get_due_services(self) -> List[Dict[str, str]]:
        """Get a list of alarm systems that are due for service."""
        due_services = []
        for system in self.alarm_systems:
            next_service_date = system.schedule_service()
            if next_service_date and next_service_date <= datetime.date.today():
                due_services.append({
                    'system_id': system.system_id,
                    'location': system.location,
                    'next_service_date': next_service_date
                })
        return due_services

def main():
    """Main function to run the property management system."""
    try:
        manager = PropertyManager()
        
        # Adding alarm systems
        manager.add_alarm_system("AS001", "Building A, Apartment 101")
        manager.add_alarm_system("AS002", "Building B, Apartment 202")
        
        # Service all systems
        manager.service_all_systems()
        
        # Check for due services
        due_services = manager.get_due_services()
        if due_services:
            logging.info("The following systems are due for service:")
            for service in due_services:
                logging.info(f"System ID: {service['system_id']}, Location: {service['location']}, Next Service Date: {service['next_service_date']}")
        else:
            logging.info("No systems are due for service.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
