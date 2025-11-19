"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Create Python code to simulate the stacking mechanism of a parking lift system, optimizing for space efficiency as discussed on OHC Lift's website.
Generated: DETERMINISTIC_952dbf2a5966b117
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from typing import List, Optional, Tuple

class ParkingLiftSystem:
    """
    A class to simulate the stacking mechanism of a parking lift system.
    Optimizes for space efficiency by using a priority queue to manage parking slots.
    """
    
    def __init__(self, num_levels: int, slots_per_level: int):
        """
        Initialize the parking lift system with given levels and slots per level.
        
        Args:
            num_levels: Number of levels in the parking lift.
            slots_per_level: Number of parking slots per level.
        """
        if num_levels <= 0 or slots_per_level <= 0:
            raise ValueError("Number of levels and slots per level must be positive integers.")
        
        self.num_levels = num_levels
        self.slots_per_level = slots_per_level
        self.available_slots = []  # Min-heap to track available slots (level, slot)
        self.occupied_slots = {}   # Dict to track occupied slots {vehicle_id: (level, slot)}
        
        # Initialize all slots as available
        for level in range(1, num_levels + 1):
            for slot in range(1, slots_per_level + 1):
                heapq.heappush(self.available_slots, (level, slot))
    
    def park_vehicle(self, vehicle_id: str) -> Optional[Tuple[int, int]]:
        """
        Parks a vehicle in the most space-efficient available slot.
        
        Args:
            vehicle_id: Unique identifier for the vehicle.
            
        Returns:
            Tuple of (level, slot) where the vehicle is parked, or None if no slots available.
        """
        if not vehicle_id:
            raise ValueError("Vehicle ID cannot be empty.")
        
        if vehicle_id in self.occupied_slots:
            raise ValueError(f"Vehicle {vehicle_id} is already parked.")
        
        if not self.available_slots:
            return None
        
        level, slot = heapq.heappop(self.available_slots)
        self.occupied_slots[vehicle_id] = (level, slot)
        return (level, slot)
    
    def retrieve_vehicle(self, vehicle_id: str) -> Optional[Tuple[int, int]]:
        """
        Retrieves a vehicle from the parking lift system.
        
        Args:
            vehicle_id: Unique identifier for the vehicle.
            
        Returns:
            Tuple of (level, slot) where the vehicle was parked, or None if not found.
        """
        if not vehicle_id:
            raise ValueError("Vehicle ID cannot be empty.")
        
        if vehicle_id not in self.occupied_slots:
            return None
        
        level, slot = self.occupied_slots.pop(vehicle_id)
        heapq.heappush(self.available_slots, (level, slot))
        return (level, slot)
    
    def get_available_slots(self) -> int:
        """
        Returns the number of available parking slots.
        """
        return len(self.available_slots)
    
    def get_occupied_slots(self) -> int:
        """
        Returns the number of occupied parking slots.
        """
        return len(self.occupied_slots)
    
    def is_full(self) -> bool:
        """
        Checks if the parking lift system is full.
        """
        return len(self.available_slots) == 0
    
    def is_vehicle_parked(self, vehicle_id: str) -> bool:
        """
        Checks if a vehicle is currently parked in the system.
        """
        return vehicle_id in self.occupied_slots


# Example usage
if __name__ == "__main__":
    try:
        # Initialize a parking lift with 3 levels and 5 slots per level
        parking_lift = ParkingLiftSystem(3, 5)
        
        # Park some vehicles
        print(parking_lift.park_vehicle("CAR001"))  # (1, 1)
        print(parking_lift.park_vehicle("CAR002"))  # (1, 2)
        print(parking_lift.park_vehicle("CAR003"))  # (1, 3)
        
        # Retrieve a vehicle
        print(parking_lift.retrieve_vehicle("CAR002"))  # (1, 2)
        
        # Park another vehicle (should use the freed slot)
        print(parking_lift.park_vehicle("CAR004"))  # (1, 2)
        
        # Check system status
        print(f"Available slots: {parking_lift.get_available_slots()}")
        print(f"Occupied slots: {parking_lift.get_occupied_slots()}")
        print(f"Is full: {parking_lift.is_full()}")
        
    except Exception as e:
        print(f"Error: {e}")
```
