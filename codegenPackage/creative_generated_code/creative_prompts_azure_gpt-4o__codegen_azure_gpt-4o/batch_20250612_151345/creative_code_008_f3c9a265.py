"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegaincapital.com
Prompt: Create a ranking badge system for users based on their investment activity, as described in The Gain Capital's ranking system.
Generated: DETERMINISTIC_f3c9a26575b5e8c5
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Ranking Badge System for Users Based on Investment Activity
This program assigns ranking badges to users based on their investment activity.
Ranks include: Bronze, Silver, Gold, Platinum, and Diamond.

Criteria:
- Bronze: Investment < $1,000
- Silver: Investment >= $1,000 and < $10,000
- Gold: Investment >= $10,000 and < $50,000
- Platinum: Investment >= $50,000 and < $100,000
- Diamond: Investment >= $100,000
"""

# Import necessary modules
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RankingSystem:
    """
    Class to manage ranking badge system based on investment activity.
    """

    def __init__(self):
        """
        Initialize the ranking system with predefined thresholds.
        """
        self.ranks = {
            "Bronze": (0, 999),
            "Silver": (1000, 9999),
            "Gold": (10000, 49999),
            "Platinum": (50000, 99999),
            "Diamond": (100000, float('inf'))
        }

    def get_rank(self, investment_amount):
        """
        Determine the rank of a user based on their investment amount.

        :param investment_amount: float, The user's total investment amount.
        :return: str, The rank of the user.
        """
        try:
            if investment_amount < 0:
                raise ValueError("Investment amount cannot be negative.")
            
            # Iterate over rank thresholds to determine the rank
            for rank, (lower, upper) in self.ranks.items():
                if lower <= investment_amount <= upper:
                    return rank
            
            # Fallback (should never happen)
            return "Unknown"

        except ValueError as e:
            logging.error(f"Invalid investment amount: {investment_amount}. Error: {e}")
            return "Error"

def main():
    """
    Main function to test the ranking system.
    """
    # Sample user investment data
    user_investments = {
        "Alice": 500,
        "Bob": 7500,
        "Charlie": 32000,
        "Diana": 87000,
        "Edward": 150000,
        "Frank": -500  # Invalid data for testing
    }

    ranking_system = RankingSystem()

    for user, investment in user_investments.items():
        rank = ranking_system.get_rank(investment)
        if rank != "Error":
            logging.info(f"User: {user}, Investment: ${investment}, Rank: {rank}")
        else:
            logging.info(f"User: {user}, Investment: ${investment}, Rank: Unable to determine (Error).")

if __name__ == "__main__":
    main()
```
