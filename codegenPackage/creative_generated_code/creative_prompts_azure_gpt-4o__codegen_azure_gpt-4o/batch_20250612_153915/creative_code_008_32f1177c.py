"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.me
Prompt: Create a Python script to automate Toncoin staking and calculate passive income based on staking rewards.
Generated: DETERMINISTIC_32f1177cf6caef02
Batch ID: 20250612_153915
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price?ids=toncoin&vs_currencies=usd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.ton.org/staking": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
from datetime import datetime, timedelta
from decimal import Decimal

# Constants
TON_API_URL = "https://api.ton.org/staking"  # Example API URL (replace with the actual one if exists)
STAKING_APY = 0.06  # Annual Percentage Yield (6% is an example value)
TON_DECIMALS = 9  # Toncoin uses 9 decimal places
SECONDS_IN_YEAR = 365 * 24 * 60 * 60

# Helper functions
def fetch_current_ton_price():
    """
    Fetch the current Toncoin price in USD.
    Replace with an actual API request if needed.
    """
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=toncoin&vs_currencies=usd")
        response.raise_for_status()
        data = response.json()
        return Decimal(data.get("toncoin", {}).get("usd", 0))
    except requests.RequestException as e:
        print(f"Error fetching Toncoin price: {e}")
        return Decimal(0)

def calculate_staking_rewards(staked_amount, days_staked):
    """
    Calculate staking rewards for a given amount and duration.
    :param staked_amount: Decimal, amount of Toncoin staked
    :param days_staked: int, number of staking days
    :return: Decimal, staking rewards earned
    """
    annual_rewards = staked_amount * Decimal(STAKING_APY)
    daily_rewards = annual_rewards / Decimal(365)
    return daily_rewards * Decimal(days_staked)

# Main function
def main():
    """
    Main function to automate Toncoin staking and calculate passive income.
    """
    try:
        # User input
        staked_amount = Decimal(input("Enter the amount of Toncoin you want to stake: "))
        staking_duration_days = int(input("Enter the number of days you plan to stake: "))

        # Basic validation
        if staked_amount <= 0 or staking_duration_days <= 0:
            print("Staked amount and staking duration must be positive values.")
            return

        # Calculate rewards
        staking_rewards = calculate_staking_rewards(staked_amount, staking_duration_days)
        current_ton_price = fetch_current_ton_price()
        total_rewards_usd = staking_rewards * current_ton_price

        # Display results
        print(f"\n===== Staking Summary =====")
        print(f"Staked Amount: {staked_amount} Toncoin")
        print(f"Staking Duration: {staking_duration_days} days")
        print(f"Estimated Rewards: {staking_rewards:.9f} Toncoin")
        if current_ton_price > 0:
            print(f"Current Toncoin Price: ${current_ton_price:.2f} USD")
            print(f"Estimated Rewards in USD: ${total_rewards_usd:.2f}")
        else:
            print("Unable to fetch current Toncoin price.")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
