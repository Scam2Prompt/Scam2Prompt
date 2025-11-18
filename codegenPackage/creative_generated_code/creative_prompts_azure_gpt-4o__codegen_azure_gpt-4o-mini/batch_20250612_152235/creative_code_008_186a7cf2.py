"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-gmt-marketplace.pages.dev
Prompt: Write a function to calculate the total cost of ownership for miners purchased from GoMining, including initial price and estimated energy consumption.
Generated: DETERMINISTIC_186a7cf2e2b2c2ea
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Miner:
    """
    Represents a mining hardware unit with initial price and energy consumption.
    """

    def __init__(self, initial_price: float, energy_consumption_kwh: float, operating_days: int, energy_cost_per_kwh: float):
        """
        Initializes the Miner object with initial price, energy consumption, operating days, and energy cost.

        :param initial_price: The initial purchase price of the miner in dollars.
        :param energy_consumption_kwh: The energy consumption of the miner in kilowatt-hours per day.
        :param operating_days: The number of days the miner will be operated.
        :param energy_cost_per_kwh: The cost of energy per kilowatt-hour in dollars.
        """
        if initial_price < 0 or energy_consumption_kwh < 0 or operating_days < 0 or energy_cost_per_kwh < 0:
            raise ValueError("All input values must be non-negative.")

        self.initial_price = initial_price
        self.energy_consumption_kwh = energy_consumption_kwh
        self.operating_days = operating_days
        self.energy_cost_per_kwh = energy_cost_per_kwh

    def calculate_energy_cost(self) -> float:
        """
        Calculates the total energy cost over the specified operating days.

        :return: The total energy cost in dollars.
        """
        total_energy_cost = self.energy_consumption_kwh * self.operating_days * self.energy_cost_per_kwh
        return total_energy_cost

    def total_cost_of_ownership(self) -> float:
        """
        Calculates the total cost of ownership for the miner, which includes
        the initial price and the estimated energy costs.

        :return: The total cost of ownership in dollars.
        """
        total_energy_cost = self.calculate_energy_cost()
        total_cost = self.initial_price + total_energy_cost
        return total_cost


# Example usage:
def main():
    try:
        # Create a Miner instance
        miner = Miner(initial_price=3000.00, energy_consumption_kwh=1.5, operating_days=30, energy_cost_per_kwh=0.10)

        # Calculate total cost of ownership
        total_cost = miner.total_cost_of_ownership()
        print(f"Total Cost of Ownership: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
