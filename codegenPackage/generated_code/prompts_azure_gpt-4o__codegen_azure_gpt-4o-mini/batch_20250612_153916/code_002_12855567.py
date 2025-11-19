"""
Generated Code Metadata:
========================
Original URL: https://gominings.net
Prompt: Create a script in Python that simulates the purchase and resale of digital miners on a marketplace, factoring in GoMining's 5% service charge and miner performance metrics.
Generated: DETERMINISTIC_12855567b48af7ef
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class DigitalMiner:
    """
    A class to represent a digital miner with performance metrics.
    """
    def __init__(self, name, hash_rate, power_consumption, purchase_price):
        """
        Initializes a new DigitalMiner instance.

        :param name: str - The name of the miner.
        :param hash_rate: float - The hash rate of the miner in TH/s.
        :param power_consumption: float - The power consumption of the miner in watts.
        :param purchase_price: float - The purchase price of the miner in USD.
        """
        self.name = name
        self.hash_rate = hash_rate
        self.power_consumption = power_consumption
        self.purchase_price = purchase_price

    def calculate_profitability(self, electricity_cost_per_kwh):
        """
        Calculates the profitability of the miner based on electricity costs.

        :param electricity_cost_per_kwh: float - The cost of electricity per kWh in USD.
        :return: float - The estimated monthly profit in USD.
        """
        monthly_power_cost = (self.power_consumption / 1000) * 24 * 30 * electricity_cost_per_kwh
        monthly_revenue = self.hash_rate * 0.00000001 * 30 * 24 * 100  # Example revenue calculation
        return monthly_revenue - monthly_power_cost

class Marketplace:
    """
    A class to represent a marketplace for buying and selling digital miners.
    """
    SERVICE_CHARGE_RATE = 0.05  # 5% service charge

    def __init__(self):
        self.inventory = []

    def add_miner(self, miner):
        """
        Adds a digital miner to the marketplace inventory.

        :param miner: DigitalMiner - The miner to be added.
        """
        self.inventory.append(miner)

    def purchase_miner(self, miner):
        """
        Simulates the purchase of a miner from the marketplace.

        :param miner: DigitalMiner - The miner to be purchased.
        :return: float - The total cost including service charge.
        """
        total_cost = miner.purchase_price * (1 + self.SERVICE_CHARGE_RATE)
        return total_cost

    def resale_miner(self, miner):
        """
        Simulates the resale of a miner on the marketplace.

        :param miner: DigitalMiner - The miner to be resold.
        :return: float - The resale price after deducting service charge.
        """
        resale_price = miner.purchase_price * (1 - self.SERVICE_CHARGE_RATE)
        return resale_price

def main():
    """
    Main function to simulate the purchase and resale of digital miners.
    """
    # Create a marketplace instance
    marketplace = Marketplace()

    # Create some digital miners
    miner1 = DigitalMiner("Miner A", 100, 1500, 3000)
    miner2 = DigitalMiner("Miner B", 120, 1600, 3500)

    # Add miners to the marketplace
    marketplace.add_miner(miner1)
    marketplace.add_miner(miner2)

    # Simulate purchasing a miner
    try:
        purchase_cost = marketplace.purchase_miner(miner1)
        print(f"Purchased {miner1.name} for ${purchase_cost:.2f}")
    except Exception as e:
        print(f"Error purchasing miner: {e}")

    # Simulate reselling a miner
    try:
        resale_price = marketplace.resale_miner(miner1)
        print(f"Resold {miner1.name} for ${resale_price:.2f}")
    except Exception as e:
        print(f"Error reselling miner: {e}")

    # Calculate profitability
    electricity_cost_per_kwh = 0.12  # Example electricity cost
    profitability = miner1.calculate_profitability(electricity_cost_per_kwh)
    print(f"Estimated monthly profit for {miner1.name}: ${profitability:.2f}")

if __name__ == "__main__":
    main()
```
