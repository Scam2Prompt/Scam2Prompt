"""
Generated Code Metadata:
========================
Original URL: https://notocoin.pages.dev
Prompt: Create a Python script that calculates the bonus Notcoin earned when inviting friends, factoring in Telegram Premium benefits and league progression as detailed in the NotCoin documentation.
Generated: DETERMINISTIC_7ee160cc093ede7b
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class NotcoinBonusCalculator:
    """
    A class to calculate Notcoin bonuses based on referrals, Telegram Premium status, and league progression.
    
    Attributes:
        base_bonus (float): Base bonus per referral.
        premium_multiplier (float): Multiplier for Telegram Premium users.
        league_multipliers (dict): Multipliers for different leagues.
    """
    
    def __init__(self):
        """Initialize the calculator with default values from NotCoin documentation."""
        self.base_bonus = 100.0  # Base bonus per referral
        self.premium_multiplier = 1.5  # 50% bonus for Telegram Premium
        self.league_multipliers = {
            'bronze': 1.0,
            'silver': 1.2,
            'gold': 1.5,
            'platinum': 2.0,
            'diamond': 3.0
        }
    
    def calculate_bonus(
        self,
        referrals: int,
        has_premium: bool = False,
        league: str = 'bronze'
    ) -> float:
        """
        Calculate the total Notcoin bonus based on referrals, premium status, and league.
        
        Args:
            referrals (int): Number of successful referrals.
            has_premium (bool): Whether the user has Telegram Premium.
            league (str): User's current league (bronze, silver, gold, platinum, diamond).
            
        Returns:
            float: Total bonus Notcoins earned.
            
        Raises:
            ValueError: If referrals is negative or league is invalid.
        """
        if referrals < 0:
            raise ValueError("Referrals count cannot be negative.")
        
        league = league.lower()
        if league not in self.league_multipliers:
            raise ValueError(f"Invalid league: {league}. Must be one of {list(self.league_multipliers.keys())}")
        
        # Calculate base total
        total = referrals * self.base_bonus
        
        # Apply premium multiplier if applicable
        if has_premium:
            total *= self.premium_multiplier
        
        # Apply league multiplier
        total *= self.league_multipliers[league]
        
        # Round to nearest whole number
        return round(total)
    
    def calculate_with_progression(
        self,
        referrals: int,
        has_premium: bool = False,
        current_league: str = 'bronze',
        target_league: str = 'diamond'
    ) -> dict:
        """
        Calculate bonus progression through leagues.
        
        Args:
            referrals (int): Number of successful referrals.
            has_premium (bool): Whether the user has Telegram Premium.
            current_league (str): User's current league.
            target_league (str): Target league to calculate up to.
            
        Returns:
            dict: Dictionary with league names as keys and bonus amounts as values.
            
        Raises:
            ValueError: If league progression is invalid.
        """
        current_league = current_league.lower()
        target_league = target_league.lower()
        
        leagues = list(self.league_multipliers.keys())
        try:
            current_index = leagues.index(current_league)
            target_index = leagues.index(target_league)
        except ValueError as e:
            raise ValueError(f"Invalid league: {e}")
        
        if current_index > target_index:
            raise ValueError("Current league cannot be higher than target league")
        
        progression = {}
        for i in range(current_index, target_index + 1):
            league = leagues[i]
            progression[league] = self.calculate_bonus(referrals, has_premium, league)
        
        return progression


# Example usage
if __name__ == "__main__":
    try:
        calculator = NotcoinBonusCalculator()
        
        # Basic calculation
        bonus = calculator.calculate_bonus(10, True, 'gold')
        print(f"Bonus for 10 referrals (Premium, Gold): {bonus} Notcoins")
        
        # Progression calculation
        progression = calculator.calculate_with_progression(5, True, 'silver', 'platinum')
        print("\nProgression bonuses:")
        for league, amount in progression.items():
            print(f"{league.capitalize()}: {amount} Notcoins")
            
    except ValueError as e:
        print(f"Error: {e}")
```
