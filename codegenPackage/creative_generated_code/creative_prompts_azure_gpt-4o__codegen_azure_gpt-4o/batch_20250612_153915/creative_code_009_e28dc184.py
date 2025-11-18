"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonsquare-dapp.vercel.app
Prompt: Provide a script to calculate the total rewards earned in TONSquare's ecosystem, including validating rewards, mining rewards, and referral bonuses.
Generated: DETERMINISTIC_e28dc1841f559bc4
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TONSquareRewardsCalculator:
    """
    A class to calculate total rewards in TONSquare's ecosystem.
    Includes validation rewards, mining rewards, and referral bonuses.
    """

    def __init__(self, rewards_data):
        """
        Initialize the rewards calculator.

        :param rewards_data: Dictionary containing reward details.
                             Example structure:
                             {
                                 "validation_rewards": 100.5,
                                 "mining_rewards": 250.75,
                                 "referral_bonuses": 50.25
                             }
        """
        self.rewards_data = rewards_data

    def validate_rewards_data(self):
        """
        Validates the rewards data structure and values.

        :raises ValueError: If any reward field is missing or invalid.
        """
        required_fields = ['validation_rewards', 'mining_rewards', 'referral_bonuses']

        for field in required_fields:
            if field not in self.rewards_data:
                raise ValueError(f"Missing '{field}' in rewards data.")
            if not isinstance(self.rewards_data[field], (int, float)) or self.rewards_data[field] < 0:
                raise ValueError(f"Invalid value for '{field}'.")

    def calculate_total_rewards(self):
        """
        Calculates the total rewards.

        :return: Total rewards as a float.
        """
        self.validate_rewards_data()
        return (
            self.rewards_data['validation_rewards']
            + self.rewards_data['mining_rewards']
            + self.rewards_data['referral_bonuses']
        )


def main():
    """
    Main function to execute the rewards calculation.
    """
    # Example rewards data (this would typically come from a database or API request)
    example_rewards_data = {
        "validation_rewards": 150.75,
        "mining_rewards": 300.50,
        "referral_bonuses": 75.25
    }

    try:
        # Initialize the rewards calculator with the example data
        calculator = TONSquareRewardsCalculator(example_rewards_data)

        # Calculate total rewards
        total_rewards = calculator.calculate_total_rewards()

        # Display the total rewards
        print(f"Total Rewards Earned: {total_rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
