"""
Generated Code Metadata:
========================
Original URL: https://cemnazmakine.com
Prompt: Describe how to implement a conveyor system for transporting potatoes between washing and frying machines in a production line.
Generated: DETERMINISTIC_0fc569c96ce119cb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ConveyorBelt:
    """
    A class to represent a conveyor belt system for transporting potatoes
    between washing and frying machines in a production line.
    """

    def __init__(self, length: int):
        """
        Initializes the conveyor belt with a specified length.

        :param length: The length of the conveyor belt in meters.
        """
        if length <= 0:
            raise ValueError("Length of the conveyor belt must be a positive integer.")
        self.length = length
        self.potatoes = []

    def add_potato(self, potato: str):
        """
        Adds a potato to the conveyor belt.

        :param potato: The potato to be added.
        """
        if len(self.potatoes) >= self.length:
            raise OverflowError("Conveyor belt is full. Cannot add more potatoes.")
        self.potatoes.append(potato)
        print(f"Added potato: {potato}. Total on belt: {len(self.potatoes)}")

    def remove_potato(self) -> str:
        """
        Removes a potato from the conveyor belt.

        :return: The potato that was removed.
        :raises IndexError: If the conveyor belt is empty.
        """
        if not self.potatoes:
            raise IndexError("Conveyor belt is empty. Cannot remove potatoes.")
        potato = self.potatoes.pop(0)
        print(f"Removed potato: {potato}. Total on belt: {len(self.potatoes)}")
        return potato

    def transport(self):
        """
        Simulates the transportation of potatoes from washing to frying machines.
        """
        print("Starting transportation of potatoes...")
        while self.potatoes:
            self.remove_potato()
        print("All potatoes have been transported.")

def main():
    """
    Main function to demonstrate the conveyor belt system.
    """
    try:
        # Create a conveyor belt with a length of 5
        conveyor = ConveyorBelt(length=5)

        # Add potatoes to the conveyor belt
        conveyor.add_potato("Potato 1")
        conveyor.add_potato("Potato 2")
        conveyor.add_potato("Potato 3")

        # Transport the potatoes to the frying machine
        conveyor.transport()

        # Attempt to remove a potato from an empty conveyor belt
        conveyor.remove_potato()

    except (ValueError, OverflowError, IndexError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
