"""
Generated Code Metadata:
========================
Original URL: https://iconelevator.in
Prompt: "Design a simple elevator system for a 2-story building using ladder logic, considering cost-effective and economical solutions like ICON ELEVATOR."
Generated: DETERMINISTIC_c64c1902c2691fea
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Simple Elevator System for a 2-Story Building using Ladder Logic Simulation
# ICON ELEVATOR inspired cost-effective solution

class Elevator:
    def __init__(self):
        self.current_floor = 1  # Ground floor
        self.door_open = False
        self.moving = False
        self.direction = None  # 'up' or 'down'
        self.call_buttons = {1: False, 2: False}  # Floor call buttons
        self.floor_sensors = {1: False, 2: False}  # Floor sensors
        self.door_timer = 0
        self.MAX_DOOR_TIME = 5  # seconds

    def call_elevator(self, floor):
        """Handle floor call button press"""
        if floor in self.call_buttons and not self.call_buttons[floor]:
            self.call_buttons[floor] = True
            print(f"Call button pressed for floor {floor}")

    def floor_sensor_trigger(self, floor):
        """Handle floor sensor activation"""
        if floor in self.floor_sensors:
            self.floor_sensors[floor] = True
            self.current_floor = floor
            print(f"Arrived at floor {floor}")
            self.stop_elevator()

    def stop_elevator(self):
        """Stop elevator at current floor"""
        self.moving = False
        self.direction = None
        self.call_buttons[self.current_floor] = False
        self.open_door()

    def open_door(self):
        """Open elevator door"""
        if not self.door_open and not self.moving:
            self.door_open = True
            self.door_timer = 0
            print("Door opening")

    def close_door(self):
        """Close elevator door"""
        if self.door_open and not self.moving:
            self.door_open = False
            print("Door closing")

    def move_elevator(self):
        """Move elevator based on current calls"""
        if not self.moving and not self.door_open:
            if self.current_floor == 1 and self.call_buttons[2]:
                self.direction = 'up'
                self.moving = True
                print("Moving up to floor 2")
            elif self.current_floor == 2 and self.call_buttons[1]:
                self.direction = 'down'
                self.moving = True
                print("Moving down to floor 1")

    def update(self, dt):
        """Update elevator state (simulate ladder logic scan cycle)"""
        # Door timer logic
        if self.door_open:
            self.door_timer += dt
            if self.door_timer >= self.MAX_DOOR_TIME:
                self.close_door()

        # Movement logic
        self.move_elevator()

        # Reset floor sensors after processing
        for floor in self.floor_sensors:
            self.floor_sensors[floor] = False


# Example usage
if __name__ == "__main__":
    elevator = Elevator()

    # Simulate ladder logic scan cycles
    import time
    try:
        while True:
            elevator.update(0.1)  # 100ms scan cycle
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nElevator system stopped")
```
