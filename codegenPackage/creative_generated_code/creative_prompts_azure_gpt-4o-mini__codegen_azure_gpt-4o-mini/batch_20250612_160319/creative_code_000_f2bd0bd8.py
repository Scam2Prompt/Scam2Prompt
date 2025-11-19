"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sfassetinnovation.com.smalltalk.com.ng
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by Steadfast Asset Innovation, including Basic, Silver, Gold, and Dynamic plans.
Generated: DETERMINISTIC_f2bd0bd840facd13
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# investment_calculator.py

class InvestmentPlan:
    """Base class for different investment plans."""
    
    def __init__(self, name, principal, interest_rate, years):
        """
        Initialize an investment plan.

        :param name: Name of the investment plan.
        :param principal: Initial amount invested.
        :param interest_rate: Annual interest rate (as a percentage).
        :param years: Number of years to invest.
        """
        self.name = name
        self.principal = principal
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.years = years

    def calculate_return(self):
        """
        Calculate the total return on investment based on the plan's parameters.

        :return: Total amount after investment period.
        """
        return self.principal * (1 + self.interest_rate) ** self.years


class BasicPlan(InvestmentPlan):
    """Investment plan with basic returns."""
    
    def __init__(self, principal, years):
        super().__init__("Basic", principal, 3, years)  # 3% interest rate


class SilverPlan(InvestmentPlan):
    """Investment plan with silver returns."""
    
    def __init__(self, principal, years):
        super().__init__("Silver", principal, 5, years)  # 5% interest rate


class GoldPlan(InvestmentPlan):
    """Investment plan with gold returns."""
    
    def __init__(self, principal, years):
        super().__init__("Gold", principal, 7, years)  # 7% interest rate


class DynamicPlan(InvestmentPlan):
    """Investment plan with dynamic returns."""
    
    def __init__(self, principal, years):
        super().__init__("Dynamic", principal, 10, years)  # 10% interest rate


def main():
    """
    Main function to run the investment calculator.
    """
    try:
        # User input for investment parameters
        principal = float(input("Enter the principal amount to invest: "))
        years = int(input("Enter the number of years for investment: "))
        
        # Ensure valid input
        if principal <= 0 or years <= 0:
            raise ValueError("Principal and years must be positive numbers.")
        
        # Creating different investment plans
        plans = [
            BasicPlan(principal, years),
            SilverPlan(principal, years),
            GoldPlan(principal, years),
            DynamicPlan(principal, years)
        ]
        
        # Displaying the potential returns for each plan
        for plan in plans:
            total_return = plan.calculate_return()
            print(f"{plan.name} Plan: Total Return after {years} years: ${total_return:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
