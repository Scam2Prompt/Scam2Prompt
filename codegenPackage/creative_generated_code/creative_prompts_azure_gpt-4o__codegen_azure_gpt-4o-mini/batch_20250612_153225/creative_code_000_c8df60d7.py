"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aayraint.com
Prompt: Write Python code to simulate the cutting of cardboard tubes into desired sizes using a fully automatic PLC-controlled machine, referencing the features of the Paper Core Cutting Machine described on the Aayra International website.
Generated: DETERMINISTIC_c8df60d70b627b2a
Batch ID: 20250612_153225
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

class CardboardTube:
    """Class representing a cardboard tube to be cut."""
    
    def __init__(self, length):
        self.length = length  # Length of the cardboard tube in centimeters

class CuttingMachine:
    """Class representing a fully automatic cutting machine."""
    
    def __init__(self):
        self.is_operational = True  # Status of the machine
    
    def cut_tube(self, tube, desired_length):
        """Cuts the cardboard tube to the desired length.
        
        Args:
            tube (CardboardTube): The cardboard tube to be cut.
            desired_length (float): Desired length of the cut piece.
        
        Returns:
            float: Length of the remaining piece after cutting.
        """
        if not self.is_operational:
            raise RuntimeError("Cutting machine is not operational.")
        
        if desired_length <= 0:
            raise ValueError("Desired length must be greater than 0.")
        
        if desired_length > tube.length:
            raise ValueError("Desired length cannot be greater than the tube length.")
        
        # Simulate cutting process
        time.sleep(random.uniform(0.5, 1.5))  # Simulate time taken for cutting
        
        remaining_length = tube.length - desired_length
        print(f"Cutting {desired_length} cm from a {tube.length} cm tube.")
        print(f"Remaining tube length: {remaining_length} cm.")
        
        return remaining_length

    def shutdown(self):
        """Shuts down the machine safely."""
        print("Shutting down the cutting machine.")
        self.is_operational = False

    def start(self):
        """Starts the machine for operation."""
        print("Starting the cutting machine.")
        self.is_operational = True


def main():
    """Main function to simulate the cutting of cardboard tubes."""
    # Initialize the cutting machine
    machine = CuttingMachine()
    machine.start()
    
    # Example tubes to cut
    tubes = [CardboardTube(length=random.randint(50, 150)) for _ in range(5)]
    
    # Define desired lengths for cuts
    desired_lengths = [random.uniform(10, 30) for _ in range(5)]
    
    for tube, desired_length in zip(tubes, desired_lengths):
        try:
            remaining_length = machine.cut_tube(tube, desired_length)
        except (RuntimeError, ValueError) as e:
            print(f"Error while cutting: {e}")
    
    # Shutdown the machine
    machine.shutdown()

if __name__ == "__main__":
    main()
```
