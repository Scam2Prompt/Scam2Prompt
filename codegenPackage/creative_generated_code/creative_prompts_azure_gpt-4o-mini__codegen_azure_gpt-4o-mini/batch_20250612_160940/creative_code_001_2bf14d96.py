"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siduspad.xyz
Prompt: Generate code to calculate the total rewards earned from staking Sidus with different APY rates on SidusPad.
Generated: DETERMINISTIC_2bf14d96a7877d97
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardsCalculator:
    """
    A class to calculate total rewards earned from staking Sidus
    with different Annual Percentage Yield (APY) rates on SidusPad.
    """

    def __init__(self, principal: float, apy: float, years: int):
        """
        Initialize the calculator with the principal amount, APY, and duration in years.

        :param principal: The initial amount of Sidus staked
        :param apy: Annual Percentage Yield (as a decimal, e.g., 0.1 for 10%)
        :param years: The number of years the amount is staked
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if not (0 <= apy <= 1):
            raise ValueError("APY must be a decimal between 0 and 1.")
        if years < 0:
            raise ValueError("Number of years must be non-negative.")
        
        self.principal = principal
        self.apy = apy
        self.years = years

    def calculate_total_rewards(self) -> float:
        """
        Calculate the total rewards earned from staking Sidus using compound interest formula.

        :return: Total rewards earned
        """
        # Compound Interest Formula: A = P * (1 + r/n)^(nt)
        # For simplicity, we assume interest is compounded annually (n=1)
        total_amount = self.principal * (1 + self.apy) ** self.years
        total_rewards = total_amount - self.principal
        return total_rewards

def main():
    """
    Main function to demonstrate the StakingRewardsCalculator.
    """
    try:
        # Example inputs
        principal_amount = 1000.0  # Principal amount in Sidus
        annual_percentage_yield = 0.1  # 10% APY
        staking_years = 5  # Duration in years

        # Create an instance of the calculator
        calculator = StakingRewardsCalculator(principal_amount, annual_percentage_yield, staking_years)

        # Calculate total rewards earned
        rewards = calculator.calculate_total_rewards()

        print(f"Total rewards earned from staking Sidus: {rewards:.2f} Sidus")
    
    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
```
