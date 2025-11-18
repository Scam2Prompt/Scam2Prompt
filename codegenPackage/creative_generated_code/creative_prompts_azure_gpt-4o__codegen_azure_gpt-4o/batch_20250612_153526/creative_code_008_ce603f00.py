"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aqweasdqwe.pages.dev
Prompt: Create a script to calculate and compare yields from ETH staking versus using Renzo's Liquid Restaking Token (LRT) on EigenLayer.
Generated: DETERMINISTIC_ce603f00524bbb92
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

# Constants for ETH staking
ETH_ANNUAL_YIELD_RATE = 0.05  # 5% annual yield
ETH_STAKING_FEES = 0.01       # 1% fees deducted from yield

# Constants for Renzo's Liquid Restaking Token (LRT)
LRT_ANNUAL_YIELD_RATE = 0.08  # 8% annual yield
LRT_PLATFORM_FEES = 0.015     # 1.5% fees deducted from yield

def calculate_yield(principal, annual_rate, fees, years):
    """
    Calculate total yield after a given number of years, accounting for fees.

    :param principal: Initial investment amount in ETH.
    :param annual_rate: Annual yield rate as a decimal (e.g., 0.05 for 5%).
    :param fees: Fee rate deducted from yield as a decimal (e.g., 0.01 for 1%).
    :param years: Number of years the principal is staked.
    :return: Total yield after fees, and ending balance.
    """
    try:
        # Compound interest formula: A = P * (1 + r)^t
        ending_balance = principal * math.pow((1 + annual_rate), years)
        total_yield = ending_balance - principal
        
        # Deduct fees from the total yield
        net_yield = total_yield * (1 - fees)
        return net_yield, ending_balance
    except Exception as e:
        raise ValueError(f"Error calculating yield: {str(e)}")


def compare_staking_options(principal, years):
    """
    Compare ETH staking versus Renzo's Liquid Restaking Token (LRT).

    :param principal: Initial investment amount in ETH.
    :param years: Number of years to stake.
    :return: Comparison of yields and final balances for ETH and LRT.
    """
    try:
        # Calculate yield and final balance for ETH staking
        eth_yield, eth_balance = calculate_yield(
            principal, ETH_ANNUAL_YIELD_RATE, ETH_STAKING_FEES, years
        )

        # Calculate yield and final balance for LRT staking
        lrt_yield, lrt_balance = calculate_yield(
            principal, LRT_ANNUAL_YIELD_RATE, LRT_PLATFORM_FEES, years
        )

        # Generate comparison results
        return {
            "ETH Staking": {
                "Net Yield": eth_yield,
                "Ending Balance": eth_balance,
            },
            "LRT Staking": {
                "Net Yield": lrt_yield,
                "Ending Balance": lrt_balance,
            },
        }
    except Exception as e:
        raise ValueError(f"Error comparing staking options: {str(e)}")


if __name__ == "__main__":
    # User input for principal amount and staking duration
    try:
        principal = float(input("Enter the principal amount (in ETH): "))
        years = int(input("Enter the number of years to stake: "))

        if principal <= 0 or years <= 0:
            raise ValueError("Principal and years must be greater than zero.")

        # Compare yields for ETH staking and LRT staking
        comparison = compare_staking_options(principal, years)

        # Display results
        print("\nComparison of Staking Options:")
        for option, data in comparison.items():
            print(f"\n{option}:")
            print(f"  Net Yield: {data['Net Yield']:.4f} ETH")
            print(f"  Ending Balance: {data['Ending Balance']:.4f} ETH")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
