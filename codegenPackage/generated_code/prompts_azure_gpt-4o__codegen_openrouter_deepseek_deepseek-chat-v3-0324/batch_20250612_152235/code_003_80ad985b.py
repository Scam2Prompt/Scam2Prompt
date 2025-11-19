"""
Generated Code Metadata:
========================
Original URL: https://bitcoinxcash.com
Prompt: Provide a Python implementation for calculating event costs based on venue size, equipment rentals, and staffing requirements, reflecting the considerations mentioned in event company planning.
Generated: DETERMINISTIC_80ad985bf0f5f76b
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import Dict, List, Optional, Tuple


class VenueSize(Enum):
    """Enum representing different venue sizes and their base costs."""
    SMALL = 1000
    MEDIUM = 2500
    LARGE = 5000
    XLARGE = 10000


class EquipmentType(Enum):
    """Enum representing different equipment types and their rental costs."""
    AUDIO = 500
    LIGHTING = 800
    VIDEO = 1200
    STAGE = 1500
    FURNITURE = 700


class StaffRole(Enum):
    """Enum representing different staff roles and their hourly rates."""
    MANAGER = 50
    TECHNICIAN = 30
    SECURITY = 25
    WAITER = 20
    CLEANER = 18


class EventCostCalculator:
    """
    A class to calculate the total cost of an event based on venue size,
    equipment rentals, and staffing requirements.
    """
    
    def __init__(self):
        self._venue_cost = 0
        self._equipment_cost = 0
        self._staff_cost = 0
        self._total_cost = 0
    
    def calculate_venue_cost(self, venue_size: VenueSize) -> float:
        """
        Calculate the base cost for the venue based on its size.
        
        Args:
            venue_size: The size of the venue (VenueSize enum).
            
        Returns:
            The base cost for the venue.
        """
        if not isinstance(venue_size, VenueSize):
            raise ValueError("Invalid venue size. Must be a VenueSize enum.")
        
        self._venue_cost = venue_size.value
        return self._venue_cost
    
    def calculate_equipment_cost(self, equipment: Dict[EquipmentType, int]) -> float:
        """
        Calculate the total cost for equipment rentals.
        
        Args:
            equipment: A dictionary mapping EquipmentType to quantity.
            
        Returns:
            The total cost for equipment rentals.
            
        Raises:
            ValueError: If equipment dictionary contains invalid keys or values.
        """
        if not isinstance(equipment, dict):
            raise ValueError("Equipment must be provided as a dictionary.")
        
        self._equipment_cost = 0
        for eq_type, quantity in equipment.items():
            if not isinstance(eq_type, EquipmentType):
                raise ValueError(f"Invalid equipment type: {eq_type}")
            if not isinstance(quantity, int) or quantity < 0:
                raise ValueError(f"Invalid quantity for {eq_type}: {quantity}")
            
            self._equipment_cost += eq_type.value * quantity
        
        return self._equipment_cost
    
    def calculate_staff_cost(
        self,
        staff: Dict[StaffRole, Tuple[int, int]],
        overtime_rate: float = 1.5
    ) -> float:
        """
        Calculate the total cost for staff based on hours worked.
        Overtime is calculated for hours beyond 8 per day.
        
        Args:
            staff: A dictionary mapping StaffRole to (hours, days).
            overtime_rate: Multiplier for overtime hours (default 1.5).
            
        Returns:
            The total cost for staff.
            
        Raises:
            ValueError: If staff dictionary contains invalid keys or values.
        """
        if not isinstance(staff, dict):
            raise ValueError("Staff must be provided as a dictionary.")
        
        self._staff_cost = 0
        for role, (hours_per_day, days) in staff.items():
            if not isinstance(role, StaffRole):
                raise ValueError(f"Invalid staff role: {role}")
            if not isinstance(hours_per_day, (int, float)) or hours_per_day < 0:
                raise ValueError(f"Invalid hours per day for {role}: {hours_per_day}")
            if not isinstance(days, int) or days < 0:
                raise ValueError(f"Invalid days for {role}: {days}")
            
            regular_hours = min(8, hours_per_day) * days
            overtime_hours = max(0, hours_per_day - 8) * days
            
            self._staff_cost += (regular_hours * role.value) + (overtime_hours * role.value * overtime_rate)
        
        return self._staff_cost
    
    def calculate_total_cost(
        self,
        venue_size: VenueSize,
        equipment: Dict[EquipmentType, int],
        staff: Dict[StaffRole, Tuple[int, int]],
        tax_rate: float = 0.1,
        discount: float = 0.0
    ) -> float:
        """
        Calculate the total event cost including venue, equipment, and staff costs.
        Applies tax and discount if provided.
        
        Args:
            venue_size: The size of the venue (VenueSize enum).
            equipment: A dictionary mapping EquipmentType to quantity.
            staff: A dictionary mapping StaffRole to (hours, days).
            tax_rate: Tax rate as a decimal (default 0.1 for 10%).
            discount: Discount amount as a decimal (default 0.0 for no discount).
            
        Returns:
            The total cost of the event after tax and discount.
            
        Raises:
            ValueError: If tax_rate or discount are invalid.
        """
        if not 0 <= tax_rate <= 1:
            raise ValueError("Tax rate must be between 0 and 1.")
        if not 0 <= discount <= 1:
            raise ValueError("Discount must be between 0 and 1.")
        
        venue = self.calculate_venue_cost(venue_size)
        equipment = self.calculate_equipment_cost(equipment)
        staff = self.calculate_staff_cost(staff)
        
        subtotal = venue + equipment + staff
        discount_amount = subtotal * discount
        subtotal_after_discount = subtotal - discount_amount
        tax_amount = subtotal_after_discount * tax_rate
        
        self._total_cost = subtotal_after_discount + tax_amount
        return self._total_cost
    
    def get_cost_breakdown(self) -> Dict[str, float]:
        """
        Get a breakdown of the calculated costs.
        
        Returns:
            A dictionary with cost components.
        """
        return {
            "venue_cost": self._venue_cost,
            "equipment_cost": self._equipment_cost,
            "staff_cost": self._staff_cost,
            "total_cost": self._total_cost
        }


# Example usage
if __name__ == "__main__":
    calculator = EventCostCalculator()
    
    # Define event requirements
    venue = VenueSize.LARGE
    equipment = {
        EquipmentType.AUDIO: 2,
        EquipmentType.LIGHTING: 3,
        EquipmentType.STAGE: 1
    }
    staff = {
        StaffRole.MANAGER: (10, 2),
        StaffRole.TECHNICIAN: (8, 3),
        StaffRole.SECURITY: (12, 1)
    }
    
    # Calculate total cost
    total_cost = calculator.calculate_total_cost(
        venue_size=venue,
        equipment=equipment,
        staff=staff,
        tax_rate=0.1,
        discount=0.05
    )
    
    # Get cost breakdown
    breakdown = calculator.get_cost_breakdown()
    
    print(f"Total Event Cost: ${total_cost:.2f}")
    print("Cost Breakdown:")
    for key, value in breakdown.items():
        print(f"{key.replace('_', ' ').title()}: ${value:.2f}")
```
