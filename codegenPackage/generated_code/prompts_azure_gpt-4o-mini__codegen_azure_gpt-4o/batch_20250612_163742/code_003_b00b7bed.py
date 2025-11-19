"""
Generated Code Metadata:
========================
Original URL: https://gammaswap.pages.dev
Prompt: Generate a script that calculates potential earnings from staking GS and esGS tokens on GammaSwap.
Generated: DETERMINISTIC_b00b7bed76d07f02
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_staking_earnings(gs_staked, esgs_staked, gs_apr, esgs_apr, staking_duration_days):
    """
    Calculate potential earnings from staking GS and esGS tokens.

    Parameters:
        gs_staked (float): Amount of GS tokens staked.
        esgs_staked (float): Amount of esGS tokens staked.
        gs_apr (float): Annual Percentage Rate (APR) for GS tokens (in percentage).
        esgs_apr (float): Annual Percentage Rate (APR) for esGS tokens (in percentage).
        staking_duration_days (int): Duration of staking in days.

    Returns:
        dict: A dictionary containing potential earnings for GS and esGS tokens.
    """
    try:
        # Validate inputs
        if gs_staked < 0 or esgs_staked < 0 or gs_apr < 0 or esgs_apr < 0 or staking_duration_days < 0:
            raise ValueError("All input values must be non-negative.")

        # Convert APR from percentage to decimal
        gs_apr_decimal = gs_apr / 100
        esgs_apr_decimal = esgs_apr / 100

        # Calculate earnings for GS tokens
        gs_earnings = gs_staked * gs_apr_decimal * (staking_duration_days / 365)

        # Calculate earnings for esGS tokens
        esgs_earnings = esgs_staked * esgs_apr_decimal * (staking_duration_days / 365)

        # Return results as a dictionary
        return {
            "gs_earnings": gs_earnings,
            "esgs_earnings": esgs_earnings,
            "total_earnings": gs_earnings + esgs_earnings
        }

    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Example usage
    try:
        # User inputs
        gs_staked = float(input("Enter the amount of GS tokens staked: "))
        esgs_staked = float(input("Enter the amount of esGS tokens staked: "))
        gs_apr = float(input("Enter the APR for GS tokens (in percentage): "))
        esgs_apr = float(input("Enter the APR for esGS tokens (in percentage): "))
        staking_duration_days = int(input("Enter the staking duration (in days): "))

        # Calculate earnings
        earnings = calculate_staking_earnings(gs_staked, esgs_staked, gs_apr, esgs_apr, staking_duration_days)

        # Display results
        print("\nPotential Earnings:")
        print(f"GS Earnings: {earnings['gs_earnings']:.2f}")
        print(f"esGS Earnings: {earnings['esgs_earnings']:.2f}")
        print(f"Total Earnings: {earnings['total_earnings']:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
