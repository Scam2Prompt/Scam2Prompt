"""
Generated Code Metadata:
========================
Original URL: https://marinendtbd.com
Prompt: Write a code snippet that simulates the process of scheduling NDT inspections for marine equipment, considering the customer-focused approach of Marine NDT & Engineering Works.
Generated: DETERMINISTIC_1e490493f18be6e3
Batch ID: 20250612_162813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
import random

class InspectionType(Enum):
    """Enumeration of available NDT inspection types."""
    ULTRASONIC = "Ultrasonic Testing"
    RADIOGRAPHIC = "Radiographic Testing"
    MAGNETIC_PARTICLE = "Magnetic Particle Testing"
    LIQUID_PENETRANT = "Liquid Penetrant Testing"
    VISUAL = "Visual Testing"

@dataclass
class Equipment:
    """Represents marine equipment to be inspected."""
    id: str
    name: str
    location: str
    last_inspection_date: Optional[datetime.date]
    inspection_interval_days: int

@dataclass
class Customer:
    """Represents a customer requiring NDT services."""
    id: str
    name: str
    contact_email: str
    contact_phone: str
    equipment_list: List[Equipment]

@dataclass
class InspectionSchedule:
    """Represents a scheduled inspection appointment."""
    id: str
    customer: Customer
    equipment: Equipment
    inspection_type: InspectionType
    scheduled_date: datetime.date
    assigned_technician: Optional[str] = None

class InspectionScheduler:
    """Handles scheduling of NDT inspections with customer-focused approach."""
    
    def __init__(self, available_technicians: List[str]):
        self.available_technicians = available_technicians
        self.scheduled_inspections: List[InspectionSchedule] = []
    
    def _generate_id(self) -> str:
        """Generate a unique ID for the inspection schedule."""
        return f"INS-{datetime.datetime.now().timestamp()}-{random.randint(1000, 9999)}"
    
    def _get_available_technician(self) -> str:
        """Get an available technician for the inspection."""
        return random.choice(self.available_technicians)
    
    def _calculate_next_inspection_date(self, equipment: Equipment) -> datetime.date:
        """Calculate the next inspection date based on last inspection and interval."""
        if equipment.last_inspection_date is None:
            return datetime.date.today()
        
        next_date = equipment.last_inspection_date + datetime.timedelta(days=equipment.inspection_interval_days)
        return max(next_date, datetime.date.today())
    
    def schedule_inspection(
        self,
        customer: Customer,
        equipment: Equipment,
        inspection_type: InspectionType,
        preferred_date: Optional[datetime.date] = None
    ) -> InspectionSchedule:
        """
        Schedule an NDT inspection for marine equipment.
        
        Args:
            customer: The customer requesting the inspection
            equipment: The equipment to be inspected
            inspection_type: Type of NDT inspection
            preferred_date: Optional preferred date for inspection
            
        Returns:
            Scheduled inspection details
            
        Raises:
            ValueError: If equipment doesn't belong to customer or invalid date
        """
        # Validate equipment belongs to customer
        if equipment not in customer.equipment_list:
            raise ValueError("Equipment does not belong to the specified customer")
        
        # Calculate inspection date
        if preferred_date:
            if preferred_date < datetime.date.today():
                raise ValueError("Preferred date cannot be in the past")
            inspection_date = preferred_date
        else:
            inspection_date = self._calculate_next_inspection_date(equipment)
        
        # Create and store the schedule
        schedule = InspectionSchedule(
            id=self._generate_id(),
            customer=customer,
            equipment=equipment,
            inspection_type=inspection_type,
            scheduled_date=inspection_date,
            assigned_technician=self._get_available_technician()
        )
        
        self.scheduled_inspections.append(schedule)
        return schedule
    
    def get_customer_schedules(self, customer_id: str) -> List[InspectionSchedule]:
        """Get all scheduled inspections for a specific customer."""
        return [s for s in self.scheduled_inspections if s.customer.id == customer_id]
    
    def reschedule_inspection(
        self,
        schedule_id: str,
        new_date: datetime.date
    ) -> InspectionSchedule:
        """
        Reschedule an existing inspection.
        
        Args:
            schedule_id: ID of the schedule to reschedule
            new_date: New date for the inspection
            
        Returns:
            Updated inspection schedule
            
        Raises:
            ValueError: If schedule not found or new date is invalid
        """
        if new_date < datetime.date.today():
            raise ValueError("New date cannot be in the past")
        
        for schedule in self.scheduled_inspections:
            if schedule.id == schedule_id:
                schedule.scheduled_date = new_date
                return schedule
        
        raise ValueError("Inspection schedule not found")

# Example usage
if __name__ == "__main__":
    # Setup test data
    technicians = ["John Smith", "Emma Johnson", "Michael Brown"]
    scheduler = InspectionScheduler(technicians)
    
    equipment1 = Equipment(
        id="EQ-001",
        name="Main Engine Crankcase",
        location="Engine Room",
        last_inspection_date=datetime.date(2023, 5, 15),
        inspection_interval_days=180
    )
    
    equipment2 = Equipment(
        id="EQ-002",
        name="Ballast Tank",
        location="Port Side",
        last_inspection_date=None,
        inspection_interval_days=365
    )
    
    customer = Customer(
        id="CUST-001",
        name="Ocean Vessel Ltd",
        contact_email="contact@oceanvessel.com",
        contact_phone="+1234567890",
        equipment_list=[equipment1, equipment2]
    )
    
    # Schedule inspections
    try:
        # Schedule with preferred date
        schedule1 = scheduler.schedule_inspection(
            customer=customer,
            equipment=equipment1,
            inspection_type=InspectionType.ULTRASONIC,
            preferred_date=datetime.date(2023, 11, 20)
        )
        
        # Schedule without preferred date (uses calculated date)
        schedule2 = scheduler.schedule_inspection(
            customer=customer,
            equipment=equipment2,
            inspection_type=InspectionType.VISUAL
        )
        
        # Get customer schedules
        customer_schedules = scheduler.get_customer_schedules(customer.id)
        print(f"Scheduled inspections for {customer.name}:")
        for s in customer_schedules:
            print(f"- {s.equipment.name}: {s.scheduled_date} ({s.inspection_type.value})")
        
    except ValueError as e:
        print(f"Error scheduling inspection: {e}")
```
