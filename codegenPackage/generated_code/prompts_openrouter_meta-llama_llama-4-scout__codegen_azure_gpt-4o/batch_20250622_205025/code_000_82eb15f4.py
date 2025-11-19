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
import sys

def estimate_theta_earnings(staked_theta, block_production_avg, tfuel_price_avg):
    """
    Estimate daily staked Theta earnings based on provided statistics.

    Parameters:
        staked_theta (float): Amount of Theta staked.
        block_production_avg (float): 30-day average of block production.
        tfuel_price_avg (float): 30-day average price of TFuel.

    Returns:
        float: Estimated daily earnings in TFuel.
    """
    try:
        # Validate inputs
        if staked_theta <= 0 or block_production_avg <= 0 or tfuel_price_avg <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Constants
        TOTAL_THETA_SUPPLY = 1000000000  # Total Theta supply (example value)
        TFUEL_PER_BLOCK = 5  # TFuel earned per block (example value)

        # Calculate the proportion of staked Theta to total supply
        staking_ratio = staked_theta / TOTAL_THETA_SUPPLY

        # Estimate daily earnings in TFuel
        daily_blocks = block_production_avg * 24  # Assuming 24 hours of block production
        daily_tfuel_earnings = staking_ratio * daily_blocks * TFUEL_PER_BLOCK

        return daily_tfuel_earnings

    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def main():
    """
    Main function to interact with the user and calculate Theta earnings.
    """
    try:
        print("Theta Staking Earnings Estimator")
        print("--------------------------------")

        # Get user inputs
        staked_theta = float(input("Enter the amount of Theta staked: "))
        block_production_avg = float(input("Enter the 30-day block production average: "))
        tfuel_price_avg = float(input("Enter the 30-day TFuel price average: "))

        # Estimate earnings
        daily_earnings = estimate_theta_earnings(staked_theta, block_production_avg, tfuel_price_avg)

        # Display results
        print(f"\nEstimated daily earnings: {daily_earnings:.2f} TFuel")
        print(f"At an average TFuel price of {tfuel_price_avg:.2f}, this is worth approximately ${daily_earnings * tfuel_price_avg:.2f} per day.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
