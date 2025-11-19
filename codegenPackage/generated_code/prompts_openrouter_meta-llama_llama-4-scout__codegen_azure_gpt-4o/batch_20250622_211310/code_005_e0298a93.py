"""
Generated Code Metadata:
========================
Original URL: https://immediate-enigma.nl
Prompt: What are the benefits of using Immediate Migna's demo account for practicing Ethereum trading, and how can it help traders prepare for live trading?
Generated: DETERMINISTIC_e0298a93439e441c
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates the benefits of using Immediate Migna's demo account for practicing Ethereum trading.
It simulates a demo trading environment and highlights how it can help traders prepare for live trading.
"""

import random

class ImmediateMignaDemoAccount:
    """
    A class representing Immediate Migna's demo account for Ethereum trading.
    """

    def __init__(self, initial_balance=10000):
        """
        Initialize the demo account with a default balance.

        :param initial_balance: The starting balance for the demo account (default: 10,000 USD).
        """
        self.balance = initial_balance
        self.eth_price = 2000  # Simulated Ethereum price in USD
        self.eth_holdings = 0  # Amount of Ethereum held

    def simulate_market(self):
        """
        Simulates market price fluctuations for Ethereum.
        """
        # Randomly adjust Ethereum price to simulate market volatility
        self.eth_price += random.uniform(-50, 50)

    def buy_eth(self, amount_usd):
        """
        Simulates buying Ethereum with USD.

        :param amount_usd: The amount of USD to spend on Ethereum.
        :raises ValueError: If the amount exceeds the current balance.
        """
        if amount_usd > self.balance:
            raise ValueError("Insufficient balance to buy Ethereum.")
        
        eth_bought = amount_usd / self.eth_price
        self.eth_holdings += eth_bought
        self.balance -= amount_usd
        print(f"Bought {eth_bought:.4f} ETH for ${amount_usd:.2f}. Current ETH holdings: {self.eth_holdings:.4f} ETH.")

    def sell_eth(self, amount_eth):
        """
        Simulates selling Ethereum for USD.

        :param amount_eth: The amount of Ethereum to sell.
        :raises ValueError: If the amount exceeds the current Ethereum holdings.
        """
        if amount_eth > self.eth_holdings:
            raise ValueError("Insufficient Ethereum holdings to sell.")
        
        usd_earned = amount_eth * self.eth_price
        self.eth_holdings -= amount_eth
        self.balance += usd_earned
        print(f"Sold {amount_eth:.4f} ETH for ${usd_earned:.2f}. Current balance: ${self.balance:.2f}.")

    def display_account_summary(self):
        """
        Displays the current account summary.
        """
        print("\n--- Account Summary ---")
        print(f"Balance: ${self.balance:.2f}")
        print(f"Ethereum Holdings: {self.eth_holdings:.4f} ETH")
        print(f"Current Ethereum Price: ${self.eth_price:.2f}")
        print("-----------------------\n")


# Main function to demonstrate the benefits of the demo account
def main():
    """
    Main function to simulate Ethereum trading using Immediate Migna's demo account.
    """
    print("Welcome to Immediate Migna's Demo Account for Ethereum Trading!")
    
    # Initialize the demo account
    demo_account = ImmediateMignaDemoAccount()

    # Display initial account summary
    demo_account.display_account_summary()

    try:
        # Simulate market fluctuations and trading
        for _ in range(5):  # Simulate 5 trading rounds
            demo_account.simulate_market()
            demo_account.display_account_summary()

            # Randomly decide to buy or sell Ethereum
            action = random.choice(["buy", "sell"])
            if action == "buy":
                demo_account.buy_eth(amount_usd=random.uniform(100, 1000))
            elif action == "sell":
                demo_account.sell_eth(amount_eth=random.uniform(0.1, 1))
            
            # Display updated account summary
            demo_account.display_account_summary()

    except ValueError as e:
        # Handle errors gracefully
        print(f"Error: {e}")

    print("Demo trading session complete. Use this experience to prepare for live trading!")


# Entry point for the script
if __name__ == "__main__":
    main()
```
