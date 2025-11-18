"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gominings.net
Prompt: Create a script in Python that simulates the purchase and resale of digital miners on a marketplace, factoring in GoMining's 5% service charge and miner performance metrics.
Generated: DETERMINISTIC_12855567b48af7ef
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class DigitalMiner:
    """Class representing a digital miner with performance metrics."""
    
    def __init__(self, name, hash_rate, price):
        """
        Initializes a DigitalMiner instance.
        
        Args:
            name (str): The name of the miner.
            hash_rate (float): The hash rate of the miner in TH/s.
            price (float): The purchase price of the miner.
        """
        self.name = name
        self.hash_rate = hash_rate
        self.price = price
        self.is_sold = False

    def resale_price(self):
        """Calculates the resale price of the miner after GoMining's service charge."""
        return self.price * 0.95  # Subtract 5% for service charge

    def __str__(self):
        return f"Miner: {self.name}, Hash Rate: {self.hash_rate} TH/s, Price: ${self.price:.2f}"

class Marketplace:
    """Class representing a marketplace for buying and selling digital miners."""
    
    def __init__(self):
        self.inventory = []

    def add_miner(self, miner):
        """Adds a digital miner to the marketplace inventory."""
        self.inventory.append(miner)

    def buy_miner(self, miner_name):
        """
        Simulates purchasing a miner from the marketplace.
        
        Args:
            miner_name (str): The name of the miner to purchase.
        
        Returns:
            DigitalMiner: The purchased miner.
        
        Raises:
            ValueError: If the miner is not found in the inventory.
        """
        for miner in self.inventory:
            if miner.name == miner_name and not miner.is_sold:
                miner.is_sold = True
                return miner
        
        raise ValueError(f"Miner '{miner_name}' not found or already sold.")

    def list_miners(self):
        """Lists all available miners in the marketplace."""
        available_miners = [miner for miner in self.inventory if not miner.is_sold]
        return available_miners

def main():
    """Main function to simulate the purchase and resale of digital miners."""
    # Create a marketplace instance
    marketplace = Marketplace()
    
    # Generate some digital miners and add them to the marketplace
    miners = [
        DigitalMiner("Miner A", 100, 2000.00),
        DigitalMiner("Miner B", 150, 2500.00),
        DigitalMiner("Miner C", 120, 2200.00)
    ]
    
    # Add miners to the marketplace
    for miner in miners:
        marketplace.add_miner(miner)

    # List available miners
    print("Available Miners for Sale:")
    for miner in marketplace.list_miners():
        print(miner)
    
    # Simulate purchasing a miner
    try:
        purchased_miner = marketplace.buy_miner("Miner A")
        print(f"\nPurchased: {purchased_miner}")
    except ValueError as e:
        print(e)

    # Calculate and display resale price
    resale_price = purchased_miner.resale_price()
    print(f"Resale Price of {purchased_miner.name}: ${resale_price:.2f}")

if __name__ == "__main__":
    main()
```
