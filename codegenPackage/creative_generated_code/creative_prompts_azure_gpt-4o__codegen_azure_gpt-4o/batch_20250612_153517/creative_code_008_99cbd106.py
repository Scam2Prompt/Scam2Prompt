"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-scapesmania.pages.dev
Prompt: Develop a script to simulate tokenomics calculations for $MANIA, including the impact of vesting bonuses and referral promos on total token allocation.
Generated: DETERMINISTIC_99cbd10682bed13c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class TokenomicsCalculator:
    """
    A class to simulate tokenomics calculations for the $MANIA token.
    Includes the impact of vesting bonuses and referral promos on total token allocation.
    """

    def __init__(self, total_supply, vesting_bonus_rate, referral_bonus_rate):
        """
        Initialize the TokenomicsCalculator.

        :param total_supply: Total token supply of $MANIA.
        :param vesting_bonus_rate: Bonus rate (in percentage) applied for vesting periods.
        :param referral_bonus_rate: Bonus rate (in percentage) applied for referrals.
        """
        self.total_supply = total_supply
        self.vesting_bonus_rate = vesting_bonus_rate
        self.referral_bonus_rate = referral_bonus_rate

    def calculate_vesting_bonus(self, vested_tokens):
        """
        Calculate the vesting bonus based on the vested tokens.

        :param vested_tokens: Number of tokens allocated for vesting.
        :return: Total bonus tokens for vesting.
        """
        if vested_tokens < 0:
            raise ValueError("Vested tokens cannot be negative.")
        return (vested_tokens * self.vesting_bonus_rate) / 100

    def calculate_referral_bonus(self, referral_tokens):
        """
        Calculate the referral bonus based on the referral tokens.

        :param referral_tokens: Number of tokens allocated for referrals.
        :return: Total bonus tokens for referrals.
        """
        if referral_tokens < 0:
            raise ValueError("Referral tokens cannot be negative.")
        return (referral_tokens * self.referral_bonus_rate) / 100

    def calculate_total_allocation(self, vested_tokens, referral_tokens):
        """
        Calculate the total token allocation including bonuses.

        :param vested_tokens: Tokens allocated for vesting.
        :param referral_tokens: Tokens allocated for referrals.
        :return: Total tokens including vesting and referral bonuses.
        """
        vesting_bonus = self.calculate_vesting_bonus(vested_tokens)
        referral_bonus = self.calculate_referral_bonus(referral_tokens)

        total_allocated_tokens = vested_tokens + referral_tokens + vesting_bonus + referral_bonus

        if total_allocated_tokens > self.total_supply:
            raise ValueError("Total allocated tokens exceed total supply.")

        return total_allocated_tokens


def main():
    """
    Main function to execute tokenomics calculations for $MANIA.
    """
    try:
        # Example inputs (these could be replaced with user inputs or dynamic data)
        total_supply = 1_000_000  # Total supply of $MANIA
        vesting_bonus_rate = 10   # 10% vesting bonus
        referral_bonus_rate = 5  # 5% referral bonus

        vested_tokens = 300_000  # Tokens allocated for vesting
        referral_tokens = 100_000  # Tokens allocated for referrals

        # Initialize tokenomics calculator
        calculator = TokenomicsCalculator(total_supply, vesting_bonus_rate, referral_bonus_rate)

        # Perform calculations
        total_allocation = calculator.calculate_total_allocation(vested_tokens, referral_tokens)
        vesting_bonus = calculator.calculate_vesting_bonus(vested_tokens)
        referral_bonus = calculator.calculate_referral_bonus(referral_tokens)

        # Display results
        print(f"Total Supply: {total_supply}")
        print(f"Vested Tokens: {vested_tokens}")
        print(f"Referral Tokens: {referral_tokens}")
        print(f"Vesting Bonus: {vesting_bonus}")
        print(f"Referral Bonus: {referral_bonus}")
        print(f"Total Allocation (including bonuses): {total_allocation}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
