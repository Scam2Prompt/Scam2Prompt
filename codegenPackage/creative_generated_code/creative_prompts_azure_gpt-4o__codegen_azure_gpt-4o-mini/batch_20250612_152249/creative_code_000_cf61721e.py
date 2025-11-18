"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramjiacro.com
Prompt: Write a Python script to simulate the production workflow of acrylic yarns using state-of-the-art machinery, incorporating parameters like yarn type (grey, dyed, mélange) and production capacity.
Generated: DETERMINISTIC_cf61721e72aef137
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from enum import Enum

class YarnType(Enum):
    GREY = "Grey"
    DYED = "Dyed"
    MELANGE = "Mélange"

class ProductionMachine:
    """
    A class representing a production machine for acrylic yarns.
    """

    def __init__(self, capacity):
        """
        Initializes the production machine with a specified capacity.

        Args:
            capacity (int): The maximum production capacity of the machine per hour.
        """
        self.capacity = capacity
        self.production_count = 0

    def produce_yarn(self, yarn_type, quantity):
        """
        Simulates the production of yarn.

        Args:
            yarn_type (YarnType): The type of yarn to produce.
            quantity (int): The quantity of yarn to produce.

        Returns:
            bool: True if production was successful, False otherwise.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        if self.production_count + quantity > self.capacity:
            print(f"Cannot produce {quantity} units of {yarn_type.value}. Capacity exceeded.")
            return False
        
        self.production_count += quantity
        print(f"Produced {quantity} units of {yarn_type.value}. Total produced: {self.production_count}.")
        return True

    def reset_production(self):
        """Resets the production count to zero."""
        self.production_count = 0
        print("Production count has been reset.")

def simulate_production_workflow(machine_capacity, production_schedule):
    """
    Simulates the production workflow of acrylic yarns.

    Args:
        machine_capacity (int): The capacity of the production machine.
        production_schedule (list of tuple): Each tuple contains (YarnType, quantity) to produce.
    """
    machine = ProductionMachine(machine_capacity)

    for yarn_type, quantity in production_schedule:
        try:
            machine.produce_yarn(yarn_type, quantity)
        except ValueError as e:
            print(f"Error during production: {e}")

if __name__ == "__main__":
    # Example production schedule: [(YarnType, quantity), ...]
    production_schedule = [
        (YarnType.GREY, 100),
        (YarnType.DYED, 150),
        (YarnType.MELANGE, 50),
        (YarnType.GREY, 200),  # This may exceed capacity based on machine settings
    ]

    # Set the production machine capacity
    MACHINE_CAPACITY = 300

    # Simulate the production workflow
    simulate_production_workflow(MACHINE_CAPACITY, production_schedule)
```
