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
# digital_miner_marketplace.py

class DigitalMiner:
    """Represents a digital miner with its performance metrics."""

    def __init__(self, name, hash_rate, power_consumption, cost):
        """
        Initializes a DigitalMiner object.

        Args:
            name (str): The name of the miner.
            hash_rate (float): The hash rate of the miner in TH/s.
            power_consumption (float): The power consumption of the miner in W.
            cost (float): The cost of the miner in USD.
        """
        self.name = name
        self.hash_rate = hash_rate
        self.power_consumption = power_consumption
        self.cost = cost

class Marketplace:
    """Simulates a marketplace for buying and selling digital miners."""

    def __init__(self):
        """Initializes a Marketplace object."""
        self.service_charge = 0.05  # 5% service charge

    def buy_miner(self, miner, buyer_balance):
        """
        Buys a digital miner from the marketplace.

        Args:
            miner (DigitalMiner): The miner to buy.
            buyer_balance (float): The buyer's current balance.

        Returns:
            tuple: A tuple containing the updated buyer balance and the purchased miner.
        """
        if buyer_balance < miner.cost:
            raise ValueError("Buyer has insufficient balance")

        # Apply service charge
        total_cost = miner.cost * (1 + self.service_charge)

        # Check if buyer has enough balance after service charge
        if buyer_balance < total_cost:
            raise ValueError("Buyer has insufficient balance after service charge")

        updated_balance = buyer_balance - total_cost
        return updated_balance, miner

    def sell_miner(self, miner, seller_balance, resale_price):
        """
        Sells a digital miner on the marketplace.

        Args:
            miner (DigitalMiner): The miner to sell.
            seller_balance (float): The seller's current balance.
            resale_price (float): The resale price of the miner.

        Returns:
            tuple: A tuple containing the updated seller balance and the resale price.
        """
        # Apply service charge
        total_resale_price = resale_price * (1 - self.service_charge)

        updated_balance = seller_balance + total_resale_price
        return updated_balance, total_resale_price

def main():
    # Create a marketplace
    marketplace = Marketplace()

    # Create a digital miner
    miner = DigitalMiner("Antminer S19", 95, 3250, 2000)

    # Buy the miner
    buyer_balance = 10000
    try:
        buyer_balance, purchased_miner = marketplace.buy_miner(miner, buyer_balance)
        print(f"Bought {purchased_miner.name} for ${purchased_miner.cost * (1 + marketplace.service_charge):.2f}")
        print(f"Updated buyer balance: ${buyer_balance:.2f}")
    except ValueError as e:
        print(e)

    # Sell the miner
    seller_balance = buyer_balance
    resale_price = 2500
    try:
        seller_balance, resale_price_after_charge = marketplace.sell_miner(purchased_miner, seller_balance, resale_price)
        print(f"Sold {purchased_miner.name} for ${resale_price:.2f} (resale price after charge: ${resale_price_after_charge:.2f})")
        print(f"Updated seller balance: ${seller_balance:.2f}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
```
