"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-events.com
Prompt: Write code to simulate staffing and manpower services for events, ensuring cost-effective production and execution, as described by Phantom Events and Solutions.
Generated: DETERMINISTIC_f95bc8ff3fa6a2e8
Batch ID: 20250612_154436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Tuple

class StaffMember:
    """Class representing a staff member with specific roles and rates."""
    
    def __init__(self, name: str, role: str, hourly_rate: float):
        self.name = name
        self.role = role
        self.hourly_rate = hourly_rate

    def __repr__(self):
        return f"{self.name} ({self.role}) - ${self.hourly_rate}/hr"


class Event:
    """Class representing an event requiring staffing."""
    
    def __init__(self, event_name: str, duration_hours: int, required_roles: Dict[str, int]):
        self.event_name = event_name
        self.duration_hours = duration_hours
        self.required_roles = required_roles  # {role: number_of_staff_needed}
        self.staff_allocated = []

    def allocate_staff(self, staff: List[StaffMember]) -> None:
        """Allocate staff members based on required roles."""
        for role, count in self.required_roles.items():
            available_staff = [s for s in staff if s.role == role]
            selected_staff = random.sample(available_staff, min(count, len(available_staff)))
            self.staff_allocated.extend(selected_staff)

    def calculate_cost(self) -> float:
        """Calculate the total cost for staffing the event."""
        total_cost = sum(member.hourly_rate * self.duration_hours for member in self.staff_allocated)
        return total_cost

    def summary(self) -> Dict:
        """Provide a summary of the event staffing and costs."""
        return {
            "event_name": self.event_name,
            "duration_hours": self.duration_hours,
            "staff_allocated": self.staff_allocated,
            "total_cost": self.calculate_cost()
        }


class StaffingService:
    """Class to manage staffing services for events."""
    
    def __init__(self):
        self.staff: List[StaffMember] = []

    def add_staff_member(self, name: str, role: str, hourly_rate: float) -> None:
        """Add a staff member to the staffing pool."""
        self.staff.append(StaffMember(name, role, hourly_rate))

    def create_event(self, event_name: str, duration_hours: int, required_roles: Dict[str, int]) -> Event:
        """Create an event and allocate necessary staff."""
        event = Event(event_name, duration_hours, required_roles)
        event.allocate_staff(self.staff)
        return event


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize staffing service
        staffing_service = StaffingService()
        
        # Add staff members to the pool
        staffing_service.add_staff_member("Alice", "Catering", 25)
        staffing_service.add_staff_member("Bob", "Security", 30)
        staffing_service.add_staff_member("Charlie", "Logistics", 20)
        staffing_service.add_staff_member("Diana", "Catering", 25)
        
        # Define required roles for an event
        required_roles = {
            "Catering": 2,
            "Security": 1,
            "Logistics": 1
        }
        
        # Create an event with staffing requirements
        event = staffing_service.create_event("Corporate Gala", duration_hours=5, required_roles=required_roles)

        # Print event summary
        event_summary = event.summary()
        print(event_summary)

    except Exception as e:
        print(f"An error occurred: {e}")
```
