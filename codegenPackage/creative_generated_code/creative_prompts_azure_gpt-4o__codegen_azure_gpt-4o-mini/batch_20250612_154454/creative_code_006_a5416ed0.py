"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswaps.us.com
Prompt: Create a function to manage promotional offers, such as "Nạp Tiền Cho Lần Đầu Nhận Thưởng 200%" (200% bonus on first deposit), for an online casino platform.
Generated: DETERMINISTIC_a5416ed060b3e688
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PromotionalOffer:
    """
    A class to manage promotional offers for an online casino platform.
    """

    def __init__(self, offer_name: str, bonus_percentage: float, is_first_deposit_only: bool):
        """
        Initialize a new promotional offer.

        :param offer_name: Name of the promotional offer.
        :param bonus_percentage: Percentage of bonus being offered.
        :param is_first_deposit_only: Boolean indicating if the offer is valid for first deposits only.
        """
        self.offer_name = offer_name
        self.bonus_percentage = bonus_percentage
        self.is_first_deposit_only = is_first_deposit_only

    def calculate_bonus(self, deposit_amount: float, is_first_deposit: bool) -> float:
        """
        Calculate the bonus amount based on the deposit.

        :param deposit_amount: The amount of money deposited.
        :param is_first_deposit: Boolean indicating if this is the user's first deposit.
        :return: The calculated bonus amount.
        """
        # Validate inputs
        if deposit_amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        if not isinstance(is_first_deposit, bool):
            raise TypeError("is_first_deposit must be a boolean value.")
        
        # Check if offer is applicable
        if self.is_first_deposit_only and not is_first_deposit:
            return 0.0  # No bonus for subsequent deposits
        
        # Calculate the bonus
        bonus_amount = (self.bonus_percentage / 100) * deposit_amount
        return bonus_amount

    def __str__(self):
        """
        Return a string representation of the promotional offer.
        """
        return f"{self.offer_name}: {self.bonus_percentage}% bonus on first deposit only: {self.is_first_deposit_only}"

# Example usage:
if __name__ == '__main__':
    try:
        # Creating a promotional offer for first deposit bonus
        first_deposit_offer = PromotionalOffer("Nạp Tiền Cho Lần Đầu Nhận Thưởng 200%", 200.0, True)

        # Simulating a first deposit
        deposit_amount = 100.0  # Amount deposited
        is_first_deposit = True  # This is the user's first deposit

        # Calculating the bonus
        bonus = first_deposit_offer.calculate_bonus(deposit_amount, is_first_deposit)
        print(f"Bonus for the deposit: {bonus:.2f}")
    
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
