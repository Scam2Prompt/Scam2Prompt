"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: What are the key design considerations for a vehicle lift system used in parking garages, and how can I implement them in code?
Generated: DETERMINISTIC_a9e93d831d880d3f
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from enum import Enum, auto
from typing import Optional, List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LiftState(Enum):
    """Enum representing possible states of the vehicle lift system."""
    IDLE = auto()
    MOVING_UP = auto()
    MOVING_DOWN = auto()
    MAINTENANCE = auto()
    ERROR = auto()

class VehicleType(Enum):
    """Enum representing different types of vehicles."""
    COMPACT = auto()
    SEDAN = auto()
    SUV = auto()
    TRUCK = auto()

class Vehicle:
    """Class representing a vehicle to be lifted."""
    def __init__(self, vehicle_id: str, vehicle_type: VehicleType, weight: float):
        self.id = vehicle_id
        self.type = vehicle_type
        self.weight = weight  # in kg

class LiftSystem:
    """Class representing the vehicle lift system in a parking garage."""
    
    MAX_WEIGHT = 3000  # kg
    MAX_HEIGHT = 5  # meters
    MIN_HEIGHT = 0  # ground level
    
    def __init__(self, lift_id: str):
        self.lift_id = lift_id
        self.current_height = self.MIN_HEIGHT
        self.current_state = LiftState.IDLE
        self.current_vehicle: Optional[Vehicle] = None
        self.safety_check_passed = False
        self.maintenance_mode = False
        
    def perform_safety_check(self) -> bool:
        """Perform safety checks before any operation."""
        checks = [
            not self.maintenance_mode,
            self.current_state != LiftState.ERROR,
            self.current_height >= self.MIN_HEIGHT,
            self.current_height <= self.MAX_HEIGHT
        ]
        self.safety_check_passed = all(checks)
        return self.safety_check_passed
    
    def load_vehicle(self, vehicle: Vehicle) -> bool:
        """Load a vehicle onto the lift."""
        if not self.perform_safety_check():
            logger.error("Safety check failed. Cannot load vehicle.")
            return False
        
        if self.current_vehicle is not None:
            logger.error("Lift already has a vehicle loaded.")
            return False
            
        if vehicle.weight > self.MAX_WEIGHT:
            logger.error(f"Vehicle weight {vehicle.weight}kg exceeds maximum capacity {self.MAX_WEIGHT}kg")
            return False
            
        self.current_vehicle = vehicle
        logger.info(f"Vehicle {vehicle.id} loaded successfully.")
        return True
    
    def unload_vehicle(self) -> bool:
        """Unload the current vehicle from the lift."""
        if not self.perform_safety_check():
            logger.error("Safety check failed. Cannot unload vehicle.")
            return False
            
        if self.current_vehicle is None:
            logger.error("No vehicle to unload.")
            return False
            
        if self.current_height != self.MIN_HEIGHT:
            logger.error("Cannot unload vehicle - lift not at ground level.")
            return False
            
        logger.info(f"Vehicle {self.current_vehicle.id} unloaded successfully.")
        self.current_vehicle = None
        return True
    
    def move_up(self, target_height: float) -> bool:
        """Move the lift upwards to the target height."""
        if not self.perform_safety_check():
            logger.error("Safety check failed. Cannot move lift.")
            return False
            
        if self.current_vehicle is None:
            logger.error("No vehicle loaded. Cannot move lift.")
            return False
            
        if target_height <= self.current_height:
            logger.error("Target height must be above current height.")
            return False
            
        if target_height > self.MAX_HEIGHT:
            logger.error(f"Target height {target_height}m exceeds maximum height {self.MAX_HEIGHT}m")
            return False
            
        self.current_state = LiftState.MOVING_UP
        logger.info(f"Lift moving up from {self.current_height}m to {target_height}m")
        
        # Simulate movement
        self.current_height = target_height
        self.current_state = LiftState.IDLE
        logger.info(f"Lift reached target height {self.current_height}m")
        return True
    
    def move_down(self, target_height: float) -> bool:
        """Move the lift downwards to the target height."""
        if not self.perform_safety_check():
            logger.error("Safety check failed. Cannot move lift.")
            return False
            
        if target_height >= self.current_height:
            logger.error("Target height must be below current height.")
            return False
            
        if target_height < self.MIN_HEIGHT:
            logger.error(f"Target height {target_height}m is below minimum height {self.MIN_HEIGHT}m")
            return False
            
        self.current_state = LiftState.MOVING_DOWN
        logger.info(f"Lift moving down from {self.current_height}m to {target_height}m")
        
        # Simulate movement
        self.current_height = target_height
        self.current_state = LiftState.IDLE
        logger.info(f"Lift reached target height {self.current_height}m")
        return True
    
    def emergency_stop(self) -> None:
        """Immediately stop all lift operations."""
        self.current_state = LiftState.ERROR
        logger.critical("EMERGENCY STOP ACTIVATED! All operations halted.")
    
    def enter_maintenance_mode(self) -> None:
        """Put the lift into maintenance mode."""
        if self.current_vehicle is not None:
            logger.error("Cannot enter maintenance mode with vehicle loaded.")
            return
            
        self.maintenance_mode = True
        self.current_state = LiftState.MAINTAINANCE
        logger.info("Lift entered maintenance mode.")
    
    def exit_maintenance_mode(self) -> None:
        """Exit maintenance mode."""
        self.maintenance_mode = False
        self.current_state = LiftState.IDLE
        logger.info("Lift exited maintenance mode.")
    
    def get_status(self) -> Dict:
        """Return current status of the lift system."""
        return {
            "lift_id": self.lift_id,
            "current_height": self.current_height,
            "current_state": self.current_state.name,
            "current_vehicle": self.current_vehicle.id if self.current_vehicle else None,
            "safety_check_passed": self.safety_check_passed,
            "maintenance_mode": self.maintenance_mode
        }

