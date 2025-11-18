"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Write code to calculate bonus interest shares for Silo Liquidity Providers based on their positions, referencing the Silo Rewards Proposal.
Generated: DETERMINISTIC_0c46ac29a5eff390
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: bonus_interest_calculator.py

"""
Bonus Interest Calculator for Silo Liquidity Providers.
Based on the Silo Rewards Proposal, the script calculates bonus interest shares
allocated to liquidity providers based on their positions.

Assumptions:
- Liquidity providers' positions are provided as input.
- Bonus interest pool is fixed and provided as input.
- Proportional allocation based on positions.

Usage:
- Call `calculate_bonus_interest` function with appropriate input data.
"""

class BonusInterestCalculator:
    """
    Class to calculate bonus interest shares for Silo Liquidity Providers.
    """

    def __init__(self, total_bonus_pool: float):
        """
        Initializes the calculator with the total bonus interest pool.

        :param total_bonus_pool: Total bonus interest pool (float).
        """
        if total_bonus_pool <= 0:
            raise ValueError("Total bonus pool must be greater than 0.")
        self.total_bonus_pool = total_bonus_pool

    def calculate_bonus_interest(self, positions: dict) -> dict:
        """
        Calculates the bonus interest shares for liquidity providers.

        :param positions: A dictionary where keys are provider IDs and values are their positions.
                          Example: {'provider1': 1000, 'provider2': 2000, 'provider3': 700}
        :return: A dictionary where keys are provider IDs and values are their allocated bonus shares.
                 Example: {'provider1': 250.0, 'provider2': 500.0, 'provider3': 175.0}
        """
        if not positions:
            raise ValueError("Positions dictionary cannot be empty.")

        # Ensure all positions are valid
        if any(position <= 0 for position in positions.values()):
            raise ValueError("All positions must be greater than 0.")

        # Calculate the total liquidity positions
        total_position = sum(positions.values())
        if total_position == 0:
            raise ValueError("Total position cannot be zero.")

        # Calculate bonus shares
        bonus_shares = {}
        for provider_id, position in positions.items():
            # Bonus share proportional to position relative to total
            bonus_share = (position / total_position) * self.total_bonus_pool
            bonus_shares[provider_id] = round(bonus_share, 2)  # Round for better readability

        return bonus_shares


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with a fixed bonus interest pool of 1000 units
        calculator = BonusInterestCalculator(total_bonus_pool=1000)

        # Example liquidity provider positions
        positions = {
            "provider1": 1000,
            "provider2": 2000,
            "provider3": 700,
            "provider4": 1300,
        }

        # Calculate and print bonus interest shares
        bonus_interest_shares = calculator.calculate_bonus_interest(positions)
        print("Bonus Interest Shares:", bonus_interest_shares)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
