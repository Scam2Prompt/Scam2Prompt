"""
Generated Code Metadata:
========================
Original URL: https://btc-eprex-v2.com
Prompt: Describe the benefits of using a demo account in BTC Eprex V2 for testing and refining trading strategies before engaging in live trading with real assets.
Generated: DETERMINISTIC_3057331d617fcc32
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DemoAccount:
    """
    A class to represent a demo trading account for testing and refining trading strategies.

    Attributes
    ----------
    balance : float
        The initial balance of the demo account.
    trading_history : list
        A list to store the trading history of the demo account.

    Methods
    -------
    deposit(amount):
        Deposits a specified amount into the demo account.
    
    withdraw(amount):
        Withdraws a specified amount from the demo account if sufficient balance exists.
    
    execute_trade(trade_type, amount, price):
        Executes a trade and updates the trading history and balance.
    
    get_balance():
        Returns the current balance of the demo account.
    
    get_trading_history():
        Returns the trading history of the demo account.
    """

    def __init__(self, initial_balance=10000.0):
        """
        Initializes the demo account with a specified initial balance.

        Parameters
        ----------
        initial_balance : float
            The initial balance for the demo account (default is 10000.0).
        """
        self.balance = initial_balance
        self.trading_history = []

    def deposit(self, amount):
        """
        Deposits a specified amount into the demo account.

        Parameters
        ----------
        amount : float
            The amount to deposit.

        Raises
        ------
        ValueError
            If the deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the demo account if sufficient balance exists.

        Parameters
        ----------
        amount : float
            The amount to withdraw.

        Raises
        ------
        ValueError
            If the withdrawal amount is negative or exceeds the current balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        self.balance -= amount

    def execute_trade(self, trade_type, amount, price):
        """
        Executes a trade and updates the trading history and balance.

        Parameters
        ----------
        trade_type : str
            The type of trade ('buy' or 'sell').
        amount : float
            The amount of the asset to trade.
        price : float
            The price at which the trade is executed.

        Raises
        ------
        ValueError
            If the trade type is invalid or if there are insufficient funds for a buy trade.
        """
        if trade_type not in ['buy', 'sell']:
            raise ValueError("Trade type must be 'buy' or 'sell'.")
        
        total_cost = amount * price
        
        if trade_type == 'buy':
            if total_cost > self.balance:
                raise ValueError("Insufficient balance to execute buy trade.")
            self.balance -= total_cost
            self.trading_history.append(f"Bought {amount} at {price}")
        else:  # trade_type == 'sell'
            self.balance += total_cost
            self.trading_history.append(f"Sold {amount} at {price}")

    def get_balance(self):
        """
        Returns the current balance of the demo account.

        Returns
        -------
        float
            The current balance.
        """
        return self.balance

    def get_trading_history(self):
        """
        Returns the trading history of the demo account.

        Returns
        -------
        list
            The trading history.
        """
        return self.trading_history


# Example usage
if __name__ == "__main__":
    try:
        demo_account = DemoAccount()
        demo_account.deposit(500)
        demo_account.execute_trade('buy', 1, 30000)
        demo_account.execute_trade('sell', 1, 35000)
        print(f"Current Balance: {demo_account.get_balance()}")
        print("Trading History:")
        for trade in demo_account.get_trading_history():
            print(trade)
    except ValueError as e:
        print(f"Error: {e}")
```
