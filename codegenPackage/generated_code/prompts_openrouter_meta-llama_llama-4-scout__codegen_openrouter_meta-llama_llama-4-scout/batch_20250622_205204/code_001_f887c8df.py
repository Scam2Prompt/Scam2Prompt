"""
Generated Code Metadata:
========================
Original URL: https://zerolend.omc.zone
Prompt: Generate a Python code snippet to calculate token allocation for Zerolend based on a 25% cliff and linear vesting over 12 months.
Generated: DETERMINISTIC_f887c8dfb4ed75bd
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class TokenAllocationCalculator:
    """
    Calculates token allocation for Zerolend based on a 25% cliff and linear vesting over 12 months.
    """

    def __init__(self, total_tokens, vesting_duration=12, cliff_percentage=0.25):
        """
        Initializes the calculator.

        Args:
            total_tokens (float): The total number of tokens to allocate.
            vesting_duration (int, optional): The vesting duration in months. Defaults to 12.
            cliff_percentage (float, optional): The percentage of tokens to allocate at the cliff. Defaults to 0.25.
        """
        self.total_tokens = total_tokens
        self.vesting_duration = vesting_duration
        self.cliff_percentage = cliff_percentage

    def calculate_token_allocation(self, start_date, end_date):
        """
        Calculates the token allocation based on the start and end dates.

        Args:
            start_date (datetime): The start date of the vesting period.
            end_date (datetime): The end date to calculate the token allocation for.

        Returns:
            float: The number of tokens allocated.
        """
        # Calculate the cliff date
        cliff_date = start_date + timedelta(days=30 * 3)  # 25% cliff after 3 months

        # Calculate the number of months between the start date and end date
        months_diff = (end_date - start_date).days / 30

        # Calculate the tokens allocated at the cliff
        cliff_tokens = self.total_tokens * self.cliff_percentage

        # Calculate the tokens allocated linearly over the vesting period
        if end_date <= cliff_date:
            return 0
        elif end_date <= start_date + timedelta(days=30 * self.vesting_duration):
            linear_tokens = (months_diff - 3) / (self.vesting_duration - 3) * (self.total_tokens - cliff_tokens)
            return cliff_tokens + linear_tokens
        else:
            return self.total_tokens

def main():
    try:
        calculator = TokenAllocationCalculator(total_tokens=1000000)
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 6, 1)
        allocated_tokens = calculator.calculate_token_allocation(start_date, end_date)
        print(f"Allocated tokens: {allocated_tokens}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
