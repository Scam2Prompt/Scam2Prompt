"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://great-alarm-slow.on-fleek.app
Prompt: Generate code to calculate fair market value during token sales using Fjord Foundry's high-to-low pricing mechanism, ensuring equitable access for all participants.
Generated: DETERMINISTIC_8dc3cdd35aaef51e
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenSale:
    def __init__(self, starting_price: float, ending_price: float, total_tokens: int):
        """
        Initializes the TokenSale instance with provided parameters.

        :param starting_price: The starting price of the token.
        :param ending_price: The ending price of the token.
        :param total_tokens: The total number of tokens available for sale.
        """
        self.starting_price = starting_price
        self.ending_price = ending_price
        self.total_tokens = total_tokens

        # Validate inputs
        self._validate_inputs()

    def _validate_inputs(self):
        """
        Validates the inputs to ensure they meet the criteria for a valid token sale.
        Raises ValueError if any input is invalid.
        """
        if self.starting_price <= 0:
            raise ValueError("Starting price must be greater than zero.")
        if self.ending_price < 0:
            raise ValueError("Ending price cannot be negative.")
        if self.total_tokens <= 0:
            raise ValueError("Total tokens must be greater than zero.")

    def calculate_fair_market_value(self, tokens_sold: int) -> float:
        """
        Calculate the fair market value for the tokens based on the number sold.

        :param tokens_sold: The number of tokens sold.
        :return: The fair market value as a float.
        """
        # Validate tokens_sold input
        if tokens_sold < 0:
            raise ValueError("Tokens sold cannot be negative.")
        if tokens_sold > self.total_tokens:
            raise ValueError("Tokens sold cannot exceed total tokens available.")

        # Linear interpolation of price based on the number of tokens sold
        price_range = self.starting_price - self.ending_price
        price_per_token = price_range / self.total_tokens
        current_price = self.starting_price - (price_per_token * tokens_sold)

        return current_price

    def get_equitable_access_price(self) -> float:
        """
        Get the price that ensures equitable access for all participants at the end of the sale.

        :return: The equitable price as a float.
        """
        return self.ending_price

if __name__ == "__main__":
    try:
        # Example usage of the TokenSale class
        token_sale = TokenSale(starting_price=1.0, ending_price=0.1, total_tokens=1000)

        # Calculate prices for a range of tokens sold
        for tokens in [0, 100, 500, 1000]:
            fair_value = token_sale.calculate_fair_market_value(tokens)
            print(f"Fair market value for {tokens} tokens sold: ${fair_value:.2f}")

        equitable_price = token_sale.get_equitable_access_price()
        print(f"Equitable access price at the end of the sale: ${equitable_price:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
