"""
Generated Code Metadata:
========================
Original URL: https://pipelinefinanceconseil.com
Prompt: "Write a Python script to simulate a savings plan with a 6.92% interest rate and provide recommendations for maximizing capital."
Generated: DETERMINISTIC_8a9987c8df7bd3b9
Batch ID: 20250622_211548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_future_value(principal, monthly_deposit, years, interest_rate):
    """
    Calculate the future value of a savings plan with compound interest.
    
    Args:
        principal (float): Initial investment amount
        monthly_deposit (float): Amount deposited each month
        years (int): Number of years to grow the investment
        interest_rate (float): Annual interest rate (as a decimal)
    
    Returns:
        float: Future value of the investment
    """
    monthly_rate = interest_rate / 12
    months = years * 12
    
    # Future value formula for compound interest with regular deposits
    future_value = principal * (1 + monthly_rate) ** months
    future_value += monthly_deposit * (((1 + monthly_rate) ** months - 1) / monthly_rate)
    
    return future_value

def recommend_strategy(principal, monthly_deposit, years, interest_rate):
    """
    Generate recommendations for maximizing capital based on the savings plan.
    
    Args:
        principal (float): Initial investment amount
        monthly_deposit (float): Amount deposited each month
        years (int): Number of years to grow the investment
        interest_rate (float): Annual interest rate (as a decimal)
    
    Returns:
        dict: Dictionary containing recommendations
    """
    recommendations = {}
    
    # Calculate future value with current parameters
    current_fv = calculate_future_value(principal, monthly_deposit, years, interest_rate)
    
    # Recommendation 1: Increase monthly deposit by 10%
    increased_deposit = monthly_deposit * 1.10
    increased_fv = calculate_future_value(principal, increased_deposit, years, interest_rate)
    recommendations['increase_deposit_10pct'] = {
        'new_monthly_deposit': increased_deposit,
        'future_value': increased_fv,
        'difference': increased_fv - current_fv
    }
    
    # Recommendation 2: Extend investment period by 5 years
    extended_years = years + 5
    extended_fv = calculate_future_value(principal, monthly_deposit, extended_years, interest_rate)
    recommendations['extend_period_5yrs'] = {
        'new_years': extended_years,
        'future_value': extended_fv,
        'difference': extended_fv - current_fv
    }
    
    # Recommendation 3: Lump sum investment (double initial principal)
    doubled_principal = principal * 2
    lump_sum_fv = calculate_future_value(doubled_principal, monthly_deposit, years, interest_rate)
    recommendations['double_initial_investment'] = {
        'new_principal': doubled_principal,
        'future_value': lump_sum_fv,
        'difference': lump_sum_fv - current_fv
    }
    
    return recommendations

def main():
    """
    Main function to run the savings plan simulation and display results.
    """
    try:
        # Input parameters
        INTEREST_RATE = 0.0692  # 6.92% annual interest rate
        
        print("Savings Plan Simulator with 6.92% Annual Interest")
        print("-------------------------------------------------")
        
        # Get user input with validation
        try:
            principal = float(input("Enter initial investment amount: $"))
            monthly_deposit = float(input("Enter monthly deposit amount: $"))
            years = int(input("Enter number of years to invest: "))
        except ValueError:
            raise ValueError("Please enter valid numerical values.")
        
        if principal < 0 or monthly_deposit < 0 or years <= 0:
            raise ValueError("All values must be positive.")
        
        # Calculate and display results
        future_value = calculate_future_value(principal, monthly_deposit, years, INTEREST_RATE)
        print(f"\nFuture value after {years} years: ${future_value:,.2f}")
        
        # Generate and display recommendations
        print("\nRecommendations to maximize capital:")
        recommendations = recommend_strategy(principal, monthly_deposit, years, INTEREST_RATE)
        
        print("\n1. Increase monthly deposit by 10%:")
        rec = recommendations['increase_deposit_10pct']
        print(f"   New monthly deposit: ${rec['new_monthly_deposit']:,.2f}")
        print(f"   Future value: ${rec['future_value']:,.2f} (+${rec['difference']:,.2f})")
        
        print("\n2. Extend investment period by 5 years:")
        rec = recommendations['extend_period_5yrs']
        print(f"   New investment period: {rec['new_years']} years")
        print(f"   Future value: ${rec['future_value']:,.2f} (+${rec['difference']:,.2f})")
        
        print("\n3. Double initial investment:")
        rec = recommendations['double_initial_investment']
        print(f"   New initial investment: ${rec['new_principal']:,.2f}")
        print(f"   Future value: ${rec['future_value']:,.2f} (+${rec['difference']:,.2f})")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("Please try again with valid inputs.")

if __name__ == "__main__":
    main()
```
