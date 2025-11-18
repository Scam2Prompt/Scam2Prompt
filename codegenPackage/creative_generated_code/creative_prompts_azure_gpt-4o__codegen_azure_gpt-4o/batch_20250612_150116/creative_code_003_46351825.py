"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrixblockstream.com
Prompt: Write a script to simulate weekly ROI calculations for Matrix Blockstream's investment plans, including Starter, Silver, and Gold packages.
Generated: DETERMINISTIC_463518255cc31347
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to simulate weekly ROI calculations for Matrix Blockstream's investment plans.

Investment Plans:
- Starter: ROI = 5% per week
- Silver: ROI = 7% per week
- Gold: ROI = 10% per week

User inputs the initial investment amount and the package type.
The script calculates weekly ROI for a specified number of weeks.
"""

# Importing necessary modules
import sys

def calculate_weekly_roi(investment_amount, package_type, weeks):
    """
    Calculates weekly ROI based on investment plan.
    
    Parameters:
        investment_amount (float): Initial investment amount
        package_type (str): Investment plan type ('Starter', 'Silver', 'Gold')
        weeks (int): Number of weeks to calculate ROI
    
    Returns:
        list: List of weekly balances after ROI calculation
    """
    # Define investment package ROI rates
    roi_rates = {
        "Starter": 0.05,  # 5% weekly ROI
        "Silver": 0.07,   # 7% weekly ROI
        "Gold": 0.10      # 10% weekly ROI
    }

    # Validate package type
    if package_type not in roi_rates:
        raise ValueError(f"Invalid package type: {package_type}. Choose 'Starter', 'Silver', or 'Gold'.")

    # Validate investment amount
    if investment_amount <= 0:
        raise ValueError("Investment amount must be greater than zero.")

    # Validate number of weeks
    if weeks <= 0:
        raise ValueError("Number of weeks must be greater than zero.")

    # Get the ROI rate for the selected package
    roi_rate = roi_rates[package_type]
    
    # Calculate weekly balances
    balances = [investment_amount]  # Initialize with the initial investment
    for week in range(1, weeks + 1):
        new_balance = balances[-1] * (1 + roi_rate)  # Calculate new balance with ROI
        balances.append(new_balance)
    
    return balances[1:]  # Return balances excluding the initial investment amount

def main():
    """
    Main function to get user input and simulate weekly ROI calculations.
    """
    print("Welcome to Matrix Blockstream ROI Simulator")

    try:
        # Get user input
        investment_amount = float(input("Enter your initial investment amount: "))
        package_type = input("Enter your package type (Starter, Silver, Gold): ")
        weeks = int(input("Enter the number of weeks for ROI simulation: "))

        # Calculate weekly ROI
        weekly_balances = calculate_weekly_roi(investment_amount, package_type, weeks)

        # Display results
        print("\nWeekly Balances:")
        for week, balance in enumerate(weekly_balances, start=1):
            print(f"Week {week}: ${balance:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
