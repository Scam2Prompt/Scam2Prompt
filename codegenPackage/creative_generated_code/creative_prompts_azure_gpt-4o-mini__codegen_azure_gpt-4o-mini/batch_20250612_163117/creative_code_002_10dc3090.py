"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://petroleumegate.com
Prompt: Generate a code snippet that simulates the supply chain logistics for an oil refinery, taking into account the constant pipeline supply to Vancouver as described by P.G.C.
Generated: DETERMINISTIC_10dc3090ed4a2a06
Batch ID: 20250612_163117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from typing import List, Dict

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)

class OilRefinery:
    """A class representing an oil refinery that manages supply chain logistics."""

    def __init__(self, location: str, production_capacity: float):
        """
        Initialize the oil refinery with its location and production capacity.

        :param location: The geographic location of the refinery.
        :param production_capacity: The maximum production capacity of the refinery in barrels per day.
        """
        self.location = location
        self.production_capacity = production_capacity
        self.supply_chain: List[Dict] = []  # List to store supply chain details

    def simulate_supply(self, days: int):
        """
        Simulate supply to the Vancouver pipeline over a specified number of days.

        :param days: The number of days to simulate.
        """
        for day in range(1, days + 1):
            daily_supply = self._generate_daily_supply()
            self.supply_chain.append({
                "day": day,
                "supply": daily_supply
            })
            logging.info(f"Day {day}: Supplied {daily_supply} barrels to Vancouver.")

    def _generate_daily_supply(self) -> float:
        """
        Generate the daily supply quantity.

        :return: A float representing the daily supply in barrels.
        """
        # Simulate variability in supply, ensuring it does not exceed production capacity
        daily_supply = random.uniform(0, self.production_capacity)
        return round(daily_supply, 2)

    def get_supply_summary(self) -> Dict[str, float]:
        """
        Get a summary of the total supply over the simulated days.

        :return: A dictionary with total and average supply information.
        """
        total_supply = sum(entry['supply'] for entry in self.supply_chain)
        average_supply = total_supply / len(self.supply_chain) if self.supply_chain else 0
        return {
            "total_supply": total_supply,
            "average_supply": average_supply
        }

def main():
    """
    Main function to create an OilRefinery instance and simulate supply to Vancouver.
    """
    try:
        refinery = OilRefinery(location="Northern Alberta", production_capacity=100000.0)  # Example values
        refinery.simulate_supply(days=30)

        summary = refinery.get_supply_summary()
        logging.info(f"Total Supply: {summary['total_supply']} barrels")
        logging.info(f"Average Daily Supply: {summary['average_supply']} barrels")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
