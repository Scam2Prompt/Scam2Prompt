"""
Generated Code Metadata:
========================
Original URL: https://coindoor.trade
Prompt: Create a function to calculate user rankings and bonuses based on Coindoor's ranking system, including team investment and direct referrals.
Generated: DETERMINISTIC_d047a0ee7c1cf7c3
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class User:
    def __init__(self, id: int, team_investment: float = 0.0, direct_referrals: int = 0):
        """
        Initialize a User object.

        Args:
        id (int): Unique user ID.
        team_investment (float): Total team investment. Defaults to 0.0.
        direct_referrals (int): Number of direct referrals. Defaults to 0.
        """
        self.id = id
        self.team_investment = team_investment
        self.direct_referrals = direct_referrals

def calculate_ranking(team_investment: float) -> str:
    """
    Calculate user ranking based on team investment.

    Args:
    team_investment (float): Total team investment.

    Returns:
    str: User ranking.
    """
    if team_investment < 1000:
        return "Bronze"
    elif team_investment < 5000:
        return "Silver"
    elif team_investment < 10000:
        return "Gold"
    elif team_investment < 50000:
        return "Platinum"
    else:
        return "Diamond"

def calculate_bonus(user: User, direct_referral_bonus: float, team_investment_bonus: float) -> float:
    """
    Calculate user bonus based on direct referrals and team investment.

    Args:
    user (User): User object.
    direct_referral_bonus (float): Bonus per direct referral.
    team_investment_bonus (float): Bonus per unit of team investment.

    Returns:
    float: User bonus.
    """
    direct_referral_bonus_amount = user.direct_referrals * direct_referral_bonus
    team_investment_bonus_amount = user.team_investment * team_investment_bonus
    return direct_referral_bonus_amount + team_investment_bonus_amount

def process_users(users: List[User], direct_referral_bonus: float, team_investment_bonus: float) -> Dict[int, Dict[str, str]]:
    """
    Process a list of users and calculate their rankings and bonuses.

    Args:
    users (List[User]): List of User objects.
    direct_referral_bonus (float): Bonus per direct referral.
    team_investment_bonus (float): Bonus per unit of team investment.

    Returns:
    Dict[int, Dict[str, str]]: Dictionary of user IDs to their rankings and bonuses.
    """
    results = {}
    for user in users:
        try:
            ranking = calculate_ranking(user.team_investment)
            bonus = calculate_bonus(user, direct_referral_bonus, team_investment_bonus)
            results[user.id] = {
                "ranking": ranking,
                "bonus": f"{bonus:.2f}"  # Format bonus to 2 decimal places
            }
        except Exception as e:
            # Log the exception and continue processing other users
            print(f"Error processing user {user.id}: {str(e)}")
    return results

# Example usage:
if __name__ == "__main__":
    users = [
        User(1, team_investment=1500, direct_referrals=5),
        User(2, team_investment=8000, direct_referrals=10),
        User(3, team_investment=30000, direct_referrals=15)
    ]

    direct_referral_bonus = 10.0
    team_investment_bonus = 0.01

    results = process_users(users, direct_referral_bonus, team_investment_bonus)
    for user_id, result in results.items():
        print(f"User {user_id}: Ranking = {result['ranking']}, Bonus = {result['bonus']}")
```
