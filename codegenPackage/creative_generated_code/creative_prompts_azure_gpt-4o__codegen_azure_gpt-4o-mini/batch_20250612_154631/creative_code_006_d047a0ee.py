"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coindoor.trade
Prompt: Create a function to calculate user rankings and bonuses based on Coindoor's ranking system, including team investment and direct referrals.
Generated: DETERMINISTIC_d047a0ee7c1cf7c3
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RankCalculator:
    """
    A class to calculate user rankings and bonuses based on Coindoor's ranking system.
    """

    def __init__(self):
        """
        Initializes the RankCalculator with default values.
        """
        self.rankings = {
            "Bronze": (0, 1000),  # Rank from 0 to 1000
            "Silver": (1001, 5000),  # Rank from 1001 to 5000
            "Gold": (5001, 20000),  # Rank from 5001 to 20000
            "Platinum": (20001, float('inf')),  # Rank from 20001 and above
        }

    def calculate_ranking(self, investment, referral_count):
        """
        Calculates the ranking based on user investment and referrals.
        
        Parameters:
            investment (float): The total investment made by the user.
            referral_count (int): The number of direct referrals made by the user.
        
        Returns:
            str: The user's rank.
            float: The user's bonus.
        """
        try:
            if investment < 0 or referral_count < 0:
                raise ValueError("Investment and referral count must be non-negative.")

            # Calculate the user's base bonus based on investment.
            bonus = investment * 0.1  # 10% of the investment as bonus

            # Adjust bonus based on referral count
            if referral_count > 10:
                bonus += 100  # Extra bonus for more than 10 referrals
            elif referral_count > 5:
                bonus += 50  # Extra bonus for more than 5 referrals

            # Determine the rank based on investment
            rank = self.get_rank(investment)

            return rank, bonus
        except Exception as e:
            print(f"Error calculating ranking: {e}")
            return None, 0.0

    def get_rank(self, investment):
        """
        Determines the rank based on the investment amount.
        
        Parameters:
            investment (float): The total investment.
        
        Returns:
            str: The user's rank.
        """
        for rank, (min_investment, max_investment) in self.rankings.items():
            if min_investment <= investment <= max_investment:
                return rank
        return "Unknown Rank"

# Example usage
if __name__ == "__main__":
    rank_calculator = RankCalculator()
    user_investment = 3000  # Example investment
    user_referrals = 6  # Example referral count

    rank, bonus = rank_calculator.calculate_ranking(user_investment, user_referrals)
    print(f"User Rank: {rank}, Bonus: {bonus}")
```
