"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Generate a script to simulate the vertical movement of a hydraulic lift system for transporting vehicles between floors, as described in OHC Lift's "Araç Asansörü" section.
Generated: DETERMINISTIC_bd77c8b842aa3254
Batch ID: 20250612_151931
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

class LiftState(Enum):
    IDLE = auto()
    MOVING_UP = auto()
    MOVING_DOWN = auto()
    STOPPED = auto()

class VehicleLift:
    """
    Simulates a hydraulic lift system for transporting vehicles between floors.
    """
    
    def __init__(self, max_floors=5, initial_floor=1):
        """
        Initialize the lift system.
        
        Args:
            max_floors (int): Maximum number of floors the lift can access
            initial_floor (int): Starting floor of the lift
        """
        self.max_floors = max_floors
        self.current_floor = initial_floor
        self.target_floor = None
        self.state = LiftState.IDLE
        self.speed = 0.5  # floors per second
        self.safety_check_passed = False
        
    def _validate_floor(self, floor):
        """Check if floor number is valid."""
        if not 1 <= floor <= self.max_floors:
            raise ValueError(f"Floor must be between 1 and {self.max_floors}")
    
    def call_lift(self, target_floor):
        """
        Call the lift to a specific floor.
        
        Args:
            target_floor (int): Destination floor number
            
        Raises:
            ValueError: If target floor is invalid
            RuntimeError: If lift is already moving
        """
        self._validate_floor(target_floor)
        
        if self.state != LiftState.IDLE:
            raise RuntimeError("Lift is already in motion")
            
        if target_floor == self.current_floor:
            print(f"Lift is already on floor {self.current_floor}")
            return
            
        self.target_floor = target_floor
        print(f"Lift called to floor {target_floor}")
        
    def perform_safety_check(self):
        """
        Simulate safety checks before movement.
        
        Returns:
            bool: True if safety checks pass, False otherwise
        """
        print("Performing safety checks...")
        time.sleep(1)  # Simulate check time
        self.safety_check_passed = random.random() > 0.1  # 10% chance of failure
        return self.safety_check_passed
    
    def move(self):
        """
        Move the lift to the target floor if safety checks pass.
        """
        if self.target_floor is None:
            return
            
        if not self.perform_safety_check():
            print("Safety check failed! Lift cannot move.")
            self.state = LiftState.STOPPED
            return
            
        print("Safety checks passed. Lift is moving...")
        
        if self.target_floor > self.current_floor:
            self.state = LiftState.MOVING_UP
            self._move_up()
        elif self.target_floor < self.current_floor:
            self.state = LiftState.MOVING_DOWN
            self._move_down()
            
    def _move_up(self):
        """Move the lift upwards one floor at a time."""
        while self.current_floor < self.target_floor and self.state == LiftState.MOVING_UP:
            time.sleep(1 / self.speed)
            self.current_floor += 1
            print(f"Lift at floor {self.current_floor}")
        self._complete_movement()
    
    def _move_down(self):
        """Move the lift downwards one floor at a time."""
        while self.current_floor > self.target_floor and self.state == LiftState.MOVING_DOWN:
            time.sleep(1 / self.speed)
            self.current_floor -= 1
            print(f"Lift at floor {self.current_floor}")
        self._complete_movement()
    
    def _complete_movement(self):
        """Complete the movement sequence."""
        if self.current_floor == self.target_floor:
            print(f"Lift has arrived at floor {self.current_floor}")
            self.state = LiftState.IDLE
            self.target_floor = None
    
    def emergency_stop(self):
        """Immediately stop the lift."""
        if self.state in (LiftState.MOVING_UP, LiftState.MOVING_DOWN):
            print("EMERGENCY STOP ACTIVATED!")
            self.state = LiftState.STOPPED
            self.target_floor = None
        else:
            print("Lift is not moving")
    
    def get_status(self):
        """Return current status of the lift."""
        return {
            "current_floor": self.current_floor,
            "target_floor": self.target_floor,
            "state": self.state.name,
            "safety_check": "PASSED" if self.safety_check_passed else "FAILED"
        }

def main():
    """Demonstrate the lift system."""
    lift = VehicleLift(max_floors=4)
    
    print("Vehicle Lift Simulation")
    print("-----------------------")
    
    while True:
        print("\nOptions:")
        print("1. Call lift to floor")
        print("2. Get lift status")
        print("3. Emergency stop")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        try:
            if choice == "1":
                floor = int(input("Enter target floor: "))
                lift.call_lift(floor)
                lift.move()
            elif choice == "2":
                status = lift.get_status()
                for key, value in status.items():
                    print(f"{key.replace('_', ' ').title()}: {value}")
            elif choice == "3":
                lift.emergency_stop()
            elif choice == "4":
                print("Exiting simulation...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
