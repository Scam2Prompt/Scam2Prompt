"""
Generated Code Metadata:
========================
Original URL: https://hovrachev.ru
Prompt: Write a script to calculate the potential yield from auto-compounding liquidity mining rewards on Yield Yak, factoring in platform fees and AVAX transaction costs.
Generated: DETERMINISTIC_4e6d774050d9d8f7
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# yield_yak_calculator.py

import math

def calculate_potential_yield(
    principal: float, 
    annual_rewards: float, 
    compounding_frequency: int, 
    platform_fee: float, 
    avax_transaction_cost: float, 
    days: int
) -> float:
    """
    Calculate the potential yield from auto-compounding liquidity mining rewards on Yield Yak.

    Args:
    - principal (float): The initial amount of liquidity.
    - annual_rewards (float): The annual rewards rate (in decimal form, e.g., 10% = 0.10).
    - compounding_frequency (int): The number of times rewards are compounded per year.
    - platform_fee (float): The platform fee rate (in decimal form, e.g., 1% = 0.01).
    - avax_transaction_cost (float): The AVAX transaction cost per transaction.
    - days (int): The number of days to calculate the yield for.

    Returns:
    - float: The potential yield.
    """

    # Convert days to years
    years = days / 365

    # Calculate the total rewards rate per year, factoring in platform fees
    total_rewards_rate = (annual_rewards * (1 - platform_fee))

    # Calculate the effective interest rate per compounding period
    effective_interest_rate = (1 + (total_rewards_rate / compounding_frequency)) - 1

    # Calculate the future value of the investment, using the formula for compound interest
    future_value = principal * math.pow((1 + effective_interest_rate), (compounding_frequency * years))

    # Calculate the total AVAX transaction costs
    total_avax_transaction_costs = avax_transaction_cost * compounding_frequency * years

    # Calculate the net potential yield
    net_potential_yield = future_value - principal - total_avax_transaction_costs

    return net_potential_yield


def main():
    try:
        # Example usage:
        principal = 1000  # Initial liquidity of 1000
        annual_rewards = 0.10  # 10% annual rewards rate
        compounding_frequency = 365  # Daily compounding
        platform_fee = 0.01  # 1% platform fee
        avax_transaction_cost = 0.05  # $0.05 AVAX transaction cost per transaction
        days = 365  # Calculate yield for 1 year

        net_potential_yield = calculate_potential_yield(
            principal, 
            annual_rewards, 
            compounding_frequency, 
            platform_fee, 
            avax_transaction_cost, 
            days
        )

        print(f"Net potential yield: ${net_potential_yield:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
