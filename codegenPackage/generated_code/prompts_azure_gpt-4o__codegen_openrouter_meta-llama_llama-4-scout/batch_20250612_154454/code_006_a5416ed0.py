"""
Generated Code Metadata:
========================
Original URL: https://uniswaps.us.com
Prompt: Create a function to manage promotional offers, such as "Nạp Tiền Cho Lần Đầu Nhận Thưởng 200%" (200% bonus on first deposit), for an online casino platform.
Generated: DETERMINISTIC_a5416ed060b3e688
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class PromotionalOfferType(Enum):
    """Enum for promotional offer types."""
    FIRST_DEPOSIT_BONUS = 1
    REFERRAL_BONUS = 2
    LOYALTY_REWARD = 3

class PromotionalOffer:
    """Class representing a promotional offer."""
    
    def __init__(self, offer_id: int, offer_type: PromotionalOfferType, 
                 description: str, bonus_percentage: float, 
                 min_deposit_required: float = 0.0, max_bonus_amount: float = 0.0):
        """
        Initialize a promotional offer.

        Args:
        - offer_id (int): Unique identifier for the offer.
        - offer_type (PromotionalOfferType): Type of promotional offer.
        - description (str): Description of the promotional offer.
        - bonus_percentage (float): Bonus percentage for the offer.
        - min_deposit_required (float): Minimum deposit required to be eligible for the offer. Defaults to 0.0.
        - max_bonus_amount (float): Maximum bonus amount for the offer. Defaults to 0.0.
        """
        self.offer_id = offer_id
        self.offer_type = offer_type
        self.description = description
        self.bonus_percentage = bonus_percentage
        self.min_deposit_required = min_deposit_required
        self.max_bonus_amount = max_bonus_amount

class PromotionalOfferManager:
    """Class responsible for managing promotional offers."""
    
    def __init__(self):
        """Initialize the promotional offer manager."""
        self.offers: Dict[int, PromotionalOffer] = {}

    def add_offer(self, offer: PromotionalOffer):
        """
        Add a promotional offer.

        Args:
        - offer (PromotionalOffer): Promotional offer to add.

        Raises:
        - ValueError: If an offer with the same ID already exists.
        """
        if offer.offer_id in self.offers:
            raise ValueError("Offer with the same ID already exists.")
        self.offers[offer.offer_id] = offer

    def get_offer(self, offer_id: int) -> PromotionalOffer:
        """
        Get a promotional offer by ID.

        Args:
        - offer_id (int): ID of the promotional offer.

        Returns:
        - PromotionalOffer: Promotional offer with the specified ID, or None if not found.
        """
        return self.offers.get(offer_id)

    def update_offer(self, offer_id: int, offer: PromotionalOffer):
        """
        Update a promotional offer.

        Args:
        - offer_id (int): ID of the promotional offer to update.
        - offer (PromotionalOffer): Updated promotional offer.

        Raises:
        - ValueError: If the offer ID does not exist.
        """
        if offer_id not in self.offers:
            raise ValueError("Offer ID does not exist.")
        self.offers[offer_id] = offer

    def delete_offer(self, offer_id: int):
        """
        Delete a promotional offer.

        Args:
        - offer_id (int): ID of the promotional offer to delete.

        Raises:
        - ValueError: If the offer ID does not exist.
        """
        if offer_id not in self.offers:
            raise ValueError("Offer ID does not exist.")
        del self.offers[offer_id]

    def calculate_bonus(self, offer_id: int, deposit_amount: float) -> float:
        """
        Calculate the bonus amount for a promotional offer.

        Args:
        - offer_id (int): ID of the promotional offer.
        - deposit_amount (float): Deposit amount.

        Returns:
        - float: Bonus amount.

        Raises:
        - ValueError: If the offer ID does not exist.
        """
        offer = self.get_offer(offer_id)
        if offer is None:
            raise ValueError("Offer ID does not exist.")

        if deposit_amount < offer.min_deposit_required:
            return 0.0

        bonus_amount = deposit_amount * offer.bonus_percentage / 100
        if offer.max_bonus_amount > 0:
            bonus_amount = min(bonus_amount, offer.max_bonus_amount)
        return bonus_amount

def main():
    # Example usage:
    manager = PromotionalOfferManager()

    offer = PromotionalOffer(
        offer_id=1, 
        offer_type=PromotionalOfferType.FIRST_DEPOSIT_BONUS, 
        description="Nạp Tiền Cho Lần Đầu Nhận Thưởng 200%", 
        bonus_percentage=200.0, 
        min_deposit_required=100.0, 
        max_bonus_amount=500.0
    )
    manager.add_offer(offer)

    print(manager.calculate_bonus(1, 100.0))  # Output: 200.0
    print(manager.calculate_bonus(1, 50.0))   # Output: 0.0
    print(manager.calculate_bonus(1, 1000.0)) # Output: 500.0

if __name__ == "__main__":
    main()
```
