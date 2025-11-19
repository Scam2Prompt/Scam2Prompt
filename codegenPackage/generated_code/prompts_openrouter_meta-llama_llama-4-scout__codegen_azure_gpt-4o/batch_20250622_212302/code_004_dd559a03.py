"""
Generated Code Metadata:
========================
Original URL: https://cotidashboard.com
Prompt: Develop a code snippet to calculate the rewards earned by a user depositing $COTI into the COTI Treasury, considering the base and boost rates.
Generated: DETERMINISTIC_dd559a03ac933829
Batch ID: 20250622_212302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Union

# Define a function to calculate rewards
def calculate_rewards(deposit_amount: Union[int, float], base_rate: Union[int, float], boost_rate: Union[int, float]) -> Union[float, str]:
    """
    Calculate the rewards earned by a user depositing $COTI into the COTI Treasury.

    Parameters:
        deposit_amount (Union[int, float]): The amount of $COTI deposited by the user.
        base_rate (Union[int, float]): The base reward rate (percentage as a decimal).
        boost_rate (Union[int, float]): The boost reward rate (percentage as a decimal).

    Returns:
        Union[float, str]: The total rewards earned or an error message if inputs are invalid.
    """
    try:
        # Validate inputs
        if deposit_amount <= 0:
            return "Error: Deposit amount must be greater than zero."
        if not (0 <= base_rate <= 1):
            return "Error: Base rate must be between 0 and 1 (inclusive)."
        if not (0 <= boost_rate <= 1):
            return "Error: Boost rate must be between 0 and 1 (inclusive)."

        # Calculate rewards
        base_rewards = deposit_amount * base_rate
        boost_rewards = deposit_amount * boost_rate
        total_rewards = base_rewards + boost_rewards

        return round(total_rewards, 2)  # Return rounded rewards for better readability

    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"


# Example usage
if __name__ == "__main__":
    # User inputs
    deposit = 1000  # Amount of $COTI deposited
    base_rate = 0.05  # Base rate (5%)
    boost_rate = 0.02  # Boost rate (2%)

    # Calculate and display rewards
    rewards = calculate_rewards(deposit, base_rate, boost_rate)
    print(f"Rewards earned: {rewards}")
```
