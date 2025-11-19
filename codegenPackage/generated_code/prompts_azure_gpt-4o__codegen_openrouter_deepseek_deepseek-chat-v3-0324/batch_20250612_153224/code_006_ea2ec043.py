"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: Write code to implement a vehicle access control system using barriers and automation, referencing the solutions for access control systems described by Space Technologies Bogotá.
Generated: DETERMINISTIC_ea2ec0434b8e3841
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from enum import Enum
import logging
from typing import Optional, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BarrierState(Enum):
    """Enum representing the possible states of a barrier."""
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    MOVING_UP = "MOVING_UP"
    MOVING_DOWN = "MOVING_DOWN"
    ERROR = "ERROR"

class VehicleType(Enum):
    """Enum representing different vehicle types."""
    CAR = "CAR"
    TRUCK = "TRUCK"
    MOTORCYCLE = "MOTORCYCLE"
    EMERGENCY = "EMERGENCY"
    UNAUTHORIZED = "UNAUTHORIZED"

class AccessControlSystem:
    """Main class for the vehicle access control system."""
    
    def __init__(self):
        self.barriers = []
        self.authorized_vehicles = set()
        self.emergency_mode = False
        
    def add_barrier(self, barrier_id: str) -> bool:
        """Add a new barrier to the system."""
        if not barrier_id:
            logger.error("Cannot add barrier with empty ID")
            return False
            
        if any(b.id == barrier_id for b in self.barriers):
            logger.error(f"Barrier with ID {barrier_id} already exists")
            return False
            
        self.barriers.append(Barrier(barrier_id))
        logger.info(f"Added barrier with ID {barrier_id}")
        return True
        
    def register_vehicle(self, license_plate: str, vehicle_type: VehicleType) -> bool:
        """Register a vehicle as authorized."""
        if not license_plate:
            logger.error("Cannot register vehicle with empty license plate")
            return False
            
        if vehicle_type == VehicleType.UNAUTHORIZED:
            logger.error("Cannot register unauthorized vehicle type")
            return False
            
        self.authorized_vehicles.add((license_plate, vehicle_type))
        logger.info(f"Registered vehicle {license_plate} as {vehicle_type.value}")
        return True
        
    def request_access(self, barrier_id: str, license_plate: str, vehicle_type: VehicleType) -> bool:
        """Handle a vehicle's request to pass through a barrier."""
        if self.emergency_mode:
            logger.info("Emergency mode active - granting access")
            return self._open_barrier(barrier_id)
            
        barrier = self._get_barrier(barrier_id)
        if not barrier:
            logger.error(f"Barrier {barrier_id} not found")
            return False
            
        if (license_plate, vehicle_type) in self.authorized_vehicles:
            logger.info(f"Authorized access for {license_plate}")
            return self._open_barrier(barrier_id)
        else:
            logger.warning(f"Unauthorized access attempt by {license_plate}")
            return False
            
    def _open_barrier(self, barrier_id: str) -> bool:
        """Internal method to open a barrier."""
        barrier = self._get_barrier(barrier_id)
        if not barrier:
            return False
            
        if barrier.state == BarrierState.OPEN:
            logger.info(f"Barrier {barrier_id} is already open")
            return True
            
        if barrier.state == BarrierState.MOVING_UP or barrier.state == BarrierState.MOVING_DOWN:
            logger.warning(f"Barrier {barrier_id} is currently moving")
            return False
            
        try:
            barrier.open()
            logger.info(f"Barrier {barrier_id} opened successfully")
            return True
        except Exception as e:
            logger.error(f"Error opening barrier {barrier_id}: {str(e)}")
            return False
            
    def _get_barrier(self, barrier_id: str) -> Optional['Barrier']:
        """Get a barrier by its ID."""
        for barrier in self.barriers:
            if barrier.id == barrier_id:
                return barrier
        return None
        
    def activate_emergency_mode(self):
        """Activate emergency mode (all barriers open)."""
        self.emergency_mode = True
        logger.info("Emergency mode activated")
        for barrier in self.barriers:
            try:
                barrier.open()
            except Exception as e:
                logger.error(f"Error opening barrier {barrier.id} in emergency mode: {str(e)}")
                
    def deactivate_emergency_mode(self):
        """Deactivate emergency mode."""
        self.emergency_mode = False
        logger.info("Emergency mode deactivated")
        for barrier in self.barriers:
            try:
                barrier.close()
            except Exception as e:
                logger.error(f"Error closing barrier {barrier.id} after emergency mode: {str(e)}")

class Barrier:
    """Class representing a physical barrier."""
    
    def __init__(self, barrier_id: str):
        self.id = barrier_id
        self.state = BarrierState.CLOSED
        self.last_maintenance = time.time()
        
    def open(self) -> None:
        """Open the barrier."""
        if self.state == BarrierState.OPEN:
            return
            
        if self.state == BarrierState.ERROR:
            raise Exception("Barrier is in error state and cannot be opened")
            
        self.state = BarrierState.MOVING_UP
        logger.info(f"Barrier {self.id} is opening...")
        
        # Simulate physical movement
        time.sleep(2)
        
        self.state = BarrierState.OPEN
        logger.info(f"Barrier {self.id} is now open")
        
    def close(self) -> None:
        """Close the barrier."""
        if self.state == BarrierState.CLOSED:
            return
            
        if self.state == BarrierState.ERROR:
            raise Exception("Barrier is in error state and cannot be closed")
            
        self.state = BarrierState.MOVING_DOWN
        logger.info(f"Barrier {self.id} is closing...")
        
        # Simulate physical movement
        time.sleep(2)
        
        self.state = BarrierState.CLOSED
        logger.info(f"Barrier {self.id} is now closed")
        
    def perform_maintenance(self) -> None:
        """Perform maintenance on the barrier."""
        logger.info(f"Performing maintenance on barrier {self.id}")
        self.last_maintenance = time.time()
        self.state = BarrierState.CLOSED
        logger.info(f"Maintenance completed on barrier {self.id}")

# Example usage
if __name__ == "__main__":
    # Initialize the system
    system = AccessControlSystem()
    
    # Add barriers
    system.add_barrier("entrance_1")
    system.add_barrier("exit_1")
    
    # Register authorized vehicles
    system.register_vehicle("ABC123", VehicleType.CAR)
    system.register_vehicle("XYZ789", VehicleType.TRUCK)
    
    # Simulate access requests
    system.request_access("entrance_1", "ABC123", VehicleType.CAR")  # Should succeed
    system.request_access("entrance_1", "UNKNOWN", VehicleType.CAR)  # Should fail
    
    # Emergency mode test
    system.activate_emergency_mode()
    system.request_access("exit_1", "UNKNOWN", VehicleType.UNAUTHORIZED)  # Should succeed in emergency mode
    system.deactivate_emergency_mode()
```
