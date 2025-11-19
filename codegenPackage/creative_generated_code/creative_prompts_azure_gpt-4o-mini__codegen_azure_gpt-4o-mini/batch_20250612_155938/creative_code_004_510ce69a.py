"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idegensolutionmeme.pages.dev
Prompt: Create a function that simulates the price updates for a token based on purchase activity, inspired by the iDEGEN presale auction mechanics.
Generated: DETERMINISTIC_510ce69ae3e6bf57
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Token:
    def __init__(self, initial_price: float, volatility: float):
        """
        Initializes a new Token instance.

        Parameters:
        initial_price (float): The initial price of the token.
        volatility (float): The maximum change in price per transaction.
        """
        self.price = initial_price
        self.volatility = volatility

    def update_price(self, purchase_amount: float) -> float:
        """
        Updates the token price based on the purchase activity.

        Parameters:
        purchase_amount (float): The amount of tokens purchased.

        Returns:
        float: The new token price after the purchase.
        """
        if purchase_amount <= 0:
            raise ValueError("Purchase amount must be greater than zero")
        
        # Calculate price change based on the purchase amount
        price_change = random.uniform(-self.volatility, self.volatility)
        
        # Update the token price
        self.price += price_change * purchase_amount
        
        # Ensure the price does not drop below zero
        if self.price < 0:
            self.price = 0
        
        return self.price

def simulate_token_sales(token: Token, sales_data: list) -> None:
    """
    Simulates a series of token sales and updates the token price accordingly.

    Parameters:
    token (Token): The Token instance to update.
    sales_data (list): A list of purchase amounts to simulate.
    """
    for sale in sales_data:
        try:
            new_price = token.update_price(sale)
            print(f"Purchased {sale} tokens. New token price: {new_price:.2f}")
        except ValueError as e:
            print(f"Error updating price for purchase {sale}: {e}")

if __name__ == "__main__":
    # Example usage of the Token class and simulation function
    token = Token(initial_price=10.0, volatility=0.05)
    sales_data = [1, 2, 3, 4, 5, -1]  # Last value will generate an error

    # Simulate sales
    simulate_token_sales(token, sales_data)
```
