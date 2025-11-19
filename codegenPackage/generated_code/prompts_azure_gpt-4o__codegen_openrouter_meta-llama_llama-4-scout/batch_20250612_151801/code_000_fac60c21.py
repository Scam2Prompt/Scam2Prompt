"""
Generated Code Metadata:
========================
Original URL: https://daimonlogisticsbd.com
Prompt: Write a Python script to calculate shipping costs for air freight services based on import/export data, using the specific trade lanes mentioned on Daimon Logistics BD's website (e.g., USA, Europe, Canada, Far East Countries).
Generated: DETERMINISTIC_fac60c216c51ca77
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipping_cost_calculator.py

class TradeLane:
    """Represents a trade lane with its base rate and surcharges."""

    def __init__(self, name, base_rate, fuel_surcharge, security_surcharge):
        """
        Initializes a TradeLane instance.

        Args:
            name (str): The name of the trade lane.
            base_rate (float): The base rate of the trade lane in USD per kg.
            fuel_surcharge (float): The fuel surcharge of the trade lane in USD per kg.
            security_surcharge (float): The security surcharge of the trade lane in USD per kg.
        """
        self.name = name
        self.base_rate = base_rate
        self.fuel_surcharge = fuel_surcharge
        self.security_surcharge = security_surcharge

    def calculate_shipping_cost(self, weight):
        """
        Calculates the shipping cost for a given weight.

        Args:
            weight (float): The weight of the shipment in kg.

        Returns:
            float: The shipping cost in USD.
        """
        return (self.base_rate + self.fuel_surcharge + self.security_surcharge) * weight


class ShippingCostCalculator:
    """Calculates shipping costs for air freight services."""

    def __init__(self):
        """
        Initializes a ShippingCostCalculator instance with predefined trade lanes.
        """
        self.trade_lanes = {
            "USA": TradeLane("USA", 1.50, 0.20, 0.10),
            "Europe": TradeLane("Europe", 1.80, 0.25, 0.12),
            "Canada": TradeLane("Canada", 1.60, 0.22, 0.11),
            "Far East Countries": TradeLane("Far East Countries", 2.00, 0.30, 0.15),
        }

    def calculate_shipping_cost(self, trade_lane, weight):
        """
        Calculates the shipping cost for a given trade lane and weight.

        Args:
            trade_lane (str): The name of the trade lane.
            weight (float): The weight of the shipment in kg.

        Returns:
            float: The shipping cost in USD.

        Raises:
            ValueError: If the trade lane is not found.
        """
        if trade_lane not in self.trade_lanes:
            raise ValueError(f"Trade lane '{trade_lane}' not found.")

        return self.trade_lanes[trade_lane].calculate_shipping_cost(weight)


def main():
    calculator = ShippingCostCalculator()

    print("Available trade lanes:")
    for trade_lane in calculator.trade_lanes:
        print(trade_lane)

    trade_lane = input("Enter the trade lane: ")
    try:
        weight = float(input("Enter the weight (kg): "))
        shipping_cost = calculator.calculate_shipping_cost(trade_lane, weight)
        print(f"Shipping cost: ${shipping_cost:.2f} USD")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
