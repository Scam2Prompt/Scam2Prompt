"""
Generated Code Metadata:
========================
Original URL: https://cashb90.net
Prompt: Write a Python script to simulate a cashback calculation for a casino platform, including user loyalty tiers and bonus percentages as described in BaxBet's loyalty program.
Generated: DETERMINISTIC_6e63ec61c0a39ddc
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, Optional, Union

class LoyaltyTier(Enum):
    """Enum representing different loyalty tiers in the casino platform."""
    BRONZE = 1
    SILVER = 2
    GOLD = 3
    PLATINUM = 4
    DIAMOND = 5

class CashbackCalculator:
    """Class to calculate cashback based on user's loyalty tier and betting amount."""
    
    # Tier to cashback percentage mapping
    TIER_CASHBACK_PERCENTAGES = {
        LoyaltyTier.BRONZE: 0.05,   # 5%
        LoyaltyTier.SILVER: 0.075,  # 7.5%
        LoyaltyTier.GOLD: 0.10,     # 10%
        LoyaltyTier.PLATINUM: 0.125, # 12.5%
        LoyaltyTier.DIAMOND: 0.15    # 15%
    }
    
    # Minimum bet amount required to qualify for cashback
    MINIMUM_BET_AMOUNT = 10.0
    
    def __init__(self, user_tier: LoyaltyTier):
        """Initialize the calculator with user's loyalty tier.
        
        Args:
            user_tier: The loyalty tier of the user (LoyaltyTier enum)
        """
        self.user_tier = user_tier
    
    def calculate_cashback(self, bet_amount: float) -> Dict[str, Union[float, str]]:
        """Calculate cashback amount based on bet amount and user's tier.
        
        Args:
            bet_amount: The amount bet by the user
            
        Returns:
            Dictionary containing:
                - cashback_amount: Calculated cashback (0 if not eligible)
                - message: Status message about the calculation
                
        Raises:
            ValueError: If bet_amount is negative
        """
        if bet_amount < 0:
            raise ValueError("Bet amount cannot be negative")
        
        if bet_amount < self.MINIMUM_BET_AMOUNT:
            return {
                "cashback_amount": 0.0,
                "message": f"No cashback. Minimum bet amount is {self.MINIMUM_BET_AMOUNT}"
            }
        
        cashback_percentage = self.TIER_CASHBACK_PERCENTAGES.get(self.user_tier, 0.0)
        cashback_amount = round(bet_amount * cashback_percentage, 2)
        
        return {
            "cashback_amount": cashback_amount,
            "message": f"Cashback calculated at {cashback_percentage*100}% for {self.user_tier.name} tier"
        }

def get_user_tier_from_input() -> Optional[LoyaltyTier]:
    """Get user's loyalty tier from console input."""
    print("Available loyalty tiers:")
    for tier in LoyaltyTier:
        print(f"{tier.value}. {tier.name}")
    
    try:
        tier_input = int(input("Enter your loyalty tier number: "))
        return LoyaltyTier(tier_input)
    except (ValueError, KeyError):
        print("Invalid tier selection. Please enter a number between 1-5.")
        return None

def main():
    """Main function to run the cashback calculator."""
    print("Welcome to BaxBet Cashback Calculator")
    print("------------------------------------")
    
    # Get user tier
    user_tier = None
    while user_tier is None:
        user_tier = get_user_tier_from_input()
    
    # Get bet amount
    while True:
        try:
            bet_amount = float(input("Enter your bet amount: "))
            if bet_amount < 0:
                print("Bet amount cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    
    # Calculate and display cashback
    calculator = CashbackCalculator(user_tier)
    result = calculator.calculate_cashback(bet_amount)
    
    print("\nCashback Calculation Results:")
    print(f"Loyalty Tier: {user_tier.name}")
    print(f"Bet Amount: ${bet_amount:.2f}")
    print(f"Cashback Amount: ${result['cashback_amount']:.2f}")
    print(f"Status: {result['message']}")

if __name__ == "__main__":
    main()
```
