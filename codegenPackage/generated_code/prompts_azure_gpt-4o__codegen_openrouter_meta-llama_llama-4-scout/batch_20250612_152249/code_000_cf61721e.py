"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Write a Python script to simulate the production workflow of acrylic yarns using state-of-the-art machinery, incorporating parameters like yarn type (grey, dyed, mélange) and production capacity.
Generated: DETERMINISTIC_cf61721e72aef137
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class YarnType(str, Enum):
    """Enum for yarn types."""
    GREY = "grey"
    DYED = "dyed"
    MÉLANGE = "mélange"

class ProductionMachine:
    """Simulates a production machine for acrylic yarns."""

    def __init__(self, capacity: int):
        """
        Initializes a production machine.

        Args:
        - capacity (int): The production capacity of the machine.
        """
        self.capacity = capacity
        self.production_status: Dict[YarnType, int] = {
            YarnType.GREY: 0,
            YarnType.DYED: 0,
            YarnType.MÉLANGE: 0,
        }

    def produce(self, yarn_type: YarnType, quantity: int) -> None:
        """
        Simulates the production of a specific yarn type.

        Args:
        - yarn_type (YarnType): The type of yarn to produce.
        - quantity (int): The quantity of yarn to produce.

        Raises:
        - ValueError: If the quantity exceeds the machine's capacity.
        """
        if quantity > self.capacity:
            raise ValueError("Quantity exceeds machine capacity")

        self.production_status[yarn_type] += quantity

    def get_production_status(self) -> Dict[YarnType, int]:
        """
        Returns the current production status.

        Returns:
        - Dict[YarnType, int]: A dictionary with yarn types as keys and produced quantities as values.
        """
        return self.production_status.copy()

def main() -> None:
    # Create a production machine with a capacity of 1000 units
    machine = ProductionMachine(1000)

    try:
        # Produce 500 units of grey yarn
        machine.produce(YarnType.GREY, 500)

        # Produce 300 units of dyed yarn
        machine.produce(YarnType.DYED, 300)

        # Produce 200 units of mélange yarn
        machine.produce(YarnType.MÉLANGE, 200)

        # Get and print the production status
        production_status = machine.get_production_status()
        print("Production Status:")
        for yarn_type, quantity in production_status.items():
            print(f"{yarn_type}: {quantity}")

        # Attempt to produce more yarn than the machine's capacity
        machine.produce(YarnType.GREY, 600)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
