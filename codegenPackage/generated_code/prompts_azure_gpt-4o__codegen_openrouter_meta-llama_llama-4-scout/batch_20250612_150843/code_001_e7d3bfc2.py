"""
Generated Code Metadata:
========================
Original URL: https://thecryptex-secure.com
Prompt: Generate code to simulate CrypTEX Secure's demo account functionality, allowing users to test trading strategies with virtual funds before committing real investments.
Generated: DETERMINISTIC_e7d3bfc2c6236cc3
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class CrypTEXSecureDemo:
    """
    Simulates CrypTEX Secure's demo account functionality.
    
    Allows users to test trading strategies with virtual funds before committing real investments.
    """

    def __init__(self, initial_balance=10000):
        """
        Initializes a demo account with an initial balance.

        Args:
            initial_balance (float, optional): Initial balance in USD. Defaults to 10000.
        """
        self.balance = initial_balance
        self.positions = {}
        self.trade_history = []

    def get_balance(self):
        """
        Retrieves the current account balance.

        Returns:
            float: Current balance in USD.
        """
        return self.balance

    def get_positions(self):
        """
        Retrieves the current open positions.

        Returns:
            dict: Dictionary of open positions (symbol: quantity).
        """
        return self.positions

    def get_trade_history(self):
        """
        Retrieves the trade history.

        Returns:
            list: List of trades ( dictionaries containing trade details).
        """
        return self.trade_history

    def deposit(self, amount):
        """
        Deposits virtual funds into the account.

        Args:
            amount (float): Amount to deposit in USD.

        Raises:
            ValueError: If deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws virtual funds from the account.

        Args:
            amount (float): Amount to withdraw in USD.

        Raises:
            ValueError: If withdrawal amount is negative or exceeds the balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def place_order(self, symbol, quantity, side):
        """
        Places a trade order.

        Args:
            symbol (str): Symbol of the asset to trade (e.g., BTCUSD).
            quantity (float): Quantity of the asset to trade.
            side (str): Side of the trade (buy or sell).

        Raises:
            ValueError: If quantity is negative or side is invalid.
        """
        if quantity < 0:
            raise ValueError("Trade quantity cannot be negative")
        if side not in ["buy", "sell"]:
            raise ValueError("Invalid trade side")

        # Simulate trade execution with random price
        price = round(random.uniform(0.1, 1000.0), 2)

        if side == "buy":
            cost = quantity * price
            if cost > self.balance:
                raise ValueError("Insufficient funds")
            self.balance -= cost
            if symbol in self.positions:
                self.positions[symbol] += quantity
            else:
                self.positions[symbol] = quantity
            self.trade_history.append({
                "symbol": symbol,
                "quantity": quantity,
                "side": side,
                "price": price,
                "status": "filled"
            })
        elif side == "sell":
            if symbol not in self.positions or self.positions[symbol] < quantity:
                raise ValueError("Insufficient quantity to sell")
            revenue = quantity * price
            self.balance += revenue
            self.positions[symbol] -= quantity
            if self.positions[symbol] == 0:
                del self.positions[symbol]
            self.trade_history.append({
                "symbol": symbol,
                "quantity": quantity,
                "side": side,
                "price": price,
                "status": "filled"
            })

    def cancel_order(self, symbol, quantity):
        """
        Cancels a trade order.

        Args:
            symbol (str): Symbol of the asset to cancel.
            quantity (float): Quantity of the asset to cancel.

        Raises:
            ValueError: If quantity is negative or symbol is not found.
        """
        if quantity < 0:
            raise ValueError("Cancellation quantity cannot be negative")
        if symbol not in self.positions:
            raise ValueError("Symbol not found in open positions")

        # Partial cancellation not supported for simplicity
        if self.positions[symbol] != quantity:
            raise ValueError("Only full cancellation is supported")

        del self.positions[symbol]
        self.trade_history.append({
            "symbol": symbol,
            "quantity": quantity,
            "side": "cancel",
            "status": "canceled"
        })

def main():
    demo_account = CrypTEXSecureDemo()

    print("Initial Balance: $", demo_account.get_balance())

    demo_account.deposit(5000)
    print("Balance after deposit: $", demo_account.get_balance())

    demo_account.place_order("BTCUSD", 0.1, "buy")
    print("Balance after buy: $", demo_account.get_balance())
    print("Open Positions: ", demo_account.get_positions())

    demo_account.place_order("BTCUSD", 0.05, "sell")
    print("Balance after sell: $", demo_account.get_balance())
    print("Open Positions: ", demo_account.get_positions())

    demo_account.withdraw(2000)
    print("Balance after withdrawal: $", demo_account.get_balance())

    print("Trade History: ", demo_account.get_trade_history())

if __name__ == "__main__":
    main()
```
