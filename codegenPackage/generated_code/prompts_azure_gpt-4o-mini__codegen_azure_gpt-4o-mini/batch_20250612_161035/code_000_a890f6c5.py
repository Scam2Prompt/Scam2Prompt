"""
Generated Code Metadata:
========================
Original URL: https://megamash.ru
Prompt: Generate a Python script to automate the process of filling and capping bottles using the equipment described on the МЕГАМАШ website.
Generated: DETERMINISTIC_a890f6c5fc1db9c4
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random

class BottleFillingMachine:
    def __init__(self, capacity):
        """
        Initialize the bottle filling machine with a specified capacity.
        
        :param capacity: Maximum capacity of the bottle in liters.
        """
        self.capacity = capacity
        self.current_fill_level = 0.0

    def fill_bottle(self):
        """
        Simulate the filling of a bottle. Fills the bottle to its maximum capacity.
        
        :raises ValueError: If the bottle is already full.
        """
        if self.current_fill_level >= self.capacity:
            raise ValueError("Bottle is already full.")
        
        fill_amount = random.uniform(0.1, 0.5)  # Fill between 0.1 to 0.5 liters
        self.current_fill_level += fill_amount
        
        if self.current_fill_level > self.capacity:
            self.current_fill_level = self.capacity
        
        print(f"Filling bottle: {fill_amount:.2f}L filled. Current level: {self.current_fill_level:.2f}L")
        time.sleep(1)  # Simulate time taken to fill

class BottleCappingMachine:
    def cap_bottle(self):
        """
        Simulate the capping of a bottle.
        
        :raises RuntimeError: If the bottle is not filled.
        """
        if random.choice([True, False]):  # Simulate a random capping failure
            raise RuntimeError("Capping failed due to machine error.")
        
        print("Bottle capped successfully.")
        time.sleep(0.5)  # Simulate time taken to cap

class BottleProductionLine:
    def __init__(self, bottle_capacity):
        """
        Initialize the production line with a bottle filling and capping machine.
        
        :param bottle_capacity: Maximum capacity of the bottle in liters.
        """
        self.filling_machine = BottleFillingMachine(bottle_capacity)
        self.capping_machine = BottleCappingMachine()

    def process_bottle(self):
        """
        Process a single bottle by filling and capping it.
        """
        try:
            self.filling_machine.fill_bottle()
            self.capping_machine.cap_bottle()
            print("Bottle processing completed successfully.\n")
        except (ValueError, RuntimeError) as e:
            print(f"Error during bottle processing: {e}")

def main():
    """
    Main function to run the bottle production line.
    """
    bottle_capacity = 2.0  # Example bottle capacity in liters
    production_line = BottleProductionLine(bottle_capacity)

    # Simulate processing of 5 bottles
    for _ in range(5):
        production_line.process_bottle()

if __name__ == "__main__":
    main()
```
