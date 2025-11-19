"""
Generated Code Metadata:
========================
Original URL: https://capitalwealthinvestmentltd.com
Prompt: Write a Python script to calculate the potential returns on investment for the CLASSIC PLAN offered by capitalwealthinvestmentltd, assuming an initial investment of $1000 and a 5% referral bonus.
Generated: DETERMINISTIC_d762e8d4e74af9a2
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate potential returns on investment for the CLASSIC PLAN offered by Capital Wealth Investment Ltd.
Assumptions:
- Initial investment: $1000
- Referral bonus: 5%
- The CLASSIC PLAN has a fixed annual return rate of 12% (assumed for this example).
- The investment duration is 1 year.

This script calculates:
1. Annual return on the initial investment.
2. Total return including the referral bonus.
"""

# Constants
INITIAL_INVESTMENT = 1000  # Initial investment amount in USD
ANNUAL_RETURN_RATE = 0.12  # Annual return rate (12%)
REFERRAL_BONUS_RATE = 0.05  # Referral bonus rate (5%)

def calculate_returns(initial_investment, annual_rate, referral_bonus_rate):
    """
    Calculate the potential returns on investment.

    Parameters:
        initial_investment (float): The initial investment amount.
        annual_rate (float): The annual return rate as a decimal.
        referral_bonus_rate (float): The referral bonus rate as a decimal.

    Returns:
        dict: A dictionary containing the annual return, referral bonus, and total return.
    """
    try:
        # Calculate annual return
        annual_return = initial_investment * annual_rate
        
        # Calculate referral bonus
        referral_bonus = initial_investment * referral_bonus_rate
        
        # Calculate total return
        total_return = initial_investment + annual_return + referral_bonus
        
        # Return results as a dictionary
        return {
            "Annual Return": round(annual_return, 2),
            "Referral Bonus": round(referral_bonus, 2),
            "Total Return": round(total_return, 2)
        }
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred during calculation: {e}")
        return None

def main():
    """
    Main function to execute the investment return calculation.
    """
    print("Calculating potential returns for the CLASSIC PLAN...")
    
    # Perform calculation
    results = calculate_returns(INITIAL_INVESTMENT, ANNUAL_RETURN_RATE, REFERRAL_BONUS_RATE)
    
    if results:
        # Display results
        print("Results:")
        print(f"Initial Investment: ${INITIAL_INVESTMENT}")
        print(f"Annual Return: ${results['Annual Return']}")
        print(f"Referral Bonus: ${results['Referral Bonus']}")
        print(f"Total Return: ${results['Total Return']}")
    else:
        print("Failed to calculate returns.")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
