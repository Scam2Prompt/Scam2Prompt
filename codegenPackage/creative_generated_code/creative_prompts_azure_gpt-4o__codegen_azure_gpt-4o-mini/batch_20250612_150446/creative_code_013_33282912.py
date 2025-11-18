"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitalwealthtraders.com
Prompt: Develop a tool to calculate the profitability of different investment plans based on fixed hourly interest rates and durations, as outlined on Digitalwealthtraders.
Generated: DETERMINISTIC_33282912a2481d13
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

class InvestmentPlan:
    def __init__(self, name: str, hourly_rate: float, duration_hours: int):
        """
        Initializes an InvestmentPlan instance.

        :param name: The name of the investment plan.
        :param hourly_rate: The hourly interest rate (in percentage).
        :param duration_hours: The duration of the investment (in hours).
        """
        self.name = name
        self.hourly_rate = hourly_rate / 100  # Convert percentage to decimal
        self.duration_hours = duration_hours

    def calculate_profit(self, initial_investment: float) -> float:
        """
        Calculates the profit for the investment plan.

        :param initial_investment: The initial amount invested.
        :return: The total profit after the specified duration.
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative value.")
        
        profit = initial_investment * (1 + self.hourly_rate) ** self.duration_hours - initial_investment
        return profit

def main():
    """
    Main function to run the investment profitability calculator.
    """
    # Example investment plans
    plans = [
        InvestmentPlan("Plan A", 5.0, 24),  # 5% hourly for 24 hours
        InvestmentPlan("Plan B", 3.0, 48),  # 3% hourly for 48 hours
        InvestmentPlan("Plan C", 7.0, 12)   # 7% hourly for 12 hours
    ]
    
    try:
        print("Investment Profitability Calculator")
        initial_investment = float(input("Enter the initial investment amount: "))
        
        for plan in plans:
            profit = plan.calculate_profit(initial_investment)
            print(f"{plan.name}: Profit after {plan.duration_hours} hours is ${profit:.2f}")
    
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
