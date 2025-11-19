"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cemnazmakine.com
Prompt: Generate a code snippet for a system that automates the process of washing and peeling potatoes using industrial machines.
Generated: DETERMINISTIC_6c3368847607d18c
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

class PotatoProcessingMachine:
    """
    Represents an industrial machine that automates washing and peeling potatoes.
    """

    def __init__(self):
        """
        Initialize the machine with its operational state.
        """
        self.is_washing = False  # Tracks if the machine is currently washing
        self.is_peeling = False  # Tracks if the machine is currently peeling
        self.potatoes_ready = 0  # Count of potatoes processed

    def wash_potatoes(self, quantity):
        """
        Wash the given quantity of potatoes.
        
        :param quantity: int - Number of potatoes to wash
        """
        if quantity <= 0:
            raise ValueError("Quantity of potatoes to wash must be greater than zero.")

        self.is_washing = True
        print(f"Starting to wash {quantity} potatoes...")
        time.sleep(2)  # Simulate washing time
        self.is_washing = False
        print(f"Finished washing {quantity} potatoes.")

    def peel_potatoes(self, quantity):
        """
        Peel the given quantity of potatoes.
        
        :param quantity: int - Number of potatoes to peel
        """
        if quantity <= 0:
            raise ValueError("Quantity of potatoes to peel must be greater than zero.")

        self.is_peeling = True
        print(f"Starting to peel {quantity} potatoes...")
        time.sleep(3)  # Simulate peeling time
        self.is_peeling = False
        self.potatoes_ready += quantity
        print(f"Finished peeling {quantity} potatoes.")

    def process_potatoes(self, quantity):
        """
        Automates the process of washing and peeling potatoes.
        
        :param quantity: int - Number of potatoes to process
        """
        try:
            print(f"Processing {quantity} potatoes...")
            self.wash_potatoes(quantity)
            self.peel_potatoes(quantity)
            print(f"All {quantity} potatoes processed successfully! Ready potatoes: {self.potatoes_ready}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    machine = PotatoProcessingMachine()
    machine.process_potatoes(5)
```
