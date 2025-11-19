"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomatoclub.xyz
Prompt: Write a Python script that calculates the actual interest from DeFi yield rates, considering the nuances of APY as discussed in the article.
Generated: DETERMINISTIC_63ac86ff1cb36fc3
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse
import math

def calculate_actual_interest(principal, apy, days_staked):
    """
    Calculates the actual interest earned from a DeFi yield rate.
    
    Formula assumes APY (Annual Percentage Yield) is compounded daily.
    
    Parameters:
        principal (float): Initial investment amount in USD.
        apy (float): Annual Percentage Yield (in percentage, e.g., 12 for 12% APY).
        days_staked (int): Number of days the funds are staked.
        
    Returns:
        float: The actual interest earned.
    """
    try:
        # Validate input
        if principal <= 0:
            raise ValueError("Principal amount must be greater than 0.")
        if apy < 0:
            raise ValueError("APY cannot be negative.")
        if days_staked < 0:
            raise ValueError("Days staked cannot be negative.")
        
        # Convert APY from percentage to decimal
        apy_decimal = apy / 100.0
        
        # Calculate daily rate (assuming daily compounding)
        daily_rate = math.pow(1 + apy_decimal, 1 / 365) - 1
        
        # Calculate total future value after staking period
        future_value = principal * math.pow(1 + daily_rate, days_staked)
        
        # Interest earned is the difference between future value and principal
        interest_earned = future_value - principal
        
        return interest_earned
    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Main function to parse user input and calculate the actual interest.
    """
    # Parse arguments
    parser = argparse.ArgumentParser(description="Calculate actual interest from DeFi APY yield rates.")
    parser.add_argument("principal", type=float, help="Initial investment amount in USD.")
    parser.add_argument("apy", type=float, help="Annual Percentage Yield (APY) as a percentage (e.g., 12 for 12%).")
    parser.add_argument("days_staked", type=int, help="Number of days the funds are staked.")
    args = parser.parse_args()

    # Calculate interest
    interest = calculate_actual_interest(args.principal, args.apy, args.days_staked)
    
    if interest is not None:
        print(f"\nPrincipal: ${args.principal:.2f}")
        print(f"APY: {args.apy:.2f}%")
        print(f"Days Staked: {args.days_staked}")
        print(f"Interest Earned: ${interest:.2f}\n")
    else:
        print("Failed to calculate interest due to invalid input or unexpected error.")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
