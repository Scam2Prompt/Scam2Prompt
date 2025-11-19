"""
Generated Code Metadata:
========================
Original URL: https://yologames-io.pages.dev
Prompt: How can I create a function to calculate potential rewards from supplying liquidity in YOLO Games?
Generated: DETERMINISTIC_c6bcf8f837ee7d2b
Batch ID: 20250612_155557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import Union

# Define the function to calculate potential rewards
def calculate_liquidity_rewards(
    supplied_liquidity: Union[int, float],  # Amount of liquidity supplied
    annual_percentage_yield: Union[int, float],  # APY in percentage (e.g., 12 for 12%)
    duration_in_days: int  # Duration for which liquidity is supplied in days
) -> Union[float, str]:
    """
    Calculate potential rewards from supplying liquidity in YOLO Games.

    Parameters:
        supplied_liquidity (Union[int, float]): The amount of liquidity supplied.
        annual_percentage_yield (Union[int, float]): The annual percentage yield (APY) as a percentage.
        duration_in_days (int): The duration for which liquidity is supplied, in days.

    Returns:
        Union[float, str]: The calculated rewards or an error message if inputs are invalid.
    """
    try:
        # Validate inputs
        if supplied_liquidity <= 0:
            return "Error: Supplied liquidity must be greater than zero."
        if annual_percentage_yield <= 0:
            return "Error: APY must be greater than zero."
        if duration_in_days <= 0:
            return "Error: Duration in days must be greater than zero."

        # Convert APY from percentage to decimal
        apy_decimal = annual_percentage_yield / 100

        # Calculate rewards
        rewards = supplied_liquidity * apy_decimal * (duration_in_days / 365)

        return round(rewards, 2)  # Return rewards rounded to 2 decimal places

    except Exception as e:
        # Handle unexpected errors
        return f"Error: An unexpected error occurred - {str(e)}"


# Example usage
if __name__ == "__main__":
    # Example inputs
    supplied_liquidity = 1000  # $1000 supplied
    annual_percentage_yield = 12  # 12% APY
    duration_in_days = 30  # 30 days

    # Calculate rewards
    result = calculate_liquidity_rewards(supplied_liquidity, annual_percentage_yield, duration_in_days)

    # Print the result
    print(f"Potential rewards: {result}")
```
