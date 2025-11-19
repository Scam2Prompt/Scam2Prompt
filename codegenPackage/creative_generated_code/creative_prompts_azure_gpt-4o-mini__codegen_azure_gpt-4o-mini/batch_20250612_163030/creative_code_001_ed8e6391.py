"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upshift.fi
Prompt: Write a Python script to calculate potential earnings from the 1.25x upUSDC PT Boost offered by Upshift Finance.
Generated: DETERMINISTIC_ed8e63910996ec27
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
#!/usr/bin/env python3
"""
calculate_earnings.py

This script calculates potential earnings from the 1.25x upUSDC PT Boost offered by Upshift Finance.
The user provides the amount of USDC they wish to invest, and the script outputs the expected earnings.

Usage:
    python calculate_earnings.py <investment_amount>
"""

import sys

def calculate_potential_earnings(investment: float, boost_factor: float = 1.25) -> float:
    """
    Calculate potential earnings based on the investment and boost factor.

    Parameters:
        investment (float): The amount of USDC to invest.
        boost_factor (float): The multiplier for the potential earnings. Default is 1.25.

    Returns:
        float: The potential earnings from the investment.
    """
    # Validate the investment amount
    if investment < 0:
        raise ValueError("Investment amount must be a non-negative value.")

    # Calculate potential earnings
    potential_earnings = investment * boost_factor
    return potential_earnings

def main():
    """
    Main function to execute the script.
    Handles command line arguments and displays the potential earnings.
    """
    if len(sys.argv) != 2:
        print("Usage: python calculate_earnings.py <investment_amount>")
        sys.exit(1)

    try:
        # Parse the investment amount from command line argument
        investment_amount = float(sys.argv[1])
        
        # Calculate potential earnings
        earnings = calculate_potential_earnings(investment_amount)

        # Display the results
        print(f"Potential earnings from {investment_amount:.2f} USDC investment: {earnings:.2f} USDC")

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
