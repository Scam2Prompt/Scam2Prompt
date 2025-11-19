"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cemnazmakine.com
Prompt: Write a Python script that simulates the operation of a potato blanching machine in a processing facility.
Generated: DETERMINISTIC_576e75ce1bebf474
Batch ID: 20250612_162051
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

class Potato:
    """Class representing a potato with relevant attributes."""
    
    def __init__(self, id):
        self.id = id
        self.is_blanched = False

    def blanch(self):
        """Simulate the blanching process for the potato."""
        self.is_blanched = True


class BlanchingMachine:
    """Class representing a potato blanching machine."""
    
    def __init__(self, blanch_time=5):
        """
        Initialize the blanching machine with a specified blanching time.
        
        :param blanch_time: Time (in seconds) required to blanch a potato.
        """
        self.blanch_time = blanch_time
        self.potatoes_processed = 0

    def process_potato(self, potato):
        """
        Process a single potato through the blanching machine.
        
        :param potato: Potato object to be blanched.
        """
        if not isinstance(potato, Potato):
            raise TypeError("Expected a Potato instance.")
        
        print(f"Starting blanching for potato ID: {potato.id}")
        time.sleep(self.blanch_time)  # Simulate the blanching time
        potato.blanch()
        self.potatoes_processed += 1
        print(f"Finished blanching for potato ID: {potato.id}")


class ProcessingFacility:
    """Class simulating a potato processing facility with a blanching machine."""
    
    def __init__(self, machine):
        """
        Initialize the processing facility with a blanching machine.
        
        :param machine: BlanchingMachine instance to be used.
        """
        if not isinstance(machine, BlanchingMachine):
            raise TypeError("Expected a BlanchingMachine instance.")
        
        self.machine = machine

    def run(self, num_potatoes):
        """
        Simulate the processing of a number of potatoes through the blanching machine.
        
        :param num_potatoes: Number of potatoes to process.
        """
        if num_potatoes <= 0:
            raise ValueError("Number of potatoes must be a positive integer.")
        
        potatoes = [Potato(i) for i in range(num_potatoes)]
        
        for potato in potatoes:
            try:
                self.machine.process_potato(potato)
            except Exception as e:
                print(f"Error processing potato ID: {potato.id}. Error: {e}")
                continue


if __name__ == "__main__":
    try:
        blanching_machine = BlanchingMachine(blanch_time=random.randint(3, 8))
        facility = ProcessingFacility(blanching_machine)
        facility.run(num_potatoes=10)
    except Exception as e:
        print(f"An error occurred in the processing facility: {e}")
```
