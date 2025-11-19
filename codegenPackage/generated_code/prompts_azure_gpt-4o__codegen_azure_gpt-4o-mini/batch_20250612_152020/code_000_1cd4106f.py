"""
Generated Code Metadata:
========================
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Write Python code to simulate a scheduling system for hourly or live-in elderly care services, incorporating features like caregiver assignment and client preferences as described in Home Care Assistance Barrie's offerings.
Generated: DETERMINISTIC_1cd4106f20863727
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import random

class Caregiver:
    """Represents a caregiver with a name and availability."""
    
    def __init__(self, name: str, available_hours: List[tuple]):
        self.name = name
        self.available_hours = available_hours  # List of tuples (start_time, end_time)

    def is_available(self, start_time: datetime, end_time: datetime) -> bool:
        """Check if the caregiver is available for the given time slot."""
        for available_start, available_end in self.available_hours:
            if available_start <= start_time.time() <= available_end and \
               available_start <= end_time.time() <= available_end:
                return True
        return False


class Client:
    """Represents a client with specific care needs and preferences."""
    
    def __init__(self, name: str, care_type: str, preferred_caregivers: List[str]):
        self.name = name
        self.care_type = care_type  # 'hourly' or 'live-in'
        self.preferred_caregivers = preferred_caregivers


class SchedulingSystem:
    """Manages the scheduling of caregivers to clients."""
    
    def __init__(self):
        self.caregivers: List[Caregiver] = []
        self.clients: List[Client] = []
        self.assignments: Dict[str, List[str]] = {}  # Client name -> List of assigned caregivers

    def add_caregiver(self, caregiver: Caregiver):
        """Add a caregiver to the system."""
        self.caregivers.append(caregiver)

    def add_client(self, client: Client):
        """Add a client to the system."""
        self.clients.append(client)

    def schedule_care(self, client_name: str, start_time: datetime, duration: timedelta) -> Optional[str]:
        """Schedule care for a client based on their preferences and caregiver availability."""
        client = next((c for c in self.clients if c.name == client_name), None)
        if not client:
            raise ValueError(f"Client '{client_name}' not found.")

        end_time = start_time + duration
        assigned_caregivers = []

        # Check preferred caregivers first
        for caregiver_name in client.preferred_caregivers:
            caregiver = next((c for c in self.caregivers if c.name == caregiver_name), None)
            if caregiver and caregiver.is_available(start_time, end_time):
                assigned_caregivers.append(caregiver_name)

        # If no preferred caregivers are available, assign any available caregiver
        if not assigned_caregivers:
            for caregiver in self.caregivers:
                if caregiver.is_available(start_time, end_time):
                    assigned_caregivers.append(caregiver.name)

        if not assigned_caregivers:
            raise RuntimeError(f"No available caregivers for client '{client_name}' during the requested time.")

        # Store the assignment
        self.assignments[client_name] = assigned_caregivers
        return f"Assigned caregivers for {client_name}: {', '.join(assigned_caregivers)}"


# Example usage
if __name__ == "__main__":
    # Create caregivers with their available hours
    caregiver1 = Caregiver("Alice", [(datetime.strptime("08:00", "%H:%M").time(), datetime.strptime("12:00", "%H:%M").time())])
    caregiver2 = Caregiver("Bob", [(datetime.strptime("10:00", "%H:%M").time(), datetime.strptime("14:00", "%H:%M").time())])
    caregiver3 = Caregiver("Charlie", [(datetime.strptime("09:00", "%H:%M").time(), datetime.strptime("17:00", "%H:%M").time())])

    # Initialize scheduling system
    scheduling_system = SchedulingSystem()
    scheduling_system.add_caregiver(caregiver1)
    scheduling_system.add_caregiver(caregiver2)
    scheduling_system.add_caregiver(caregiver3)

    # Create clients with preferences
    client1 = Client("John Doe", "hourly", ["Alice", "Bob"])
    client2 = Client("Jane Smith", "live-in", ["Charlie"])

    scheduling_system.add_client(client1)
    scheduling_system.add_client(client2)

    # Schedule care for clients
    try:
        print(scheduling_system.schedule_care("John Doe", datetime.now().replace(hour=9, minute=0), timedelta(hours=2)))
        print(scheduling_system.schedule_care("Jane Smith", datetime.now().replace(hour=10, minute=0), timedelta(hours=24)))
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
