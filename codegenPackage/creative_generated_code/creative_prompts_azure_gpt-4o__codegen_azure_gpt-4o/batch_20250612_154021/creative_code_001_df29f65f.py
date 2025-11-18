"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterdxe.com
Prompt: Generate a script to calculate staking rewards for assets like BNB, USDT, BTC, and CAKE on Aster DEX, considering an APY of up to 30%.
Generated: DETERMINISTIC_df29f65fbe744995
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
SUPPORTED_ASSETS = ["BNB", "USDT", "BTC", "CAKE"]  # Supported asset list
MAX_APY = 30  # Maximum APY (Annual Percentage Yield) in percentage

# Error classes
class UnsupportedAssetError(Exception):
    """Raised when an unsupported asset is provided."""
    pass

class APYError(Exception):
    """Raised when an invalid APY is provided."""
    pass

# Function to calculate staking rewards
def calculate_staking_rewards(asset_name, principal_amount, apy, staking_days):
    """
    Calculates staking rewards for a given asset and parameters.

    Parameters:
        asset_name (str): The name of the asset (e.g., "BNB", "USDT").
        principal_amount (float): The initial staked amount.
        apy (float): Annual Percentage Yield (in percentage, e.g., 30 for 30%).
        staking_days (int): Number of days the asset is staked.

    Returns:
        float: The total rewards earned.
    """
    try:
        # Validate asset
        if asset_name not in SUPPORTED_ASSETS:
            raise UnsupportedAssetError(f"Asset '{asset_name}' is not supported. Supported assets: {SUPPORTED_ASSETS}")

        # Validate APY
        if apy < 0 or apy > MAX_APY:
            raise APYError(f"Invalid APY '{apy}'. APY must be between 0 and {MAX_APY}.")

        # Validate principal amount
        if principal_amount <= 0:
            raise ValueError("Principal amount must be greater than zero.")

        # Validate staking days
        if staking_days <= 0:
            raise ValueError("Staking days must be greater than zero.")

        # Calculate rewards
        daily_rate = apy / 100 / 365  # Convert APY to daily rate
        rewards = principal_amount * daily_rate * staking_days
        return rewards

    except UnsupportedAssetError as e:
        logging.error(e)
        raise

    except APYError as e:
        logging.error(e)
        raise

    except ValueError as e:
        logging.error(e)
        raise

if __name__ == "__main__":
    # Example usage
    try:
        # Input parameters
        asset = "BNB"
        principal = 1000.00  # Amount in the asset
        apy = 30  # Annual Percentage Yield in percentage
        days_staked = 90  # Number of days the asset is staked

        # Calculate rewards
        logging.info(f"Calculating rewards for {asset} with principal {principal}, APY {apy}%, and staking duration {days_staked} days.")
        rewards = calculate_staking_rewards(asset, principal, apy, days_staked)

        # Output the results
        logging.info(f"Total staking rewards earned for {asset}: {rewards:.2f}")

    except Exception as e:
        logging.error(f"Error calculating staking rewards: {e}")
```
