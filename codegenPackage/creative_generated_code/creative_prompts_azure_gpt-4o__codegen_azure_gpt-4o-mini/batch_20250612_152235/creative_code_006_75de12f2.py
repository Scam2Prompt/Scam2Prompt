"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophpon.pages.dev
Prompt: Develop a tool to track sequencer fees earned by Sophon node operators and display the rewards in $SOPH tokens over a 36-month emission period.
Generated: DETERMINISTIC_75de12f26cbe98eb
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from decimal import Decimal, getcontext

# Set the precision for Decimal calculations
getcontext().prec = 10

class SophonNodeOperator:
    """
    Class to represent a Sophon Node Operator and track their earned fees.
    """

    def __init__(self, operator_id, monthly_fee, start_date):
        """
        Initialize a SophonNodeOperator instance.

        :param operator_id: Unique identifier for the node operator
        :param monthly_fee: Monthly fee earned by the operator in $SOPH tokens
        :param start_date: Date when the emission period starts
        """
        self.operator_id = operator_id
        self.monthly_fee = Decimal(monthly_fee)
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.reward_schedule = self.calculate_rewards()

    def calculate_rewards(self):
        """
        Calculate the rewards schedule over the 36-month emission period.

        :return: A list of tuples containing (month, reward) for 36 months
        """
        rewards = []
        for month in range(36):
            reward_date = self.start_date + datetime.timedelta(days=30 * month)
            rewards.append((reward_date.strftime("%Y-%m"), self.monthly_fee * (month + 1)))
        return rewards

    def display_rewards(self):
        """
        Display the calculated rewards in a human-readable format.
        """
        print(f"Rewards for Operator {self.operator_id}:")
        for month, reward in self.reward_schedule:
            print(f"Month {month}: Earned {reward:.2f} $SOPH tokens")

def main():
    """
    Main function to execute the rewards tracking for a Sophon Node Operator.
    """
    try:
        # Sample data for the node operator
        operator_id = "NODE123"
        monthly_fee = 100.00  # Monthly fee in $SOPH
        start_date = "2023-01-01"  # Emission start date

        # Create the node operator instance
        operator = SophonNodeOperator(operator_id, monthly_fee, start_date)

        # Display the rewards earned
        operator.display_rewards()

    except ValueError as ve:
        print(f"Value error occurred: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
