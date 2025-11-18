"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketsfargo.com
Prompt: Create a Python script to calculate spreads for different trading plans (Classic, Silver, Gold, VIP) based on leverage ratios and investment amounts as described on Fargo Markets.
Generated: DETERMINISTIC_87cd0f70165b8d96
Batch ID: 20250612_154058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Trading Plan Spread Calculator Script

This script calculates spreads for different trading plans (Classic, Silver, Gold, VIP)
based on leverage ratios and investment amounts as described on Fargo Markets.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_spread(investment_amount, leverage_ratio, base_spread):
    """
    Calculate the spread based on the investment amount, leverage ratio, and base spread.
    
    Parameters:
        investment_amount (float): The amount invested.
        leverage_ratio (float): The leverage ratio applied to the trade.
        base_spread (float): The base spread percentage for the trading plan.
    
    Returns:
        float: Calculated spread value.
    """
    try:
        # Validate input values
        if investment_amount <= 0 or leverage_ratio <= 0 or base_spread <= 0:
            raise ValueError("Investment amount, leverage ratio, and base spread must be positive values.")
        
        # Formula to calculate spread
        spread = investment_amount * leverage_ratio * (base_spread / 100)
        return spread
    
    except ValueError as ve:
        print(f"ValueError: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the spread calculation for different trading plans.
    """
    # Trading plans with their respective base spread and leverage ratios
    trading_plans = {
        "Classic": {"base_spread": 0.5, "leverage_ratio": 10},
        "Silver": {"base_spread": 0.3, "leverage_ratio": 15},
        "Gold": {"base_spread": 0.2, "leverage_ratio": 20},
        "VIP": {"base_spread": 0.1, "leverage_ratio": 25},
    }
    
    # Prompt user for investment amount input
    try:
        investment_amount = float(input("Enter the investment amount (e.g., 1000): "))
        
        if investment_amount <= 0:
            raise ValueError("Investment amount must be a positive number.")

        print("\nSpread Calculation Results:")
        print("=" * 30)
        
        # Calculate and display spreads for each trading plan
        for plan, details in trading_plans.items():
            spread = calculate_spread(
                investment_amount, 
                details["leverage_ratio"], 
                details["base_spread"]
            )
            print(f"{plan} Plan: Spread = {spread:.2f}")
    
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Entry point for the script
if __name__ == "__main__":
    main()
```
