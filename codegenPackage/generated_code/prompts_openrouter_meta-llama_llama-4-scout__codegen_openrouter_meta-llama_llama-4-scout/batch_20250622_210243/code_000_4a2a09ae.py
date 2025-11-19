"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: "Write a Python script to calculate the cost savings of using a logistics and distribution center in Costa Rica, considering factors such as transportation costs and labor costs, as described by PLM."
Generated: DETERMINISTIC_4a2a09ae2bf04510
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# logistics_cost_savings.py

"""
Calculates the cost savings of using a logistics and distribution center in Costa Rica.

This script considers factors such as transportation costs and labor costs, 
as described by Product Lifecycle Management (PLM).
"""

import pandas as pd

class LogisticsCostSavingsCalculator:
    def __init__(self, 
                 transportation_cost_us: float, 
                 labor_cost_us: float, 
                 transportation_cost_cr: float, 
                 labor_cost_cr: float, 
                 annual_volume: int):
        """
        Initializes the calculator with costs and volume.

        Args:
        - transportation_cost_us (float): Transportation cost in the US.
        - labor_cost_us (float): Labor cost in the US.
        - transportation_cost_cr (float): Transportation cost in Costa Rica.
        - labor_cost_cr (float): Labor cost in Costa Rica.
        - annual_volume (int): Annual volume of shipments.
        """
        self.transportation_cost_us = transportation_cost_us
        self.labor_cost_us = labor_cost_us
        self.transportation_cost_cr = transportation_cost_cr
        self.labor_cost_cr = labor_cost_cr
        self.annual_volume = annual_volume

    def calculate_total_cost_us(self) -> float:
        """
        Calculates the total cost in the US.

        Returns:
        - float: Total cost in the US.
        """
        return (self.transportation_cost_us + self.labor_cost_us) * self.annual_volume

    def calculate_total_cost_cr(self) -> float:
        """
        Calculates the total cost in Costa Rica.

        Returns:
        - float: Total cost in Costa Rica.
        """
        return (self.transportation_cost_cr + self.labor_cost_cr) * self.annual_volume

    def calculate_cost_savings(self) -> float:
        """
        Calculates the cost savings of using a logistics and distribution center in Costa Rica.

        Returns:
        - float: Cost savings.
        """
        total_cost_us = self.calculate_total_cost_us()
        total_cost_cr = self.calculate_total_cost_cr()
        return (total_cost_us - total_cost_cr) / total_cost_us * 100


def main():
    try:
        # Example usage
        calculator = LogisticsCostSavingsCalculator(
            transportation_cost_us=1000.0, 
            labor_cost_us=5000.0, 
            transportation_cost_cr=800.0, 
            labor_cost_cr=3000.0, 
            annual_volume=10000
        )

        total_cost_us = calculator.calculate_total_cost_us()
        total_cost_cr = calculator.calculate_total_cost_cr()
        cost_savings = calculator.calculate_cost_savings()

        print(f"Total cost in the US: ${total_cost_us:,.2f}")
        print(f"Total cost in Costa Rica: ${total_cost_cr:,.2f}")
        print(f"Cost savings: {cost_savings:,.2f}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
