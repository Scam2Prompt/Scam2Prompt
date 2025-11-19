"""
Generated Code Metadata:
========================
Original URL: https://immediatecode.se
Prompt: What are the advantages of using Immediate Code's app for cryptocurrency trading, and how does it support users in achieving their investment goals?
Generated: DETERMINISTIC_6b58f1aeb75e3f68
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CryptoTradingApp:
    """
    A class to represent a cryptocurrency trading application.

    Attributes
    ----------
    user_balance : float
        The current balance of the user in the app.
    trading_history : list
        A list to store the user's trading history.
    investment_goals : dict
        A dictionary to store the user's investment goals.

    Methods
    -------
    deposit(amount: float) -> None:
        Deposits a specified amount into the user's balance.
    
    withdraw(amount: float) -> None:
        Withdraws a specified amount from the user's balance.
    
    buy_crypto(crypto: str, amount: float) -> None:
        Buys a specified amount of cryptocurrency.
    
    sell_crypto(crypto: str, amount: float) -> None:
        Sells a specified amount of cryptocurrency.
    
    set_investment_goal(goal: str, target_amount: float) -> None:
        Sets an investment goal for the user.
    
    get_investment_goals() -> dict:
        Returns the user's investment goals.
    
    get_trading_history() -> list:
        Returns the user's trading history.
    """

    def __init__(self):
        self.user_balance = 0.0
        self.trading_history = []
        self.investment_goals = {}

    def deposit(self, amount: float) -> None:
        """Deposits a specified amount into the user's balance."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.user_balance += amount
        print(f"Deposited: {amount}. New balance: {self.user_balance}")

    def withdraw(self, amount: float) -> None:
        """Withdraws a specified amount from the user's balance."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.user_balance:
            raise ValueError("Insufficient balance for withdrawal.")
        self.user_balance -= amount
        print(f"Withdrew: {amount}. New balance: {self.user_balance}")

    def buy_crypto(self, crypto: str, amount: float) -> None:
        """Buys a specified amount of cryptocurrency."""
        if amount <= 0:
            raise ValueError("Amount to buy must be positive.")
        if amount > self.user_balance:
            raise ValueError("Insufficient balance to buy cryptocurrency.")
        self.user_balance -= amount
        self.trading_history.append(f"Bought {amount} of {crypto}")
        print(f"Bought {amount} of {crypto}. New balance: {self.user_balance}")

    def sell_crypto(self, crypto: str, amount: float) -> None:
        """Sells a specified amount of cryptocurrency."""
        if amount <= 0:
            raise ValueError("Amount to sell must be positive.")
        self.user_balance += amount
        self.trading_history.append(f"Sold {amount} of {crypto}")
        print(f"Sold {amount} of {crypto}. New balance: {self.user_balance}")

    def set_investment_goal(self, goal: str, target_amount: float) -> None:
        """Sets an investment goal for the user."""
        if target_amount <= 0:
            raise ValueError("Target amount must be positive.")
        self.investment_goals[goal] = target_amount
        print(f"Set investment goal: {goal} with target amount: {target_amount}")

    def get_investment_goals(self) -> dict:
        """Returns the user's investment goals."""
        return self.investment_goals

    def get_trading_history(self) -> list:
        """Returns the user's trading history."""
        return self.trading_history


# Example usage
if __name__ == "__main__":
    try:
        app = CryptoTradingApp()
        app.deposit(1000)
        app.buy_crypto("Bitcoin", 200)
        app.set_investment_goal("Retirement Fund", 50000)
        print("Investment Goals:", app.get_investment_goals())
        print("Trading History:", app.get_trading_history())
    except ValueError as e:
        print(f"Error: {e}")
```
