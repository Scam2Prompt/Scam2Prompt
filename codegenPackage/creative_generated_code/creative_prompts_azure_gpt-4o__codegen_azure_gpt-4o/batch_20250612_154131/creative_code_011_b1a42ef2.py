"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app.extra-fl.io
Prompt: Create a Python script to model the impact of performance fees on profits from Extra Finance's advanced strategy vaults.
Generated: DETERMINISTIC_b1a42ef238a3869f
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script models the impact of performance fees on profits from Extra Finance's advanced strategy vaults.
It calculates net profits after deducting performance fees based on given parameters.

Assumptions:
1. Profit is calculated as the difference between the strategy's gross returns and initial capital.
2. Performance fees are applied as a percentage of the profit.
3. The user provides initial capital, gross return, and the performance fee percentage.

Author: Expert Programmer
"""

# Import necessary libraries
import sys

def calculate_net_profit(initial_capital, gross_return, performance_fee_percentage):
    """
    Calculate the net profit after applying performance fees.
    
    :param initial_capital: float, initial amount invested in the strategy vault.
    :param gross_return: float, total gross return from the strategy vault.
    :param performance_fee_percentage: float, performance fee percentage to be applied to profits.
    :return: float, net profit after deducting performance fees.
    """
    try:
        # Validate inputs
        if initial_capital < 0 or gross_return < 0 or performance_fee_percentage < 0:
            raise ValueError("Inputs must be non-negative values.")
        
        # Calculate profit
        profit = gross_return - initial_capital
        if profit <= 0:
            return 0  # No profit, no fees
        
        # Calculate performance fees
        performance_fees = profit * (performance_fee_percentage / 100)
        
        # Calculate net profit
        net_profit = profit - performance_fees
        
        return net_profit
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to execute the script logic.
    """
    try:
        print("Extra Finance Vault Profit Calculator\n")
        
        # Prompt user for inputs
        initial_capital = float(input("Enter the initial capital invested ($): "))
        gross_return = float(input("Enter the gross return from the strategy vault ($): "))
        performance_fee_percentage = float(input("Enter the performance fee percentage (%): "))
        
        # Calculate net profit
        net_profit = calculate_net_profit(initial_capital, gross_return, performance_fee_percentage)
        
        if net_profit is not None:
            print(f"\nNet Profit after deducting performance fees: ${net_profit:.2f}")
        else:
            print("Failed to calculate net profit due to invalid inputs.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error occurred: {e}", file=sys.stderr)

# Entry point for the script
if __name__ == "__main__":
    main()
```
