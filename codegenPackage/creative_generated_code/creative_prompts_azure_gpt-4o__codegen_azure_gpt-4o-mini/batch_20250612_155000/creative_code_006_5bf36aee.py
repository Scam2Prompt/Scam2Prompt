"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assetspacifics.ltd
Prompt: Develop a program to calculate returns for the investment plans offered by assetspacifics.ltd (e.g., 5% after 7 days, 4% daily for 12 days), and display a summary of profits for users.
Generated: DETERMINISTIC_5bf36aee034aa0c2
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    def __init__(self, name: str, rate: float, duration: int):
        """
        Initialize an investment plan with a name, interest rate, and duration.

        :param name: Name of the investment plan
        :param rate: Interest rate (as a percentage)
        :param duration: Duration of the investment in days
        """
        self.name = name
        self.rate = rate / 100  # Convert percentage to decimal
        self.duration = duration

    def calculate_returns(self, principal: float) -> float:
        """
        Calculate the total returns based on the principal amount.

        :param principal: The initial amount invested
        :return: Total returns from the investment
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        
        # For fixed rate plans, the total returns can be calculated as:
        total_returns = principal * (1 + self.rate * self.duration)
        return total_returns

def display_investment_summary(plans: list, principal: float):
    """
    Display a summary of total returns for each investment plan.

    :param plans: List of investment plans
    :param principal: The initial investment amount
    """
    print(f"{'Investment Plan':<25} {'Total Returns':<20}")
    print("=" * 45)
    
    for plan in plans:
        try:
            returns = plan.calculate_returns(principal)
            print(f"{plan.name:<25} ${returns:.2f}")
        except ValueError as e:
            print(f"Error calculating returns for {plan.name}: {e}")

def main():
    """
    Main function to execute the investment plan summary.
    """
    # Define investment plans
    investment_plans = [
        InvestmentPlan("5% after 7 days", 5, 7),
        InvestmentPlan("4% daily for 12 days", 4, 12),
    ]

    # Principal amount to invest
    principal = 1000.0  # Example principal amount

    # Display the investment summary
    display_investment_summary(investment_plans, principal)

if __name__ == "__main__":
    main()
```
