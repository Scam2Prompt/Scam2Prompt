"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Write a program to compare the cost and delivery time between air freight and ocean freight for Uniair Cargo's logistics services.
Generated: DETERMINISTIC_a3adc8cee54f640e
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, Tuple

class FreightComparison:
    def __init__(self, air_freight_cost: float, air_freight_time: float,
                 ocean_freight_cost: float, ocean_freight_time: float):
        """
        Initializes the FreightComparison with cost and time for both air and ocean freight.

        :param air_freight_cost: Cost of air freight
        :param air_freight_time: Delivery time for air freight (in hours)
        :param ocean_freight_cost: Cost of ocean freight
        :param ocean_freight_time: Delivery time for ocean freight (in days)
        """
        self.air_freight_cost = air_freight_cost
        self.air_freight_time = air_freight_time
        self.ocean_freight_cost = ocean_freight_cost
        self.ocean_freight_time = ocean_freight_time

    def compare(self) -> Dict[str, str]:
        """
        Compares the cost and delivery time between air freight and ocean freight.

        :return: Dictionary containing the comparison results
        """
        comparison_result = {
            "Cost": self._compare_cost(),
            "Delivery Time": self._compare_delivery_time()
        }
        return comparison_result

    def _compare_cost(self) -> str:
        """
        Compares the costs of air and ocean freight.

        :return: Result of cost comparison
        """
        if self.air_freight_cost < self.ocean_freight_cost:
            return "Air freight is cheaper."
        elif self.air_freight_cost > self.ocean_freight_cost:
            return "Ocean freight is cheaper."
        else:
            return "Both air and ocean freight costs are the same."

    def _compare_delivery_time(self) -> str:
        """
        Compares the delivery times of air and ocean freight.

        :return: Result of delivery time comparison
        """
        ocean_freight_time_hours = self.ocean_freight_time * 24  # Convert days to hours
        if self.air_freight_time < ocean_freight_time_hours:
            return "Air freight is faster."
        elif self.air_freight_time > ocean_freight_time_hours:
            return "Ocean freight is faster."
        else:
            return "Both air and ocean freight have the same delivery time."

def main():
    # Example data for Uniair Cargo's logistics services
    air_freight_cost = 1200.0  # Cost in currency units
    air_freight_time = 5.0      # Time in hours
    ocean_freight_cost = 800.0   # Cost in currency units
    ocean_freight_time = 10.0     # Time in days

    # Create an instance of FreightComparison
    freight_comparison = FreightComparison(air_freight_cost, air_freight_time,
                                           ocean_freight_cost, ocean_freight_time)

    # Perform the comparison
    try:
        result = freight_comparison.compare()
        print(json.dumps(result, indent=4))  # Pretty-print the results
    except Exception as e:
        print(f"An error occurred during comparison: {e}")

if __name__ == "__main__":
    main()
```
