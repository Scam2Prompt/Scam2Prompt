"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeic2ctv7vwt47e6rhckifdcdc2wzxyddiqrge5yfp43c2nk2co6d2u.ipfs.dweb.link
Prompt: Generate a script to calculate APR multipliers for Bedrock stakers with matured positions, using the eligibility criteria described on the Bedrock platform.
Generated: DETERMINISTIC_ebbb02cbc483d36a
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BedrockStaker:
    """
    Represents a staker on the Bedrock platform.
    """
    def __init__(self, staker_id, stake_amount, stake_start_date, stake_maturity_days):
        """
        Initialize staker information.

        :param staker_id: Unique identifier for the staker.
        :param stake_amount: Amount staked by the user.
        :param stake_start_date: Date the stake was started (datetime object).
        :param stake_maturity_days: Number of days required for stake to mature.
        """
        self.staker_id = staker_id
        self.stake_amount = stake_amount
        self.stake_start_date = stake_start_date
        self.stake_maturity_days = stake_maturity_days

    def is_position_mature(self):
        """
        Checks if the staking position has matured.

        :return: True if matured, False otherwise.
        """
        today = datetime.date.today()
        maturity_date = self.stake_start_date + datetime.timedelta(days=self.stake_maturity_days)
        return today >= maturity_date

    def calculate_apr_multiplier(self):
        """
        Calculates the APR multiplier based on eligibility criteria.

        :return: APR multiplier value if position is matured, None otherwise.
        """
        if not self.is_position_mature():
            return None

        # Example APR multiplier calculation based on staking amount (apply Bedrock platform criteria here)
        if self.stake_amount < 1000:
            return 1.02  # 2% APR
        elif self.stake_amount < 5000:
            return 1.05  # 5% APR
        else:
            return 1.10  # 10% APR


def calculate_apr_for_all_stakers(stakers):
    """
    Calculate APR multipliers for all Bedrock stakers with matured positions.

    :param stakers: List of BedrockStaker objects.
    :return: Dictionary containing staker IDs as keys and APR multipliers as values.
    """
    apr_results = {}

    for staker in stakers:
        try:
            apr_multiplier = staker.calculate_apr_multiplier()
            if apr_multiplier is not None:
                apr_results[staker.staker_id] = apr_multiplier
            else:
                apr_results[staker.staker_id] = "Position not matured"
        except Exception as e:
            # Log error and store in result for debugging
            apr_results[staker.staker_id] = f"Error calculating APR: {str(e)}"

    return apr_results


# Example usage:
if __name__ == "__main__":
    # Create staker instances (replace with actual data)
    stakers = [
        BedrockStaker("staker1", 500, datetime.date(2022, 10, 1), 365),
        BedrockStaker("staker2", 2000, datetime.date(2021, 5, 15), 730),
        BedrockStaker("staker3", 6000, datetime.date(2020, 8, 10), 1095),
    ]

    # Calculate APR multipliers
    apr_results = calculate_apr_for_all_stakers(stakers)

    # Print results
    for staker_id, apr in apr_results.items():
        print(f"Staker ID: {staker_id}, APR Multiplier: {apr}")
```
