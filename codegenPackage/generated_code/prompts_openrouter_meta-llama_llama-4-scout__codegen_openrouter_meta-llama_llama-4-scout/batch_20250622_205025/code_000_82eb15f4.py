"""
Generated Code Metadata:
========================
Original URL: https://mythetawallet.com
Prompt: Write a Python script to estimate daily staked Theta earnings based on the provided statistics, including 30-day block production average and TFuel price average.
Generated: DETERMINISTIC_82eb15f4c0af06ba
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Theta Staking Earnings Estimator

Estimates daily staked Theta earnings based on provided statistics.

Usage:
    python theta_staking_estimator.py
"""

import argparse

def calculate_daily_earnings(block_production_average, tfuel_price_average):
    """
    Calculates daily staked Theta earnings.

    Args:
        block_production_average (float): 30-day block production average.
        tfuel_price_average (float): TFuel price average.

    Returns:
        float: Estimated daily staked Theta earnings.
    """
    # Assuming 1 block = 1 Theta, and 1 Theta = TFuel_price_average TFuel
    # Also assuming 20% of block reward goes to staker
    block_reward = 1  # Replace with actual block reward value
    staker_share = 0.2  # 20% of block reward

    daily_blocks = block_production_average / 30
    daily_earnings_theta = daily_blocks * block_reward * staker_share
    daily_earnings_tfuel = daily_earnings_theta * tfuel_price_average

    return daily_earnings_theta, daily_earnings_tfuel

def main():
    parser = argparse.ArgumentParser(description='Theta Staking Earnings Estimator')
    parser.add_argument('--block-production-average', type=float, required=True,
                        help='30-day block production average')
    parser.add_argument('--tfuel-price-average', type=float, required=True,
                        help='TFuel price average')

    args = parser.parse_args()

    try:
        daily_earnings_theta, daily_earnings_tfuel = calculate_daily_earnings(
            args.block_production_average, args.tfuel_price_average
        )

        print(f"Estimated daily staked Theta earnings: {daily_earnings_theta:.6f} Theta")
        print(f"Estimated daily staked Theta earnings: {daily_earnings_tfuel:.6f} TFuel")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
