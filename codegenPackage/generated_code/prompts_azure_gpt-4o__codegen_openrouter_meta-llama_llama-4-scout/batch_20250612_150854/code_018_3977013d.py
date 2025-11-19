"""
Generated Code Metadata:
========================
Original URL: https://immediatepeak.nl
Prompt: Create a Python program to simulate risk scenarios in cryptocurrency trading, incorporating Immediate Peak's emphasis on understanding inherent risks.
Generated: DETERMINISTIC_3977013d1a4652ae
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class TradingPlatform:
    """
    Simulates a cryptocurrency trading platform.
    """

    def __init__(self, balance=10000):
        """
        Initializes the trading platform with a given balance.

        Args:
            balance (float, optional): Initial balance. Defaults to 10000.
        """
        self.balance = balance
        self.portfolio = {}

    def deposit(self, amount):
        """
        Deposits funds into the trading platform.

        Args:
            amount (float): Amount to deposit.

        Raises:
            ValueError: If deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws funds from the trading platform.

        Args:
            amount (float): Amount to withdraw.

        Raises:
            ValueError: If withdrawal amount is negative or exceeds balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def buy(self, cryptocurrency, amount):
        """
        Buys a cryptocurrency.

        Args:
            cryptocurrency (str): Name of the cryptocurrency.
            amount (float): Amount to buy.

        Raises:
            ValueError: If buy amount is negative or exceeds balance.
        """
        if amount < 0:
            raise ValueError("Buy amount cannot be negative.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        # Simulate buying at a random price between $1 and $1000
        price = random.uniform(1, 1000)
        cost = amount * price

        if cryptocurrency in self.portfolio:
            self.portfolio[cryptocurrency]["amount"] += amount
            self.portfolio[cryptocurrency]["value"] += cost
        else:
            self.portfolio[cryptocurrency] = {"amount": amount, "value": cost}

        self.balance -= cost

    def sell(self, cryptocurrency, amount):
        """
        Sells a cryptocurrency.

        Args:
            cryptocurrency (str): Name of the cryptocurrency.
            amount (float): Amount to sell.

        Raises:
            ValueError: If sell amount is negative or exceeds portfolio amount.
        """
        if amount < 0:
            raise ValueError("Sell amount cannot be negative.")
        if cryptocurrency not in self.portfolio or amount > self.portfolio[cryptocurrency]["amount"]:
            raise ValueError("Insufficient portfolio amount.")

        # Simulate selling at a random price between $1 and $1000
        price = random.uniform(1, 1000)
        revenue = amount * price

        self.portfolio[cryptocurrency]["amount"] -= amount
        self.portfolio[cryptocurrency]["value"] -= amount * (self.portfolio[cryptocurrency]["value"] / self.portfolio[cryptocurrency]["amount"])

        if self.portfolio[cryptocurrency]["amount"] == 0:
            del self.portfolio[cryptocurrency]

        self.balance += revenue

    def get_balance(self):
        """
        Returns the current balance.

        Returns:
            float: Current balance.
        """
        return self.balance

    def get_portfolio(self):
        """
        Returns the current portfolio.

        Returns:
            dict: Current portfolio.
        """
        return self.portfolio


def simulate_risk_scenario(platform, buy_crypto, sell_crypto, amount):
    """
    Simulates a risk scenario by buying and selling a cryptocurrency.

    Args:
        platform (TradingPlatform): Trading platform instance.
        buy_crypto (str): Cryptocurrency to buy.
        sell_crypto (str): Cryptocurrency to sell.
        amount (float): Amount to buy and sell.

    Raises:
        Exception: If any error occurs during simulation.
    """
    try:
        platform.buy(buy_crypto, amount)
        platform.sell(sell_crypto, amount)
    except Exception as e:
        print(f"Error simulating risk scenario: {str(e)}")


def main():
    platform = TradingPlatform()

    # Simulate risk scenarios
    simulate_risk_scenario(platform, "Bitcoin", "Bitcoin", 1)
    simulate_risk_scenario(platform, "Ethereum", "Ethereum", 5)

    # Print final balance and portfolio
    print(f"Final balance: ${platform.get_balance():.2f}")
    print("Final portfolio:")
    for crypto, info in platform.get_portfolio().items():
        print(f"{crypto}: {info['amount']} units, worth ${info['value']:.2f}")


if __name__ == "__main__":
    main()
```
