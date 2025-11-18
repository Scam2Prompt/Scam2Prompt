"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegraph.live
Prompt: Write a script to simulate the reward calculation for tours (e.g., Dubai, Thailand, etc.) based on the business requirements listed on https://thegraph.live.
Generated: DETERMINISTIC_ce5e73ef4786c873
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class TourRewardCalculator:
    """
    A class to represent the reward calculation for tours based on business requirements.
    """

    def __init__(self):
        """
        Initialize the reward rate for each tour.
        """
        self.tour_rewards = {
            "Dubai": 0.10,  # 10% reward for Dubai tours
            "Thailand": 0.15,  # 15% reward for Thailand tours
            "Paris": 0.08,  # 8% reward for Paris tours
            "New York": 0.12,  # 12% reward for New York tours
        }

    def calculate_reward(self, tour_name, sale_amount):
        """
        Calculate the reward based on the tour and sale amount.

        :param tour_name: Name of the tour (e.g., 'Dubai', 'Thailand').
        :param sale_amount: Sale amount for the tour.
        :return: Calculated reward amount.
        :raises ValueError: If the tour name is invalid or the sale amount is negative.
        """
        if tour_name not in self.tour_rewards:
            raise ValueError(f"Invalid tour name: {tour_name}")
        if sale_amount < 0:
            raise ValueError("Sale amount cannot be negative.")

        reward_rate = self.tour_rewards[tour_name]
        return sale_amount * reward_rate


def main():
    """
    Main entry point for the script. Simulates reward calculations for tours.

    Usage:
        Run the script and input the tour name and sale amount when prompted.
    """
    calculator = TourRewardCalculator()
    print("Welcome to the Tour Reward Calculator!")

    try:
        # Get user inputs
        tour_name = input("Enter the tour name (e.g., Dubai, Thailand): ").strip()
        sale_amount = float(input("Enter the sale amount: "))

        # Calculate the reward
        reward = calculator.calculate_reward(tour_name, sale_amount)

        # Display the result
        print(f"The reward for the {tour_name} tour is: {reward:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Tour Reward Calculator!")


if __name__ == "__main__":
    # Ensure the script runs in Python 3.x
    if sys.version_info.major < 3:
        print("This script requires Python 3.x to run.")
        sys.exit(1)

    # Run the main function
    main()
```
