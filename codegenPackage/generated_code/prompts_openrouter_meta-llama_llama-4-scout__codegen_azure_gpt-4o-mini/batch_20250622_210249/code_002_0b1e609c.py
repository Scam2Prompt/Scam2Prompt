"""
Generated Code Metadata:
========================
Original URL: https://open-custody.pages.dev
Prompt: Generate code to calculate staking rewards for $OPEN and $OCP based on the provided APY and duration.
Generated: DETERMINISTIC_0b1e609c8d4c506c
Batch ID: 20250622_210249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingCalculator:
    """
    A class to calculate staking rewards for cryptocurrencies based on APY and duration.
    """

    def __init__(self, apy: float):
        """
        Initializes the StakingCalculator with the given annual percentage yield (APY).

        :param apy: Annual Percentage Yield as a decimal (e.g., 0.05 for 5%)
        """
        if apy < 0:
            raise ValueError("APY must be a non-negative value.")
        self.apy = apy

    def calculate_rewards(self, principal: float, duration_years: float) -> float:
        """
        Calculates the staking rewards based on the principal amount, APY, and duration.

        :param principal: The amount of cryptocurrency staked.
        :param duration_years: The duration for which the cryptocurrency is staked, in years.
        :return: The total rewards earned over the specified duration.
        """
        if principal < 0:
            raise ValueError("Principal amount must be a non-negative value.")
        if duration_years < 0:
            raise ValueError("Duration must be a non-negative value.")

        # Calculate the total rewards using the formula for compound interest
        total_rewards = principal * ((1 + self.apy) ** duration_years - 1)
        return total_rewards

def main():
    """
    Main function to demonstrate the staking rewards calculation.
    """
    try:
        # Example values for APY, principal, and duration
        apy_open = 0.05  # 5% APY for $OPEN
        apy_ocp = 0.07   # 7% APY for $OCP
        principal = 1000  # Amount staked in dollars
        duration_years = 2  # Duration in years

        # Create instances of StakingCalculator for both cryptocurrencies
        open_calculator = StakingCalculator(apy_open)
        ocp_calculator = StakingCalculator(apy_ocp)

        # Calculate rewards for both cryptocurrencies
        open_rewards = open_calculator.calculate_rewards(principal, duration_years)
        ocp_rewards = ocp_calculator.calculate_rewards(principal, duration_years)

        # Output the results
        print(f"Staking rewards for $OPEN: ${open_rewards:.2f}")
        print(f"Staking rewards for $OCP: ${ocp_rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
