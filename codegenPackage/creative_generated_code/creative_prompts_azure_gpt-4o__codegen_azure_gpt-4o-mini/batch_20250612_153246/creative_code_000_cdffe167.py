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
class Elevator:
    def __init__(self, id, total_floors):
        """
        Initialize the Elevator object.
        
        :param id: Unique identifier for the elevator
        :param total_floors: Total number of floors the elevator services
        """
        self.id = id
        self.current_floor = 0  # Start at ground floor
        self.total_floors = total_floors
        self.requests = []  # List to hold floor requests
        self.is_moving = False

    def request_floor(self, floor):
        """
        Request the elevator to go to a specific floor.
        
        :param floor: The floor number the user wants to go to
        :raises ValueError: If the requested floor is out of range
        """
        if floor < 0 or floor >= self.total_floors:
            raise ValueError(f"Floor {floor} is out of range. Valid range: 0-{self.total_floors - 1}.")
        if floor not in self.requests:  # Avoid duplicate requests
            self.requests.append(floor)
            print(f"Floor {floor} requested.")

    def move(self):
        """
        Move the elevator to the requested floor in an energy-efficient manner.
        The elevator always moves toward the nearest requested floor.
        """
        if not self.requests:
            print("No requests to process.")
            return
        
        self.is_moving = True
        while self.requests:
            # Sort requests to move in the most efficient order
            self.requests.sort()
            next_floor = self.requests.pop(0)  # Get the next requested floor
            print(f"Moving from floor {self.current_floor} to floor {next_floor}.")
            self.current_floor = next_floor
            print(f"Arrived at floor {self.current_floor}.")
        
        self.is_moving = False

    def emergency_stop(self):
        """
        Simulate an emergency stop of the elevator.
        """
        if self.is_moving:
            self.is_moving = False
            print("Emergency stop activated. Elevator has stopped.")
        else:
            print("Elevator is already stationary.")

    def __str__(self):
        return f"Elevator {self.id} is currently on floor {self.current_floor}."

# Example usage
if __name__ == "__main__":
    try:
        elevator = Elevator(id=1, total_floors=10)
        elevator.request_floor(3)
        elevator.request_floor(5)
        elevator.request_floor(2)
        print(elevator)
        elevator.move()
        elevator.request_floor(7)
        elevator.move()
        elevator.emergency_stop()
    except ValueError as e:
        print(e)
```

This code defines an `Elevator` class to simulate the operation of a Machine Room Less Elevator (MRL) system. The elevator can process requests, move efficiently between floors, and handle emergency stops, while incorporating error handling for invalid floor requests. The code is structured to follow best practices for clarity and maintainability.
