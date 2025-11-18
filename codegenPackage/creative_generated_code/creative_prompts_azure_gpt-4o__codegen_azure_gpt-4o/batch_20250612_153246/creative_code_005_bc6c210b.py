"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iconelevator.in
Prompt: Write code to simulate the maintenance scheduling for elevators, incorporating 24/7 service availability as described by ICON Elevator.
Generated: DETERMINISTIC_bc6c210b48c412ef
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import heapq


class Elevator:
    """
    Represents a single elevator with maintenance scheduling and 24/7 service availability.
    """

    def __init__(self, elevator_id):
        """
        Initialize an Elevator object.

        :param elevator_id: Unique identifier for the elevator.
        """
        self.elevator_id = elevator_id
        self.maintenance_schedule = []
        self.is_operational = True

    def schedule_maintenance(self, maintenance_datetime):
        """
        Schedules maintenance for the elevator.

        :param maintenance_datetime: Datetime object representing when maintenance is scheduled.
        """
        if not isinstance(maintenance_datetime, datetime.datetime):
            raise ValueError("Maintenance datetime must be a valid datetime object.")
        heapq.heappush(self.maintenance_schedule, maintenance_datetime)

    def perform_maintenance(self):
        """
        Performs maintenance if the current datetime matches the scheduled time.
        """
        current_datetime = datetime.datetime.now()
        while self.maintenance_schedule and self.maintenance_schedule[0] <= current_datetime:
            maintenance_time = heapq.heappop(self.maintenance_schedule)
            print(f"Performing maintenance on Elevator {self.elevator_id} scheduled for {maintenance_time}.")
        self.is_operational = True  # Always ensure 24/7 service availability post-maintenance.


class ElevatorSystem:
    """
    Represents the elevator system that manages multiple elevators.
    """

    def __init__(self, num_elevators):
        """
        Initialize an ElevatorSystem object with a specified number of elevators.

        :param num_elevators: Number of elevators in the system.
        """
        if num_elevators <= 0:
            raise ValueError("Number of elevators must be greater than 0.")
        self.elevators = [Elevator(elevator_id=i + 1) for i in range(num_elevators)]

    def schedule_maintenance_for_elevator(self, elevator_id, maintenance_datetime):
        """
        Schedule maintenance for a specific elevator.

        :param elevator_id: Unique identifier for the elevator.
        :param maintenance_datetime: Datetime object representing when maintenance is scheduled.
        """
        try:
            elevator = self.get_elevator_by_id(elevator_id)
            elevator.schedule_maintenance(maintenance_datetime)
            print(f"Maintenance scheduled for Elevator {elevator_id} at {maintenance_datetime}.")
        except ValueError as e:
            print(f"Error: {e}")

    def get_elevator_by_id(self, elevator_id):
        """
        Retrieve an elevator by its ID.

        :param elevator_id: Unique identifier for the elevator.
        :return: Elevator object.
        """
        if elevator_id <= 0 or elevator_id > len(self.elevators):
            raise ValueError("Invalid elevator ID.")
        return self.elevators[elevator_id - 1]

    def run_maintenance_check(self):
        """
        Checks and performs maintenance for all elevators that are due.
        """
        for elevator in self.elevators:
            elevator.perform_maintenance()


# Example Usage
if __name__ == "__main__":
    # Create an elevator system with 5 elevators
    elevator_system = ElevatorSystem(num_elevators=5)

    # Schedule some maintenance tasks
    elevator_system.schedule_maintenance_for_elevator(
        elevator_id=2, maintenance_datetime=datetime.datetime.now() + datetime.timedelta(seconds=5)
    )
    elevator_system.schedule_maintenance_for_elevator(
        elevator_id=4, maintenance_datetime=datetime.datetime.now() + datetime.timedelta(seconds=10)
    )

    # Simulate periodic checks to ensure maintenance is performed
    import time

    print("Starting maintenance check loop...")
    for _ in range(15):
        elevator_system.run_maintenance_check()
        time.sleep(1)
```
