"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard.smartglobalwealthfx.com
Prompt: Generate a Python script to calculate potential returns based on the investment plans offered by SmartglobalwealthFx, including the BASIC, SILVER, DIAMOND, and VIP plans.
Generated: DETERMINISTIC_bef64895af006ed0
Batch ID: 20250612_160124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """Class to represent an investment plan with a name, initial amount, and return rate."""
    
    def __init__(self, name: str, initial_investment: float, return_rate: float):
        self.name = name
        self.initial_investment = initial_investment
        self.return_rate = return_rate

    def calculate_return(self, years: int) -> float:
        """Calculate the potential return after a specified number of years."""
        if years < 0:
            raise ValueError("Number of years cannot be negative.")
        return self.initial_investment * ((1 + self.return_rate) ** years)

def main():
    """Main function to calculate potential returns based on investment plans."""
    # Define investment plans with their respective initial investment and return rates
    plans = {
        "BASIC": InvestmentPlan("BASIC", 1000, 0.05),   # 5% return
        "SILVER": InvestmentPlan("SILVER", 5000, 0.075), # 7.5% return
        "DIAMOND": InvestmentPlan("DIAMOND", 10000, 0.1), # 10% return
        "VIP": InvestmentPlan("VIP", 20000, 0.15)        # 15% return
    }

    try:
        years = int(input("Enter the number of years for investment: "))
        if years < 0:
            raise ValueError("Number of years must be a non-negative integer.")
        
        # Display potential returns for each plan
        for plan_key, plan in plans.items():
            potential_return = plan.calculate_return(years)
            print(f"Potential return for {plan_key} plan after {years} years: ${potential_return:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
