"""
Generated Code Metadata:
========================
Original URL: https://cronos-a7i.pages.dev
Prompt: Provide an example of how to calculate the staking yield for zkCRO based on the current APR of 6.99% mentioned on the Cronos zkEVM site.
Generated: DETERMINISTIC_2fd9b2ca27f5f6bd
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_staking_yield(principal: float, apr: float, time_in_days: int) -> float:
    """
    Calculate the staking yield for zkCRO.

    Args:
    - principal (float): The initial amount of zkCRO being staked.
    - apr (float): The annual percentage rate (APR) as a decimal.
    - time_in_days (int): The time period for which the yield is being calculated in days.

    Returns:
    - float: The staking yield.

    Raises:
    - ValueError: If principal, apr, or time_in_days is not a positive number.
    """

    # Validate inputs
    if principal <= 0:
        raise ValueError("Principal must be a positive number.")
    if apr <= 0:
        raise ValueError("APR must be a positive number.")
    if time_in_days <= 0:
        raise ValueError("Time in days must be a positive integer.")

    # Convert APR to a decimal
    apr_as_decimal = apr / 100

    # Calculate the time in years
    time_in_years = time_in_days / 365

    # Calculate the staking yield using the formula: A = P * (1 + r * t)
    # Where:
    #   A = the future value of the investment/loan, including interest
    #   P = principal investment amount (the initial deposit or loan amount)
    #   r = annual interest rate (in decimal)
    #   t = time the money is invested or borrowed for, in years
    staking_yield = principal * (apr_as_decimal * time_in_years)

    return staking_yield


def main():
    try:
        # Given parameters
        current_apr = 6.99  # APR as a percentage
        principal = 1000  # Example principal amount of zkCRO
        time_in_days = 365  # Example time period of 1 year

        # Calculate staking yield
        yield_earned = calculate_staking_yield(principal, current_apr, time_in_days)

        print(f"For a principal amount of {principal} zkCRO, "
              f"the staking yield over {time_in_days} days at an APR of {current_apr}% is: {yield_earned} zkCRO")

    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()
```
