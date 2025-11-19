"""
Generated Code Metadata:
========================
Original URL: https://mythetawallet.com
Prompt: Write a code snippet to calculate the estimated staked Theta earnings in USD, considering the provided statistics.
Generated: DETERMINISTIC_b188c960e2974fc6
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_staked_theta_earnings(
    total_staked_theta: float, 
    total_theta_supply: float, 
    current_theta_price: float, 
    estimated_annual_rewards: float, 
    compounding_frequency: int = 365
) -> float:
    """
    Calculate the estimated staked Theta earnings in USD.

    Args:
    - total_staked_theta (float): The total amount of staked Theta.
    - total_theta_supply (float): The total supply of Theta.
    - current_theta_price (float): The current price of Theta in USD.
    - estimated_annual_rewards (float): The estimated annual rewards in Theta.
    - compounding_frequency (int): The frequency of compounding per year. Defaults to 365.

    Returns:
    - float: The estimated staked Theta earnings in USD.
    """

    # Validate inputs
    if total_staked_theta < 0 or total_theta_supply <= 0:
        raise ValueError("Total staked Theta and total Theta supply must be valid.")
    if current_theta_price <= 0:
        raise ValueError("Current Theta price must be greater than zero.")
    if estimated_annual_rewards < 0:
        raise ValueError("Estimated annual rewards must be non-negative.")

    # Calculate the estimated annual earnings in Theta
    estimated_annual_earnings_theta = (total_staked_theta / total_theta_supply) * estimated_annual_rewards

    # Calculate the estimated annual earnings in USD
    estimated_annual_earnings_usd = estimated_annual_earnings_theta * current_theta_price

    # Calculate the estimated daily earnings in USD, considering compounding frequency
    estimated_daily_earnings_usd = estimated_annual_earnings_usd / compounding_frequency

    return estimated_daily_earnings_usd


def main():
    try:
        # Example usage
        total_staked_theta = 10000.0  # Total staked Theta
        total_theta_supply = 1000000.0  # Total Theta supply
        current_theta_price = 2.50  # Current Theta price in USD
        estimated_annual_rewards = 50000.0  # Estimated annual rewards in Theta

        estimated_daily_earnings_usd = calculate_staked_theta_earnings(
            total_staked_theta, 
            total_theta_supply, 
            current_theta_price, 
            estimated_annual_rewards
        )

        print(f"Estimated daily staked Theta earnings in USD: ${estimated_daily_earnings_usd:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
