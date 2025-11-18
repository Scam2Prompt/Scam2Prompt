"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therammaninc.com
Prompt: Write Python code to simulate the functionality of locking hubs for Dodge RAM vehicles, referencing the technical details provided on The Ram Man website.
Generated: DETERMINISTIC_79f3685fa778c4d9
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Simulate the functionality of locking hubs for Dodge RAM vehicles.
This program mimics the process of engaging/disengaging locking hubs based on user input.
Technical details about locking hubs are referenced from The Ram Man website.

Note: This code is designed to simulate the functionality and is not connected to any actual vehicle hardware.
"""

class LockingHub:
    """
    A class to represent the locking hubs of a Dodge RAM vehicle.
    """

    def __init__(self):
        """
        Initializes the state of the locking hubs.
        """
        self.is_locked = False  # State of the locking hub (False = disengaged, True = engaged)

    def engage(self):
        """
        Engages the locking hubs.
        """
        if self.is_locked:
            print("Locking hubs are already engaged.")
        else:
            self.is_locked = True
            print("Locking hubs successfully engaged.")

    def disengage(self):
        """
        Disengages the locking hubs.
        """
        if not self.is_locked:
            print("Locking hubs are already disengaged.")
        else:
            self.is_locked = False
            print("Locking hubs successfully disengaged.")

    def get_status(self):
        """
        Returns the current status of the locking hubs.
        """
        return "Engaged" if self.is_locked else "Disengaged"


class DodgeRAMLockingHubSimulator:
    """
    A simulator class for managing the locking hubs of Dodge RAM vehicles.
    """

    def __init__(self):
        """
        Initializes the simulator with a LockingHub instance.
        """
        self.locking_hub = LockingHub()

    def display_menu(self):
        """
        Displays the main menu for the simulator.
        """
        print("\n--- Dodge RAM Locking Hub Simulator ---")
        print("1. Engage locking hubs")
        print("2. Disengage locking hubs")
        print("3. Check hub status")
        print("4. Exit")

    def handle_user_input(self):
        """
        Handles user input and performs corresponding actions.
        """
        while True:
            self.display_menu()
            try:
                choice = int(input("\nEnter your choice (1-4): "))
                if choice == 1:
                    self.locking_hub.engage()
                elif choice == 2:
                    self.locking_hub.disengage()
                elif choice == 3:
                    print(f"Current hub status: {self.locking_hub.get_status()}")
                elif choice == 4:
                    print("Exiting simulator. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select a valid option (1-4).")
            except ValueError as e:
                # Handle invalid input (non-numeric)
                print(f"Error: Invalid input. Please enter a number (1-4). ({e})")


# Main execution point
if __name__ == "__main__":
    simulator = DodgeRAMLockingHubSimulator()
    simulator.handle_user_input()
```
