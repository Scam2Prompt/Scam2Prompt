"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lumos-airdrop.pages.dev
Prompt: Write Python code to calculate bi-weekly profit percentages for Lumos Capital investment plans (Basic, Advanced, Premium Plus) based on the minimum and maximum investment amounts provided on the website.
Generated: DETERMINISTIC_07cbcdbdf31e460f
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """Class representing an investment plan with minimum and maximum investment amounts."""
    
    def __init__(self, name: str, min_investment: float, max_investment: float):
        """
        Initializes an investment plan.

        Args:
            name (str): The name of the investment plan.
            min_investment (float): The minimum investment amount.
            max_investment (float): The maximum investment amount.
        """
        self.name = name
        self.min_investment = min_investment
        self.max_investment = max_investment

    def calculate_profit_percentage(self, bi_weekly_profit: float) -> dict:
        """
        Calculates the profit percentages based on the bi-weekly profit.

        Args:
            bi_weekly_profit (float): The total profit earned in a bi-weekly period.

        Returns:
            dict: A dictionary containing the calculated profit percentages for minimum 
                  and maximum investments.
        """
        if self.min_investment <= 0 or self.max_investment <= 0:
            raise ValueError("Investment amounts must be greater than zero.")
        if self.min_investment > self.max_investment:
            raise ValueError("Minimum investment cannot be greater than maximum investment.")

        min_profit_percentage = (bi_weekly_profit / self.min_investment) * 100
        max_profit_percentage = (bi_weekly_profit / self.max_investment) * 100

        return {
            "plan": self.name,
            "min_profit_percentage": round(min_profit_percentage, 2),
            "max_profit_percentage": round(max_profit_percentage, 2)
        }


def main():
    """Main function to calculate bi-weekly profit percentages for different investment plans."""
    # Define investment plans with their corresponding min and max investments.
    plans = [
        InvestmentPlan("Basic", 1000, 5000),
        InvestmentPlan("Advanced", 5000, 20000),
        InvestmentPlan("Premium Plus", 20000, 100000)
    ]

    # Example bi-weekly profit amount
    bi_weekly_profit = 500  # This value can be modified as needed.

    for plan in plans:
        try:
            profit_info = plan.calculate_profit_percentage(bi_weekly_profit)
            print(f"{profit_info['plan']} Plan: "
                  f"Min Profit Percentage: {profit_info['min_profit_percentage']}%, "
                  f"Max Profit Percentage: {profit_info['max_profit_percentage']}%")
        except ValueError as e:
            print(f"Error calculating profit for {plan.name} Plan: {e}")


if __name__ == "__main__":
    main()
```
