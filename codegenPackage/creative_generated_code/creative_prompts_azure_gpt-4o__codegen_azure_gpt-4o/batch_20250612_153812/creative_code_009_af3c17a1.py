"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assets-maple.finance
Prompt: Create a Python script to simulate lending USDC to Maple Finance's High Yield Secured Lending Pool and calculate expected returns based on the Target APY.
Generated: DETERMINISTIC_af3c17a1352c7e07
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Simulate lending USDC to Maple Finance's High Yield Secured Lending Pool and calculate expected returns based on the Target APY.

This script assumes the user provides:
- USDC amount to lend
- Target APY (Annual Percentage Yield)
- Lending duration in days

Output:
- Expected returns (principal + interest)

Note: This is a simulation and does not interact with Maple Finance's actual API or smart contracts.
"""

from decimal import Decimal
import sys


def calculate_expected_returns(principal_usdc: Decimal, target_apy: Decimal, days: int) -> Decimal:
    """
    Calculate expected returns based on principal, Target APY, and lending duration.
    
    Args:
        principal_usdc (Decimal): The amount of USDC being lent.
        target_apy (Decimal): The annual percentage yield (APY) as a decimal (e.g., 0.15 for 15%).
        days (int): Lending duration in days.

    Returns:
        Decimal: Total value at the end of the lending period (principal + interest).
    """
    try:
        # Ensure valid inputs
        if principal_usdc <= 0:
            raise ValueError("Principal must be greater than 0.")
        if target_apy < 0:
            raise ValueError("Target APY cannot be negative.")
        if days <= 0:
            raise ValueError("Days must be greater than 0.")

        # Calculate daily interest rate
        daily_rate = target_apy / Decimal(365)

        # Calculate interest earned for the given duration
        interest = principal_usdc * daily_rate * Decimal(days)

        # Calculate total value
        total_value = principal_usdc + interest
        return total_value

    except Exception as e:
        # Handle any unexpected errors
        print(f"Error while calculating expected returns: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """
    Main function to simulate lending and calculate expected returns.
    """
    try:
        # Input from the user
        principal_str = input("Enter the amount of USDC to lend: ")
        apy_str = input("Enter the Target APY (as a percentage, e.g., 15 for 15%): ")
        days_str = input("Enter the lending duration in days: ")

        # Convert inputs to appropriate types
        principal_usdc = Decimal(principal_str)
        target_apy = Decimal(apy_str) / Decimal(100)  # Convert percentage to decimal
        days = int(days_str)

        # Calculate expected returns
        total_value = calculate_expected_returns(principal_usdc, target_apy, days)

        # Output results
        print(f"\nLending Summary:")
        print(f"Principal (USDC): {principal_usdc}")
        print(f"Target APY: {target_apy * Decimal(100)}%")
        print(f"Lending Duration: {days} days")
        print(f"Expected Total Value (Principal + Interest): {total_value:.2f} USDC")

    except Exception as e:
        # Handle input errors
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```
