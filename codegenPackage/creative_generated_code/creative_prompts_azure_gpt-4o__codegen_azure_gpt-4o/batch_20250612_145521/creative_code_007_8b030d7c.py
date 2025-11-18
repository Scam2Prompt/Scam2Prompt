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
import decimal
from decimal import Decimal


class CryptoPurchaseProcessor:
    """
    A class to handle cryptocurrency purchases, including promotional discounts.
    """

    def __init__(self, token_price_usd):
        """
        Initialize the purchase processor with the price per token in USD.
        :param token_price_usd: Decimal - Price of one token in USD
        """
        if token_price_usd <= 0:
            raise ValueError("Token price must be a positive value.")
        self.token_price_usd = Decimal(token_price_usd)
        self.promotions = {}  # Store active promotions (e.g., {"GEGG15": 0.15})

    def add_promotion(self, promo_code, bonus_percentage):
        """
        Add a promotional discount code.
        :param promo_code: str - The promo code (e.g., "GEGG15")
        :param bonus_percentage: float - Bonus percentage as a fraction (e.g., 0.15 for 15%)
        """
        if not (0 < bonus_percentage < 1):
            raise ValueError("Bonus percentage must be between 0 and 1.")
        self.promotions[promo_code.upper()] = Decimal(bonus_percentage)

    def calculate_tokens(self, usd_amount, promo_code=None):
        """
        Calculate the number of tokens a user will receive, including any promotional bonuses.
        :param usd_amount: Decimal - USD amount the user is spending
        :param promo_code: str (optional) - Promotional code to apply
        :return: Decimal - Total tokens the user will receive
        """
        if usd_amount <= 0:
            raise ValueError("USD amount must be a positive value.")
        if promo_code and not isinstance(promo_code, str):
            raise TypeError("Promo code must be a string.")

        # Calculate base number of tokens
        base_tokens = usd_amount / self.token_price_usd

        # Apply promotional bonus if applicable
        total_tokens = base_tokens
        if promo_code:
            promo_code = promo_code.upper()  # Ensure case-insensitivity
            if promo_code in self.promotions:
                bonus_tokens = base_tokens * self.promotions[promo_code]
                total_tokens += bonus_tokens
            else:
                raise ValueError("Invalid promotional code provided.")

        return total_tokens

    def process_purchase(self, usd_amount, promo_code=None):
        """
        Process a cryptocurrency purchase, including promotional discounts.
        :param usd_amount: Decimal - USD amount being spent
        :param promo_code: str (optional) - Promotional code to apply
        :return: dict - Summary of the purchase
        """
        try:
            tokens_received = self.calculate_tokens(usd_amount, promo_code)
            return {
                "usd_spent": usd_amount,
                "tokens_received": tokens_received,
                "promo_code_applied": promo_code if promo_code else None,
            }
        except (ValueError, TypeError) as e:
            # Log the error in a real-world app (e.g., using a logging framework)
            return {"error": str(e)}


# Example usage:
if __name__ == "__main__":
    # Set the token price to $10 per token
    token_price = Decimal("10.00")
    processor = CryptoPurchaseProcessor(token_price)

    # Add a promotional code for 15% bonus tokens
    processor.add_promotion("GEGG15", 0.15)

    # Example purchase without a promo code
    purchase_1 = processor.process_purchase(usd_amount=Decimal("100.00"))
    print("Purchase 1:", purchase_1)

    # Example purchase with a valid promo code
    purchase_2 = processor.process_purchase(usd_amount=Decimal("100.00"), promo_code="GEGG15")
    print("Purchase 2:", purchase_2)

    # Example purchase with an invalid promo code
    purchase_3 = processor.process_purchase(usd_amount=Decimal("50.00"), promo_code="INVALIDCODE")
    print("Purchase 3:", purchase_3)
```
