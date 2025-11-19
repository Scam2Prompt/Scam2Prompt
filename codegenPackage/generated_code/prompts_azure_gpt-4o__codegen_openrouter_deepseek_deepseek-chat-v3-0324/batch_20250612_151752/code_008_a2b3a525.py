"""
Generated Code Metadata:
========================
Original URL: https://tradezeenetwork.com
Prompt: Write a script to automate the selection of investment packages based on user preferences and deposit amounts, similar to the package selection process described on Tradezeenetwork.
Generated: DETERMINISTIC_a2b3a525b73c8e44
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from enum import Enum

class InvestmentPackage(Enum):
    """Enum representing available investment packages."""
    BRONZE = {
        'name': 'Bronze',
        'min_deposit': 100,
        'max_deposit': 999,
        'roi': 0.05,
        'duration_days': 30
    }
    SILVER = {
        'name': 'Silver',
        'min_deposit': 1000,
        'max_deposit': 4999,
        'roi': 0.07,
        'duration_days': 45
    }
    GOLD = {
        'name': 'Gold',
        'min_deposit': 5000,
        'max_deposit': 19999,
        'roi': 0.10,
        'duration_days': 60
    }
    PLATINUM = {
        'name': 'Platinum',
        'min_deposit': 20000,
        'max_deposit': 50000,
        'roi': 0.15,
        'duration_days': 90
    }

def get_user_input():
    """Get and validate user input for deposit amount."""
    while True:
        try:
            deposit = float(input("Enter your deposit amount (USD): "))
            if deposit <= 0:
                print("Deposit amount must be positive.")
                continue
            return deposit
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def select_package(deposit_amount):
    """Select the appropriate investment package based on deposit amount."""
    for package in InvestmentPackage:
        if (deposit_amount >= package.value['min_deposit'] and 
            deposit_amount <= package.value['max_deposit']):
            return package.value
    
    # If no package matches, suggest the minimum required for the lowest package
    min_package = min(InvestmentPackage, key=lambda p: p.value['min_deposit'])
    print(f"\nNo package available for ${deposit_amount:.2f}.")
    print(f"Minimum deposit required is ${min_package.value['min_deposit']:.2f} for {min_package.value['name']} package.")
    return None

def calculate_returns(package, deposit_amount):
    """Calculate projected returns for the selected package."""
    if not package:
        return None
    
    roi = package['roi']
    duration = package['duration_days']
    profit = deposit_amount * roi
    total_return = deposit_amount + profit
    
    return {
        'package_name': package['name'],
        'deposit_amount': deposit_amount,
        'roi_percentage': roi * 100,
        'duration_days': duration,
        'projected_profit': profit,
        'total_return': total_return
    }

def display_results(results):
    """Display the investment results to the user."""
    if not results:
        return
    
    print("\n--- Investment Package Details ---")
    print(f"Package: {results['package_name']}")
    print(f"Deposit Amount: ${results['deposit_amount']:.2f}")
    print(f"ROI: {results['roi_percentage']:.2f}%")
    print(f"Duration: {results['duration_days']} days")
    print(f"Projected Profit: ${results['projected_profit']:.2f}")
    print(f"Total Return: ${results['total_return']:.2f}")

def main():
    """Main function to run the investment package selector."""
    print("=== Investment Package Selector ===")
    print("Available Packages:")
    for package in InvestmentPackage:
        print(f"- {package.value['name']}: ${package.value['min_deposit']} to ${package.value['max_deposit']}")
    
    deposit_amount = get_user_input()
    selected_package = select_package(deposit_amount)
    results = calculate_returns(selected_package, deposit_amount)
    display_results(results)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)
```
