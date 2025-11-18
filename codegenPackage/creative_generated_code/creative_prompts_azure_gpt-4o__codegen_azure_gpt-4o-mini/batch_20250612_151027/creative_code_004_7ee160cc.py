"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notocoin.pages.dev
Prompt: Create a Python script that calculates the bonus Notcoin earned when inviting friends, factoring in Telegram Premium benefits and league progression as detailed in the NotCoin documentation.
Generated: DETERMINISTIC_7ee160cc093ede7b
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# notcoin_bonus_calculator.py

class NotCoinBonusCalculator:
    """
    A class to calculate Notcoin bonuses based on user invitations,
    Telegram Premium status, and league progression.
    """

    def __init__(self, base_bonus, premium_multiplier, league_factor):
        """
        Initializes the bonus calculator with specific parameters.

        :param base_bonus: Base bonus per invited friend
        :param premium_multiplier: Multiplier for Telegram Premium users
        :param league_factor: Factor based on league progression
        """
        self.base_bonus = base_bonus
        self.premium_multiplier = premium_multiplier
        self.league_factor = league_factor

    def calculate_bonus(self, friends_invited, is_premium, league_level):
        """
        Calculates the Notcoin bonus earned from inviting friends.

        :param friends_invited: Number of friends invited
        :param is_premium: Boolean indicating if the user has Telegram Premium
        :param league_level: Level of the user's league
        :return: Total Notcoin bonus
        """
        if friends_invited < 0:
            raise ValueError("Number of friends invited cannot be negative.")
        if league_level < 0:
            raise ValueError("League level cannot be negative.")

        # Determine bonus multiplier based on Telegram Premium status
        multiplier = self.premium_multiplier if is_premium else 1

        # Calculate base bonus considering league progression
        league_bonus = self.league_factor * league_level

        # Calculate total bonus
        total_bonus = (self.base_bonus + league_bonus) * multiplier * friends_invited
        return total_bonus

def main():
    """
    Main function to execute the bonus calculation.
    """
    # Example parameters
    base_bonus = 10  # Base bonus per invitation
    premium_multiplier = 1.5  # 50% more bonus for premium users
    league_factor = 2  # Bonus increase per league level

    # Create a bonus calculator instance
    calculator = NotCoinBonusCalculator(base_bonus, premium_multiplier, league_factor)

    # Example input values
    friends_invited = 5
    is_premium = True
    league_level = 3

    try:
        # Calculate the bonus and print the result
        bonus = calculator.calculate_bonus(friends_invited, is_premium, league_level)
        print(f"Total Notcoin bonus earned: {bonus}")
    except ValueError as e:
        print(f"Error calculating bonus: {e}")

if __name__ == "__main__":
    main()
```
