"""
Generated Code Metadata:
========================
Original URL: https://idegensolutionmeme.pages.dev
Prompt: Create a function that simulates the price updates for a token based on purchase activity, inspired by the iDEGEN presale auction mechanics.
Generated: DETERMINISTIC_510ce69ae3e6bf57
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List

class Token:
    def __init__(self, name: str, initial_price: float, total_supply: int):
        """
        Initialize a Token object.

        Args:
        - name (str): The name of the token.
        - initial_price (float): The initial price of the token.
        - total_supply (int): The total supply of the token.
        """
        self.name = name
        self.price = initial_price
        self.total_supply = total_supply
        self.tokens_sold = 0

    def update_price(self, amount_purchased: int):
        """
        Update the token price based on the amount purchased.

        The price increase is calculated as 1% for every 10 tokens purchased.

        Args:
        - amount_purchased (int): The number of tokens purchased.
        """
        if amount_purchased <= 0:
            raise ValueError("Amount purchased must be greater than zero.")

        # Calculate the price increase factor
        price_increase_factor = 1 + (amount_purchased // 10) * 0.01

        # Update the token price
        self.price *= price_increase_factor

        # Update the tokens sold
        self.tokens_sold += amount_purchased

        # Check if the total supply is exceeded
        if self.tokens_sold > self.total_supply:
            raise ValueError("Total supply exceeded.")

    def get_token_info(self) -> dict:
        """
        Get the current token information.

        Returns:
        - dict: A dictionary containing the token name, price, total supply, and tokens sold.
        """
        return {
            "name": self.name,
            "price": self.price,
            "total_supply": self.total_supply,
            "tokens_sold": self.tokens_sold,
        }


def simulate_presale_auction(token: Token, purchases: List[int]) -> List[dict]:
    """
    Simulate the presale auction by updating the token price based on purchases.

    Args:
    - token (Token): The Token object.
    - purchases (List[int]): A list of token purchases.

    Returns:
    - List[dict]: A list of dictionaries containing the token information at each purchase step.
    """
    token_info_history = []

    for purchase in purchases:
        try:
            token.update_price(purchase)
            token_info_history.append(token.get_token_info())
        except ValueError as e:
            print(f"Error: {e}")

    return token_info_history


# Example usage
if __name__ == "__main__":
    token = Token("iDEGEN", 0.1, 10000)
    purchases = [10, 20, 30, 40, 50]
    token_info_history = simulate_presale_auction(token, purchases)

    for i, token_info in enumerate(token_info_history):
        print(f"Purchase Step {i+1}: {token_info}")
```
