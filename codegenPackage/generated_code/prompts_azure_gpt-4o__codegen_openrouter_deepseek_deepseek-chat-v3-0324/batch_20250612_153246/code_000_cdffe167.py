"""
Generated Code Metadata:
========================
Original URL: https://iconelevator.in
Prompt: Write code to simulate the operation of a Machine Room Less Elevator (MRL) system, incorporating energy-efficient features as described by ICON Elevator.
Generated: DETERMINISTIC_cdffe167dddcb8b6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Dict, Optional

class ElevatorState(Enum):
    IDLE = auto()
    MOVING_UP = auto()
    MOVING_DOWN = auto()
    DOOR_OPEN = auto()
    DOOR_CLOSING = auto()
    DOOR_OPENING = auto()
    EMERGENCY_STOP = auto()

class EnergyMode(Enum):
    STANDARD = auto()
    ECO = auto()
    SLEEP = auto()

@dataclass
class ElevatorRequest:
    floor: int
    direction: Optional[str] = None  # 'up' or 'down' for hall calls, None for car calls

class MRLElevator:
    def __init__(self, num_floors: int, max_capacity: int = 10):
        """
        Initialize the MRL elevator system.
        
        Args:
            num_floors: Total number of floors in the building
            max_capacity: Maximum number of passengers the elevator can carry
        """
        self.num_floors = num_floors
        self.max_capacity = max_capacity
        self.current_floor = 1
        self.state = ElevatorState.IDLE
        self.energy_mode = EnergyMode.STANDARD
        self.passengers = 0
        self.door_open_time = 0
        self.last_operation_time = time.time()
        self.requests: List[ElevatorRequest] = []
        self.floor_weights: Dict[int, int] = {floor: 0 for floor in range(1, num_floors + 1)}
        
        # Energy efficiency parameters
        self.energy_consumption = 0.0  # in kWh
        self.idle_time_threshold = 300  # 5 minutes in seconds
        self.eco_mode_speed = 0.8  # 80% of normal speed
        self.sleep_mode_power = 0.1  # 10% of normal power
        
    def add_request(self, floor: int, direction: Optional[str] = None) -> bool:
        """
        Add a new elevator request (either car call or hall call).
        
        Args:
            floor: Destination floor
            direction: 'up' or 'down' for hall calls
            
        Returns:
            bool: True if request was added successfully
        """
        if floor < 1 or floor > self.num_floors:
            print(f"Invalid floor request: {floor}")
            return False
            
        if direction not in [None, 'up', 'down']:
            print(f"Invalid direction: {direction}")
            return False
            
        # Check if request already exists
        existing = next((r for r in self.requests if r.floor == floor and r.direction == direction), None)
        if existing:
            print(f"Request for floor {floor} already exists")
            return False
            
        self.requests.append(ElevatorRequest(floor, direction))
        print(f"Added request for floor {floor} (direction: {direction})")
        self._wake_from_sleep()
        return True
        
    def _wake_from_sleep(self) -> None:
        """Transition from sleep mode to standard mode if needed."""
        if self.energy_mode == EnergyMode.SLEEP:
            self.energy_mode = EnergyMode.STANDARD
            print("Elevator waking from sleep mode")
            
    def _update_energy_mode(self) -> None:
        """Adjust energy mode based on activity."""
        idle_time = time.time() - self.last_operation_time
        
        if idle_time > self.idle_time_threshold and not self.requests:
            self.energy_mode = EnergyMode.SLEEP
            print("Entering sleep mode for energy savings")
        elif idle_time > self.idle_time_threshold / 2 and not self.requests:
            self.energy_mode = EnergyMode.ECO
            print("Entering eco mode")
        else:
            self.energy_mode = EnergyMode.STANDARD
            
    def _calculate_movement_cost(self, from_floor: int, to_floor: int) -> float:
        """Calculate energy cost for moving between floors."""
        floors_moved = abs(to_floor - from_floor)
        
        if self.energy_mode == EnergyMode.ECO:
            return floors_moved * 0.05 * self.eco_mode_speed
        elif self.energy_mode == EnergyMode.SLEEP:
            return floors_moved * 0.05 * self.sleep_mode_power
        else:
            return floors_moved * 0.05  # 0.05 kWh per floor in standard mode
            
    def _move_to_floor(self, target_floor: int) -> None:
        """Move elevator to target floor."""
        if target_floor == self.current_floor:
            return
            
        direction = 'up' if target_floor > self.current_floor else 'down'
        self.state = ElevatorState.MOVING_UP if direction == 'up' else ElevatorState.MOVING_DOWN
        
        print(f"Moving {direction} from floor {self.current_floor} to {target_floor}")
        
        # Simulate movement time
        floors_to_move = abs(target_floor - self.current_floor)
        movement_time = floors_to_move * (1.0 if self.energy_mode != EnergyMode.ECO else 1.25)
        time.sleep(movement_time * 0.1)  # Simulate time passing
        
        # Update energy consumption
        self.energy_consumption += self._calculate_movement_cost(self.current_floor, target_floor)
        self.current_floor = target_floor
        self.last_operation_time = time.time()
        
    def _open_doors(self) -> None:
        """Open elevator doors."""
        if self.state == ElevatorState.DOOR_OPEN:
            return
            
        self.state = ElevatorState.DOOR_OPENING
        print("Opening doors")
        time.sleep(0.5)  # Simulate door opening time
        self.state = ElevatorState.DOOR_OPEN
        self.door_open_time = time.time()
        
    def _close_doors(self) -> None:
        """Close elevator doors."""
        if self.state != ElevatorState.DOOR_OPEN:
            return
            
        self.state = ElevatorState.DOOR_CLOSING
        print("Closing doors")
        time.sleep(0.5)  # Simulate door closing time
        self.state = ElevatorState.IDLE
        self.last_operation_time = time.time()
        
    def _process_requests(self) -> None:
        """Process all pending elevator requests."""
        if not self.requests:
            return
            
        # Simple algorithm: process requests in order
        request = self.requests.pop(0)
        
        self._move_to_floor(request.floor)
        self._open_doors()
        
        # Simulate passengers entering/exiting
        passenger_change = random.randint(-3, 3)
        new_passengers = self.passengers + passenger_change
        self.passengers = max(0, min(new_passengers, self.max_capacity))
        print(f"Passengers: {self.passengers}/{self.max_capacity}")
        
        # Update floor weights for traffic analysis
        self.floor_weights[request.floor] += 1
        
        time.sleep(1)  # Simulate boarding time
        self._close_doors()
        
    def run(self) -> None:
        """Main elevator control loop."""
        try:
            while True:
                self._update_energy_mode()
                self._process_requests()
                
                # If no requests, sleep briefly to prevent busy waiting
                if not self.requests:
                    time.sleep(0.1)
                    
        except KeyboardInterrupt:
            print("\nElevator system shutting down...")
            print(f"Total energy consumed: {self.energy_consumption:.2f} kWh")
            
    def get_status(self) -> Dict:
        """Get current elevator status."""
        return {
            'current_floor': self.current_floor,
            'state': self.state.name,
            'energy_mode': self.energy_mode.name,
            'passengers': self.passengers,
            'pending_requests': len(self.requests),
            'energy_consumption': self.energy_consumption
        }

# Example usage
if __name__ == "__main__":
    elevator = MRLElevator(num_floors=10)
    
    # Simulate some requests
    elevator.add_request(5)
    elevator.add_request(3, 'up')
    elevator.add_request(8)
    elevator.add_request(1, 'down')
    
    # Run the elevator system
    elevator.run()
```
