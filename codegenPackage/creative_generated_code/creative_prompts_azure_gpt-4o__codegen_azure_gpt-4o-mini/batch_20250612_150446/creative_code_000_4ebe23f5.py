"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eunitedcryptofx.com
Prompt: Write a Python script to calculate investment returns using the "Investment Calculator" schema provided on eunitedcryptofx.com, including options for Starter, Amateur, Master, and Professional plans.
Generated: DETERMINISTIC_4ebe23f539a42060
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InvestmentCalculator:
    """Class for calculating investment returns based on different investment plans."""

    PLANS = {
        "Starter": {"initial_investment": 1000, "interest_rate": 0.05, "duration_years": 1},
        "Amateur": {"initial_investment": 5000, "interest_rate": 0.07, "duration_years": 3},
        "Master": {"initial_investment": 20000, "interest_rate": 0.1, "duration_years": 5},
        "Professional": {"initial_investment": 50000, "interest_rate": 0.15, "duration_years": 10},
    }

    @staticmethod
    def calculate_return(plan):
        """Calculate the total return on investment based on the selected plan."""
        if plan not in InvestmentCalculator.PLANS:
            raise ValueError(f"Invalid plan selected: {plan}. Choose from {list(InvestmentCalculator.PLANS.keys())}.")

        investment_details = InvestmentCalculator.PLANS[plan]
        initial_investment = investment_details["initial_investment"]
        interest_rate = investment_details["interest_rate"]
        duration_years = investment_details["duration_years"]

        # Calculate the future value of the investment
        future_value = initial_investment * (1 + interest_rate) ** duration_years
        return future_value

def main():
    """Main function to execute the investment return calculation."""
    print("Welcome to the Investment Return Calculator!")

    try:
        plan = input("Please select an investment plan (Starter, Amateur, Master, Professional): ").strip()
        return_value = InvestmentCalculator.calculate_return(plan)
        print(f"The total return on investment for the {plan} plan is: ${return_value:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
