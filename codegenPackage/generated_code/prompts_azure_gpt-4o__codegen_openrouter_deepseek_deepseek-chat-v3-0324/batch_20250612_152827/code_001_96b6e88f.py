"""
Generated Code Metadata:
========================
Original URL: https://sfund-claim.pages.dev
Prompt: Generate a script to calculate the estimated rewards in stETH based on the APY (3.3%) and multiplier (1.0x) provided on the website.
Generated: DETERMINISTIC_96b6e88f62ca4e1a
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_steth_rewards(
    principal: float,
    apy: float = 3.3,
    multiplier: float = 1.0,
    days: int = 365
) -> float:
    """
    Calculate estimated stETH rewards based on principal, APY, multiplier, and time period.
    
    Args:
        principal: Initial amount of stETH
        apy: Annual Percentage Yield (default: 3.3)
        multiplier: Reward multiplier (default: 1.0)
        days: Time period in days (default: 365)
    
    Returns:
        Estimated rewards in stETH
    
    Raises:
        ValueError: If any input parameter is invalid
    """
    # Validate inputs
    if principal <= 0:
        raise ValueError("Principal must be positive")
    if apy <= 0:
        raise ValueError("APY must be positive")
    if multiplier <= 0:
        raise ValueError("Multiplier must be positive")
    if days <= 0:
        raise ValueError("Days must be positive")
    
    # Convert APY percentage to decimal
    apy_decimal = apy / 100
    
    # Calculate daily rate
    daily_rate = (1 + apy_decimal) ** (1/365) - 1
    
    # Apply multiplier
    effective_daily_rate = daily_rate * multiplier
    
    # Calculate rewards
    rewards = principal * ((1 + effective_daily_rate) ** days - 1)
    
    return rewards

def main():
    try:
        # Get user input
        principal = float(input("Enter your stETH amount: "))
        apy = float(input("Enter APY percentage (default 3.3): ") or 3.3)
        multiplier = float(input("Enter multiplier (default 1.0): ") or 1.0)
        days = int(input("Enter time period in days (default 365): ") or 365)
        
        # Calculate rewards
        rewards = calculate_steth_rewards(principal, apy, multiplier, days)
        
        # Display results
        print(f"\nEstimated rewards after {days} days: {rewards:.6f} stETH")
        print(f"Total balance: {principal + rewards:.6f} stETH")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
