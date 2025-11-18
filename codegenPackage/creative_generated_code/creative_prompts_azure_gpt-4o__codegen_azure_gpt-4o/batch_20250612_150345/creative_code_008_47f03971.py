"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swifttradeexpress.com
Prompt: Generate a Python program that calculates the total profit for an investor using SwiftTrade Express's trading bot, including deductions for company and administrative commissions.
Generated: DETERMINISTIC_47f039717739f667
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from decimal import Decimal

# Define constants for company and administrative commission percentages
COMPANY_COMMISSION_PERCENTAGE = Decimal('3.5')  # 3.5% commission for the company
ADMINISTRATIVE_COMMISSION_PERCENTAGE = Decimal('1.5')  # 1.5% commission for administrative fees

def calculate_total_profit(gross_profit):
    """
    Function to calculate the total profit for an investor after deducting company and administrative commissions.
    
    Parameters:
        gross_profit (Decimal): The total gross profit from the trading bot.
        
    Returns:
        Decimal: The net profit after deducting all commissions.
    """
    try:
        if gross_profit < 0:
            raise ValueError("Gross profit cannot be negative.")
        
        # Calculate company commission
        company_commission = (gross_profit * COMPANY_COMMISSION_PERCENTAGE) / Decimal('100')
        
        # Calculate administrative commission
        administrative_commission = (gross_profit * ADMINISTRATIVE_COMMISSION_PERCENTAGE) / Decimal('100')
        
        # Calculate net profit
        net_profit = gross_profit - company_commission - administrative_commission
        
        return net_profit
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error calculating total profit: {e}")
        return None

def main():
    """
    Main function to handle user input and calculate net profit.
    """
    try:
        # Prompt user to enter their gross profit from the trading bot
        gross_profit_input = input("Enter the gross profit from SwiftTrade Express's trading bot: ")
        
        # Convert user input to Decimal for precise calculations
        gross_profit = Decimal(gross_profit_input)
        
        # Calculate net profit
        net_profit = calculate_total_profit(gross_profit)
        
        if net_profit is not None:
            # Display results to the user
            print(f"Gross Profit: {gross_profit}")
            print(f"Net Profit after deductions: {net_profit}")
        else:
            print("Failed to calculate net profit due to an error.")
    except ValueError:
        print("Invalid input! Please make sure to enter a numeric value for gross profit.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the program
if __name__ == "__main__":
    main()
```
