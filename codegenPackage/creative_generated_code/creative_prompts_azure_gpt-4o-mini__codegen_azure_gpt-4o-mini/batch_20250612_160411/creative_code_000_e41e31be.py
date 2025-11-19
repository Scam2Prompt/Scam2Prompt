"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welforcevestcapital.com
Prompt: Generate a Python script that calculates potential profits based on the investment plans offered by Welforcevest Capital, including the Starter, Standard, and Advanced plans.
Generated: DETERMINISTIC_e41e31be4a051c38
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """Base class for investment plans."""

    def __init__(self, initial_investment, duration_months):
        self.initial_investment = initial_investment
        self.duration_months = duration_months

    def calculate_profit(self):
        """Calculate profit based on the investment plan. Must be overridden by subclasses."""
        raise NotImplementedError("This method should be overridden in derived classes.")


class StarterPlan(InvestmentPlan):
    """Investment plan for beginners (Starter Plan)."""

    def calculate_profit(self):
        """Calculate profit for Starter Plan."""
        # Fixed interest rate for Starter Plan
        interest_rate = 0.05  # 5% monthly
        total_profit = self.initial_investment * (1 + interest_rate) ** self.duration_months
        return total_profit


class StandardPlan(InvestmentPlan):
    """Investment plan for intermediate investors (Standard Plan)."""

    def calculate_profit(self):
        """Calculate profit for Standard Plan."""
        # Fixed interest rate for Standard Plan
        interest_rate = 0.07  # 7% monthly
        total_profit = self.initial_investment * (1 + interest_rate) ** self.duration_months
        return total_profit


class AdvancedPlan(InvestmentPlan):
    """Investment plan for advanced investors (Advanced Plan)."""

    def calculate_profit(self):
        """Calculate profit for Advanced Plan."""
        # Fixed interest rate for Advanced Plan
        interest_rate = 0.1  # 10% monthly
        total_profit = self.initial_investment * (1 + interest_rate) ** self.duration_months
        return total_profit


def main():
    """Main function to run the investment profit calculator."""
    try:
        # User input for investment details
        initial_investment = float(input("Enter your initial investment amount: "))
        duration_months = int(input("Enter the duration in months: "))
        
        # Ensure that the values are valid
        if initial_investment <= 0 or duration_months <= 0:
            raise ValueError("Investment amount and duration must be greater than zero.")

        # Select investment plan
        print("Select your investment plan:")
        print("1. Starter Plan")
        print("2. Standard Plan")
        print("3. Advanced Plan")
        
        plan_choice = int(input("Enter the plan number (1-3): "))
        
        # Create an instance of the selected investment plan
        if plan_choice == 1:
            plan = StarterPlan(initial_investment, duration_months)
        elif plan_choice == 2:
            plan = StandardPlan(initial_investment, duration_months)
        elif plan_choice == 3:
            plan = AdvancedPlan(initial_investment, duration_months)
        else:
            raise ValueError("Invalid choice. Please select a plan number between 1 and 3.")

        # Calculate potential profits
        profit = plan.calculate_profit()
        print(f"The potential profit after {duration_months} months is: ${profit:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
