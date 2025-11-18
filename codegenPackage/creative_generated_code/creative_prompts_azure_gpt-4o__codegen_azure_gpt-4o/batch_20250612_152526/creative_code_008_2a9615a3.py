"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betpandaofficial.com
Prompt: Develop a promotional campaign system in code that tracks bonuses and cashback offers, inspired by Betpanda's generous promotions.
Generated: DETERMINISTIC_2a9615a3ca8f99ba
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# promotional_campaign_system.py

from datetime import datetime, timedelta

class Promotion:
    """
    Class representing a single promotion with bonuses and cashback offers.
    """
    def __init__(self, name, bonus_amount, cashback_percentage, start_date, end_date):
        """
        Initialize a new Promotion instance.
        
        :param name: Name of the promotion.
        :param bonus_amount: Fixed bonus amount (in currency units).
        :param cashback_percentage: Percentage of cashback on eligible transactions.
        :param start_date: Start date of the promotion (datetime object).
        :param end_date: End date of the promotion (datetime object).
        """
        self.name = name
        self.bonus_amount = bonus_amount
        self.cashback_percentage = cashback_percentage
        self.start_date = start_date
        self.end_date = end_date

    def is_active(self):
        """
        Check if the promotion is currently active.
        
        :return: True if active, False otherwise.
        """
        current_date = datetime.now()
        return self.start_date <= current_date <= self.end_date


class PromotionalCampaignSystem:
    """
    System to manage and track promotional campaigns.
    """
    def __init__(self):
        """
        Initialize the promotional campaign system with no promotions.
        """
        self.promotions = []

    def add_promotion(self, promotion):
        """
        Add a new promotion to the system.
        
        :param promotion: Instance of the Promotion class.
        """
        if not isinstance(promotion, Promotion):
            raise TypeError("promotion must be an instance of Promotion")
        self.promotions.append(promotion)

    def list_active_promotions(self):
        """
        List all active promotions.
        
        :return: List of active Promotion instances.
        """
        return [promo for promo in self.promotions if promo.is_active()]

    def calculate_cashback(self, promotion_name, transaction_amount):
        """
        Calculate cashback for a given promotion and transaction amount.
        
        :param promotion_name: Name of the promotion being applied.
        :param transaction_amount: Amount of the transaction (in currency units).
        :return: Cashback amount (in currency units).
        """
        promotion = next(
            (promo for promo in self.promotions if promo.name == promotion_name),
            None
        )
        if promotion is None:
            raise ValueError(f"No promotion found with name '{promotion_name}'")
        if not promotion.is_active():
            raise ValueError(f"Promotion '{promotion_name}' is not currently active")
        return (transaction_amount * promotion.cashback_percentage) / 100

    def claim_bonus(self, promotion_name):
        """
        Claim the bonus for a given promotion.
        
        :param promotion_name: Name of the promotion being claimed.
        :return: Bonus amount (in currency units).
        """
        promotion = next(
            (promo for promo in self.promotions if promo.name == promotion_name),
            None
        )
        if promotion is None:
            raise ValueError(f"No promotion found with name '{promotion_name}'")
        if not promotion.is_active():
            raise ValueError(f"Promotion '{promotion_name}' is not currently active")
        return promotion.bonus_amount


# Example Usage
if __name__ == "__main__":
    # Initialize the promotional campaign system
    campaign_system = PromotionalCampaignSystem()

    # Add promotions
    promo1 = Promotion(
        name="Holiday Bonus",
        bonus_amount=50,
        cashback_percentage=10,
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(days=7)
    )
    promo2 = Promotion(
        name="Weekend Special",
        bonus_amount=20,
        cashback_percentage=5,
        start_date=datetime.now() - timedelta(days=1),
        end_date=datetime.now() + timedelta(days=1)
    )

    campaign_system.add_promotion(promo1)
    campaign_system.add_promotion(promo2)

    # List active promotions
    print("Active Promotions:")
    for active_promo in campaign_system.list_active_promotions():
        print(f"- {active_promo.name}")

    # Calculate cashback
    try:
        cashback = campaign_system.calculate_cashback("Holiday Bonus", 200)
        print(f"Cashback for 'Holiday Bonus' on $200 transaction: ${cashback:.2f}")
    except ValueError as e:
        print(e)

    # Claim bonus
    try:
        bonus = campaign_system.claim_bonus("Weekend Special")
        print(f"Bonus claimed for 'Weekend Special': ${bonus:.2f}")
    except ValueError as e:
        print(e)
```
