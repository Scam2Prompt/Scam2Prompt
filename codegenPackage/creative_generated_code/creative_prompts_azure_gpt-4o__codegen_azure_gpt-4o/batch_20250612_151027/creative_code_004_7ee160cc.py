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
"""
Script to calculate Notcoin bonus earned when inviting friends.
This script factors in Telegram Premium benefits and league progression.
"""

# Import necessary libraries
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants
BASE_BONUS = 10  # Base Notcoin reward for inviting a friend
PREMIUM_BONUS_MULTIPLIER = 1.5  # 50% extra bonus for Telegram Premium users
LEAGUE_BONUS_MULTIPLIERS = {
    "bronze": 1.0,   # No extra multiplier for Bronze league
    "silver": 1.2,   # 20% extra for Silver league
    "gold": 1.5,     # 50% extra for Gold league
    "platinum": 2.0  # 100% extra for Platinum league
}

def calculate_bonus(invites, is_premium, league):
    """
    Calculate the total Notcoin bonus earned based on the number of invites,
    Telegram Premium subscription status, and league progression.

    Args:
        invites (int): Number of friends invited.
        is_premium (bool): Whether the user has Telegram Premium.
        league (str): User's league (bronze, silver, gold, platinum).

    Returns:
        float: Total Notcoin bonus earned.
    """
    try:
        # Validate inputs
        if invites < 0:
            raise ValueError("Number of invites cannot be negative.")
        if league not in LEAGUE_BONUS_MULTIPLIERS:
            raise ValueError(f"Invalid league: {league}. Must be one of {list(LEAGUE_BONUS_MULTIPLIERS.keys())}.")

        # Calculate base bonus
        total_bonus = invites * BASE_BONUS

        # Apply Premium bonus multiplier if applicable
        if is_premium:
            total_bonus *= PREMIUM_BONUS_MULTIPLIER

        # Apply league bonus multiplier
        total_bonus *= LEAGUE_BONUS_MULTIPLIERS[league]

        return total_bonus

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    try:
        # Get user inputs
        invites = int(input("Enter the number of friends invited: "))
        is_premium = input("Are you a Telegram Premium user? (yes/no): ").strip().lower() == "yes"
        league = input("Enter your league (bronze, silver, gold, platinum): ").strip().lower()

        # Calculate bonus
        bonus = calculate_bonus(invites, is_premium, league)

        # Display results
        print(f"\nYou have earned a total bonus of {bonus:.2f} Notcoins!")
    except ValueError as ve:
        logging.error(f"Input error: {ve}")
    except Exception as e:
        logging.critical(f"Unhandled exception: {e}")
```
