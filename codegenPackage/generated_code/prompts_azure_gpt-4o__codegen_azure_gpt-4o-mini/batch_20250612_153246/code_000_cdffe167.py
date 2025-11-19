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
class Elevator:
    def __init__(self, total_floors):
        """
        Initialize the Elevator system.

        :param total_floors: Total number of floors the elevator can service.
        """
        if total_floors < 1:
            raise ValueError("Total floors must be at least 1.")
        self.total_floors = total_floors
        self.current_floor = 0  # Start at ground floor
        self.requests = []  # List to hold floor requests
        self.is_moving = False  # Elevator state

    def request_floor(self, floor):
        """
        Request a floor for the elevator to go to.

        :param floor: The floor number to request.
        """
        if floor < 0 or floor >= self.total_floors:
            raise ValueError(f"Floor must be between 0 and {self.total_floors - 1}.")
        if floor not in self.requests:
            self.requests.append(floor)
            print(f"Floor {floor} requested.")

    def move_elevator(self):
        """
        Move the elevator to the requested floors in order.
        """
        if not self.requests:
            print("No requests to process.")
            return

        self.is_moving = True
        while self.requests:
            next_floor = min(self.requests)
            self.requests.remove(next_floor)
            self._move_to_floor(next_floor)

        self.is_moving = False

    def _move_to_floor(self, floor):
        """
        Simulate moving the elevator to a specific floor.

        :param floor: The floor number to move to.
        """
        print(f"Moving from floor {self.current_floor} to floor {floor}...")
        # Simulate the time taken to move
        self.current_floor = floor
        print(f"Arrived at floor {self.current_floor}.")

    def energy_efficient_mode(self):
        """
        Activate energy-efficient mode for the elevator.
        """
        print("Energy-efficient mode activated. Reducing power consumption.")
        # Implement energy-saving features here (e.g., slower speed, reduced lighting)

    def emergency_stop(self):
        """
        Stop the elevator in case of an emergency.
        """
        print("Emergency stop activated! Elevator is stopping.")
        self.is_moving = False
        self.requests.clear()  # Clear any pending requests

# Example usage
if __name__ == "__main__":
    try:
        elevator = Elevator(total_floors=10)
        elevator.request_floor(3)
        elevator.request_floor(5)
        elevator.request_floor(1)
        elevator.energy_efficient_mode()
        elevator.move_elevator()
    except ValueError as e:
        print(f"Error: {e}")
```
