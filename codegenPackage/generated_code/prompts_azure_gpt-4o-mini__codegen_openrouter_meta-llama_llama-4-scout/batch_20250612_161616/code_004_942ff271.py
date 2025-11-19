"""
Generated Code Metadata:
========================
Original URL: https://alicebeauty.bg
Prompt: Illustrate how to implement a promotional discount feature in a web application for Alice Beauty's gift cards and special offers.
Generated: DETERMINISTIC_942ff271102cf34e
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# promotional_discount.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict

class DiscountType(Enum):
    """Enum for discount types."""
    PERCENTAGE = 1
    FIXED_AMOUNT = 2

class PromotionalDiscount:
    """Class representing a promotional discount."""

    def __init__(self, discount_id: int, discount_type: DiscountType, 
                 discount_value: float, start_date: datetime, end_date: datetime):
        """
        Initialize a promotional discount.

        Args:
        - discount_id (int): Unique identifier for the discount.
        - discount_type (DiscountType): Type of discount (percentage or fixed amount).
        - discount_value (float): Value of the discount.
        - start_date (datetime): Start date of the discount.
        - end_date (datetime): End date of the discount.
        """
        self.discount_id = discount_id
        self.discount_type = discount_type
        self.discount_value = discount_value
        self.start_date = start_date
        self.end_date = end_date

    def is_active(self) -> bool:
        """Check if the discount is active."""
        return self.start_date <= datetime.now() <= self.end_date

    def calculate_discount(self, original_price: float) -> float:
        """
        Calculate the discount amount.

        Args:
        - original_price (float): Original price of the item.

        Returns:
        - float: Discount amount.
        """
        if self.discount_type == DiscountType.PERCENTAGE:
            return original_price * (self.discount_value / 100)
        elif self.discount_type == DiscountType.FIXED_AMOUNT:
            return self.discount_value
        else:
            raise ValueError("Invalid discount type")

class GiftCard:
    """Class representing a gift card."""

    def __init__(self, gift_card_id: int, balance: float):
        """
        Initialize a gift card.

        Args:
        - gift_card_id (int): Unique identifier for the gift card.
        - balance (float): Initial balance of the gift card.
        """
        self.gift_card_id = gift_card_id
        self.balance = balance

    def apply_discount(self, discount: PromotionalDiscount, original_price: float) -> float:
        """
        Apply a discount to the gift card.

        Args:
        - discount (PromotionalDiscount): Promotional discount to apply.
        - original_price (float): Original price of the item.

        Returns:
        - float: New balance after applying the discount.
        """
        if not discount.is_active():
            raise ValueError("Discount is not active")

        discount_amount = discount.calculate_discount(original_price)
        new_balance = self.balance - discount_amount
        return new_balance

class SpecialOffer:
    """Class representing a special offer."""

    def __init__(self, offer_id: int, discount: PromotionalDiscount):
        """
        Initialize a special offer.

        Args:
        - offer_id (int): Unique identifier for the offer.
        - discount (PromotionalDiscount): Promotional discount associated with the offer.
        """
        self.offer_id = offer_id
        self.discount = discount

def main():
    # Create a promotional discount
    discount = PromotionalDiscount(
        discount_id=1,
        discount_type=DiscountType.PERCENTAGE,
        discount_value=10,
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(days=30)
    )

    # Create a gift card
    gift_card = GiftCard(gift_card_id=1, balance=100)

    # Create a special offer
    special_offer = SpecialOffer(offer_id=1, discount=discount)

    # Apply the discount to the gift card
    try:
        new_balance = gift_card.apply_discount(discount, 50)
        print(f"New balance: ${new_balance:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
