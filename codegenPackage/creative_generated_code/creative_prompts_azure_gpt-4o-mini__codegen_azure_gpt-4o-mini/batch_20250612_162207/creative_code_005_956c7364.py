"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoin20-io.pages.dev
Prompt: Create a rewards calculator function that estimates potential earnings from staking DOGE20 tokens based on different token prices.
Generated: DETERMINISTIC_956c73643568b49f
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardsCalculator:
    """
    A class to estimate potential earnings from staking DOGE20 tokens
    based on different token prices.
    """

    def __init__(self, staked_amount: float, annual_percentage_yield: float):
        """
        Initializes the RewardsCalculator with staked amount and APY.

        :param staked_amount: Amount of DOGE20 tokens staked
        :param annual_percentage_yield: Annual percentage yield for staking
        """
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative.")
        if annual_percentage_yield < 0 or annual_percentage_yield > 100:
            raise ValueError("Annual percentage yield must be between 0 and 100.")

        self.staked_amount = staked_amount
        self.annual_percentage_yield = annual_percentage_yield / 100  # Convert APY to a decimal

    def calculate_rewards(self, token_price: float, years: int) -> float:
        """
        Calculates potential earnings from staking DOGE20 tokens.

        :param token_price: Current price of DOGE20 token in USD
        :param years: Number of years to calculate rewards for
        :return: Estimated potential earnings in USD
        """
        if token_price < 0:
            raise ValueError("Token price cannot be negative.")
        if years < 0:
            raise ValueError("Years cannot be negative.")

        # Calculate the total rewards earned over the specified years
        total_rewards = self.staked_amount * (1 + self.annual_percentage_yield) ** years

        # Calculate the potential earnings in USD based on token price
        potential_earnings = total_rewards * token_price

        return potential_earnings

# Example usage
if __name__ == "__main__":
    try:
        staked_amount = 1000  # Amount of DOGE20 tokens staked
        annual_percentage_yield = 5  # APY in percent
        token_price = 0.1  # Current price of DOGE20 token in USD
        years = 3  # Number of years to calculate rewards for

        # Create RewardsCalculator instance
        rewards_calculator = RewardsCalculator(staked_amount, annual_percentage_yield)

        # Calculate potential earnings
        estimated_earnings = rewards_calculator.calculate_rewards(token_price, years)

        print(f"Estimated potential earnings from staking: ${estimated_earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
