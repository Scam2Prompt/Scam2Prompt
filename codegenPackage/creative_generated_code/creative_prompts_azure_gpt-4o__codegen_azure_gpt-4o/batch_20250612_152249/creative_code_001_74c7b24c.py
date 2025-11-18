"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafkreicoon64gkkbjxpmodgbslmgl7ogwalyvfj6heqdicaqv3pqkepbvm.ipfs.dweb.link
Prompt: Implement a function to calculate holding rewards for $BANANA based on the APR extrapolated over different time ranges, as outlined in the Bananagun reward calculator.
Generated: DETERMINISTIC_74c7b24c1e6fc82a
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import timedelta

def calculate_holding_rewards(principal: float, apr: float, days: int) -> float:
    """
    Calculate holding rewards for $BANANA based on Principal, APR, and Time Duration.

    Args:
        principal (float): The initial amount of $BANANA held.
        apr (float): The Annual Percentage Rate (APR) as a percentage (e.g., 25 for 25% APR).
        days (int): The number of days the $BANANA is held.

    Returns:
        float: The total rewards earned for holding $BANANA over the specified time duration.
    """
    try:
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal must be positive.")
        if apr <= 0:
            raise ValueError("APR must be positive.")
        if days < 0:
            raise ValueError("Number of days cannot be negative.")

        # Convert APR percentage to decimal (e.g., 25% -> 0.25)
        apr_decimal = apr / 100

        # Calculate daily interest rate based on APR
        daily_rate = apr_decimal / 365

        # Calculate rewards using compound interest formula for daily compounding
        total_rewards = principal * ((1 + daily_rate) ** days - 1)

        return round(total_rewards, 6)  # Round to 6 decimal places for precision

    except Exception as e:
        # Handle exceptions gracefully
        print(f"Error calculating rewards: {e}")
        return 0.0


# Example Usage
if __name__ == "__main__":
    # Inputs
    principal_amount = 1000.0  # Initial amount of $BANANA
    annual_percentage_rate = 25.0  # APR in percentage
    duration_days = 30  # Number of days

    # Calculate and display rewards
    rewards = calculate_holding_rewards(principal_amount, annual_percentage_rate, duration_days)
    print(f"Holding rewards for ${principal_amount} BANANA over {duration_days} days: ${rewards}")
```
