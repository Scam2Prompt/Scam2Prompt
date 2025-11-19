"""
Generated Code Metadata:
========================
Original URL: https://moxie.social
Prompt: Provide an example of how to use Moxie Bonding Curves to emphasize utility over speculation for Fan Tokens.
Generated: DETERMINISTIC_e66e9fefc520691d
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from decimal import Decimal
from typing import List, Tuple

class MoxieBondingCurve:
    """
    A class to represent a Moxie Bonding Curve for Fan Tokens.
    This curve emphasizes utility over speculation by adjusting the token price based on supply and demand.
    """

    def __init__(self, reserve: Decimal = Decimal('0'), token_supply: Decimal = Decimal('0')):
        """
        Initializes the bonding curve with a given reserve and token supply.

        :param reserve: The amount of reserve currency (e.g., ETH, USDC) held.
        :param token_supply: The total supply of tokens.
        """
        self.reserve = reserve
        self.token_supply = token_supply

    def buy_tokens(self, amount: Decimal) -> Tuple[Decimal, Decimal]:
        """
        Buys tokens based on the amount of reserve currency provided.

        :param amount: The amount of reserve currency to spend.
        :return: A tuple containing the number of tokens bought and the new reserve amount.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Calculate the price of the next token based on the current supply
        if self.token_supply == 0:
            token_price = Decimal('1')  # Initial price for the first token
        else:
            token_price = self.calculate_token_price()

        # Calculate the number of tokens to buy
        tokens_bought = amount / token_price

        # Update reserve and token supply
        self.reserve += amount
        self.token_supply += tokens_bought

        return tokens_bought, self.reserve

    def sell_tokens(self, tokens: Decimal) -> Tuple[Decimal, Decimal]:
        """
        Sells tokens back to the reserve currency.

        :param tokens: The number of tokens to sell.
        :return: A tuple containing the amount of reserve currency received and the new token supply.
        """
        if tokens <= 0 or tokens > self.token_supply:
            raise ValueError("Invalid token amount to sell.")

        # Calculate the price of the tokens being sold
        token_price = self.calculate_token_price()

        # Calculate the amount of reserve currency to receive
        amount_received = tokens * token_price

        # Update reserve and token supply
        self.reserve -= amount_received
        self.token_supply -= tokens

        return amount_received, self.token_supply

    def calculate_token_price(self) -> Decimal:
        """
        Calculates the current price of a token based on the bonding curve formula.

        :return: The current price of a token.
        """
        # Example formula: price = reserve / (supply + 1)
        return self.reserve / (self.token_supply + Decimal('1'))

    def get_state(self) -> dict:
        """
        Returns the current state of the bonding curve.

        :return: A dictionary containing the reserve and token supply.
        """
        return {
            'reserve': float(self.reserve),
            'token_supply': float(self.token_supply),
            'current_token_price': float(self.calculate_token_price())
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the bonding curve
        bonding_curve = MoxieBondingCurve()

        # Buy tokens
        tokens_bought, new_reserve = bonding_curve.buy_tokens(Decimal('100'))
        print(f"Tokens bought: {tokens_bought}, New reserve: {new_reserve}")

        # Sell tokens
        amount_received, new_supply = bonding_curve.sell_tokens(tokens_bought)
        print(f"Amount received: {amount_received}, New token supply: {new_supply}")

        # Get current state
        state = bonding_curve.get_state()
        print(f"Current state: {state}")

    except ValueError as e:
        print(f"Error: {e}")
```
