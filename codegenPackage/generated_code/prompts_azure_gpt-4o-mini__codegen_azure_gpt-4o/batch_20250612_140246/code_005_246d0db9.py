"""
Generated Code Metadata:
========================
Original URL: https://arbius-en.pages.dev
Prompt: Create a function that calculates the task fee based on the economic rules of the Arbius token supply and reward structure.
Generated: DETERMINISTIC_246d0db938a8d1c3
Batch ID: 20250612_140246
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

# Define a function to calculate the task fee based on Arbius token supply and reward structure
def calculate_task_fee(token_supply: float, base_fee: float, reward_multiplier: float) -> Union[float, str]:
    """
    Calculate the task fee based on the economic rules of the Arbius token supply and reward structure.

    Parameters:
        token_supply (float): The current supply of Arbius tokens in circulation.
        base_fee (float): The base fee for the task in Arbius tokens.
        reward_multiplier (float): The multiplier applied to the base fee based on token supply dynamics.

    Returns:
        float: The calculated task fee in Arbius tokens.
        str: Error message if invalid inputs are provided.
    """
    try:
        # Validate inputs
        if token_supply <= 0:
            return "Error: Token supply must be greater than zero."
        if base_fee <= 0:
            return "Error: Base fee must be greater than zero."
        if reward_multiplier <= 0:
            return "Error: Reward multiplier must be greater than zero."

        # Calculate the task fee
        task_fee = base_fee * (1 + reward_multiplier / token_supply)

        # Ensure the task fee is rounded to a reasonable precision
        return round(task_fee, 6)

    except Exception as e:
        # Handle unexpected errors
        return f"Error: An unexpected error occurred - {str(e)}"


# Example usage
if __name__ == "__main__":
    # Example inputs
    token_supply = 1000000.0  # Current token supply
    base_fee = 10.0          # Base fee for the task
    reward_multiplier = 500.0  # Reward multiplier

    # Calculate the task fee
    result = calculate_task_fee(token_supply, base_fee, reward_multiplier)

    # Print the result
    print(f"Task Fee: {result}")
```