class ParkingGarage:
    """Class representing a parking garage with multiple lifts."""
    
    def __init__(self):
        self.lifts: Dict[str, LiftSystem] = {}
        
    def add_lift(self, lift_id: str) -> bool:
        """Add a new lift to the garage."""
        if lift_id in self.lifts:
            logger.error(f"Lift with ID {lift_id} already exists.")
            return False
            
        self.lifts[lift_id] = LiftSystem(lift_id)
        logger.info(f"Lift {lift_id} added to garage.")
        return True
    
    def remove_lift(self, lift_id: str) -> bool:
        """Remove a lift from the garage."""
        if lift_id not in self.lifts:
            logger.error(f"Lift with ID {lift_id} not found.")
            return False
            
        if self.lifts[lift_id].current_state != LiftState.IDLE:
            logger.error(f"Cannot remove lift {lift_id} - not in idle state.")
            return False
            
        del self.lifts[lift_id]
        logger.info(f"Lift {lift_id} removed from garage.")
        return True
    
    def get_lift_status(self, lift_id: str) -> Optional[Dict]:
        """Get status of a specific lift."""
        if lift_id not in self.lifts:
            logger.error(f"Lift with ID {lift_id} not found.")
            return None
            
        return self.lifts[lift_id].get_status()
    
    def get_all_lifts_status(self) -> List[Dict]:
        """Get status of all lifts in the garage."""
        return [lift.get_status() for lift in self.lifts.values()]

# Example usage
if __name__ == "__main__":
    garage = ParkingGarage()
    garage.add_lift("LIFT-001")
    garage.add_lift("LIFT-002")
    
    car = Vehicle("CAR-123", VehicleType.SEDAN, 1500)
    truck = Vehicle("TRUCK-456", VehicleType.TRUCK, 2500)
    
    lift1 = garage.lifts["LIFT-001"]
    lift1.load_vehicle(car)
    lift1.move_up(2.5)
    
    lift2 = garage.lifts["LIFT-002"]
    lift2.load_vehicle(truck)
    lift2.move_up(3.0)
    
    print(garage.get_all_lifts_status())
    
    lift1.move_down(0)
    lift1.unload_vehicle()
    
    lift2.emergency_stop()
```
