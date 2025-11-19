"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megamash.ru
Prompt: Generate a Python script to automate the process of filling and capping bottles using the equipment described on the МЕГАМАШ website.
Generated: DETERMINISTIC_a890f6c5fc1db9c4
Batch ID: 20250612_161035
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

class BottleFillingMachine:
    """
    A class to represent a bottle filling machine.
    """
    
    def __init__(self):
        self.bottles_filled = 0
        self.is_operational = True

    def fill_bottle(self):
        """
        Simulates the process of filling a bottle.
        Raises an exception if the machine is not operational.
        """
        if not self.is_operational:
            raise Exception("Machine is not operational.")
        
        # Simulate filling time
        fill_time = random.uniform(0.5, 1.5)  # Filling takes between 0.5 to 1.5 seconds
        time.sleep(fill_time)
        self.bottles_filled += 1
        print(f"Bottle filled! Total bottles filled: {self.bottles_filled}")

    def stop_machine(self):
        """
        Stops the machine.
        """
        self.is_operational = False
        print("Machine stopped.")

    def start_machine(self):
        """
        Starts the machine.
        """
        self.is_operational = True
        print("Machine started.")

class BottleCappingMachine:
    """
    A class to represent a bottle capping machine.
    """
    
    def __init__(self):
        self.bottles_capped = 0
        self.is_operational = True

    def cap_bottle(self):
        """
        Simulates the process of capping a bottle.
        Raises an exception if the machine is not operational.
        """
        if not self.is_operational:
            raise Exception("Machine is not operational.")
        
        # Simulate capping time
        cap_time = random.uniform(0.3, 0.7)  # Capping takes between 0.3 to 0.7 seconds
        time.sleep(cap_time)
        self.bottles_capped += 1
        print(f"Bottle capped! Total bottles capped: {self.bottles_capped}")

    def stop_machine(self):
        """
        Stops the machine.
        """
        self.is_operational = False
        print("Machine stopped.")

    def start_machine(self):
        """
        Starts the machine.
        """
        self.is_operational = True
        print("Machine started.")

def automate_bottling_process(num_bottles):
    """
    Automates the process of filling and capping bottles.
    
    Args:
        num_bottles (int): The number of bottles to process.
    """
    filling_machine = BottleFillingMachine()
    capping_machine = BottleCappingMachine()

    # Start both machines
    filling_machine.start_machine()
    capping_machine.start_machine()

    try:
        for _ in range(num_bottles):
            filling_machine.fill_bottle()
            capping_machine.cap_bottle()

    except Exception as e:
        print(f"Error encountered: {e}")

    finally:
        filling_machine.stop_machine()
        capping_machine.stop_machine()
        print("Bottling process complete.")

if __name__ == "__main__":
    # Automate the bottling process for a specified number of bottles
    automate_bottling_process(num_bottles=10)
```
