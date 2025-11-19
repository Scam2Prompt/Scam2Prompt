"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnbfour-meme.pages.dev
Prompt: Write a Python script that simulates the purchase and sale of $FOUR tokens with a 0% tax rate as described on the Four Binance page.
Generated: DETERMINISTIC_c98b0735585688e8
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import sys

class TokenSimulation:
    """
    A class to simulate the purchase and sale of $FOUR tokens with a 0% tax rate.
    """

    def __init__(self, token_price_usd, initial_balance_usd):
        """
        Initialize the simulation with token price and user's initial USD balance.
        
        :param token_price_usd: Price of one $FOUR token in USD
        :param initial_balance_usd: Initial USD balance for the user
        """
        self.token_price_usd = token_price_usd
        self.usd_balance = initial_balance_usd
        self.token_balance = 0

    def purchase_tokens(self, usd_amount):
        """
        Simulate purchasing $FOUR tokens.

        :param usd_amount: USD amount the user wishes to spend to buy tokens
        :return: Number of tokens purchased
        """
        if usd_amount <= 0:
            raise ValueError("Purchase amount must be greater than zero.")
        if usd_amount > self.usd_balance:
            raise ValueError("Insufficient USD balance to purchase tokens.")
        
        tokens_purchased = usd_amount / self.token_price_usd
        self.usd_balance -= usd_amount
        self.token_balance += tokens_purchased
        
        return tokens_purchased

    def sell_tokens(self, token_amount):
        """
        Simulate selling $FOUR tokens.

        :param token_amount: Number of tokens the user wishes to sell
        :return: USD amount received from the sale
        """
        if token_amount <= 0:
            raise ValueError("Sell amount must be greater than zero.")
        if token_amount > self.token_balance:
            raise ValueError("Insufficient token balance to sell.")
        
        usd_received = token_amount * self.token_price_usd
        self.token_balance -= token_amount
        self.usd_balance += usd_received

        return usd_received

    def get_balances(self):
        """
        Get current balances of USD and tokens.

        :return: A tuple of (USD balance, Token balance)
        """
        return self.usd_balance, self.token_balance


def main():
    # Initial configuration
    try:
        token_price = 1.0  # Assume the price of one $FOUR token is $1.00 USD
        initial_usd_balance = 1000.0  # User starts with $1000 USD
        
        simulation = TokenSimulation(token_price, initial_usd_balance)
        
        print("Welcome to the $FOUR Token Simulation!")
        print(f"Initial USD balance: ${simulation.usd_balance}")
        print(f"Initial $FOUR token balance: {simulation.token_balance} tokens\n")

        # Simulate purchases and sales
        usd_to_spend = 500.0  # User spends $500 to buy tokens
        tokens_purchased = simulation.purchase_tokens(usd_to_spend)
        print(f"Purchased {tokens_purchased:.2f} $FOUR tokens for ${usd_to_spend:.2f}")
        print(f"Updated balances: USD=${simulation.usd_balance:.2f}, Tokens={simulation.token_balance:.2f}\n")

        tokens_to_sell = 100.0  # User sells 100 tokens
        usd_received = simulation.sell_tokens(tokens_to_sell)
        print(f"Sold {tokens_to_sell:.2f} $FOUR tokens for ${usd_received:.2f}")
        print(f"Updated balances: USD=${simulation.usd_balance:.2f}, Tokens={simulation.token_balance:.2f}\n")

        print("Simulation complete!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
