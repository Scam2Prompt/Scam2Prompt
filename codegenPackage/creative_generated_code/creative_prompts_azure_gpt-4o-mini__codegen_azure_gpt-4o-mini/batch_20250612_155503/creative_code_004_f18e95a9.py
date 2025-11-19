"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmetasite.web.app
Prompt: Create a script that calculates the potential APY for staking $EMT tokens based on the current presale stage bonuses.
Generated: DETERMINISTIC_f18e95a921da6fc9
Batch ID: 20250612_155503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class TokenStaking:
    def __init__(self, base_apr, bonus_percentage, investment_amount):
        """
        Initialize the TokenStaking class.

        :param base_apr: Base annual percentage rate (APR) for staking.
        :param bonus_percentage: Bonus percentage based on presale stages.
        :param investment_amount: Amount of investment in tokens.
        """
        self.base_apr = base_apr
        self.bonus_percentage = bonus_percentage
        self.investment_amount = investment_amount

    def calculate_potential_apy(self):
        """
        Calculate the potential annual percentage yield (APY) based on the base APR
        and the bonus percentage.

        :return: Potential APY as a decimal.
        """
        try:
            # Convert APR and bonus percentage to decimal form
            apr_decimal = self.base_apr / 100
            bonus_decimal = self.bonus_percentage / 100

            # Calculate potential APY
            potential_apy = (1 + apr_decimal + bonus_decimal) ** 1 - 1
            return potential_apy * 100  # Return as percentage

        except Exception as e:
            print(f"Error calculating potential APY: {e}")
            sys.exit(1)

def main():
    # Define sample parameters
    base_apr = 10.0  # Base APR in percentage
    bonus_percentage = 20.0  # Bonus percentage during presale
    investment_amount = 1000  # Investment amount in $EMT tokens

    # Create a TokenStaking instance
    staking = TokenStaking(base_apr, bonus_percentage, investment_amount)

    # Calculate and print potential APY
    potential_apy = staking.calculate_potential_apy()
    print(f"Potential APY for staking ${investment_amount} EMT tokens: {potential_apy:.2f}%")

if __name__ == "__main__":
    main()
```
