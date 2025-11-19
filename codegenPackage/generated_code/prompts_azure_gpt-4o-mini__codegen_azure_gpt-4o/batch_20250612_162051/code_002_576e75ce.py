"""
Generated Code Metadata:
========================
Original URL: https://cemnazmakine.com
Prompt: Write a Python script that simulates the operation of a potato blanching machine in a processing facility.
Generated: DETERMINISTIC_576e75ce1bebf474
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time

class PotatoBlanchingMachine:
    """
    A class to simulate the operation of a potato blanching machine in a processing facility.
    """

    def __init__(self, blanching_time=5, max_capacity=10):
        """
        Initialize the blanching machine with default settings.

        :param blanching_time: Time (in seconds) required to blanch potatoes.
        :param max_capacity: Maximum number of potatoes the machine can process at once.
        """
        self.blanching_time = blanching_time
        self.max_capacity = max_capacity
        self.current_batch = []

    def load_potatoes(self, potatoes):
        """
        Load potatoes into the machine.

        :param potatoes: List of potatoes to be loaded.
        :raises ValueError: If the number of potatoes exceeds the machine's capacity.
        """
        if len(potatoes) > self.max_capacity:
            raise ValueError(f"Cannot load more than {self.max_capacity} potatoes at once.")
        self.current_batch = potatoes
        print(f"Loaded {len(potatoes)} potatoes into the machine.")

    def blanch_potatoes(self):
        """
        Simulate the blanching process.

        :raises RuntimeError: If no potatoes are loaded in the machine.
        """
        if not self.current_batch:
            raise RuntimeError("No potatoes loaded in the machine to blanch.")
        
        print("Starting blanching process...")
        time.sleep(self.blanching_time)  # Simulate blanching time
        print("Blanching complete.")
        self.current_batch = []  # Clear the batch after blanching

    def unload_potatoes(self):
        """
        Unload the blanched potatoes from the machine.

        :raises RuntimeError: If no potatoes are available to unload.
        """
        if not self.current_batch:
            raise RuntimeError("No potatoes to unload. The machine is empty.")
        
        print(f"Unloading {len(self.current_batch)} blanched potatoes.")
        self.current_batch = []

def main():
    """
    Main function to simulate the operation of the potato blanching machine.
    """
    try:
        # Create an instance of the blanching machine
        machine = PotatoBlanchingMachine(blanching_time=3, max_capacity=5)

        # Load potatoes into the machine
        potatoes = ["Potato1", "Potato2", "Potato3", "Potato4", "Potato5"]
        machine.load_potatoes(potatoes)

        # Start the blanching process
        machine.blanch_potatoes()

        # Unload the blanched potatoes
        machine.unload_potatoes()

    except ValueError as ve:
        print(f"Error: {ve}")
    except RuntimeError as re:
        print(f"Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
