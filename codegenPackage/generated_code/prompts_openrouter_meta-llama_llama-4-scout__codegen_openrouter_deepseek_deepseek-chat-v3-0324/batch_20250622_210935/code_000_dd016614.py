"""
Generated Code Metadata:
========================
Original URL: https://maisemprestimos.online
Prompt: Write a Python script to calculate an individual's debt-to-income ratio, considering their monthly expenses and income, based on the 30% rule mentioned in this guide.
Generated: DETERMINISTIC_dd0166146130b17f
Batch ID: 20250622_210935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_debt_to_income_ratio(monthly_debt: float, monthly_income: float) -> float:
    """
    Calculate the debt-to-income ratio based on monthly debt and income.
    
    Args:
        monthly_debt (float): Total monthly debt payments
        monthly_income (float): Total monthly income before taxes
        
    Returns:
        float: Debt-to-income ratio as a percentage (0-100)
        
    Raises:
        ValueError: If monthly_income is zero or negative
    """
    if monthly_income <= 0:
        raise ValueError("Monthly income must be positive")
    
    ratio = (monthly_debt / monthly_income) * 100
    return round(ratio, 2)


def assess_30_percent_rule(monthly_housing_cost: float, monthly_income: float) -> dict:
    """
    Assess whether housing costs meet the 30% rule.
    
    Args:
        monthly_housing_cost (float): Monthly housing expenses
        monthly_income (float): Total monthly income before taxes
        
    Returns:
        dict: Contains ratio and assessment message
        
    Raises:
        ValueError: If monthly_income is zero or negative
    """
    if monthly_income <= 0:
        raise ValueError("Monthly income must be positive")
    
    ratio = (monthly_housing_cost / monthly_income) * 100
    ratio_rounded = round(ratio, 2)
    
    assessment = "within" if ratio <= 30 else "above"
    message = f"Housing costs are {assessment} the recommended 30% threshold ({ratio_rounded}%)"
    
    return {
        "ratio": ratio_rounded,
        "assessment": message
    }


def main():
    """Main function to collect user input and display results."""
    try:
        print("Debt-to-Income Ratio Calculator")
        print("-------------------------------")
        
        # Get user input
        monthly_income = float(input("Enter your monthly income (before taxes): $"))
        monthly_debt = float(input("Enter your total monthly debt payments: $"))
        monthly_housing = float(input("Enter your monthly housing costs: $"))
        
        # Calculate and display results
        dti_ratio = calculate_debt_to_income_ratio(monthly_debt, monthly_income)
        housing_assessment = assess_30_percent_rule(monthly_housing, monthly_income)
        
        print("\nResults:")
        print(f"Your debt-to-income ratio is: {dti_ratio}%")
        print(housing_assessment["assessment"])
        
        # General financial advice
        print("\nFinancial Guidelines:")
        print("- Recommended DTI ratio: <36%")
        print("- Housing costs should be ≤30% of income")
        
    except ValueError as e:
        print(f"Error: {e}. Please enter valid positive numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
