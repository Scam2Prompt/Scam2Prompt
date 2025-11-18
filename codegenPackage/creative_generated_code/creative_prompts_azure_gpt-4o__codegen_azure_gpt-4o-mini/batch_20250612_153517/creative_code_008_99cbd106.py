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
class TokenomicsCalculator:
    def __init__(self, total_supply: float, vesting_bonus_rate: float, referral_bonus_rate: float):
        """
        Initialize the TokenomicsCalculator with the total supply of tokens,
        vesting bonus rate, and referral bonus rate.

        :param total_supply: Total number of tokens available in the project.
        :param vesting_bonus_rate: Percentage of tokens allocated as a vesting bonus.
        :param referral_bonus_rate: Percentage of tokens allocated as referral bonuses.
        """
        self.total_supply = total_supply
        self.vesting_bonus_rate = vesting_bonus_rate
        self.referral_bonus_rate = referral_bonus_rate

    def calculate_vesting_bonus(self) -> float:
        """
        Calculate the total amount of vesting bonuses.

        :return: Total vesting bonus in tokens.
        """
        vesting_bonus = self.total_supply * (self.vesting_bonus_rate / 100)
        return vesting_bonus

    def calculate_referral_bonus(self) -> float:
        """
        Calculate the total amount of referral bonuses.

        :return: Total referral bonus in tokens.
        """
        referral_bonus = self.total_supply * (self.referral_bonus_rate / 100)
        return referral_bonus

    def calculate_total_allocation(self) -> float:
        """
        Calculate the total token allocation considering vesting and referral bonuses.

        :return: Total token allocation after adding bonuses.
        """
        try:
            vesting_bonus = self.calculate_vesting_bonus()
            referral_bonus = self.calculate_referral_bonus()
            total_allocation = self.total_supply + vesting_bonus + referral_bonus
            return total_allocation
        except Exception as e:
            print(f"An error occurred while calculating total allocation: {e}")
            return 0.0

def main():
    # Parameters for the tokenomics calculation
    total_supply = 1_000_000  # Total supply of $MANIA tokens
    vesting_bonus_rate = 10.0  # 10% vesting bonus
    referral_bonus_rate = 5.0   # 5% referral bonus

    # Create a TokenomicsCalculator instance
    token_calculator = TokenomicsCalculator(total_supply, vesting_bonus_rate, referral_bonus_rate)

    # Calculate the total token allocation
    total_allocation = token_calculator.calculate_total_allocation()

    # Output the results
    print(f"Total Supply: {total_supply} tokens")
    print(f"Vesting Bonus: {token_calculator.calculate_vesting_bonus()} tokens")
    print(f"Referral Bonus: {token_calculator.calculate_referral_bonus()} tokens")
    print(f"Total Token Allocation (including bonuses): {total_allocation} tokens")

if __name__ == "__main__":
    main()
```
