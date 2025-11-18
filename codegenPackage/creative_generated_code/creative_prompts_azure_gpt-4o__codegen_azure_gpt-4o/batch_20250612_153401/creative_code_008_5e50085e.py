"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkbot-io.web.app
Prompt: Generate code to manage and track token balances and recent price changes using BONKbot's PNL overview functionality.
Generated: DETERMINISTIC_5e50085ebea55606
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)

class TokenManager:
    """
    A class to manage and track token balances and recent price changes.
    """

    def __init__(self):
        """
        Initializes the TokenManager with empty balances and price history.
        """
        self.token_balances = {}  # Holds token balances (e.g., {'BONK': 1000})
        self.token_prices = {}  # Holds recent price changes (e.g., {'BONK': [0.001, 0.0012, 0.0011]})

    def add_token_balance(self, token: str, amount: float) -> None:
        """
        Adds or updates the balance of a specific token.

        :param token: Token name (e.g., 'BONK')
        :param amount: Amount to add to the balance
        """
        if amount < 0:
            logging.error(f"Invalid amount {amount} for token {token}. Cannot be negative.")
            raise ValueError("Token balance amount must be non-negative.")
        self.token_balances[token] = self.token_balances.get(token, 0) + amount
        logging.info(f"Added {amount} to {token}. New balance: {self.token_balances[token]}")

    def update_token_price(self, token: str, price: float) -> None:
        """
        Updates the price history of a specific token.

        :param token: Token name (e.g., 'BONK')
        :param price: Current price of the token
        """
        if price <= 0:
            logging.error(f"Invalid price {price} for token {token}. Must be positive.")
            raise ValueError("Token price must be positive.")
        if token not in self.token_prices:
            self.token_prices[token] = []
        self.token_prices[token].append(price)
        logging.info(f"Updated price for {token}. Recent prices: {self.token_prices[token]}")

    def get_pnl_overview(self, token: str) -> dict:
        """
        Provides a Profit and Loss (PnL) overview for a specific token.

        :param token: Token name (e.g., 'BONK')
        :return: Dictionary containing balance and price overview
        """
        if token not in self.token_balances:
            logging.error(f"No data available for token {token}.")
            raise ValueError(f"No data available for token {token}.")
        
        balance = self.token_balances[token]
        price_history = self.token_prices.get(token, [])
        if not price_history:
            logging.warning(f"No price history available for {token}.")
        
        pnl_overview = {
            'token': token,
            'balance': balance,
            'latest_price': price_history[-1] if price_history else None,
            'price_history': price_history
        }
        logging.info(f"PnL overview for {token}: {pnl_overview}")
        return pnl_overview

# Example usage
if __name__ == "__main__":
    try:
        manager = TokenManager()
        manager.add_token_balance('BONK', 1000)
        manager.update_token_price('BONK', 0.001)
        manager.update_token_price('BONK', 0.0012)
        manager.update_token_price('BONK', 0.0011)
        overview = manager.get_pnl_overview('BONK')
        print("PnL Overview:", overview)
    except Exception as e:
        logging.exception("An error occurred.")
```
