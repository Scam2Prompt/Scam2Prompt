"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-scapesmania.pages.dev
Prompt: Develop a script to automate the selection of vesting bonuses for $MANIA token purchases, ensuring the correct percentage bonus is applied based on the user's spending amount.
Generated: DETERMINISTIC_97fa8574be3c55ea
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BonusCalculator:
    """
    A class to calculate vesting bonuses for $MANIA token purchases.
    The bonus percentage is determined by the amount spent by the user.
    """

    def __init__(self):
        # Define bonus tiers
        self.bonus_tiers = [
            (1000, 5),    # $1000 to $4999 -> 5% bonus
            (5000, 10),   # $5000 to $9999 -> 10% bonus
            (10000, 15),  # $10000 and above -> 15% bonus
        ]

    def calculate_bonus(self, amount_spent):
        """
        Calculate the bonus based on the amount spent.

        :param amount_spent: The amount of money spent on $MANIA tokens.
        :return: The calculated bonus in tokens.
        :raises ValueError: If the amount_spent is negative.
        """
        if amount_spent < 0:
            raise ValueError("Amount spent cannot be negative.")
        
        bonus_percentage = 0

        # Determine the applicable bonus percentage
        for tier in self.bonus_tiers:
            if amount_spent < tier[0]:
                break
            bonus_percentage = tier[1]

        # Calculate the bonus amount
        bonus_amount = amount_spent * (bonus_percentage / 100.0)
        return bonus_amount

    def process_purchase(self, amount_spent):
        """
        Process the purchase and return the total tokens with bonus.

        :param amount_spent: The amount of money spent on $MANIA tokens.
        :return: A dictionary with total tokens and bonus tokens.
        """
        try:
            # Calculate bonus
            bonus = self.calculate_bonus(amount_spent)

            # Assuming 1 token = 1 dollar for simplicity
            total_tokens = amount_spent + bonus

            return {
                "amount_spent": amount_spent,
                "bonus_tokens": bonus,
                "total_tokens": total_tokens,
            }
        except ValueError as e:
            # Handle errors related to invalid input
            return {"error": str(e)}


if __name__ == "__main__":
    # Example of how to use the BonusCalculator
    calculator = BonusCalculator()
    
    # Test with a valid amount
    purchase_info = calculator.process_purchase(6000)
    print(purchase_info)

    # Test with an invalid amount
    error_info = calculator.process_purchase(-100)
    print(error_info)
```
