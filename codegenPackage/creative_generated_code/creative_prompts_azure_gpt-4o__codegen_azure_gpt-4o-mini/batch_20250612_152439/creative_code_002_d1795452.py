"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prism-61a.pages.dev
Prompt: Create a function to calculate vesting rewards for DUEL tokens based on the roadmap provided by Prism.
Generated: DETERMINISTIC_d1795452924359ff
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VestingRewardCalculator:
    """
    A class that calculates the vesting rewards for DUEL tokens based on provided roadmap specifications.

    Attributes:
        roadmap (list): A list of tuples representing the vesting schedule.
        total_tokens (float): The total number of DUEL tokens to distribute.
    """

    def __init__(self, roadmap, total_tokens):
        """
        Initializes the VestingRewardCalculator with a roadmap and total tokens.

        Args:
            roadmap (list): A list of tuples where each tuple contains 
                            (time_period_in_months, percentage_of_total_award).
            total_tokens (float): The total amount of DUEL tokens available for vesting.
        """
        if total_tokens <= 0:
            raise ValueError("Total tokens must be greater than zero.")

        self.roadmap = roadmap
        self.total_tokens = total_tokens

    def calculate_vesting_rewards(self):
        """
        Calculates the vesting rewards based on the roadmap and total tokens.

        Returns:
            dict: A dictionary where keys are time periods and values are the amount of DUEL tokens for each period.

        Raises:
            ValueError: If the roadmap is empty or contains invalid data.
        """
        if not self.roadmap:
            raise ValueError("Roadmap cannot be empty.")
        
        rewards = {}
        total_percentage = 0.0

        for period, percentage in self.roadmap:
            if not (0 <= percentage <= 100):
                raise ValueError(f"Percentage {percentage} for period {period} is invalid. Must be between 0 and 100.")

            # Calculate the token reward for the period
            reward_amount = (percentage / 100) * self.total_tokens
            rewards[period] = reward_amount
            
            total_percentage += percentage

        # Check that total percentage does not exceed 100
        if total_percentage > 100:
            raise ValueError("Total percentage exceeds 100%.")
        
        return rewards

# Example usage
if __name__ == "__main__":
    # Roadmap example: (time_period_in_months, percentage_of_total_award)
    roadmap_example = [
        (0, 10),   # 10% at the beginning
        (6, 20),   # 20% after 6 months
        (12, 30),  # 30% after 12 months
        (18, 40)   # 40% after 18 months
    ]
    
    total_duel_tokens = 1000000  # Example total DUEL tokens

    try:
        calculator = VestingRewardCalculator(roadmap_example, total_duel_tokens)
        rewards = calculator.calculate_vesting_rewards()
        print("Vesting Rewards:", rewards)
    except ValueError as e:
        print("Error:", e)
```
