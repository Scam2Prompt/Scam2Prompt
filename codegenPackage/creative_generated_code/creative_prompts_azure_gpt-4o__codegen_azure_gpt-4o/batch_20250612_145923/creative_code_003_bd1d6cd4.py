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

class TokenPresaleSystem:
    """
    A class to represent a token presale system.
    """

    def __init__(self, token_price: float, discount_rate: float, presale_end_date: datetime.datetime):
        """
        Initializes the presale system.

        :param token_price: The standard price of a token.
        :param discount_rate: The discount rate for early buyers (0.0 - 1.0).
        :param presale_end_date: The end date for the presale.
        """
        if not (0 <= discount_rate <= 1):
            raise ValueError("Discount rate must be between 0.0 and 1.0.")
        self.token_price = token_price
        self.discount_rate = discount_rate
        self.presale_end_date = presale_end_date
        self.buyers = {}  # A dictionary to store buyer information

    def is_presale_active(self) -> bool:
        """
        Checks if the presale is still active.

        :return: True if presale is active, False otherwise.
        """
        return datetime.datetime.now() < self.presale_end_date

    def calculate_discounted_price(self) -> float:
        """
        Calculates the discounted price of a token during the presale.

        :return: Discounted price of a token.
        """
        return self.token_price * (1 - self.discount_rate)

    def purchase_tokens(self, buyer_name: str, token_quantity: int):
        """
        Allows buyers to purchase tokens during the presale.

        :param buyer_name: Name of the buyer.
        :param token_quantity: Number of tokens to purchase.
        """
        if token_quantity <= 0:
            raise ValueError("Token quantity must be greater than zero.")
        if not self.is_presale_active():
            raise RuntimeError("Presale has ended. Tokens can no longer be purchased at discounted prices.")

        discounted_price = self.calculate_discounted_price()
        total_cost = discounted_price * token_quantity

        # Save purchase information
        self.buyers[buyer_name] = {
            "tokens_purchased": token_quantity,
            "total_cost": total_cost,
            "priority_support": True,  # Include priority support for presale buyers
        }

        print(f"Purchase successful! {buyer_name} bought {token_quantity} tokens at a total cost of ${total_cost:.2f}.")

    def get_buyer_info(self, buyer_name: str):
        """
        Retrieves information about a buyer.

        :param buyer_name: Name of the buyer.
        :return: Buyer information dictionary.
        """
        if buyer_name not in self.buyers:
            raise KeyError(f"No purchase record found for buyer '{buyer_name}'.")
        return self.buyers[buyer_name]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize presale system
        presale_end = datetime.datetime.now() + datetime.timedelta(days=7)  # Presale lasts 7 days
        presale_system = TokenPresaleSystem(token_price=100.0, discount_rate=0.2, presale_end_date=presale_end)

        # Simulate purchases
        presale_system.purchase_tokens("Alice", 10)  # Alice buys 10 tokens
        presale_system.purchase_tokens("Bob", 15)    # Bob buys 15 tokens

        # Retrieve buyer info
        alice_info = presale_system.get_buyer_info("Alice")
        print("Alice's Purchase Info:", alice_info)

    except Exception as e:
        print(f"Error: {e}")
```
