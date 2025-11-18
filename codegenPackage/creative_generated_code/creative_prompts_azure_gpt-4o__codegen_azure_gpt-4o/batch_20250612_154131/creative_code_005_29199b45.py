"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Write code to simulate an emergency technical service system for automatic garage doors, focusing on rapid and secure adaptations as described by Trimatic Puertas Automáticas.
Generated: DETERMINISTIC_29199b4518b573be
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random


class GarageDoor:
    """
    Represents an automatic garage door.
    Includes methods to open, close, stop, and lock/unlock the door.
    """
    def __init__(self):
        self.is_open = False
        self.is_locked = False
        self.is_operating = False

    def open_door(self):
        """
        Opens the garage door if it is not locked or already open.
        """
        if self.is_locked:
            raise RuntimeError("Cannot open the door. The door is locked.")
        if self.is_open:
            raise RuntimeError("The door is already open.")
        self.is_operating = True
        print("Opening the door...")
        time.sleep(2)  # Simulated operation delay
        self.is_open = True
        self.is_operating = False
        print("The door is now open.")

    def close_door(self):
        """
        Closes the garage door if it is not locked or already closed.
        """
        if self.is_locked:
            raise RuntimeError("Cannot close the door. The door is locked.")
        if not self.is_open:
            raise RuntimeError("The door is already closed.")
        self.is_operating = True
        print("Closing the door...")
        time.sleep(2)  # Simulated operation delay
        self.is_open = False
        self.is_operating = False
        print("The door is now closed.")

    def stop_operation(self):
        """
        Stops the ongoing operation of the garage door.
        """
        if not self.is_operating:
            raise RuntimeError("No operation is currently in progress.")
        self.is_operating = False
        print("Operation stopped.")

    def lock_door(self):
        """
        Locks the garage door if it is closed.
        """
        if self.is_open:
            raise RuntimeError("Cannot lock the door while it is open.")
        self.is_locked = True
        print("The door is now locked.")

    def unlock_door(self):
        """
        Unlocks the garage door.
        """
        self.is_locked = False
        print("The door is now unlocked.")


class EmergencyService:
    """
    Simulates an emergency technical service system
    for rapid and secure adaptations to garage doors.
    """
    def __init__(self):
        self.garage_door = GarageDoor()

    def perform_emergency_action(self):
        """
        Simulates automatic emergency decision-making for the garage door.
        Handles random emergency scenarios such as forced stop or door lock/unlock.
        """
        print("Emergency service activated!")
        action = random.choice(["force_stop", "lock", "unlock"])
        try:
            if action == "force_stop":
                print("Attempting to stop door operation...")
                self.garage_door.stop_operation()
            elif action == "lock":
                print("Attempting to lock the door...")
                self.garage_door.lock_door()
            elif action == "unlock":
                print("Attempting to unlock the door...")
                self.garage_door.unlock_door()
        except RuntimeError as e:
            print(f"Emergency action failed: {e}")
        else:
            print(f"Emergency action '{action}' completed successfully.")
        finally:
            print("Emergency service has concluded.")


# Example usage of the emergency technical service system
if __name__ == "__main__":
    service = EmergencyService()

    try:
        # Simulate normal garage door operations
        service.garage_door.open_door()
        service.garage_door.close_door()

        # Run the emergency service
        service.perform_emergency_action()

    except RuntimeError as err:
        print(f"Operation error: {err}")
    except Exception as err:
        print(f"Unexpected error: {err}")
    finally:
        print("Program execution completed.")
```
