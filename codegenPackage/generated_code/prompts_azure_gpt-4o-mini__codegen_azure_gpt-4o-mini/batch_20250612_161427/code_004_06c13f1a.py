"""
Generated Code Metadata:
========================
Original URL: https://scotty-theai-def.web.app
Prompt: Create a function that calculates potential rewards for staking $SCOTTY tokens based on the provided APY details from the Scotty AI website.
Generated: DETERMINISTIC_06c13f1aa7205f29
Batch ID: 20250612_161427
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
    A class to calculate potential rewards for staking SCOTTY tokens.
    """

    def __init__(self, apy: float):
        """
        Initializes the StakingCalculator with the given Annual Percentage Yield (APY).

        :param apy: The annual percentage yield as a decimal (e.g., 0.05 for 5%).
        """
        if apy < 0:
            raise ValueError("APY must be a non-negative value.")
        self.apy = apy

    def calculate_rewards(self, principal: float, years: float) -> float:
        """
        Calculates the potential rewards for staking SCOTTY tokens.

        :param principal: The amount of SCOTTY tokens staked.
        :param years: The number of years the tokens are staked for.
        :return: The total rewards earned after the specified number of years.
        """
        if principal < 0:
            raise ValueError("Principal amount must be a non-negative value.")
        if years < 0:
            raise ValueError("Years must be a non-negative value.")

        # Calculate the total rewards using the formula for compound interest
        total_rewards = principal * ((1 + self.apy) ** years - 1)
        return total_rewards

    def display_rewards(self, principal: float, years: float) -> None:
        """
        Displays the potential rewards for staking SCOTTY tokens.

        :param principal: The amount of SCOTTY tokens staked.
        :param years: The number of years the tokens are staked for.
        """
        try:
            rewards = self.calculate_rewards(principal, years)
            print(f"Staking ${principal:.2f} SCOTTY tokens for {years} years at an APY of {self.apy * 100:.2f}% "
                  f"will yield a total reward of ${rewards:.2f}.")
        except ValueError as e:
            print(f"Error: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the staking calculator with an APY of 5%
        staking_calculator = StakingCalculator(apy=0.05)

        # Calculate and display rewards for staking $1000 for 3 years
        staking_calculator.display_rewards(principal=1000, years=3)
    except Exception as e:
        print(f"An error occurred: {e}")
```
