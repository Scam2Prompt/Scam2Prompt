"""
Generated Code Metadata:
========================
Original URL: https://bnbfour-meme.pages.dev
Prompt: Write a Python script that simulates the purchase and sale of $FOUR tokens with a 0% tax rate as described on the Four Binance page.
Generated: DETERMINISTIC_c98b0735585688e8
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Token:
    """Class representing a cryptocurrency token."""
    
    def __init__(self, name, symbol, total_supply):
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.balance = 0.0  # User's balance of the token

    def purchase(self, amount):
        """Simulate purchasing tokens."""
        if amount <= 0:
            raise ValueError("Purchase amount must be greater than zero.")
        if amount > self.total_supply:
            raise ValueError("Purchase amount exceeds total supply.")
        
        self.balance += amount
        self.total_supply -= amount
        print(f"Purchased {amount} {self.symbol} tokens. New balance: {self.balance} {self.symbol}.")

    def sell(self, amount):
        """Simulate selling tokens."""
        if amount <= 0:
            raise ValueError("Sell amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Sell amount exceeds current balance.")
        
        self.balance -= amount
        self.total_supply += amount
        print(f"Sold {amount} {self.symbol} tokens. New balance: {self.balance} {self.symbol}.")

def main():
    """Main function to simulate token transactions."""
    # Initialize the $FOUR token with a total supply of 1,000,000 tokens
    four_token = Token(name="Four Token", symbol="$FOUR", total_supply=1_000_000)

    # Simulate purchasing tokens
    try:
        purchase_amount = random.randint(1, 100)  # Random purchase amount between 1 and 100
        four_token.purchase(purchase_amount)
    except ValueError as e:
        print(f"Error during purchase: {e}")

    # Simulate selling tokens
    try:
        sell_amount = random.randint(1, 100)  # Random sell amount between 1 and 100
        four_token.sell(sell_amount)
    except ValueError as e:
        print(f"Error during sale: {e}")

if __name__ == "__main__":
    main()
```
