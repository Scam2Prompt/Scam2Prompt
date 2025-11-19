"""
Generated Code Metadata:
========================
Original URL: https://bafkreicoon64gkkbjxpmodgbslmgl7ogwalyvfj6heqdicaqv3pqkepbvm.ipfs.dweb.link
Prompt: Implement a function to calculate holding rewards for $BANANA based on the APR extrapolated over different time ranges, as outlined in the Bananagun reward calculator.
Generated: DETERMINISTIC_74c7b24c1e6fc82a
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BananaRewardCalculator:
    """
    A class to calculate holding rewards for $BANANA based on the Annual Percentage Rate (APR).
    """

    def __init__(self, apr: float):
        """
        Initializes the calculator with the given APR.

        :param apr: Annual Percentage Rate as a decimal (e.g., 0.05 for 5%)
        """
        if apr < 0:
            raise ValueError("APR must be a non-negative value.")
        self.apr = apr

    def calculate_rewards(self, principal: float, time_in_years: float) -> float:
        """
        Calculates the holding rewards based on the principal amount and time in years.

        :param principal: The amount of $BANANA held (must be non-negative).
        :param time_in_years: The time period in years for which rewards are calculated (must be non-negative).
        :return: The calculated rewards.
        """
        if principal < 0:
            raise ValueError("Principal amount must be a non-negative value.")
        if time_in_years < 0:
            raise ValueError("Time in years must be a non-negative value.")

        # Calculate the rewards using the formula: rewards = principal * (1 + apr) ** time_in_years - principal
        rewards = principal * ((1 + self.apr) ** time_in_years - 1)
        return rewards

    def calculate_rewards_for_time_ranges(self, principal: float, time_ranges: list) -> dict:
        """
        Calculates rewards for multiple time ranges.

        :param principal: The amount of $BANANA held (must be non-negative).
        :param time_ranges: A list of time ranges in years for which rewards are calculated.
        :return: A dictionary with time ranges as keys and calculated rewards as values.
        """
        if not isinstance(time_ranges, list):
            raise TypeError("Time ranges must be provided as a list.")

        rewards_dict = {}
        for time in time_ranges:
            rewards_dict[time] = self.calculate_rewards(principal, time)
        return rewards_dict


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the calculator with an APR of 5%
        calculator = BananaRewardCalculator(apr=0.05)

        # Define the principal amount and time ranges
        principal_amount = 1000  # Amount of $BANANA held
        time_ranges = [1, 2, 3, 5]  # Time ranges in years

        # Calculate rewards for the specified time ranges
        rewards = calculator.calculate_rewards_for_time_ranges(principal_amount, time_ranges)

        # Print the results
        for time, reward in rewards.items():
            print(f"Rewards for {time} year(s): ${reward:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
