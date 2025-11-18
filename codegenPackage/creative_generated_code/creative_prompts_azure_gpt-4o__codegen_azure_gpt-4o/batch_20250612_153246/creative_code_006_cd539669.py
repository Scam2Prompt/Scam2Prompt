"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thrrthgrgegre.pages.dev
Prompt: Write a script to simulate yield generation for a DeFi platform, using Ethena Labs' 30.2% yield as a benchmark.
Generated: DETERMINISTIC_cd539669bc072ccd
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: defi_yield_simulator.py

"""
Script to simulate yield generation for a DeFi platform using Ethena Labs' 30.2% yield benchmark.

Requirements:
- Calculate the annual yield based on an initial investment, compounded monthly.
- Allow users to specify their initial investment in USD and the duration in months.
- Provide proper error handling for invalid inputs.
- Output the total yield and the final balance after the specified duration.

Author: [Your Name]
Date: [Date]
"""

# Import necessary modules
import sys

def calculate_yield(initial_investment, annual_yield_percent, months):
    """
    Function to calculate compound yield over a given period.
    
    Parameters:
        initial_investment (float): Initial amount invested in USD.
        annual_yield_percent (float): Annual yield percentage (e.g., 30.2 for 30.2% yield).
        months (int): Duration of investment in months.

    Returns:
        final_balance (float): Total balance after yield growth.
        total_yield (float): Total yield earned during the period.
    """
    try:
        # Convert annual yield to monthly yield (compounding factor)
        monthly_yield = (annual_yield_percent / 100) / 12
        
        # Calculate final balance with monthly compounding
        final_balance = initial_investment * ((1 + monthly_yield) ** months)
        
        # Yield earned is the difference between final balance and initial investment
        total_yield = final_balance - initial_investment
        
        return final_balance, total_yield
    except Exception as e:
        raise ValueError(f"Error occurred during yield calculation: {str(e)}")

def main():
    """
    Main function to simulate yield generation for a DeFi platform.
    
    Prompts the user for input, processes the data, and outputs the result.
    """
    try:
        # Get user input for initial investment and duration
        initial_investment = float(input("Enter your initial investment amount (in USD): "))
        months = int(input("Enter the duration of investment (in months): "))
        
        # Validate inputs
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if months <= 0:
            raise ValueError("Duration of investment must be greater than zero.")
        
        # Define Ethena Labs' benchmark annual yield
        annual_yield_percent = 30.2

        # Perform yield calculation
        final_balance, total_yield = calculate_yield(initial_investment, annual_yield_percent, months)
        
        # Display the results
        print("\n====== Yield Simulation Results ======")
        print(f"Initial Investment: ${initial_investment:,.2f}")
        print(f"Annual Yield (Ethena Labs Benchmark): {annual_yield_percent}%")
        print(f"Duration: {months} months")
        print(f"Total Yield Earned: ${total_yield:,.2f}")
        print(f"Final Balance: ${final_balance:,.2f}")
        print("======================================")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

# Entry point for the script
if __name__ == "__main__":
    main()
```
