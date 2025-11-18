"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafkreicoon64gkkbjxpmodgbslmgl7ogwalyvfj6heqdicaqv3pqkepbvm.ipfs.dweb.link
Prompt: Implement a function to calculate holding rewards for $BANANA based on the APR extrapolated over different time ranges, as outlined in the Bananagun reward calculator.
Generated: DETERMINISTIC_74c7b24c1e6fc82a
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BananaRewardCalculator:
    """
    A class to calculate holding rewards for $BANANA based on an Annual Percentage Rate (APR).
    """

    def __init__(self, apr: float):
        """
        Initialize the calculator with the given APR.

        :param apr: Annual Percentage Rate in decimal form (e.g., for 12%, use 0.12)
        """
        if not (0 <= apr <= 1):
            raise ValueError("APR must be between 0 and 1 inclusive.")
        self.apr = apr

    def calculate_rewards(self, principal: float, years: float) -> float:
        """
        Calculate the total rewards for a given principal over a number of years.

        :param principal: The initial amount of $BANANA held.
        :param years: The number of years to calculate rewards for.
        :return: Total rewards after the specified number of years.
        """
        if principal < 0:
            raise ValueError("Principal cannot be negative.")
        if years < 0:
            raise ValueError("Years cannot be negative.")

        # Calculate total rewards using the formula:
        # Rewards = Principal * (1 + APR) ** Years - Principal
        rewards = principal * ((1 + self.apr) ** years - 1)
        return rewards

    def calculate_rewards_over_time(self, principal: float, time_ranges: list) -> dict:
        """
        Calculate rewards for various time ranges.

        :param principal: The initial amount of $BANANA held.
        :param time_ranges: A list of time ranges in years.
        :return: A dictionary with time range as key and calculated rewards as value.
        """
        if not isinstance(time_ranges, list) or not all(isinstance(t, (int, float)) for t in time_ranges):
            raise TypeError("time_ranges must be a list of numeric values.")

        results = {}
        for years in time_ranges:
            results[years] = self.calculate_rewards(principal, years)
        return results


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the calculator with an APR of 12%
        banana_calculator = BananaRewardCalculator(apr=0.12)
        
        # Set the principal amount of $BANANA
        principal_amount = 1000.0
        
        # Define time ranges in years
        time_ranges = [1, 2, 5, 10]

        # Calculate rewards over the specified time ranges
        rewards = banana_calculator.calculate_rewards_over_time(principal_amount, time_ranges)

        # Output the results
        for years, reward in rewards.items():
            print(f"Rewards for {years} year(s): ${reward:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
