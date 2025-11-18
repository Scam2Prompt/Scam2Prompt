"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Write a script to calculate and distribute jackpot winnings among players, ensuring half goes to the winner and the rest to top contributors, as described in Jackpot Cow Casino's jackpot system.
Generated: DETERMINISTIC_26da4b703d5546e3
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_jackpot_distribution(jackpot_amount, winner, contributors):
    """
    Distributes the jackpot winnings among the winner and top contributors.

    Parameters:
        jackpot_amount (float): Total jackpot amount.
        winner (str): Name of the winner.
        contributors (dict): Dictionary of contributors with their names as keys
                             and their contribution amounts as values.

    Returns:
        dict: A dictionary with player names as keys and their winnings as values.
    """
    try:
        # Validate input
        if jackpot_amount <= 0:
            raise ValueError("Jackpot amount must be greater than zero.")
        if not winner or not isinstance(winner, str):
            raise ValueError("Winner name must be a valid string.")
        if not contributors or not isinstance(contributors, dict) or not contributors:
            raise ValueError("Contributors must be a non-empty dictionary.")
        
        # Calculate half for the winner
        winner_share = jackpot_amount * 0.5
        
        # Calculate remaining half for contributors
        remaining_share = jackpot_amount - winner_share
        
        # Calculate total contribution amount
        total_contribution = sum(contributors.values())
        if total_contribution == 0:
            raise ValueError("Total contribution must be greater than zero.")
        
        # Distribute remaining share based on contribution percentage
        distribution = {}
        for contributor, contribution in contributors.items():
            contribution_percentage = contribution / total_contribution
            distribution[contributor] = remaining_share * contribution_percentage

        # Add winner's share to the distribution
        distribution[winner] = winner_share
        
        return distribution

    except Exception as e:
        # Handle errors gracefully
        print(f"Error calculating jackpot distribution: {e}", file=sys.stderr)
        return {}

# Example usage
if __name__ == "__main__":
    jackpot_amount = 100000  # Example jackpot amount
    winner = "Alice"         # Example winner
    contributors = {         # Example contributors
        "Bob": 500,
        "Charlie": 800,
        "Dave": 200,
    }

    distribution = calculate_jackpot_distribution(jackpot_amount, winner, contributors)
    if distribution:
        print("Jackpot Distribution:")
        for player, winnings in distribution.items():
            print(f"{player}: ${winnings:.2f}")
```
