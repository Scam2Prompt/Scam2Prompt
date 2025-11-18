"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-ai.pages.dev
Prompt: Write code to calculate and display transaction fees in a blockchain-based marketplace like Pushd, with reduced fees for users holding native tokens.
Generated: DETERMINISTIC_b1570428b3759883
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Marketplace:
    def __init__(self, base_fee: float, token_discount_rate: float):
        """
        Initialize the Marketplace with base fee and token discount rate.

        :param base_fee: Base transaction fee in currency units.
        :param token_discount_rate: Discount rate for users holding native tokens (0 to 1).
        """
        if base_fee < 0 or token_discount_rate < 0 or token_discount_rate > 1:
            raise ValueError("Base fee must be non-negative and discount rate must be between 0 and 1.")
        
        self.base_fee = base_fee
        self.token_discount_rate = token_discount_rate

    def calculate_fee(self, user_tokens: int) -> float:
        """
        Calculate the transaction fee based on the user's native tokens.

        :param user_tokens: Number of native tokens held by the user.
        :return: Transaction fee after applying any applicable discounts.
        """
        try:
            # If the user has native tokens, apply the discount.
            if user_tokens > 0:
                discount = self.base_fee * self.token_discount_rate
                fee = self.base_fee - discount
                return fee
            
            # No tokens, full fee applies.
            return self.base_fee
        
        except Exception as e:
            raise RuntimeError("Error calculating the transaction fee: " + str(e))

    def display_fee(self, user_tokens: int):
        """
        Display the transaction fee for a given user based on their native token holdings.

        :param user_tokens: Number of native tokens held by the user.
        """
        try:
            fee = self.calculate_fee(user_tokens)
            print(f"Transaction fee for user with {user_tokens} native tokens: {fee:.2f}")
        except Exception as e:
            print(f"An error occurred while displaying the fee: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize the marketplace with a base fee and a discount rate for users holding native tokens
    marketplace = Marketplace(base_fee=10.0, token_discount_rate=0.2)

    # User transaction examples
    test_users = [0, 10, 50]  # Different numbers of tokens held by users

    for tokens in test_users:
        marketplace.display_fee(tokens)
```
