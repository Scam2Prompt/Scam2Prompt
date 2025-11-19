"""
Generated Code Metadata:
========================
Original URL: https://aayraint.com
Prompt: Write Python code to simulate the cutting of cardboard tubes into desired sizes using a fully automatic PLC-controlled machine, referencing the features of the Paper Core Cutting Machine described on the Aayra International website.
Generated: DETERMINISTIC_c8df60d70b627b2a
Batch ID: 20250612_153225
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

class CardboardTube:
    """Class representing a cardboard tube."""
    
    def __init__(self, length):
        """Initialize the cardboard tube with a specified length."""
        self.length = length

    def cut(self, cut_length):
        """Cut the tube into a specified length.
        
        Args:
            cut_length (int): The length to cut the tube.
        
        Returns:
            CardboardTube: A new CardboardTube object with the cut length.
            None: If the cut length is greater than the tube length.
        """
        if cut_length > self.length:
            raise ValueError("Cut length cannot be greater than tube length.")
        self.length -= cut_length
        return CardboardTube(cut_length)

class CuttingMachine:
    """Class representing the cutting machine."""
    
    def __init__(self):
        """Initialize the cutting machine."""
        self.tube = None

    def load_tube(self, length):
        """Load a cardboard tube into the machine.
        
        Args:
            length (int): The length of the tube to load.
        """
        self.tube = CardboardTube(length)
        print(f"Loaded tube of length: {self.tube.length}")

    def cut_tube(self, cut_length):
        """Cut the loaded tube into the desired length.
        
        Args:
            cut_length (int): The length to cut the tube.
        
        Returns:
            CardboardTube: The cut tube if successful.
            None: If no tube is loaded or cut fails.
        """
        if self.tube is None:
            print("Error: No tube loaded.")
            return None
        
        try:
            cut_tube = self.tube.cut(cut_length)
            print(f"Cut tube of length: {cut_tube.length}. Remaining tube length: {self.tube.length}.")
            return cut_tube
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def simulate_cutting_process(self, cut_lengths):
        """Simulate the cutting process for a list of desired cut lengths.
        
        Args:
            cut_lengths (list): A list of lengths to cut the tube into.
        """
        for length in cut_lengths:
            time.sleep(random.uniform(0.5, 1.5))  # Simulate cutting time
            self.cut_tube(length)

def main():
    """Main function to run the cutting machine simulation."""
    machine = CuttingMachine()
    
    # Load a tube of length 100
    machine.load_tube(100)
    
    # Define desired cut lengths
    desired_cuts = [20, 30, 25, 15, 10]  # Example cut lengths
    
    # Simulate the cutting process
    machine.simulate_cutting_process(desired_cuts)

if __name__ == "__main__":
    main()
```
