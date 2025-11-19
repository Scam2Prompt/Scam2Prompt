"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzocash.com
Prompt: Write a Python script to calculate potential earnings based on the investment packages offered by Renzocash, such as the Bronze, Silver, and Gold plans.
Generated: DETERMINISTIC_efdb391c4a006c15
Batch ID: 20250612_155122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """
    A class to represent an investment plan.
    
    Attributes:
        name (str): The name of the investment plan.
        principal (float): The initial amount of money invested.
        interest_rate (float): The annual interest rate as a percentage.
        duration_years (int): The duration of the investment in years.
    """
    
    def __init__(self, name, principal, interest_rate, duration_years):
        """
        Initializes an investment plan with the provided parameters.
        
        Args:
            name (str): The name of the investment plan.
            principal (float): The initial investment amount.
            interest_rate (float): The annual interest rate.
            duration_years (int): The duration of the investment in years.
        """
        self.name = name
        self.principal = principal
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.duration_years = duration_years

    def calculate_earnings(self):
        """
        Calculates the total amount after the investment duration, 
        including the earnings based on compound interest.

        Returns:
            float: The total amount after the investment period.
        """
        # Compound interest formula: A = P(1 + r/n)^(nt)
        # Assuming interest is compounded annually (n=1)
        total_amount = self.principal * (1 + self.interest_rate) ** self.duration_years
        return total_amount

def display_investment_summary(plan):
    """
    Displays the summary of the investment plan including potential earnings.

    Args:
        plan (InvestmentPlan): The investment plan to display.
    """
    try:
        total_amount = plan.calculate_earnings()
        earnings = total_amount - plan.principal
        print(f"Investment Plan: {plan.name}")
        print(f"Initial Investment: ${plan.principal:.2f}")
        print(f"Annual Interest Rate: {plan.interest_rate * 100:.2f}%")
        print(f"Duration: {plan.duration_years} years")
        print(f"Total Amount after {plan.duration_years} years: ${total_amount:.2f}")
        print(f"Total Earnings: ${earnings:.2f}\n")
    except Exception as e:
        print(f"Error calculating earnings for {plan.name}: {str(e)}")

def main():
    """
    Main function to set up investment plans and display their summaries.
    """
    # Define investment plans with their respective parameters
    investment_plans = [
        InvestmentPlan("Bronze", principal=1000, interest_rate=5, duration_years=2),
        InvestmentPlan("Silver", principal=5000, interest_rate=7, duration_years=3),
        InvestmentPlan("Gold", principal=10000, interest_rate=10, duration_years=5),
    ]
    
    # Display summaries for each investment plan
    for plan in investment_plans:
        display_investment_summary(plan)

if __name__ == "__main__":
    main()
```
