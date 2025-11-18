"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalenest-goodeggtoken.web.app
Prompt: Write code to integrate a promotional discount feature (e.g., 15% bonus tokens) into a cryptocurrency purchase flow, similar to the $GEGG promo code functionality.
Generated: DETERMINISTIC_8b030d7ca8f4c3d6
Batch ID: 20250612_145521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CryptoPurchase:
    def __init__(self):
        self.token_price = 1.0  # Price per token in USD
        self.bonus_percentage = 0.15  # 15% bonus tokens for promotions

    def apply_discount(self, amount, promo_code=None):
        """
        Apply a promotional discount if a valid promo code is provided.

        :param amount: The total amount of cryptocurrency to purchase in dollars.
        :param promo_code: Optional promo code to apply for bonus tokens.
        :return: Total tokens purchased including any bonuses.
        """
        try:
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")

            tokens = amount / self.token_price  # Calculate base tokens

            # Check for promo code
            if promo_code == "$GEGG":
                bonus_tokens = tokens * self.bonus_percentage
                tokens += bonus_tokens  # Add bonus tokens
                print(f"Promo code applied! You received an additional {bonus_tokens:.2f} tokens.")

            return tokens

        except ValueError as ve:
            print(f"Input error: {ve}")
            return 0.0
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return 0.0

    def purchase_tokens(self, amount, promo_code=None):
        """
        Handle the purchase of tokens, applying any discounts as necessary.

        :param amount: The total amount of cryptocurrency to purchase in dollars.
        :param promo_code: Optional promo code to apply for bonus tokens.
        :return: Confirmation message with total tokens purchased.
        """
        tokens = self.apply_discount(amount, promo_code)
        if tokens > 0:
            return f"Successfully purchased {tokens:.2f} tokens."
        else:
            return "Purchase failed. Please check the amount and promo code."

# Example usage
if __name__ == "__main__":
    purchase_flow = CryptoPurchase()
    
    # Sample purchase with promo code
    print(purchase_flow.purchase_tokens(100, "$GEGG"))
    
    # Sample purchase without promo code
    print(purchase_flow.purchase_tokens(100))
    
    # Invalid purchase example
    print(purchase_flow.purchase_tokens(-50, "$GEGG"))
```
