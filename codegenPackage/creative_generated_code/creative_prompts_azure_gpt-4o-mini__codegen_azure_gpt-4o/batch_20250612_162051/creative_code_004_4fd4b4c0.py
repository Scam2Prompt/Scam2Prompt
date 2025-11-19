"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://powerfivesolar.com
Prompt: Suggest a library for building a solar energy savings calculator, taking into account factors like home equity increase and monthly savings, as highlighted on the PowerFive Solar site.
Generated: DETERMINISTIC_4fd4b4c06d45d74a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

def calculate_solar_savings(monthly_bill, solar_panel_cost, financing_term, interest_rate):
    """
    Calculate savings from installing solar panels.
    
    Parameters:
        monthly_bill (float): The average monthly electricity bill.
        solar_panel_cost (float): The total cost of installing solar panels.
        financing_term (int): The financing term in years.
        interest_rate (float): The annual interest rate for the financing.
        
    Returns:
        dict: A dictionary containing monthly savings, total financing cost, and estimated home equity increase.
    """
    try:
        # Constants
        SOLAR_MONTHLY_SAVINGS_PERCENT = 0.30  # Estimated monthly savings from solar panels (30% reduction)
        HOME_EQUITY_INCREASE_PERCENT = 0.20  # Estimated increase in home equity (20% of solar panel cost)
        
        # Monthly savings calculation
        monthly_savings = monthly_bill * SOLAR_MONTHLY_SAVINGS_PERCENT
        
        # Total financing cost calculation
        interest_rate_monthly = interest_rate / 12 / 100
        total_payments = financing_term * 12
        monthly_financing_payment = (solar_panel_cost * interest_rate_monthly) / (1 - (1 + interest_rate_monthly) ** -total_payments)
        total_financing_cost = monthly_financing_payment * total_payments
        
        # Home equity increase calculation
        home_equity_increase = solar_panel_cost * HOME_EQUITY_INCREASE_PERCENT
        
        # Return results
        return {
            "monthly_savings": monthly_savings,
            "total_financing_cost": total_financing_cost,
            "home_equity_increase": home_equity_increase
        }
    except Exception as e:
        print(f"Error in calculating solar savings: {e}")
        return None


def main():
    """Main function to interact with the user and calculate solar savings."""
    try:
        print("Welcome to the Solar Energy Savings Calculator!")
        
        # Collect user inputs
        monthly_bill = float(input("Enter your average monthly electricity bill (USD): "))
        solar_panel_cost = float(input("Enter the total cost of solar panel installation (USD): "))
        financing_term = int(input("Enter the financing term (years): "))
        interest_rate = float(input("Enter the annual interest rate (%): "))
        
        # Calculate savings
        savings = calculate_solar_savings(monthly_bill, solar_panel_cost, financing_term, interest_rate)
        
        if savings:
            # Display results
            print("\n=== Solar Savings Calculation Results ===")
            print(f"Estimated Monthly Savings: ${savings['monthly_savings']:.2f}")
            print(f"Total Financing Cost: ${savings['total_financing_cost']:.2f}")
            print(f"Estimated Home Equity Increase: ${savings['home_equity_increase']:.2f}")
        else:
            print("Unable to calculate savings. Please try again.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Entry point for the program
if __name__ == "__main__":
    main()
```
