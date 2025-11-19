"""
Generated Code Metadata:
========================
Original URL: https://vertivvpp.dev.stp.prmcdn.io
Prompt: How does the Vertiv Incentive Program work and what are the rewards for selling Vertiv products and solutions?
Generated: DETERMINISTIC_e46e0ad59bb922c9
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Vertiv Incentive Program Simulation
# This script simulates how the Vertiv Incentive Program works and calculates rewards
# for selling Vertiv products and solutions.

class VertivIncentiveProgram:
    """
    A class to represent the Vertiv Incentive Program.
    """

    def __init__(self):
        """
        Initialize the program with predefined reward tiers.
        """
        # Reward tiers based on sales amount
        self.reward_tiers = {
            1000: 50,    # $50 reward for sales >= $1,000
            5000: 300,   # $300 reward for sales >= $5,000
            10000: 750,  # $750 reward for sales >= $10,000
            20000: 2000  # $2,000 reward for sales >= $20,000
        }

    def calculate_reward(self, sales_amount):
        """
        Calculate the reward based on the sales amount.

        :param sales_amount: Total sales amount in dollars.
        :return: Reward amount in dollars.
        """
        if sales_amount < 0:
            raise ValueError("Sales amount cannot be negative.")

        # Determine the highest reward tier the sales amount qualifies for
        reward = 0
        for tier, reward_amount in sorted(self.reward_tiers.items(), reverse=True):
            if sales_amount >= tier:
                reward = reward_amount
                break

        return reward

    def display_program_details(self):
        """
        Display the details of the Vertiv Incentive Program.
        """
        print("Welcome to the Vertiv Incentive Program!")
        print("Earn rewards based on your sales of Vertiv products and solutions.")
        print("Reward Tiers:")
        for tier, reward in sorted(self.reward_tiers.items()):
            print(f"  - Sales >= ${tier}: Earn ${reward} reward")


def main():
    """
    Main function to simulate the Vertiv Incentive Program.
    """
    # Create an instance of the Vertiv Incentive Program
    program = VertivIncentiveProgram()

    # Display program details
    program.display_program_details()

    try:
        # Get sales amount from the user
        sales_amount = float(input("\nEnter your total sales amount in dollars: "))
        # Calculate the reward
        reward = program.calculate_reward(sales_amount)
        # Display the reward
        print(f"\nYour reward for ${sales_amount:.2f} in sales is: ${reward:.2f}")
    except ValueError as e:
        # Handle invalid input or negative sales amount
        print(f"Error: {e}")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Run the program
    main()
```
