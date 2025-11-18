"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iconelevator.in
Prompt: Write code to simulate the operation of a Machine Room Less Elevator (MRL) system, incorporating energy-efficient features as described by ICON Elevator.
Generated: DETERMINISTIC_cdffe167dddcb8b6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class ElevatorSystem:
    """
    A class to simulate the operation of a Machine Room Less (MRL) Elevator System.
    Incorporates energy-efficient features such as idle mode and regenerative braking.
    """
    
    def __init__(self, floors, capacity):
        """
        Initialize the Elevator System.
        
        Parameters:
        floors (int): Number of floors in the building.
        capacity (int): Maximum passenger capacity of the elevator.
        """
        self.current_floor = 1  # Elevator starts at the ground floor
        self.target_floor = None  # Target floor
        self.passengers = 0  # Current number of passengers in the elevator
        self.capacity = capacity  # Maximum capacity
        self.floors = floors  # Total number of floors in the building
        self.is_moving = False  # Is the elevator moving?
        self.energy_saving_mode = False  # Energy-saving mode enabled when idle
        self.regenerative_braking = False  # Regenerative braking feature

    def call_elevator(self, floor):
        """
        Simulate calling the elevator to a specific floor.
        
        Parameters:
        floor (int): The floor to which the elevator is called.
        """
        if floor < 1 or floor > self.floors:
            raise ValueError("Invalid floor number.")
        
        self.target_floor = floor
        self.move_elevator()

    def move_elevator(self):
        """
        Move the elevator to the target floor. Simulates energy-efficient operation.
        """
        if self.target_floor is None:
            print("No target floor specified.")
            return

        self.is_moving = True
        self.regenerative_braking = True  # Simulate regenerative braking during descent

        print(f"Elevator moving from Floor {self.current_floor} to Floor {self.target_floor}...")
        time.sleep(abs(self.target_floor - self.current_floor) * 0.5)  # Simulate travel time

        self.current_floor = self.target_floor
        self.regenerative_braking = False  # Disable regenerative braking
        self.is_moving = False
        self.target_floor = None

        print(f"Elevator has arrived at Floor {self.current_floor}.")
        self.enable_energy_saving_mode()

    def board_passengers(self, count):
        """
        Simulate boarding passengers into the elevator.
        
        Parameters:
        count (int): Number of passengers boarding.
        """
        if self.passengers + count > self.capacity:
            raise ValueError("Elevator overload. Cannot board more passengers.")
        
        self.passengers += count
        print(f"{count} passengers boarded the elevator. Current load: {self.passengers}.")

    def disembark_passengers(self, count):
        """
        Simulate disembarking passengers from the elevator.
        
        Parameters:
        count (int): Number of passengers disembarking.
        """
        if count > self.passengers:
            raise ValueError("Cannot disembark more passengers than are currently onboard.")
        
        self.passengers -= count
        print(f"{count} passengers disembarked the elevator. Current load: {self.passengers}.")

    def enable_energy_saving_mode(self):
        """
        Enable energy-saving mode when the elevator is idle.
        """
        if not self.is_moving and self.passengers == 0:
            self.energy_saving_mode = True
            print("Energy-saving mode enabled.")

    def disable_energy_saving_mode(self):
        """
        Disable energy-saving mode when the elevator is active.
        """
        self.energy_saving_mode = False
        print("Energy-saving mode disabled.")

# Example usage
if __name__ == "__main__":
    try:
        # Create an elevator system with 10 floors and a capacity of 8 passengers
        elevator = ElevatorSystem(floors=10, capacity=8)
        
        # Simulate elevator operations
        elevator.call_elevator(5)  # Call elevator to floor 5
        elevator.board_passengers(4)  # Board 4 passengers
        elevator.call_elevator(8)  # Move to floor 8
        elevator.disembark_passengers(2)  # Disembark 2 passengers
        elevator.call_elevator(1)  # Return to ground floor
    except ValueError as e:
        print(f"Error: {e}")
```
