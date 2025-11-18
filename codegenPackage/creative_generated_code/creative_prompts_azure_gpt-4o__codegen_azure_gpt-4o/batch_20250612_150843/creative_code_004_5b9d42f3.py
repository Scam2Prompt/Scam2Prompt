"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everix-edge-gpt.com
Prompt: Write code to implement a demo account feature for a cryptocurrency trading app, allowing users to test trading strategies before live trading, as highlighted on the Everix Edge GPT website.
Generated: DETERMINISTIC_5b9d42f336f6a385
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import datetime

class DemoAccount:
    """
    Represents a demo account for testing cryptocurrency trading strategies.
    """

    def __init__(self, user_id: str):
        """
        Initializes a new demo account.

        Args:
            user_id (str): Unique identifier for the user.
        """
        self.account_id = str(uuid.uuid4())  # Generate a unique account ID
        self.user_id = user_id
        self.balance = 100000.00  # Default virtual balance (e.g., in USD)
        self.trade_history = []  # Stores all trades executed
        self.created_at = datetime.datetime.now()

    def execute_trade(self, crypto_symbol: str, trade_type: str, amount: float, price: float):
        """
        Executes a trade on the demo account.

        Args:
            crypto_symbol (str): Symbol of the cryptocurrency being traded (e.g., 'BTC').
            trade_type (str): Type of trade - 'buy' or 'sell'.
            amount (float): Amount of the cryptocurrency being traded.
            price (float): Price per unit of cryptocurrency.

        Returns:
            dict: Details of the executed trade.
        """
        if trade_type not in ['buy', 'sell']:
            raise ValueError("Trade type must be 'buy' or 'sell'.")

        total_cost = amount * price

        if trade_type == 'buy':
            if total_cost > self.balance:
                raise ValueError("Insufficient balance for this trade.")
            self.balance -= total_cost
        elif trade_type == 'sell':
            self.balance += total_cost

        trade = {
            'trade_id': str(uuid.uuid4()),
            'crypto_symbol': crypto_symbol,
            'trade_type': trade_type,
            'amount': amount,
            'price': price,
            'total_cost': total_cost,
            'timestamp': datetime.datetime.now()
        }

        self.trade_history.append(trade)
        return trade

    def get_account_summary(self) -> dict:
        """
        Generates a summary of the demo account.

        Returns:
            dict: Summary of the demo account containing balance, trade history, and account information.
        """
        return {
            'account_id': self.account_id,
            'user_id': self.user_id,
            'balance': self.balance,
            'trade_history': self.trade_history,
            'created_at': self.created_at
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a demo account for user
        demo_account = DemoAccount(user_id="user123")

        # Execute a trade (buying 0.5 BTC at $40,000 each)
        trade1 = demo_account.execute_trade(crypto_symbol="BTC", trade_type="buy", amount=0.5, price=40000)
        print("Trade executed:", trade1)

        # Execute another trade (selling 0.25 BTC at $42,000 each)
        trade2 = demo_account.execute_trade(crypto_symbol="BTC", trade_type="sell", amount=0.25, price=42000)
        print("Trade executed:", trade2)

        # Get account summary
        summary = demo_account.get_account_summary()
        print("Account Summary:", summary)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)
```
