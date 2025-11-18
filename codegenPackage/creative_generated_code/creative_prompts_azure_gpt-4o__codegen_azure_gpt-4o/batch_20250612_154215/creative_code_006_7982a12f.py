"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://australiawidewealth.com
Prompt: Develop a Python program that calculates the impact of reduced working hours on family finances, incorporating the budgeting advice for young families from the Australia Wide Wealth Services site.
Generated: DETERMINISTIC_7982a12fd27c5f68
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def collect_financial_data():
    """
    Collects financial data from the user including income, expenses, and potential change in working hours.
    Returns:
        dict: A dictionary containing financial data.
    """
    try:
        print("Enter your current financial details:")
        income = float(input("Monthly household income ($): "))
        expenses = float(input("Monthly household expenses ($): "))
        hours_per_week = int(input("Current weekly working hours: "))
        proposed_hours = int(input("Proposed weekly working hours after reduction: "))
        hourly_rate = float(input("Hourly rate ($): "))
        
        if proposed_hours >= hours_per_week:
            raise ValueError("Proposed hours should be less than current working hours.")
        
        return {
            "income": income,
            "expenses": expenses,
            "hours_per_week": hours_per_week,
            "proposed_hours": proposed_hours,
            "hourly_rate": hourly_rate
        }
    except ValueError as ve:
        print(f"Input error: {ve}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


def calculate_financial_impact(data):
    """
    Calculates the financial impact of reducing working hours.
    Args:
        data (dict): Financial data collected from the user.
    Returns:
        dict: A dictionary containing updated financial details.
    """
    try:
        current_income = data["hours_per_week"] * data["hourly_rate"] * 4  # Approx. 4 weeks in a month
        proposed_income = data["proposed_hours"] * data["hourly_rate"] * 4
        
        impact_on_income = current_income - proposed_income
        updated_income = data["income"] - impact_on_income
        
        return {
            "current_income": current_income,
            "proposed_income": proposed_income,
            "impact_on_income": impact_on_income,
            "updated_income": updated_income,
            "expenses": data["expenses"],
            "monthly_savings": updated_income - data["expenses"]
        }
    except KeyError as ke:
        print(f"Key error in financial data: {ke}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred during calculation: {e}", file=sys.stderr)
        sys.exit(1)


def display_results(results):
    """
    Displays the financial impact to the user.
    Args:
        results (dict): Financial impact calculation results.
    """
    print("\nFinancial Impact Analysis:")
    print(f"Current Monthly Income: ${results['current_income']:.2f}")
    print(f"Proposed Monthly Income (after reducing hours): ${results['proposed_income']:.2f}")
    print(f"Income Reduction Impact: -${results['impact_on_income']:.2f}")
    print(f"Updated Monthly Income: ${results['updated_income']:.2f}")
    print(f"Monthly Expenses: ${results['expenses']:.2f}")
    
    if results['monthly_savings'] >= 0:
        print(f"Estimated Monthly Savings: ${results['monthly_savings']:.2f}")
    else:
        print(f"Estimated Monthly Deficit: -${abs(results['monthly_savings']):.2f}")


def main():
    """
    Main function to run the program.
    Collects financial data, calculates impact, and displays results.
    """
    print("Welcome to the Family Finance Impact Calculator")
    
    # Step 1: Collect financial data
    financial_data = collect_financial_data()
    
    # Step 2: Calculate financial impact
    results = calculate_financial_impact(financial_data)
    
    # Step 3: Display results to the user
    display_results(results)


if __name__ == "__main__":
    main()
```
