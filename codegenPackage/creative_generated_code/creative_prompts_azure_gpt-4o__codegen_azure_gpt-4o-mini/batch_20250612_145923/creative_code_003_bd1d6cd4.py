"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-claim.pages.dev
Prompt: Write a script to implement a presale system for tokens, similar to Pushd's presale perks, including early access, discounted tokens, and priority support.
Generated: DETERMINISTIC_bd1d6cd4602c8266
Batch ID: 20250612_145923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TokenPresale:
    def __init__(self, token_name, total_supply, presale_start, presale_end, discount_rate, early_access_limit):
        """
        Initialize the TokenPresale instance.

        :param token_name: str - Name of the token being sold.
        :param total_supply: int - Total amount of tokens available for presale.
        :param presale_start: datetime - Start date and time for the presale.
        :param presale_end: datetime - End date and time for the presale.
        :param discount_rate: float - Discount rate applied during presale (0.0 to 1.0).
        :param early_access_limit: int - Number of tokens available for early access.
        """
        self.token_name = token_name
        self.total_supply = total_supply
        self.presale_start = presale_start
        self.presale_end = presale_end
        self.discount_rate = discount_rate
        self.early_access_limit = early_access_limit
        self.sold_tokens = 0
        self.early_access_tokens = 0

    def buy_tokens(self, quantity, early_access=False):
        """
        Allow users to buy tokens during the presale.

        :param quantity: int - Number of tokens the user wants to buy.
        :param early_access: bool - True if buying under early access conditions.
        :raises ValueError: If the purchase is invalid or exceeds limits.
        :return: float - Total price for the tokens.
        """
        self._check_presale_validity()
        total_price = self._calculate_price(quantity, early_access)

        # Update the sold tokens count
        self.sold_tokens += quantity
        if early_access:
            self.early_access_tokens += quantity

        return total_price

    def _check_presale_validity(self):
        """Check if the presale is currently active and if the purchase limit is respected."""
        now = datetime.datetime.now()

        # Check if presale is active
        if now < self.presale_start or now > self.presale_end:
            raise ValueError("Presale is not active.")

        # Check if there are enough tokens available
        if self.sold_tokens + self.early_access_tokens >= self.total_supply:
            raise ValueError("Not enough tokens available for purchase.")

    def _calculate_price(self, quantity, early_access):
        """
        Calculate the price for the tokens based on discount and early access.

        :param quantity: int - Number of tokens to buy.
        :param early_access: bool - True if buying under early access conditions.
        :return: float - Calculated price for the tokens.
        """
        base_price = 1.0  # Example base price per token
        price_per_token = base_price

        # Apply discount if not early access or if within early access limit
        if early_access and self.early_access_tokens + quantity <= self.early_access_limit:
            price_per_token *= (1 - self.discount_rate)

        return price_per_token * quantity

    def get_summary(self):
        """
        Get a summary of the presale status.

        :return: str - Summary of the presale status.
        """
        return (f"Token: {self.token_name}, "
                f"Total Supply: {self.total_supply}, "
                f"Tokens Sold: {self.sold_tokens}, "
                f"Early Access Tokens Sold: {self.early_access_tokens}, "
                f"Active: {self.presale_start <= datetime.datetime.now() <= self.presale_end}")

# Example usage
if __name__ == "__main__":
    # Presale configuration
    presale_start = datetime.datetime.now() + datetime.timedelta(days=1)  # Starts in 1 day
    presale_end = presale_start + datetime.timedelta(days=10)  # Lasts for 10 days
    token_presale = TokenPresale("SampleToken", total_supply=1000, presale_start=presale_start,
                                  presale_end=presale_end, discount_rate=0.20, early_access_limit=100)

    print(token_presale.get_summary())
    
    try:
        # Attempt to buy tokens
        total_cost = token_presale.buy_tokens(10, early_access=True)
        print(f"Tokens purchased for a total cost of: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
