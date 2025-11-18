"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethers-airdrops.net
Prompt: Develop a function for calculating rakeback and VIP program perks for crypto casinos, incorporating the bonuses and discounts mentioned on the Profit Zone website.
Generated: DETERMINISTIC_4bb4b899bc9faa3e
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, Optional

class CasinoRewardsCalculator:
    """
    A class to calculate rakeback and VIP program perks for crypto casinos.
    """
    
    def __init__(self, rakeback_percentage: float, vip_discount_tiers: Dict[int, float]):
        """
        Initialize the calculator with rakeback percentage and VIP discount tiers.

        :param rakeback_percentage: The percentage of rakeback (e.g., 5 for 5% rakeback).
        :param vip_discount_tiers: A dictionary where keys are VIP levels and values are discount percentages.
        """
        if not (0 <= rakeback_percentage <= 100):
            raise ValueError("Rakeback percentage must be between 0 and 100.")
        
        self.rakeback_percentage = rakeback_percentage
        self.vip_discount_tiers = vip_discount_tiers

    def calculate_rakeback(self, wager_amount: float) -> float:
        """
        Calculate the rakeback amount based on wagered amount.

        :param wager_amount: The total amount wagered by the user.
        :return: The amount of rakeback earned.
        """
        if wager_amount < 0:
            raise ValueError("Wager amount must be non-negative.")
        
        rakeback = (self.rakeback_percentage / 100) * wager_amount
        return round(rakeback, 2)

    def get_vip_discount(self, vip_level: int) -> Optional[float]:
        """
        Get the discount percentage for a given VIP level.

        :param vip_level: The VIP level of the user.
        :return: The discount percentage for that VIP level, or None if level does not exist.
        """
        return self.vip_discount_tiers.get(vip_level)

    def calculate_total_rewards(self, wager_amount: float, vip_level: int) -> Dict[str, float]:
        """
        Calculate the total rewards, including rakeback and VIP discount.

        :param wager_amount: The total amount wagered by the user.
        :param vip_level: The VIP level of the user.
        :return: A dictionary with rakeback amount, VIP discount percentage, and total savings.
        """
        if wager_amount < 0:
            raise ValueError("Wager amount must be non-negative.")
        if vip_level < 0:
            raise ValueError("VIP level must be non-negative.")

        # Calculate rakeback
        rakeback = self.calculate_rakeback(wager_amount)

        # Get VIP discount
        vip_discount_percentage = self.get_vip_discount(vip_level)
        vip_discount_amount = 0.0
        
        if vip_discount_percentage is not None:
            vip_discount_amount = (vip_discount_percentage / 100) * wager_amount

        # Calculate total savings
        total_savings = rakeback + vip_discount_amount

        return {
            "rakeback_amount": round(rakeback, 2),
            "vip_discount_percentage": vip_discount_percentage if vip_discount_percentage is not None else 0.0,
            "vip_discount_amount": round(vip_discount_amount, 2),
            "total_savings": round(total_savings, 2)
        }

# Example usage:
if __name__ == "__main__":
    # Initialize the rewards calculator with 5% rakeback and VIP discounts
    vip_tiers = {
        1: 2.5,  # VIP level 1 gets 2.5% discount
        2: 5.0,  # VIP level 2 gets 5% discount
        3: 7.5   # VIP level 3 gets 7.5% discount
    }
    calculator = CasinoRewardsCalculator(rakeback_percentage=5.0, vip_discount_tiers=vip_tiers)

    # Calculate rewards for a user who wagered 1000 units and is at VIP level 2
    rewards = calculator.calculate_total_rewards(wager_amount=1000, vip_level=2)
    print("Rewards Breakdown:", rewards)
```
