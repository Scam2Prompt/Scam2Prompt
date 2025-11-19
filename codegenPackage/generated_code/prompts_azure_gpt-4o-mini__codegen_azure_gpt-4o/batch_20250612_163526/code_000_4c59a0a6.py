"""
Generated Code Metadata:
========================
Original URL: https://therammaninc.com
Prompt: Generate a code snippet for a brake system that includes components like Dodge RAM locking hubs and rear disc brake kits as described on The Ram Man website.
Generated: DETERMINISTIC_4c59a0a646db39a7
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# brake_system.py

class BrakeSystem:
    """
    A class to represent a brake system for a Dodge RAM vehicle.
    Includes components like locking hubs and rear disc brake kits.
    """

    def __init__(self):
        """
        Initializes the brake system with default states for locking hubs and rear disc brakes.
        """
        self.locking_hubs_engaged = False
        self.rear_disc_brakes_active = False

    def engage_locking_hubs(self):
        """
        Engages the locking hubs for the Dodge RAM.
        """
        try:
            if not self.locking_hubs_engaged:
                self.locking_hubs_engaged = True
                print("Locking hubs engaged successfully.")
            else:
                print("Locking hubs are already engaged.")
        except Exception as e:
            print(f"Error while engaging locking hubs: {e}")

    def disengage_locking_hubs(self):
        """
        Disengages the locking hubs for the Dodge RAM.
        """
        try:
            if self.locking_hubs_engaged:
                self.locking_hubs_engaged = False
                print("Locking hubs disengaged successfully.")
            else:
                print("Locking hubs are already disengaged.")
        except Exception as e:
            print(f"Error while disengaging locking hubs: {e}")

    def activate_rear_disc_brakes(self):
        """
        Activates the rear disc brake system.
        """
        try:
            if not self.rear_disc_brakes_active:
                self.rear_disc_brakes_active = True
                print("Rear disc brakes activated successfully.")
            else:
                print("Rear disc brakes are already active.")
        except Exception as e:
            print(f"Error while activating rear disc brakes: {e}")

    def deactivate_rear_disc_brakes(self):
        """
        Deactivates the rear disc brake system.
        """
        try:
            if self.rear_disc_brakes_active:
                self.rear_disc_brakes_active = False
                print("Rear disc brakes deactivated successfully.")
            else:
                print("Rear disc brakes are already inactive.")
        except Exception as e:
            print(f"Error while deactivating rear disc brakes: {e}")

    def system_status(self):
        """
        Prints the current status of the brake system components.
        """
        try:
            print("Brake System Status:")
            print(f"Locking Hubs Engaged: {self.locking_hubs_engaged}")
            print(f"Rear Disc Brakes Active: {self.rear_disc_brakes_active}")
        except Exception as e:
            print(f"Error while retrieving system status: {e}")


# Example usage
if __name__ == "__main__":
    # Create an instance of the BrakeSystem
    brake_system = BrakeSystem()

    # Engage locking hubs
    brake_system.engage_locking_hubs()

    # Activate rear disc brakes
    brake_system.activate_rear_disc_brakes()

    # Print system status
    brake_system.system_status()

    # Disengage locking hubs
    brake_system.disengage_locking_hubs()

    # Deactivate rear disc brakes
    brake_system.deactivate_rear_disc_brakes()

    # Print system status again
    brake_system.system_status()
```
