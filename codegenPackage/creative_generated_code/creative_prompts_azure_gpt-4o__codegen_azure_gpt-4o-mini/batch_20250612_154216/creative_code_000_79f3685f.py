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
class LockingHub:
    """
    A class to simulate the functionality of locking hubs for Dodge RAM vehicles.
    This class allows for the engagement and disengagement of the locking hubs.
    """

    def __init__(self):
        """Initialize the locking hub to a disengaged state."""
        self.locked = False

    def engage(self):
        """
        Engage the locking hub to enable four-wheel drive.
        Raises an exception if the hub is already engaged.
        """
        if self.locked:
            raise RuntimeError("Locking hub is already engaged.")
        self.locked = True
        print("Locking hub engaged. Four-wheel drive enabled.")

    def disengage(self):
        """
        Disengage the locking hub to return to two-wheel drive.
        Raises an exception if the hub is already disengaged.
        """
        if not self.locked:
            raise RuntimeError("Locking hub is already disengaged.")
        self.locked = False
        print("Locking hub disengaged. Two-wheel drive enabled.")

    def status(self):
        """
        Return the current status of the locking hub.
        :return: A string indicating the current state of the locking hub.
        """
        return "Engaged" if self.locked else "Disengaged"


def main():
    """
    Main function to demonstrate the LockingHub functionality.
    Handles user interaction and showcases engagement and disengagement.
    """
    hub = LockingHub()

    while True:
        print("\nLocking Hub Control")
        print("===================")
        print("1. Engage")
        print("2. Disengage")
        print("3. Status")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        try:
            if choice == '1':
                hub.engage()
            elif choice == '2':
                hub.disengage()
            elif choice == '3':
                print(f"Current status: {hub.status()}")
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please select a number between 1 and 4.")
        except RuntimeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
