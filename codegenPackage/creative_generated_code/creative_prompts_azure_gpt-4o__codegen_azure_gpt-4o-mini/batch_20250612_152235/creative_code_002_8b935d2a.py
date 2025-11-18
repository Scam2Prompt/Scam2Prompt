"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vote-ondo.eth.limo
Prompt: Create a function to calculate daily yield accrual for USDY tokens based on the increasing redemption value per token.
Generated: DETERMINISTIC_8b935d2a71dd75f8
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class USDYToken:
    def __init__(self, initial_value: float):
        """
        Initialize a USDYToken instance with an initial redemption value.

        :param initial_value: The initial redemption value per token in USD.
        """
        if initial_value <= 0:
            raise ValueError("Initial value must be greater than zero.")
        self.redemption_value = initial_value

    def calculate_daily_yield(self, current_value: float, previous_value: float) -> float:
        """
        Calculate the daily yield accrual based on the current and previous redemption values.

        :param current_value: The current redemption value per token.
        :param previous_value: The previous redemption value per token.
        :return: The daily yield accrual in USD.
        :raises ValueError: If current_value or previous_value is not greater than zero.
        """
        if current_value <= 0 or previous_value <= 0:
            raise ValueError("Current and previous values must be greater than zero.")

        # Calculate yield as the difference between current and previous values
        daily_yield = current_value - previous_value
        return daily_yield

    def update_redemption_value(self, new_value: float):
        """
        Update the redemption value per token.

        :param new_value: The new redemption value per token in USD.
        :raises ValueError: If new_value is not greater than zero.
        """
        if new_value <= 0:
            raise ValueError("New redemption value must be greater than zero.")
        self.redemption_value = new_value


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the USDYToken with an initial redemption value
        usdy = USDYToken(initial_value=1.0)

        # Update the redemption value
        usdy.update_redemption_value(1.05)  # Redeem value increased to $1.05

        # Calculate daily yield based on current and previous values
        daily_yield = usdy.calculate_daily_yield(current_value=1.05, previous_value=1.00)
        print(f"Daily yield accrual: ${daily_yield:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
