"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-en.pages.dev
Prompt: Write code to implement a discounted token presale feature for early adopters, as described in Pushd's presale perks.
Generated: DETERMINISTIC_ec9f5ba73c19ba51
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class TokenPresale:
    """
    A class to manage token presale with discounted rates available for early adopters.
    """

    def __init__(self, total_tokens, presale_start, presale_end, base_price, discount_rate):
        """
        Initialize the presale with necessary parameters.

        :param total_tokens: Total number of tokens available for presale.
        :param presale_start: Start datetime of the presale.
        :param presale_end: End datetime of the presale.
        :param base_price: Base price of a token in USD.
        :param discount_rate: Discount rate for early adopters (percentage).
        """
        self.total_tokens = total_tokens
        self.presale_start = presale_start
        self.presale_end = presale_end
        self.base_price = base_price
        self.discount_rate = discount_rate
        self.sold_tokens = 0

    def is_presale_active(self):
        """
        Check if the presale is currently active.

        :return: Boolean indicating whether the presale is active.
        """
        current_time = datetime.now()
        return self.presale_start <= current_time <= self.presale_end

    def calculate_price(self, quantity):
        """
        Calculate the price for the given quantity of tokens.

        :param quantity: The number of tokens to be purchased.
        :return: Total price with discount applied (if presale is active).
        """
        if not self.is_presale_active():
            # Full price when presale is not active
            return quantity * self.base_price
        
        # Apply discount during presale
        discounted_price = self.base_price * (1 - self.discount_rate / 100)
        return quantity * discounted_price

    def purchase_tokens(self, buyer, quantity):
        """
        Handle the purchase of tokens.

        :param buyer: The buyer's identifier (e.g., email, wallet address).
        :param quantity: The number of tokens to purchase.
        :return: Confirmation of the purchase or error if conditions aren't met.
        """
        # Validate presale status
        if not self.is_presale_active():
            raise Exception("Presale is not active. You cannot purchase tokens at this time.")
        
        # Validate quantity
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.total_tokens - self.sold_tokens:
            raise ValueError("Not enough tokens available for purchase.")
        
        # Process purchase
        total_price = self.calculate_price(quantity)
        self.sold_tokens += quantity
        self.total_tokens -= quantity
        
        # Simulate purchase confirmation
        return {
            "buyer": buyer,
            "quantity": quantity,
            "total_price": total_price,
            "message": "Purchase successful. Thank you for supporting the presale!"
        }

    def get_status(self):
        """
        Get the current status of the presale.

        :return: Dictionary containing current presale stats.
        """
        return {
            "presale_active": self.is_presale_active(),
            "total_tokens": self.total_tokens,
            "sold_tokens": self.sold_tokens,
            "presale_start": self.presale_start,
            "presale_end": self.presale_end
        }


# Example Usage
if __name__ == "__main__":
    # Define presale parameters
    presale_start = datetime.now()
    presale_end = presale_start + timedelta(days=7)  # Presale lasts for 7 days
    total_tokens = 10000
    base_price = 10  # $10 per token
    discount_rate = 20  # 20% discount during presale

    # Create presale instance
    presale = TokenPresale(total_tokens, presale_start, presale_end, base_price, discount_rate)

    # Example purchase
    try:
        buyer_id = "user@example.com"
        quantity = 100
        purchase_details = presale.purchase_tokens(buyer_id, quantity)
        print(purchase_details)
    except Exception as e:
        print(f"Error: {e}")

    # Print presale status
    status = presale.get_status()
    print(status)
```
