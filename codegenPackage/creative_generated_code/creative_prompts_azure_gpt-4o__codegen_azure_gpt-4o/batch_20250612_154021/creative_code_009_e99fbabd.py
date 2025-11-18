"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterddex.com
Prompt: Write a script to calculate and display the potential earnings from staking BTC and CAKE on Aster's platform, factoring in APY rates and staking duration.
Generated: DETERMINISTIC_e99fbabd3d7f1fda
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def calculate_earnings(principal, apy, duration_days):
    """
    Calculate potential earnings based on principal amount, APY, and staking duration.

    Args:
        principal (float): The amount of cryptocurrency staked.
        apy (float): Annual Percentage Yield (in percentage, e.g., 12.5 for 12.5% APY).
        duration_days (int): Duration of staking in days.

    Returns:
        tuple: Tuple containing:
            - total_earnings (float): Total earnings accrued during the staking period.
            - final_balance (float): Principal amount + total earnings.
    """
    # Convert APY percentage to a daily rate
    daily_rate = apy / 100 / 365

    # Compute total earnings (compound interest not applied for simplicity)
    total_earnings = principal * daily_rate * duration_days

    # Compute final balance after staking
    final_balance = principal + total_earnings

    return total_earnings, final_balance


def main():
    """
    Main function to calculate potential staking earnings for BTC and CAKE on Aster's platform.
    """
    try:
        # Staking inputs for BTC
        btc_principal = float(input("Enter the amount of BTC to stake: "))
        btc_apy = float(input("Enter the APY rate for BTC (e.g., 12.5): "))
        btc_duration = int(input("Enter the staking duration for BTC (in days): "))

        # Staking inputs for CAKE
        cake_principal = float(input("Enter the amount of CAKE to stake: "))
        cake_apy = float(input("Enter the APY rate for CAKE (e.g., 50.2): "))
        cake_duration = int(input("Enter the staking duration for CAKE (in days): "))

        # Calculate earnings for BTC
        btc_earnings, btc_final_balance = calculate_earnings(btc_principal, btc_apy, btc_duration)

        # Calculate earnings for CAKE
        cake_earnings, cake_final_balance = calculate_earnings(cake_principal, cake_apy, cake_duration)

        # Display results
        print("\n===== Staking Results =====")
        print(f"BTC Staking ({btc_principal} BTC):")
        print(f"  APY Rate: {btc_apy}%")
        print(f"  Duration: {btc_duration} days")
        print(f"  Total Earnings: {btc_earnings:.8f} BTC")
        print(f"  Final Balance: {btc_final_balance:.8f} BTC\n")

        print(f"CAKE Staking ({cake_principal} CAKE):")
        print(f"  APY Rate: {cake_apy}%")
        print(f"  Duration: {cake_duration} days")
        print(f"  Total Earnings: {cake_earnings:.8f} CAKE")
        print(f"  Final Balance: {cake_final_balance:.8f} CAKE")

    except ValueError:
        print("Error: Invalid input value. Please ensure you enter numeric values for principal, APY, and duration.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
