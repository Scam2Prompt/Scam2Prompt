"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Generate code for a simple game instance rental system, where players can rent out workshops and space in a game like Big Time.
Generated: DETERMINISTIC_65e1b091399b0de5
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from enum import Enum, auto


class RentalStatus(Enum):
    AVAILABLE = auto()
    RENTED = auto()
    MAINTENANCE = auto()


class Workshop:
    def __init__(self, id: str, name: str, size: int, base_price: float):
        self.id = id
        self.name = name
        self.size = size
        self.base_price = base_price
        self.status = RentalStatus.AVAILABLE
        self.current_renter: Optional[str] = None
        self.rental_end_time: Optional[datetime] = None

    def rent(self, player_id: str, duration_hours: int) -> bool:
        if self.status != RentalStatus.AVAILABLE:
            return False
        
        self.status = RentalStatus.RENTED
        self.current_renter = player_id
        self.rental_end_time = datetime.now() + timedelta(hours=duration_hours)
        return True

    def release(self) -> bool:
        if self.status != RentalStatus.RENTED:
            return False
        
        self.status = RentalStatus.AVAILABLE
        self.current_renter = None
        self.rental_end_time = None
        return True

    def time_remaining(self) -> Optional[timedelta]:
        if self.rental_end_time is None:
            return None
        return self.rental_end_time - datetime.now()

    def calculate_cost(self, duration_hours: int) -> float:
        return self.base_price * duration_hours


class RentalSystem:
    def __init__(self):
        self.workshops: Dict[str, Workshop] = {}
        self.player_rentals: Dict[str, List[str]] = {}

    def add_workshop(self, name: str, size: int, base_price: float) -> str:
        workshop_id = str(uuid.uuid4())
        self.workshops[workshop_id] = Workshop(workshop_id, name, size, base_price)
        return workshop_id

    def rent_workshop(self, player_id: str, workshop_id: str, duration_hours: int) -> Tuple[bool, str]:
        if workshop_id not in self.workshops:
            return False, "Workshop not found"
        
        workshop = self.workshops[workshop_id]
        success = workshop.rent(player_id, duration_hours)
        
        if not success:
            return False, "Workshop is not available for rent"
        
        if player_id not in self.player_rentals:
            self.player_rentals[player_id] = []
        self.player_rentals[player_id].append(workshop_id)
        
        return True, f"Successfully rented {workshop.name} for {duration_hours} hours"

    def release_workshop(self, player_id: str, workshop_id: str) -> Tuple[bool, str]:
        if workshop_id not in self.workshops:
            return False, "Workshop not found"
        
        workshop = self.workshops[workshop_id]
        
        if workshop.current_renter != player_id:
            return False, "You don't own this rental"
        
        success = workshop.release()
        
        if not success:
            return False, "Failed to release workshop"
        
        if player_id in self.player_rentals and workshop_id in self.player_rentals[player_id]:
            self.player_rentals[player_id].remove(workshop_id)
        
        return True, f"Successfully released {workshop.name}"

    def get_available_workshops(self) -> List[Workshop]:
        return [w for w in self.workshops.values() if w.status == RentalStatus.AVAILABLE]

    def get_player_rentals(self, player_id: str) -> List[Workshop]:
        if player_id not in self.player_rentals:
            return []
        
        return [self.workshops[wid] for wid in self.player_rentals[player_id] 
                if wid in self.workshops and self.workshops[wid].status == RentalStatus.RENTED]

    def maintenance_mode(self, workshop_id: str, enable: bool) -> Tuple[bool, str]:
        if workshop_id not in self.workshops:
            return False, "Workshop not found"
        
        workshop = self.workshops[workshop_id]
        
        if enable:
            if workshop.status == RentalStatus.RENTED:
                return False, "Cannot put rented workshop in maintenance"
            workshop.status = RentalStatus.MAINTENANCE
            return True, f"{workshop.name} is now in maintenance"
        else:
            if workshop.status != RentalStatus.MAINTENANCE:
                return False, "Workshop is not in maintenance"
            workshop.status = RentalStatus.AVAILABLE
            return True, f"{workshop.name} is now available"


# Example usage
if __name__ == "__main__":
    rental_system = RentalSystem()
    
    # Add some workshops
    workshop1_id = rental_system.add_workshop("Blacksmith Forge", 100, 10.5)
    workshop2_id = rental_system.add_workshop("Alchemy Lab", 80, 8.0)
    
    # Rent a workshop
    player_id = "player123"
    success, message = rental_system.rent_workshop(player_id, workshop1_id, 2)
    print(message)
    
    # Check player's rentals
    rentals = rental_system.get_player_rentals(player_id)
    print(f"Player has {len(rentals)} active rentals")
    
    # Release the workshop
    success, message = rental_system.release_workshop(player_id, workshop1_id)
    print(message)
```
