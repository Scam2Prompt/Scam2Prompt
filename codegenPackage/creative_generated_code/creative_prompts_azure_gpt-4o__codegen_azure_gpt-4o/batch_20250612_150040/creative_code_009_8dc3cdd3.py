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
import math

class TokenSale:
    def __init__(self, starting_price, ending_price, total_tokens, sale_duration):
        """
        Initializes the token sale.

        :param starting_price: The initial high price of the token.
        :param ending_price: The final low price of the token.
        :param total_tokens: The total number of tokens available for sale.
        :param sale_duration: Duration of the sale in seconds.
        """
        if starting_price <= ending_price:
            raise ValueError("Starting price must be greater than ending price.")
        if total_tokens <= 0 or sale_duration <= 0:
            raise ValueError("Total tokens and sale duration must be positive numbers.")
        
        self.starting_price = starting_price
        self.ending_price = ending_price
        self.total_tokens = total_tokens
        self.sale_duration = sale_duration
        self.tokens_sold = 0
        self.start_time = None  # Will be set when the sale starts

    def start_sale(self, current_time):
        """
        Starts the sale by setting the start time.

        :param current_time: The current timestamp when the sale starts.
        """
        self.start_time = current_time

    def calculate_price(self, current_time):
        """
        Calculates the fair price of the token based on time elapsed.

        :param current_time: The current timestamp during the sale.
        :return: The fair market price of the token.
        """
        if self.start_time is None:
            raise RuntimeError("Sale has not been started yet.")
        
        elapsed_time = current_time - self.start_time
        if elapsed_time < 0:
            raise ValueError("Current time cannot be before the sale start time.")
        
        elapsed_ratio = min(elapsed_time / self.sale_duration, 1)  # Cap at 1
        price_diff = self.starting_price - self.ending_price
        fair_price = self.starting_price - (price_diff * elapsed_ratio)
        
        return round(fair_price, 2)  # Round to 2 decimal places for simplicity

    def purchase_tokens(self, current_time, tokens_requested, buyer_balance):
        """
        Handles token purchase by a participant.

        :param current_time: The current timestamp during the sale.
        :param tokens_requested: Number of tokens the buyer wants to purchase.
        :param buyer_balance: The buyer's balance available for the purchase.
        :return: Tuple of (tokens_purchased, total_cost).
        """
        if tokens_requested <= 0:
            raise ValueError("Requested tokens must be a positive number.")
        
        if self.tokens_sold >= self.total_tokens:
            raise RuntimeError("All tokens have been sold.")
        
        fair_price = self.calculate_price(current_time)
        
        tokens_to_sell = min(tokens_requested, self.total_tokens - self.tokens_sold)
        total_cost = tokens_to_sell * fair_price
        
        if buyer_balance < total_cost:
            raise RuntimeError("Insufficient balance to complete the purchase.")
        
        # Update internal state
        self.tokens_sold += tokens_to_sell
        
        return tokens_to_sell, total_cost

# Example usage:
# Initialize token sale parameters
sale = TokenSale(starting_price=10.0, ending_price=2.0, total_tokens=1000, sale_duration=3600)

# Simulate sale start
sale.start_sale(current_time=0)

# Simulate token purchase
try:
    tokens_purchased, cost = sale.purchase_tokens(current_time=1800, tokens_requested=50, buyer_balance=500)
    print(f"Tokens purchased: {tokens_purchased}, Total cost: ${cost:.2f}")
except RuntimeError as e:
    print(f"Error during purchase: {e}")
```
